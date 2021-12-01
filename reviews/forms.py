from .models import Review, ReviewImage
from django.forms import ModelForm, TextInput, DateTimeInput, FileInput, Textarea

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['categoru', 'rait', 'review_title', 'prev_text', 'review_text',
                'image', 'pub_date']
        widgets = {
            'review_title': TextInput(attrs = {'class': "form-control"}),
            'prev_text': Textarea(attrs = {'class': "form-control"}),
            'review_text': Textarea(attrs = {'class': "form-control"}),
            'pub_date': DateTimeInput(attrs = {'class': "form-control"}),
        }

class ReviewImageForm(ModelForm):
    class Meta:
        model = ReviewImage
        fields = ['image_push']
        widgets = {
            'image_push': FileInput(attrs={'multiple': 'multiple'})
        }
