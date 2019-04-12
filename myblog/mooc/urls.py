from django.template.context_processors import static
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index/', views.index, name='index'),
    path('upload/',views.uploadImg),
    path('show/',views.showImg),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
