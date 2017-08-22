# -*- coding: utf-8 -*-
import io
from django.http import HttpResponse
from django.shortcuts import render_to_response
from PIL import Image
import  base64


from InterfaceModel.models import Employee

def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = 'you are search for ' + request.GET['q']
        data = Employee(name=request.GET['q'])
        data.save()

    else:
        message = 'empty'
    return HttpResponse(message)

def byte2image(request):
    request.encoding = 'utf-8'
    savepath = "/Users/lishunwang/Downloads/667.jpg"
    if request.POST:
        image = Image.open(io.BytesIO(base64.b64decode(request.POST['pic_content'])))
        image.save(savepath)
        message='success'

    else:
        message = 'fail'

    return HttpResponse(message)






