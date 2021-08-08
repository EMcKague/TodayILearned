from django.db import models
from django.db.models.fields import CharField, DateTimeField, SlugField, TextField

# Create your models here.


class Article(models.Model):
    title = CharField(max_length=100)
    body = TextField()
    slug = SlugField()
    date = DateTimeField(auto_now_add=True)
    # add in thumbnail
    # add in author

    def __str__(self):
        return self.title
