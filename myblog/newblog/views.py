from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator


def index(request):
    return HttpResponse('<h1>hello world<h1>')


def essay_content(requset):
    essay = models.Essay.objects.all()[0]
    return render(requset, 'newblog/show.html', {'essay': essay})


def get_index_page(request):
    page = request.GET.get('page')
    if page :
        page = int(page)
    else :
        page = 1
    essays = models.Essay.objects.all()
    if len(essays) >= 5:
        top_list = models.Essay.objects.order_by('-publish_date')[:5]
    else :
        top_list = models.Essay.objects.order_by('-publish_date')[:len(essays)]
    paginator = Paginator(essays,3)
    page_num = paginator.num_pages
    print('page_num',paginator.num_pages)
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page+1
    else :
        next_page = page

    if page_article_list.has_previous():
        previous = page -1
    else :
        previous = page

    return render(request, 'newblog/index.html', {'essays': page_article_list,
                                                  'page_num':range(1,page_num+1),
                                                  'curr_page':page,
                                                  'next_page':next_page,
                                                  'previous':previous,
                                                  'top_list':top_list})


def detail(request, essay_id):
    #essay = models.Essay.objects.get(essay_id=essay_id)
    #section_list = essay.content.split('\n')
    all_essay = models.Essay.objects.all()
    essay = None
    previous_index = 0
    next_index = 0
    for index,curr_essay in enumerate(all_essay):
        if index == 0:
            previous_index = 0
            next_index = 1
        elif index == len(all_essay) -1 :
            previous_index = index -1
            next_index = index
        else :
            previous_index = index -1
            next_index = index +1
        if curr_essay.essay_id == essay_id:
            essay = curr_essay
            previous_essay = all_essay[previous_index]
            next_essay = all_essay[next_index]
            break
    section_list = essay.content.split('\n')

    return render(request, 'newblog/detail.html', {'essay': essay,'section_list':section_list,
                                                   'previous_essay':previous_essay,'next_essay':next_essay})
