from django import forms
from django.contrib.auth import get_user

from .models import Ad


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ('title', 'description', 'image', 'price')
