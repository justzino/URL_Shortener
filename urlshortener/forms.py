from django import forms

from .models import URLMap


class ShortenerForm(forms.ModelForm):
    original_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "URL을 입력하세요."}
    ))

    class Meta:
        model = URLMap
        fields = ('original_url',)
