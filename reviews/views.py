from django.contrib.auth.models import User
from django.db.models.aggregates import Avg, Count, Sum
from django.shortcuts import render, redirect
from django.utils.formats import date_format

from Site_reviews.templatetags.review_tags import latest_posts
from .models import Raiting, Review, Comment, Categoru, ReviewImage
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_POST
from .forms import ReviewForm, ReviewImageForm
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, DeleteView

class ReviewUpdateView(UpdateView):
    model = Review
    template_name = "reviews/update.html"
    form_class = ReviewForm

class ReviewDeleteView(DeleteView):
    model = Review
    success_url = "/accounts/profile/"
    DeleteViewate_name = "reviews/delete.html"

def index(request):
    reviews_list = Review.objects.filter(publish = True).order_by('-pub_date')
    latest_post = Review.objects.filter(publish = True).order_by('-pub_date')[:6]
    return render(request, 'reviews/index.html', {'reviews_list': reviews_list, 'latest_post': latest_post})

def search(request):
    searc_query = request.GET.get('search', '')
    if searc_query:
        reviews_list = Review.objects.filter(Q(review_title__icontains = searc_query) | Q(review_text__icontains = searc_query) | Q(prev_text__icontains = searc_query))
    else:
        HttpResponse('Данных статей не найдено')
    return render(request, 'reviews/index.html', {'reviews_list': reviews_list})

def proba(request):
    return HttpResponse('ok')

def detail(request, review_id):
    try:
        a = Review.objects.get(id = review_id)
        comment_list = a.comment_set.order_by('id')[:10]
    except:
        raise Http404('Отзыв не найден')
    return render(request, 'reviews/detail.html', {'review': a, 'comment_list': comment_list})

def leave_comment(request, review_id):
    try:
        a = Review.objects.get(id = review_id)
    except:
        raise Http404('Отзыв не найден11')
    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect(reverse('reviews:detail', args = (a.id,)))

def star_add(request, data):
    data = [int(i) for i in data.split(':')]
    if Raiting.objects.filter(review_raiting = data[1], user_raiting = data[0]).exists() == False:
        rait = Raiting(review_raiting = Review.objects.get(id = data[1]), user_raiting = User.objects.get(id = data[0]), star = data[2], like = False)
        rait.save()  
    else: 
        rait = Raiting.objects.get(review_raiting = data[1], user_raiting = data[0])
        rait.star = data[2]
        rait.save()
    return HttpResponse( star_rait_Avg(data[1]) )

def like_add(request, data):
    data = [int(i) for i in data.split(':')]
    if Raiting.objects.filter(review_raiting = data[1], user_raiting = data[0]).exists() == False:
        rait = Raiting(review_raiting = Review.objects.get(id = data[1]), user_raiting = User.objects.get(id = data[0]), like = True)
        rait.save()  
    else: 
        rait = Raiting.objects.get(review_raiting = data[1], user_raiting = data[0])
        if rait.like == False:
            rait.like = True
        else:
            rait.like = False
        rait.save()
    return HttpResponse(like_count(data[1]))

def star_rait_Avg(id):
    star = Raiting.objects.filter(review_raiting = id)
    if star.count() > 0:
        star = [i.star for i in star if i.star != 0]
        data = round(sum(star) / len(star), 1)
    else:
        data = 0
    return data

def like_count(id):
    like = Raiting.objects.filter(review_raiting = id, like = True)
    if like.count() > 0:
        data = sum([i.like for i in like if i.like])
    else:
        data = 0
    return data

@login_required()
def reviews_add(request, review_id):
    if request.method == 'POST':
        categoru = request.POST.get('categoru')
        rait = request.POST.get('rait')
        review_title = request.POST.get('review_title')
        prev_text = request.POST.get('prev_text')
        review_text = request.POST.get('review_text')
        image = request.FILES.get('image')
        pub_date = request.POST.get('pub_date')
        image_push = request.FILES.getlist('image_push')

        pub_date = pub_date[6:10] + '-' + pub_date[3:5] + '-' + pub_date[:2] + pub_date[10:]
        categoru = Categoru.objects.get(id = categoru)
        categoru = categoru.name_categoru
        data = {
            'categoru': categoru,
            'rait': rait,
            'id_user': review_id,
            'review_title': review_title,
            'prev_text': prev_text,
            'review_text': review_text,
            'pub_date': pub_date,
        }
        
        new_review = Review(categoru = Categoru.objects.get(name_categoru = data['categoru']), rait = data['rait'], review_title = data['review_title'], 
            prev_text = data['prev_text'], review_text = data['review_text'], pub_date = data['pub_date'], 
            image = image, author_name = User.objects.get(id = data['id_user']))
        new_review.save()
        id = new_review.id
        if len(image_push) > 0:
            for elem in image_push:
                add_image = ReviewImage(image_push = elem, image = Review.objects.get(id = id))
                add_image.save()
        return redirect("/accounts/profile")        
    else:
        error = 'Неверная форма'
    form = ReviewForm()
    form_image = ReviewImageForm()
    data = {
        'form': form,
        'form_image': form_image,
        'error': error
    }
    return render(request, 'reviews/new.html', data)    

def filter_categoru(request, categ):
    categ = Categoru.objects.get(name_categoru = categ)
    list_categoru = Review.objects.filter(categoru = categ)
    return render(request, 'reviews/filter.html', {'list_categoru': list_categoru}) 