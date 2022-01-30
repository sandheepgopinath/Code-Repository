import numpy as np
import cv2

im=cv2.imread('brazing.jpg')
im=cv2.resize(im,(640,480))

#Making the image grayscale

gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

#Making the image Binary
bin=cv2.threshold(gray,250,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#cv2.imshow('Bin1',bin)

#Creating a kernel
kernel=np.ones((2,2),np.uint8)

#Closing function

closing=cv2.morphologyEx(bin,cv2.MORPH_CLOSE,kernel)

closed=closing.copy()

im2,contour=cv2.findContours(closed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


for cnt in contour:

    area = cv2.contourArea(cnt)
    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(im, ellipse, (0,255,0), 2)

cv2.imshow("Morphological Closing", closed)
cv2.imshow("Adaptive Thresholding", bin)
cv2.imshow('Contours', im)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()


cv2.waitKey(0)
cv2.destroyAllWindows()

