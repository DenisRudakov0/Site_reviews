from django.urls import path

from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add/', views.like_add, name = 'like_add'),
    path('<int:review_id>/', views.detail, name = 'detail'),
    path('<int:review_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
]
