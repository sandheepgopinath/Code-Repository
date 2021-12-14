import cv2
import numpy as np
from picamera import PiCamera
from picamera.array import PiRGBArray
import time 

camera=PiCamera()

img=PiRGBArray(camera)

time.sleep(1)
camera.capture(img,format='bgr')
image=img.array

#imgr=cv2.getRotationMatrix2D((image.shape[0]/2,image.shape[1]/2),180,1)
#cv2.warpAffine(image,imgr,(image.shape[0],image.shape[1]))
imgr=cv2.rotate(image,cv2.ROTATE_180)
cv2.imshow("Original",image)
cv2.imshow("Inverted",imgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

