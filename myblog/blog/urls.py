from django.urls import path
from . import  views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/',views.index,name = 'index'),
    path('article/<int:article_id>/',views.article_page,name='article_page'),
    path('edit/',views.edit_page,name = 'edit_page'),
    path('edit/action/',views.action_page,name='edit_action'),
    path('edit/delete/<int:article_id>/',views.edit_delete,name = 'edit_delete'),
    path('edit/change/<int:article_id>/',views.edit_change,name = 'edit_change'),
    path('edit/tocha/<int:article_id>/',views.to_change,name = 'to_change'),
    path('machine/',views.machine,name = 'machine'),
    path('xiaohang/',views.first_page, name = 'first_page'),
    path('jinglingqiu/',views.cssdemo1,name = 'jinglingqiu'),
    path('thetime/',views.thetime,name = 'thetime'),
    path('game_2048/',views.game_2048,name = 'game_2048'),
    path('weather/',views.cssdemo2,name = 'weather'),

]