# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
import argparse
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(1)
image=camera.capture(rawCapture,format="bgr")
image=cv2.rotate(image,cv2.ROTATE_180)
tracker=cv2.TrackerBoosting_create()

bbox=cv2.selectROI(image,False)
ok=tracker.init(image,bbox)




# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
	# show the frame
	frame=cv2.rotate(image,cv2.ROTATE_180)
	cv2.imshow('Frame',frame)
	#Start the timer
	timer=cv2.getTickCount()
	ok,bbox=tracker.update(frame)

 
	if ok:
        	# Tracking success
        	p1 = (int(bbox[0]), int(bbox[1]))
        	p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        	cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
	else :
        	# Tracking failure
        	cv2.putText(frame, "Tracking failure detected", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
 
        # Display tracker type on frame
	cv2.putText(frame, tracker_type + " Tracker", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,255,0),2);
 

        # Display result
	#cv2.imshow("Tracking", frame)
 



	key = cv2.waitKey(1) & 0xFF
 	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
