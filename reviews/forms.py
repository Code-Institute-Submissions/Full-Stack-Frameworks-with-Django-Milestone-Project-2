from django import forms

from .models import Review, Product


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'
        