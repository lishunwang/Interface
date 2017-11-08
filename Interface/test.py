from PIL import Image

image = Image.open("/Users/lishunwang/Downloads/6.jpeg")
print image.size
box = (0, 0, 500, 500)  #裁剪区域的左上角和右下角位置（图片左上角位置为坐标原点）
img = image.crop(box)
print img.size
print img.format
# img.show()