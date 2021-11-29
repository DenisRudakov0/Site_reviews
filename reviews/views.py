from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Raiting, Review, Comment, Categoru
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_POST

def index(request):
    reviews_list = Review.objects.all()
    categoru_list = menu()
    return render(request, 'reviews/index.html', {'reviews_list': reviews_list, 'categoru_list': categoru_list})

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

@require_POST
def like_add(request):
    review_id = int(request.POST.get('review_id'))
    user_id = int(request.POST.get('user_id'))

    user = User.objects.get(id = review_id)
    review = Review.objects.get(id = user_id)
    
    try:
        like = Raiting.objects.get(review_raiting = review, user_raiting = user)
        like.delete()
    except Exception as e:
        like = Raiting(review_raiting = review, user_raiting = user, like = True)
        like.save()
    
    a = Review.objects.get(id = review_id)
    like_count = a.readers.count()
    return JsonResponse({'like_count': like_count})

def reviews_add(request):
    return render(request, 'reviews/new.html')
