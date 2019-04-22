from django.shortcuts import render
from PIL import Image
import numpy as np
from .models import Img
from . import models
import os


# Create your views here.

def index(request):
    return render(request, 'mooc/index.html')


def uploadImg(request):
    if request.method == 'POST':
        # print(type(request.FILES.get('img')))
        img = request.FILES.get('img')
        name = request.FILES.get('img').name
        new_img = Img(img=img, name=name)
        new_img.save()
        path = os.path.abspath('.')
        picture_url = new_img.img.url.replace('/', '\\')
        path2 = path + picture_url
        picture_change(path2)
    return render(request, 'mooc/uploading.html')


def showImg(request):
    imgs = Img.objects.all()
    content = {
        'imgs': imgs,
    }
    return render(request, 'mooc/showing.html', content)


def delete(request, img_id):
    picture = models.Img.objects.get(pk=img_id)
    models.Img.objects.filter(pk=img_id).delete()
    path = os.path.abspath('.')
    picture_url = picture.img.url.replace('/', '\\')
    path2 = path + picture_url
    os.remove(path2)

    imgs = Img.objects.all()
    content = {
        'imgs': imgs,
    }
    return render(request, 'mooc/showing.html', content)


def picture_change(pictureUrl):
    # 为了便于文件的导入，可以使用相对路径，将文件和程序放在同一个文件夹下
    vec_el = np.pi / 2.2
    vec_az = np.pi / 4.
    depth = 10.
    im = Image.open(pictureUrl).convert('L')
    a = np.asarray(im).astype('float')
    grad = np.gradient(a)
    grad_x, grad_y = grad
    grad_x = grad_x * depth / 100.
    grad_y = grad_y * depth / 100.
    dx = np.cos(vec_el) * np.cos(vec_az)
    dy = np.cos(vec_el) * np.sin(vec_az)
    dz = np.sin(vec_el)
    A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
    uni_x = grad_x / A
    uni_y = grad_y / A
    uni_z = 1. / A
    a2 = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)
    a2 = a2.clip(0, 255)
    im2 = Image.fromarray(a2.astype('uint8'))
    im2.save(pictureUrl)
