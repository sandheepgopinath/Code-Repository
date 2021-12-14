import numpy as np
import cv2

im=cv2.imread('Image.jpg')
#Kernel to Blur
kernel=np.ones((5,5))/25


#Kernel for image sharpening
sharp=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])


#Kernel for edge Detection
laplacian=np.array([[0,1,0],[1,-4,1],[0,1,0]])


sharpened=cv2.filter2D(im,-1,sharp)


edge=cv2.filter2D(sharpened,-1,laplacian)
cv2.imshow('Edge',edge)

cv2.waitKey(0)
cv2.destroyAllWindows()
