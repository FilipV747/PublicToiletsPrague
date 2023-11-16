from django import forms
from prague.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['username', 'content', 'rating']
        widgets = {
            'rating': forms.RadioSelect
        }

