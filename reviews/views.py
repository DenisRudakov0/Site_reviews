from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Raiting, Review, Comment
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse

def index(request):
    reviews_list = Review.objects.all()
    return render(request, 'reviews/index.html', {'reviews_list': reviews_list})

def detail(request, review_id):
    try:
        a = Review.objects.get(id = review_id)
        like = a.readers.all()
        comment_list = a.comment_set.order_by('id')[:10]
    except:
        raise Http404('Отзыв не найден')
    return render(request, 'reviews/detail.html', {'like': like, 'review': a, 'comment_list': comment_list})

def leave_comment(request, review_id):
    try:
        a = Review.objects.get(id = review_id)
    except:
        raise Http404('Отзыв не найден')
    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect(reverse('reviews:detail', args = (a.id,)))

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
    
    return HttpResponse('ok')
    
