from django.contrib import admin
from .models import Review, Comment, Raiting, ReviewImage

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_title', 'slug', 'author_name', 'pub_date')
    prepopulated_fields = {'slug': ('review_title', 'author_name')}
    
admin.site.register(ReviewImage)
admin.site.register(Comment)
admin.site.register(Raiting)
