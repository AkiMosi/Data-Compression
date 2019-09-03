from PIL import Image
im= Image.open('a.jpg')
im=im.convert('L')
im.show()
pixelMap=im.load()
img=Image.new(im.mode,im.size)
pixelsNew=im.load()
for i in range (img.size[0]):
    for j in range(img.size[1]):
        if(pixelMap[i,j]<(32)):
            pixelMap[i,j]=(16)
        elif(pixelMap[i,j]>=(32) and pixelMap[i,j]<(64)):
            pixelMap[i,j]=(48)
        elif(pixelMap[i,j]>=(64) and pixelMap[i,j]<(96)):
            pixelMap[i,j]=(80)
        elif(pixelMap[i,j]>=(96) and pixelMap[i,j]<(127)):
            pixelMap[i,j]=(112)
        elif(pixelMap[i,j]>=(127) and pixelMap[i,j]<(160)):
            pixelMap[i,j]=(144)
        elif(pixelMap[i,j]>=(160) and pixelMap[i,j]<(191)):
            pixelMap[i,j]=(176)
        elif(pixelMap[i,j]>=(191) and pixelMap[i,j]<(224)):
            pixelMap[i,j]=(208)
        elif(pixelMap[i,j]>=(224) and pixelMap[i,j]<(255)):
            pixelMap[i,j]=(240)
im.save('new.png')
im.show()