import numpy as np
import cv2

params=cv2.SimpleBlobDetector_Params()
params.filterByArea=True
params.maxArea=900
params.minArea=100

detector=cv2.SimpleBlobDetector_create(params)

im=cv2.imread('brazing.jpg')
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
kernel=np.ones((1,1),np.uint8)
gray=cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel)
keypoints=detector.detect(gray)
x=keypoints[0].pt[0]
y=keypoints[0].pt[1]
area=keypoints[0].size
#for i in range(len(keypoints)):
#	imt=cv2.putText(im,str(i+1),(int(keypoints[i].pt[0]),int(keypoints[i].pt[1])),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2,cv2.LINE_8)

imt=cv2.putText(im,str(len(keypoints)),(20,39),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2,cv2.LINE_8)

img=cv2.drawKeypoints(imt,keypoints,np.array([]),(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Blobs',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
