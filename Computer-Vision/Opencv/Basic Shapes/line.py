import numpy as np
import cv2

pic=np.zeros((500,500,3),dtype='uint8')

cv2.line(pic,(0,0),(500,500),(123,121,121))
cv2.imshow('Line',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
