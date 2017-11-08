# -*- coding: utf-8 -*-
import io
from django.http import HttpResponse
from django.shortcuts import render_to_response
from PIL import Image
import base64

from InterfaceModel.models import Employee


def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = 'you are search for ' + request.GET['q']
        data = Employee(name=request.GET['q'])
        data.save()
    else:
        message = 'empty'
    return HttpResponse(message)


# 保存图片
def byte2image(request):
    request.encoding = 'utf-8'
    savepath = "/Users/lishunwang/Downloads/66.jpeg"
    if request.POST:
        image = Image.open(io.BytesIO(base64.b64decode(request.POST['pic_content'])))
        maxWidth = request.POST['max_width']
        maxHeight = request.POST['max_height']
        box = boxImage(image.size, maxWidth, maxHeight)
        img = image.crop(box)
        message = img.save(savepath)
    else:
        message = 'fail'
    return HttpResponse(message)


# 获取裁剪的box
def boxImage(size, maxWidth, maxHeight):
    initWidth = size[0]
    initHeight = size[1]
    templateRate = maxWidth / maxHeight
    initRate = initWidth / initHeight
    box = ()

    # 原图比指定的图片小
    if initWidth <= maxWidth and initHeight <= maxHeight:
        box = (0, 0, initWidth, initHeight)
        return box

    # 原图和指定的图宽高比例相同
    if templateRate == initRate:
        box = (float(initWidth - maxWidth) / 2, float(initHeight - maxHeight) / 2, float(initWidth + maxWidth) / 2,
               float(initHeight + maxHeight) / 2)
        return box


        # 原图和指定的图宽高比例不同


