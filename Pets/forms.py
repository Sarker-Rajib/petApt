from django import forms
from .models import Review, Pet

class FeedbackForm(forms.ModelForm):
    class Meta: 
        model = Review
        fields = ['body']
        widgets= {
          'body': forms.Textarea(attrs={'rows': 4})
        }


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['image', 'title', 'description', 'adapt_price', 'category']
