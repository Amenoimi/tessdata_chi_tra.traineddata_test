#-*- coding: utf-8 -*-　

import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('img.dfkai-sb.exp0.tif')
GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret1,thresh1=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)
ret2,thresh2=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY_INV)
ret3,thresh3=cv2.threshold(GrayImage,127,255,cv2.THRESH_TRUNC)
ret4,thresh4=cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO)
ret5,thresh5=cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO_INV)
thresh6=cv2.GaussianBlur(img,(5,5),127,255)
titles = ['Gray Image','BINARY','BINARY_INV','TRUNC','TOZERO','GaussianBlur']
images = [GrayImage, thresh1, thresh2, thresh3, thresh4,thresh6]
for i in range(len(images)):
   plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
#cv2.imwrite('output.tiff', thresh2)
plt.show()
