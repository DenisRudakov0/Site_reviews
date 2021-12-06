from django import template
from reviews.models import *

register = template.Library()

@register.simple_tag()
def get_review(name):
    return Review.objects.filter(author_name = name, publish = True)

@register.simple_tag()
def get_review_profile(name):
    return Review.objects.filter(author_name = name)

@register.simple_tag()
def star(id):
    star = Raiting.objects.filter(review_raiting = id)
    if star.count() > 0:
        star = [i.star for i in star if i.star != 0]
        data = round(sum(star) / len(star), 1)
    else:
        data = 0
    return data

@register.simple_tag()
def like(id):
    like = Raiting.objects.filter(review_raiting = id, like = True)
    if like.count() > 0:
        data = sum([i.like for i in like if i.like])
    else:
        data = 0
    return data

@register.simple_tag()
def menu_categoru():
    menu = Categoru.objects.all()
    return menu

@register.filter()
def latest_posts():
    posts = Review.objects.filter(publish = True).order_by('-pub_date')[:6]
    return posts

@register.filter()
def list_img(id):
    img_list = ReviewImage.objects.filter(image = id)
    return(img_list)