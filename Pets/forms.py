from django import forms
from .models import Review

class FeedbackForm(forms.ModelForm):
    class Meta: 
        model = Review
        fields = ['body']
        widgets= {
          'body': forms.Textarea(attrs={'rows': 4})
        }