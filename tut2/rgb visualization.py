# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = plt.axes(projection="3d")

im = Image.open("color1.jpg")
im = im.resize((288,180))
pixelmap = im.load()
x,y,z = [],[],[]
for i in range(288):
    for j in range(180):
        x.append(pixelmap[i,j][0])
        y.append(pixelmap[i,j][1])
        z.append(pixelmap[i,j][2])

tempmap = [x,y,z]
tempmap = np.array(tempmap).transpose()


#ax.scatter3D(x,y,z,cmap = 'hsv',c = x)

#
#ax.scatter3D(x,y,z,cmap = 'hsv',c = y)
#
#
plt.xlabel("Red")
plt.ylabel("Blue")

ax.scatter3D(x,y,z,cmap = 'hsv',c = z)

plt.show()