# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:44:20 2019

@author: 17pd04
"""

from PIL import Image
a=[]
temp=[]
for i in range(7):
    for j in range(7):
        for k in range(7):
            if(i+j+k == 6):
                temp=[i,j,k]
                a.append(temp)

def abc(List,pix,im):
    r_interval,g_interval,b_interval = 2**List[0],2**List[1],2**List[2]
    r_len,g_len,b,_len = 256/r_interval,256/g_interval,256/b_interval
    for i in range (im.size[0]):
        for j in range(im.size[1]):
            r,g,b=pixelMap[i,j][0],pixelMap[i,j][1],pixelMap[i,j][2]
            if()
    
    
print("Hello, World")

im= Image.open('img.jpg')
#im= im.convert('L')
pixelMap=im.load()
img=Image.new(im.mode,im.size)
pixelsNew=[]
temp=[]

#for i in range (img.size[0]):
#    for j in range(img.size[1]):
#        r,g,b=pixelMap[i,j][0],pixelMap[i,j][1],pixelMap[i,j][2]
#        if(pixelMap[i,j][0]<(127)):
#            pixelMap[i,j]=(64,g,b)
#        elif(pixelMap[i,j][0]>=(127)):
#            pixelMap[i,j]=(192,g,b)
abc(a[0],pixelMap,im)
            
#im.show()