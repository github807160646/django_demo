
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index/', views.index, name='index'),
    path('upload/',views.uploadImg, name = 'upload'),
    path('show/',views.showImg, name='show'),
    path('delete/<int:img_id>/', views.delete, name = 'delete'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
