import numpy as np
import cv2

pic=np.zeros((500,500,3),dtype='uint8')

cv2.rectangle(pic,(0,0),(500,150),(123,121,121),lineType=8)
cv2.imshow('Rectangle',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
