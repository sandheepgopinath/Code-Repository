from cifar import *
import cv2

cf=cifar('cifar-10-batches-py/')
model=cf.load_best_model()

cap=cv2.VideoCapture('http://10.1.16.120:8080/video')

while True:
    ret,frame=cap.read()
    cv2.imshow('Live Feed from Android',frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
frame=cv2.resize(frame,(32,32))
cf.test_prediction(frame)
cv2.destroyAllWindows()
cap.release()