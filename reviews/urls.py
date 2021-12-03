from django.urls import path

from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:review_id>/', views.detail, name = 'detail'),
    path('star/<data>', views.star_add, name = 'star_add'),
    path('like/<data>', views.like_add, name = 'like_add'),
    path('new/<int:review_id>', views.reviews_add, name = 'review_add'),
    path('<int:review_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
    path('new/<int:pk>/update/', views.ReviewUpdateView.as_view(), name = 'review_update'),
    path('new/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name = 'review_delete'),
]
