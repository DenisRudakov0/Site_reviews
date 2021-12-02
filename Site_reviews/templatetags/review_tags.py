from django import template
from reviews.models import *

register = template.Library()

@register.simple_tag()
def get_review(name):
    return Review.objects.filter(author_name = name)