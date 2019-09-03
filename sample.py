# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:00:36 2019

@author: 17pd04
"""

from PIL import Image
im= Image.open('img.jpg')
#im= im.convert('L')
pixelMap=im.load()
img=Image.new(im.mode,im.size)
pixelsNew=[]
temp=[]
for i in range (img.size[0]):
    for j in range(img.size[1]):
        temp=[]
        for k in range(len(pixelMap[0,0])):
            temp.append(pixelMap[i,j][k])
        pixelsNew.append(temp)
im.show()