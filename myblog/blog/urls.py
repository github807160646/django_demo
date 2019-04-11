from django.urls import path
from . import  views

urlpatterns = [
    path('index/',views.index),
    path('article/<int:article_id>/',views.article_page,name='article_page')
]