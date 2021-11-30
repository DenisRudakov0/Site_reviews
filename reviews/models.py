from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

class Categoru(models.Model):
    name_categoru = models.CharField('Имя категории', max_length = 100)

    def __str__(self):
        return f'{self.name_categoru}'

class Review(models.Model):
    RATE_AUTHOR_CHOISES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10))
    caregoru = models.ForeignKey(Categoru, on_delete=models.SET_NULL, null=True)
    review_title = models.CharField('название отзыва', max_length = 200)
    slug = models.SlugField(blank=True)
    review_text = models.TextField('текст отзыва')
    rait = models.IntegerField(max_length = 1, choices = RATE_AUTHOR_CHOISES, default=1)
    image = models.ImageField(upload_to='images/', blank=True)
    pub_date = models.DateTimeField('дата публикации')
    author_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_review')
    readers = models.ManyToManyField(User, through='Raiting', related_name='review')

    def __str__(self):
        return f'{self.review_title}'

class ReviewImage(models.Model):
    image = models.ForeignKey(Review, on_delete=models.CASCADE)
    image_push = models.ImageField(upload_to="images/%Y/%m/%d", blank=True)

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.CharField('текст комментария', max_length = 200)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Raiting(models.Model):
    RATE_CHOISES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    review_raiting = models.ForeignKey(Review, on_delete=models.CASCADE)
    user_raiting = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default = False)
    star = models.IntegerField(max_length = 1, choices = RATE_CHOISES, default = 1)
    
    def __str__(self):
        return f'{self.id}:{self.review_raiting}:{self.user_raiting}'

