from django.contrib import admin
from .models import Review, Comment, Raiting, ReviewImage, Categoru

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_title', 'slug', 'author_name', 'pub_date')
    prepopulated_fields = {'slug': ('review_title', 'author_name')}

@admin.register(Categoru)
class CategoruAdmin(admin.ModelAdmin):
    list_display = ('name_categoru',)

admin.site.register(ReviewImage)
admin.site.register(Comment)
admin.site.register(Raiting)
