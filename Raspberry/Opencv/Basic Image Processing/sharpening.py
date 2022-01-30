import numpy as np
import cv2

sharpen_kernel=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

im=cv2.imread('Image.jpg')

img=cv2.filter2D(im,-1,sharpen_kernel)

#Applying canny Algotithm

img1=cv2.Canny(img,100,200)

cv2.imshow('Sharpened Edges',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


