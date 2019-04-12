from django.shortcuts import render

from .models import Img


# Create your views here.

def index(request):
    return render(request, 'mooc/index.html')


def uploadImg(request):
    if request.method == 'POST':
        #print(type(request.FILES.get('img')))
        img = request.FILES.get('img')
        name = request.FILES.get('img').name
        new_img = Img(img=img, name=name)
        new_img.save()
    return render(request, 'mooc/uploading.html')

def showImg(request):
    imgs = Img.objects.all()
    content = {
        'imgs':imgs,
    }
    for i in imgs:
        print(type(i))
        print(i.img.url)
    return render(request, 'mooc/showing.html', content)
