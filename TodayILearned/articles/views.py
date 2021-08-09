from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.


def article_list(request):
    # grab all the articles and order them by date
    articles = Article.objects.all().order_by('date')
    # render the template 'article_list' and render the articles
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, slug):
    # print(slug)
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})
