from .models import Review
from django.forms import ModelForm, TextInput, DateTimeInput

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['caregoru', 'rait', 'review_title', 'review_text',
                'image', 'pub_date']
        widgets = {
            "review_title": TextInput(attrs = {}),
            "pub_date": DateTimeInput(attrs = {}),
        }