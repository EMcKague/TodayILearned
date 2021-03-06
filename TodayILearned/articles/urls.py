from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='listView'),
    path('create/', views.article_create, name='create'),
    path('<slug:slug>/', views.article_detail, name='detailView'),
]
