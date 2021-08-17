from django.db import models
from django.db.models.fields import CharField, DateTimeField, SlugField, TextField
from django.contrib.auth.models import User


class Article(models.Model):
    title = CharField(max_length=100)
    body = TextField()
    slug = SlugField()
    date = DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # tag = models.TextField

    def __str__(self):
        return self.title

    def snippet(self):
        # take the first 50 characters of the body
        return self.body[:50] + '...'
