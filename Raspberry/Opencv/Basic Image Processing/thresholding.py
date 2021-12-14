import numpy as np
import cv2
import matpotlib.pyplot as plt 

im=cv2.imread('Image.jpg')
r,g,b=cv2.split(im)

ret,th1=cv2.threshold(im,127,255,cv2.THRESH_BINARY)

th2=cv2.adaptiveThreshold(r,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,2)

th3=cv2.adaptiveThreshold(g,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

ret1,th4=cv2.threshold(b,120,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#cv2.imshow('Threshold',th4)
fig,ax=plt.subplot(2,2)

ax[0,0].plot(th1)


cv2.waitKey(0)
cv2.destroyAllWindows()

