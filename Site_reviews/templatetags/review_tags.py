from django import template
from reviews.models import *

register = template.Library()

@register.simple_tag()
def get_review(name):
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