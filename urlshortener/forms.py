from django import forms

from .models import URLMap


class ShortenerForm(forms.ModelForm):
    original_url = forms.URLField()

    class Meta:
        model = URLMap
        fields = ('original_url',)

