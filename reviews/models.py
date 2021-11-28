from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    review_title = models.CharField('название статьи', max_length = 200)
    review_text = models.TextField('текст статьи')
    image = models.ImageField(upload_to='images/', blank=True)
    pub_date = models.DateTimeField('дата публикации')
    author_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_review')
    readers = models.ManyToManyField(User, through='Raiting', related_name='review')

    def __str__(self):
        return f'{self.review_title} |'

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.CharField('текст комментария', max_length = 200)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Raiting(models.Model):
    RATE_CHOISES = (
        (1, 'one'),
        (2, 'two'),
        (3, 'three'),
        (4, 'four'),
        (5, 'five'),
    )
    review_raiting = models.ForeignKey(Review, on_delete=models.CASCADE)
    user_raiting = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}:{self.review_raiting}:{self.user_raiting}'

