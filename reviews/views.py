from django.shortcuts import render
from .models import Review, Comment
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

def index(request):
    reviews_list = Review.objects.all()
    return render(request, 'reviews/index.html', {'reviews_list': reviews_list})

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
        raise Http404('Отзыв не найден')

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect(reverse('reviews:detail', args = (a.id,)))
