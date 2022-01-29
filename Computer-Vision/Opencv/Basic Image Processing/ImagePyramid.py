import numpy as np
import cv2

img=cv2.imread('Image.jpg')
lower=img
for i in range(3):
	lower=cv2.pyrDown(lower)
	cv2.imshow('Lower',lower)
	cv2.waitKey(0)
upper=lower
for i in range(3):
	upper=cv2.pyrUp(upper)
	cv2.imshow('Upper',upper)
	cv2.waitKey(0)

cv2.destroyAllWindows()

