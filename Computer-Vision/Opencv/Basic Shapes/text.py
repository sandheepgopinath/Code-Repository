import numpy as np
import cv2

pic=np.zeros((500,500,3),dtype='uint8')

font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic,'Baba Yaga',(100,250),font,2,(255,23,12),6,cv2.LINE_8)

cv2.imshow('Text',pic)

cv2.waitKey(0)
cv2.destroyAllWindows()
