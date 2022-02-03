import numpy as np
import  cv2

im=cv2.imread('sasha-malia-obama-thanksgiving-pic-shutterstock-ftr-1-1.jpg')
r,g,b=cv2.split(im)
re=cv2.equalizeHist(r)

ge=cv2.equalizeHist(g)

be=cv2.equalizeHist(b)

im2=cv2.merge((re,ge,be))

cv2.imshow('Obama',im2)

cv2.waitKey(0)
cv2.destroyAllWindows()
