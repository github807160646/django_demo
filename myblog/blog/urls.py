from django.urls import path
from . import  views

urlpatterns = [
    path('index/',views.index,name = 'index'),
    path('article/<int:article_id>/',views.article_page,name='article_page'),
    path('edit/',views.edit_page,name = 'edit_page'),
    path('edit/action/',views.action_page,name='edit_action'),
    path('edit/delete/<int:article_id>/',views.edit_delete,name = 'edit_delete'),
    path('edit/change/<int:article_id>/',views.edit_change,name = 'edit_change'),
    path('edit/tocha/<int:article_id>/',views.to_change,name = 'to_change'),
]