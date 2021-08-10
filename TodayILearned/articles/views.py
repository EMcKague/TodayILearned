from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

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


@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            return redirect('articles:listView')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
