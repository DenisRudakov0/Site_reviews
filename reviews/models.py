from django.db import models

class Review(models.Model):
    review_title = models.CharField('название статьи', max_length = 200)
    review_text = models.TextField('текст статьи')
    image = models.ImageField(upload_to='images/', blank=True)
    pub_date = models.DateTimeField('дата публикации')
   
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.CharField('текст комментария', max_length = 200)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'