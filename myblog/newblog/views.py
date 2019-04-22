from django.shortcuts import render
from django.http import HttpResponse
from .models import Essay
from . import models

# Create your views here.


def index(request):
    return HttpResponse('<h1>hello world<h1>')


def essay_content(requset):
    essay = models.Essay.objects.all()[0]
    return  render(requset,'newblog/show.html',{'essay':essay})



