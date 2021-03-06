from django.shortcuts import render

from . import models

def first_page(request):
    return  render(request,'blog/first_page.html')

def machine(request):
    return render(request, 'blog/machine_learn.html')

def cssdemo1(request):
    return  render(request , 'blog/css_demo1.html')


def thetime(request):
    return  render(request, 'blog/thetime/index.html')

def game_2048(request):
    return render(request, 'blog/game_2048/index.html')

def cssdemo2(request):
    return  render(request,"blog/weather.html")


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    sections = article.content.split('\n')
    return render(request, 'blog/article_page.html', {'article': article, 'sections': sections})


def to_change(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/change_page.html', {'article': article})


def edit_page(request):
    return render(request, 'blog/edit_page.html')


def edit_delete(request, article_id):
    models.Article.objects.filter(pk=article_id).delete()
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def edit_change(request, article_id):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    models.Article.objects.filter(pk=article_id).update(title=title)
    models.Article.objects.filter(pk=article_id).update(content=content)
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def action_page(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    models.Article.objects.create(title=title, content=content)
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})
