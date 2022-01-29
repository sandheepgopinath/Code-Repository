import numpy as np
import cv2

im=cv2.imread('brazing1.JPG')
print(im.shape)
cv2.imshow('furnace',im)

cv2.waitKey(0)
cv2.destroyAllWindows()
