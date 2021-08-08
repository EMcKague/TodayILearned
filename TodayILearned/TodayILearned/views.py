from django.http import HttpResponse
from django.shortcuts import render

# Side note, make sure to specifiy in settings where templates folder can be found


def homePage(request):
    # return HttpResponse('homepage')
    return render(request, 'homepage.html')


def aboutPage(request):
    return render(request, 'about.html')
