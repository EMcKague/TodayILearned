from django.shortcuts import render
from .models import Article

# Create your views here.


def article_list(request):
    # grab all the articles and order them by date
    articles = Article.objects.all().order_by('date')
    # render the template 'article_list' and render the articles
    return render(request, 'articles/article_list.html', {'articles': articles})
