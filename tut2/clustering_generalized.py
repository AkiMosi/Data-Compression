#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:34:10 2019

@author: akimosi
"""

from PIL import Image
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random as rnd
import math as m

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

im = Image.open("img.jpg")
im = im.resize([38,21])

pixel = im.load()
r,g,b = [],[],[]
for i in range(im.size[0]):
    for j in range(im.size[1]):
        r.append(pixel[i,j][0])
        g.append(pixel[i,j][1])
        b.append(pixel[i,j][2])

ri,gi,bi = [],[],[]
k = 2

for i in range(k):
    ri.append(rnd.randint(0,255))
    gi.append(rnd.randint(0,255))
    bi.append(rnd.randint(0,255))

pix = np.array([r,g,b]).transpose()
dist1 , dist2 = [],[]
clas1,clas2 = [],[]

for i in range(len(r)):
    dist1.append(m.sqrt((ri[0] - r[i])**2 + (gi[0] - g[i])**2 + (
            bi[0] - b[i])**2))
    dist2.append(m.sqrt((ri[1] - r[i])**2 + (gi[1] - g[i])**2 + (
            bi[1] - b[i])**2))
    if(dist1[i]<dist2[i]):
        clas1.append([r[i],g[i],b[i]])
    else:
        clas2.append([r[i],g[i],b[i]])

clas1 = np.array(clas1)
clas2 = np.array(clas2)

cent1,cent2 = [],[]

cent1.append([clas1[:,0].sum()/len(clas1),clas1[:,1].sum()/len(clas1),clas1[:,2].sum()/len(clas1)])
cent2.append([clas2[:,0].sum()/len(clas2),clas2[:,1].sum()/len(clas2),clas2[:,2].sum()/len(clas2)])
count = 0

while(True):
    clas1,clas2 = [],[]
    dist1,dist2 = [],[]
    for i in range(len(r)):
        dist1.append(m.sqrt((cent1[count][0] - r[i])**2 + (cent1[count][0] - g[i])**2 + (cent1[count][0] - b[i])**2))
        dist2.append(m.sqrt((cent2[count][1] - r[i])**2 + (cent2[count][1] - g[i])**2 + (cent2[count][1] - b[i])**2))
        if(dist1[i]<dist2[i]):
            clas1.append([r[i],g[i],b[i]])
        else:
            clas2.append([r[i],g[i],b[i]])

    clas1 = np.array(clas1)
    clas2 = np.array(clas2)

    cent1.append([clas1[:,0].sum()/len(clas1),clas1[:,1].sum()/len(clas1),clas1[:,2].sum()/len(clas1)])
    cent2.append([clas2[:,0].sum()/len(clas2),clas2[:,1].sum()/len(clas2),clas2[:,2].sum()/len(clas2)])

    count += 1
    if(cent1[count] == cent1[count-1] and cent2[count] == cent2[count-1]  ):
        break

ax.scatter3D(clas1[:,0],clas1[:,1],clas1[:,2])
ax.scatter3D(clas2[:,0],clas2[:,1],clas2[:,2])
ax.scatter3D(cent1[count][0],cent1[count][1],cent1[count][2],c='r')

#im.show()