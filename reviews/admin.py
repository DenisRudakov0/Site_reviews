from django.contrib import admin
from .models import Review, Comment, Raiting, ReviewImage, Categoru

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_title', 'slug', 'author_name', 'pub_date')
    prepopulated_fields = {'slug': ('review_title', 'author_name')}
    search_fields = ('review_title', 'review_text')
    raw_id_fields = ('author_name',)

@admin.register(Categoru)
class CategoruAdmin(admin.ModelAdmin):
    list_display = ('name_categoru',)

@admin.register(ReviewImage)
class ReviewImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'image_push')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'comment_text')
    search_fields = ('author_name',)

@admin.register(Raiting)
class RaitingtAdmin(admin.ModelAdmin):
    list_display = ('review_raiting', 'user_raiting', 'like', 'star')
    list_filter = ('like', 'star')
    
