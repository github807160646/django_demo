
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index/', views.index, name='index'),
    path('hello/',views.hello,name = 'hello'),
    path('msggate/',views.msgproc, name = 'msggate'),
    path('upload/',views.uploadImg, name = 'upload'),
    path('show/',views.showImg, name='show'),
    path('delete/<int:img_id>/', views.delete, name = 'delete'),
    path('html1/',views.html1,name = 'hetml1'),
    path('html2/',views.html2,name = 'hetml2'),
    path('html3/',views.html3,name = 'hetml3'),
    path('html5/',views.html5,name = 'hetml5'),
    path('html6/',views.html6,name = 'hetml6'),
    path('html7/',views.html7,name = 'html7'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
              + static(settings.IMG_URL, document_root=settings.IMG_ROOT)
