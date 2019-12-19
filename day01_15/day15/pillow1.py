#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用pillow操作图像
# @Date    : 2019-07-18 23:01:00
# @Author  : yaolh (yaolihui129@sina.com)
# @Link    : https://github.com/yaolihui129
# @Version : 0.1

from PIL import Image

img= Image.open('./res/guido.jpg')
print(img.size)
print(img.format)
print(img.format_description)
img.save('./res/guido.png')


img2 = Image.open('./res/guido.png')
img3 = img2.crop((335,435,438,615))
for x in range(4):
    for y in range(4):
        img2.paste(img3,(95 * y,180 * x))
img2.resize((img.size[0]//2,img.size[1]//2))
img2.rotate(90)
img2.save('./res/guido2.png')