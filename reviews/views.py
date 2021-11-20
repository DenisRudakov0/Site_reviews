from django.shortcuts import render
from .models import Review, Comment

def index(request):
    return render(request, 'reviews/index.html')

# Create your views here.
