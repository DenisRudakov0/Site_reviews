from django.contrib.auth.models import User
from django.db.models.aggregates import Avg, Count, Sum
from django.shortcuts import render, redirect
from django.utils.formats import date_format
from .models import Raiting, Review, Comment, Categoru, ReviewImage
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_POST
from .forms import ReviewForm, ReviewImageForm
from django.db.models import Aggregate

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
    reviews_list = Review.objects.all()
    list_like = []
    for elem in reviews_list:
        a = Raiting.objects.filter(like = True, review_raiting = elem.id).aggregate(Sum('like'))
        star = Raiting.objects.filter(review_raiting = elem.id)
        star = [i.star for i in star if i.star != 0] 
        if len(star) >= 1:
            star = round(sum(star) / len(star), 1)
        else:
            star = 0
        a['id'] = elem.id
        a['review_title'] = elem.review_title
        a['image'] = elem.image
        a['author_name'] = elem.author_name
        a['rait'] = elem.rait
        a['review_text'] = elem.review_text
        a['star'] = star
        a['star_len'] = str(round(star / 0.05)) + '%'
        list_like.append(a)

    a = list_like
    categoru_list = menu()
    
    return render(request, 'reviews/index.html', {'reviews_list': reviews_list, 'categoru_list': categoru_list, 'a': a})

def proba(request):
    return HttpResponse('ok')

def menu():
    categoru_list = Categoru.objects.all()
    return categoru_list

def detail(request, review_id):
    categoru_list = menu()
    try:
        a = Review.objects.get(id = review_id)
        comment_list = a.comment_set.order_by('id')[:10]
    except:
        raise Http404('Отзыв не найден')
    return render(request, 'reviews/detail.html', {'review': a, 'comment_list': comment_list, 'categoru_list': categoru_list})

def leave_comment(request, review_id):
    try:
        a = Review.objects.get(id = review_id)
    except:
        raise Http404('Отзыв не найден')
    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect(reverse('reviews:detail', args = (a.id,)))

def like_add(request, data):
    return HttpResponse(8)

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
        return HttpResponse(data)        
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
