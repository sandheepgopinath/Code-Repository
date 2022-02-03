import numpy as np
import cv2

im=cv2.imread('Image.jpg')
n=6
kernel=np.ones((n,n),np.uint8)

# Erosion

eroded=cv2.erode(im,kernel,iterations=1)

#Dilation

dilated=cv2.dilate(im,kernel,iterations=1)

# Opening

opened=cv2.morphologyEx(im,cv2.MORPH_OPEN,kernel)


#Closing

closed=cv2.morphologyEx(im,cv2.MORPH_CLOSE,kernel)

cv2.imshow('Eroded',closed)

cv2.waitKey(0)
cv2.destroyAllWindows()
