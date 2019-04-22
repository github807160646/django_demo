from django.urls import path
from . import  views

urlpatterns = [
    path('index/',views.index,name = 'index'),
    path('show/',views.essay_content,name = 'show'),
]