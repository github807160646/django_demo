from django.urls import path
from . import  views

urlpatterns = [
    path('index/',views.index,name = 'index'),
    path('show/',views.essay_content,name = 'show'),
    path('essay/',views.get_index_page,name = 'essay'),
    path('detail/<int:essay_id>/',views.detail,name = 'detail'),

]