from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.


def index(request):
    return HttpResponse('<h1>hello world<h1>')


def essay_content(requset):
    essay = models.Essay.objects.all()[0]
    return render(requset, 'newblog/show.html', {'essay': essay})


def get_index_page(request):
    essays = models.Essay.objects.all()
    return render(request, 'newblog/index.html', {'essays': essays})


def detail(request, essay_id):
    essay = models.Essay.objects.get(essay_id=essay_id)
    section_list = essay.content.split('\n')

    return render(request, 'newblog/detail.html', {'essay': essay,'section_list':section_list})
