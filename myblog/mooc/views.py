from django.shortcuts import render
from PIL import Image
import numpy as np
from .models import Img
from . import models
import  os,sys
from datetime import datetime
sys.path.append("..")
from newblog import models as md




# Create your views here.

def index(request):
    post_list = md.Essay.objects.all()
    return render(request, 'mooc/index.html', {'post_list': post_list})

def hello(request):
    return  render(request,'mooc/hello.html')

def msgproc(request):
    datalist = []
    if request.method == "POST":
        usera = request.POST.get("usera", None)
        userb = request.POST.get("userb", None)
        msg = request.POST.get("msg", None)
        time = datetime.now()
        with open('msgdata.txt', 'a+') as f:
            f.write("{}--{}--{}--{}--\n".format(userb, usera, \
                                                msg, time.strftime("%Y-%m-%d %H:%M:%S")))
    if request.method == "GET":
        userc = request.GET.get("userc", None)
        if userc != None:
            with open("msgdata.txt", "r") as f:
                cnt = 0
                for line in f:
                    linedata = line.split('--')
                    if linedata[0] == userc:
                        cnt = cnt + 1
                        d = {"usera": linedata[1], "msg": linedata[2] \
                            , "time": linedata[3]}
                        datalist.append(d)
                    if cnt >= 10:
                        break
    return  render(request, "mooc/MsgSingleWeb.html",{"data":datalist})


def uploadImg(request):
    if request.method == 'POST':
        # print(type(request.FILES.get('img')))
        img = request.FILES.get('img')
        name = request.FILES.get('img').name
        new_img = Img(img=img, name=name)
        new_img.save()
        path = os.path.abspath('.')
        picture_url = new_img.img.url
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
    picture_url = picture.img.url
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

#html test
def html1(request):
    return  render(request,'mooc/html1.html')

def html2(request):
    return  render(request,'mooc/html2.html')

def html3(request):
    return  render(request,'mooc/html3.html')

def html5(request):
    return  render(request,'mooc/html5.html')

def html6(request):
    return  render(request,'mooc/html6.html')

def html7(request):
    return  render(request,'mooc/html7.html')