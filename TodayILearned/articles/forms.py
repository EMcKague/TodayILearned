from django import forms
from django.forms import widgets
from . import models


class CreateArticle(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'title-form-area', 'placeholder': 'New post title here...', 'rows': '1', 'style': 'font-size: 50px; width: 97%'}), label='')
    body = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Write your post content here...', 'rows': '20', 'style': 'font-size: 16px; width: 97%'}), label='')
    slug = forms.SlugField(widget=forms.HiddenInput())

    class Meta:
        model = models.Article
        fields = ['title', 'body', 'thumbnail', 'slug']
