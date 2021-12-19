
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v16.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v16.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import os
import time
import tkinter as tk
import tkinter.font as tkFont
import re
import numpy as np
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from datetime import datetime 
import datetime as dt
import pyodbc

videoFile='output4927.mp4'

value=0
params=cv2.SimpleBlobDetector_Params() 
params.filterByArea=True
params.maxArea=465
params.minArea=44


params.filterByCircularity = True
params.minCircularity = 0.8


brightnessThreshold=0.99
detector=cv2.SimpleBlobDetector_create(params)
message=''
flag=0
partCode=''

stopExecution=0
stopCapture=0
stopSet=0
recordStatus=0
recordFlag=True

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=INCHN08DB05\SQLHOTEL;DATABASE=IN_Digitalization;UID=ignition;PWD=!9qRw3iW$7^I%iwX$DB')
cursor = conn.cursor()


class Ui_FurnaceVisionSystem(object):
    def record(self):

        global recordStatus,fourcc,ext,out,recordFlag
        status=self.radioButton.isChecked()

        if status & recordFlag:
            recordStatus=1
        elif status & (not recordFlag):
            recordStatus=1
        elif (not status):
            recordStatus=0






    def exit_function(self):
        global stopExecution
        stopExecution=1

    def capture_function(self):
        global stopCapture
        stopCapture=1

    def add(self):
        global value
        value=int(value)+1
        self.lcdNumber.display(value)
        print(value)

    def stopSet(self):
        global stopSet
        stopSet=1
        

    def updatePartCode(self):
        global partCode
        partCode=self.lineEdit_2.text()
        print(partCode)

    def viewCam(self,image):

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image=cv2.resize(image,(1024,780))
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(qImg))


##############  Captuer Webcam Image Function for Button 1
    def capture(self):

        global stopCapture,videoFile
        cap=cv2.VideoCapture(videoFile)
       # cap = cv2.VideoCapture(0)
        while(True):
            ret, image = cap.read()
            image=cv2.resize(image,(1024,780))
          #  image=cv2.rotate(image,cv2.ROTATE_180)
            cv2.line(image,(0,640),(1024,640),(0,255,0),2)
            self.viewCam(image)
            #cv2.imshow('capture',image)
            
           
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imwrite('Webcam Capture.jpg',image)
                break

            if stopCapture==1:
                cv2.imwrite('Webcam Capture.jpg',image)
                stopCapture=0
                break


        cap.release()
        cv2.destroyAllWindows()


##############  Set parameter Function fot Button 2


    def set_params(self):
    
    
        global params,brightnessThreshold,detector,stopSet
        pos=int(0)

        def do_nothing(x):
            pass

        image=cv2.imread('Webcam Capture.jpg')
        pos+=1

        while True:
            params.maxArea=self.dial_4.value()
            params.minArea=self.dial_5.value()
            brightnessThreshold=self.dial_6.value()/100
            detector=cv2.SimpleBlobDetector_create(params)
               
            value1=(self.dial_6.value())/100
            value2=(self.dial_5.value())
            value3=(self.dial_4.value())

            self.lcdNumber.setProperty("value",value1)
            self.lcdNumber_3.setProperty("intValue", value2)
            self.lcdNumber_4.setProperty("intValue", value3)


     
            frame=image

        
            frame=cv2.addWeighted(frame,brightnessThreshold, np.zeros(frame.shape, frame.dtype), -1, 0.5)
        
     
            hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  
            frame=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            keypoints=detector.detect(gray)
        
            for i in range(len(keypoints)):
                x=int(keypoints[i].pt[0])-10
                y=int(keypoints[i].pt[1])-10
                w=20+x
                h=20+y
                cv2.rectangle(frame,(x,y),(w,h),(0,255,0),2)
            
            #cv2.imshow('Image',frame)    
            self.viewCam(frame)
            
            if stopSet==1:
                stopSet=0
                break
                

            if cv2.waitKey(1)==ord('n'):
                break

        cv2.destroyAllWindows()


############### Track Function 




    def ask_tracker(self):
        #print('Enter 0 for Boosting')
        #print('Enter 1 for MIL')
        #print('Enter 2 for KCF')
        #print('Enter 3 for TLD')
        #print('Enter 4 for Median Flow')
        #choice=input('Enter choice')
        choice='6'
        if choice=='0':
            tracker=cv2.TrackerBoosting_create()
        if choice=='1':
            tracker=cv2.TrackerMIL_create()
        if choice=='2':
            tracker=cv2.TrackerKCF_create()
        if choice=='3':
            tracker=cv2.TrackerTLD_create()
        if choice=='4':
            tracker=cv2.TrackerMedianFlow_create()
        if choice=='5':
            tracker=cv2.TrackerCSRT_create()
        if choice=='6':
            tracker=cv2.TrackerKCF_create()
        return tracker


    def realtime_capture(self):
    
    
        global detector,params,brightnessThreshold,flag,stopExecution,recordStatus,recordFlag,partCode,videoFile
   ######################################################Setting Headers in UI ############################################    
        
        date=''
        shift=''
        d=dt.datetime.now().weekday()

        if d==0:
            date="Monday"
        elif d==1:
            date="Tuesday"
        elif d==2:
            date='Wednesday'    
        elif d==3:
            date='Thursday'
        elif d==4:
            date='Friday'
        elif d==5:
            date='Saturday'
        elif date==6:
            date='Sunday'

        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        ext=str(dt.datetime.now().minute)+str(dt.datetime.now().second)
        out = cv2.VideoWriter('output'+ext+'.mp4', fourcc, 20.0, (1024,768))

        date=date+', '+str(dt.datetime.now().strftime("%B"))+' '+str(dt.datetime.now().day)
        
        if (int(dt.datetime.now().hour)>=6) & (int(dt.datetime.now().hour)<14):
            shift='Morning Shift'
        elif (int(dt.datetime.now().hour)>=14) &(int(dt.datetime.now().hour)<22):
            shift='Afternoon Shift'
        else:
            shift='Night Shift'
        print (date)
        self.label_12.setText(str(date))
        self.label_11.setText(str(shift))



        ################################################# Creating a detector #################################################

        detector=cv2.SimpleBlobDetector_create(params)
    
        
        
        ################################################Reading first frame of video ##########################################
        #cap=cv2.VideoCapture(0)
        cap=cv2.VideoCapture(videoFile)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        cap.set(cv2.CAP_PROP_FPS,120)
        remainingCount=0
    

    
        ###################################################################################
                                      #TEST DETECTION#
        ##################################################################################                            
        #Reading first frame
        ret,frame=cap.read()
    
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        brightness=hsv[2].mean()
        print('Old',brightness)
        if brightness< 90:
            frame=cv2.addWeighted(frame,brightnessThreshold, np.zeros(frame.shape, frame.dtype), -1, 0.5)
         
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        brightness=hsv[2].mean()
        print('New',brightness)
        #Detecting Blobs
    
   
        frame=cv2.addWeighted(frame,brightnessThreshold, np.zeros(frame.shape, frame.dtype), -1, 0.5)
       # frame=cv2.resize(frame,(1024,768))
       # frame=cv2.rotate(frame,cv2.ROTATE_180)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #    kernel=np.ones((2,2),np.uint8)
    #    gray=cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel)
        keypoints=detector.detect(gray)
    
        img=cv2.drawKeypoints(frame,keypoints,np.array([]),(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
   
        # Create Multitracker
    
        m_tracker=cv2.MultiTracker_create()
    
        #Adding trackers to Multitracker
        avg_size=[]
        for i in range(len(keypoints)):
            #print(keypoints[i].pt[0],keypoints[i].pt[1])
            avg_size.append(keypoints[i].size)
            roi=(keypoints[i].pt[0]-10,keypoints[i].pt[1]-10,30,30)
            m_tracker.add(self.ask_tracker(),frame,roi)
        avg_size=np.asarray(avg_size)
    #    print(avg_size.mean())
        #if avg_size.mean()<20:
        #    brightnessThreshold=1.5
        #    params.maxArea=1000
        #    params.minArea=41
        #elif avg_size.mean()<15:
        #    brightnessThreshold=2
        #    params.maxArea=1000
        #    params.minArea=41
        #elif avg_size.mean()>20:
        #    brightnessThreshold=1.7
        #    params.filterByCircularity=True
        #    params.minCircularity = 0.85
        #    params.maxArea=3000
        #    params.minArea=120
        #    print('8 Inch')
        ###################################################################################
                                      #REAL DETECTION#
        ################################################################################## 
        ret,frame=cap.read()
    
    
        #Detecting Blobs
    
   
        #frame=cv2.addWeighted(frame,brightnessThreshold, np.zeros(frame.shape, frame.dtype), -1, 0.5)
    
      #  frame=cv2.resize(frame,(1024,768))
      #  frame=cv2.rotate(frame,cv2.ROTATE_180)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #    kernel=np.ones((2,2),np.uint8)
    #    gray=cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel)
        keypoints=detector.detect(gray)
    
        img=cv2.drawKeypoints(frame,keypoints,np.array([]),(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    
        m_tracker=cv2.MultiTracker_create()
    
        #Adding trackers to Multitracker
        avg_size=[]
        for i in range(len(keypoints)):
            #print(keypoints[i].pt[0],keypoints[i].pt[1])
            avg_size.append(keypoints[i].size)
            roi=(keypoints[i].pt[0]-10,keypoints[i].pt[1]-10,30,30)
            m_tracker.add(self.ask_tracker(),frame,roi)

        
        print ('Second detection done')

        ###################################################################################
                                    #DETECTION ON VIDEO#
        ################################################################################## 
        
        
        
        # Tracking the objects on video
        total_count=0
        count=0
        obj_count=0


        while ret:
            minute=dt.datetime.now().minute
            second=dt.datetime.now().second
            hour=dt.datetime.now().hour

         ###################################################################################
                                    #SQL Update#
        ################################################################################## 
        
            
            if minute==59 and second>55 and flag==0:
            
              
                query='INSERT INTO [IN_Digitalization].[dbo].[FD_Furnace] ( Input,PartCode,t_stamp) VALUES ('+str(total_count)+",'"+str(partCode)+"',GETDATE())"
                cursor.execute(query)
                conn.commit()
                flag=1
            if minute==0 and flag==1:
                flag=0


         ###################################################################################
                                    #Video Detection#
        ################################################################################## 

            ret,frame=cap.read()
            
            if ret:
                count+=1
                frame=cv2.addWeighted(frame,brightnessThreshold, np.zeros(frame.shape, frame.dtype), -1, 0.5)
             #   frame=cv2.resize(frame,(1024,768))
             #   frame=cv2.rotate(frame,cv2.ROTATE_180)
                recordFrame=frame.copy()
                x1=0
                x2=frame.shape[0]-120
                y1=frame.shape[1]
                y2=frame.shape[0]-120
                cv2.line(frame,(x1,x2),(y1,y2),(0,255,0),2)

                (retb,boxes)=m_tracker.update(frame)
          
                for box in boxes:
                    (x, y, w, h) = [int(v) for v in box]
                    if (y+h<x2) & (y+h>80) :

                        cv2.rectangle(frame, (x, y), (x + 20, y + 20), (0, 255, 0), 2)
                        #frame=cv2.putText(frame,str(y+h),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1,cv2.LINE_8)
                    else:
                        obj_count+=1
    
                #TOTAL IS THE NUMBER OF OBJECTS IN CURRENT FRAME
                
                remaining=len(boxes)-obj_count
                
        
           
                if int(remaining)<5:
                    remainingCount+=1
                    if remainingCount%10==0:

                        numberCrossed=0
                        print(len(boxes))
                        for box in boxes:
                            (x, y, w, h) = [int(v) for v in box]
                       
                            if (y+h>x2) & (y+h<80):

                                ## Hiding the already detected objects
                                frame=cv2.rectangle(frame, (x, y), (x + w+8, y + h+8), (0, 255,0), -1)
                            
                            else:
                                numberCrossed+=1
                        frame=cv2.rectangle(frame,(0,frame.shape[0]),(frame.shape[1],frame.shape[1]),(0,255,0),-1) 
                    
    ##                       
    #                    if len(boxes)==0:
    #                        new_frame=frame
                        
                        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                        keypoints=detector.detect(gray)


                        # Create new tracking if more than 5 parts are detected
                        if len(keypoints)>10:
                            remainingCount=0
                            #print('inside')
                            #m_tracker.release()
                            m_tracker=cv2.MultiTracker_create()
                            avg_size=[]
                        
                            for i in range(len(keypoints)):
        #                        print('Test',keypoints[i].size)
                                #print(keypoints[i].pt[0],keypoints[i].pt[1])
                                roi=(keypoints[i].pt[0]-10,keypoints[i].pt[1]-10,30,30)
                                avg_size.append(keypoints[i].size)
                                m_tracker.add(self.ask_tracker(),frame,roi)
                            #print(len(keypoints),' Keypoints')  
                            avg_size=np.asarray(avg_size)
                            #print(avg_size.mean())
                            #if avg_size.mean()<20:
                            #    brightnessThreshold=1.5
                            #    params.maxArea=1000
                            #    params.minArea=41
                            #elif avg_size.mean()<15:
                            #    brightnessThreshold=2
                            #    params.maxArea=1000
                            #    params.minArea=41
                            #elif avg_size.mean()>20:
                            #    brightnessThreshold=1.7
                            #    params.filterByCircularity=True
                            #    params.minCircularity = 0.85
                            #    params.maxArea=3000
                            #    params.minArea=120
                            #    print('8 inch')
                        
                            total_count=total_count+(len(boxes)-remaining)
                obj_count=0
                frame=cv2.putText(frame,'In Frame:'+str(remaining),(0,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3,cv2.LINE_8)
                #frame=cv2.putText(frame,'Total:'+str(total_count+len(boxes)-remaining),(0,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5,cv2.LINE_8)
                #print(total_count,len(boxes),remaining,total_count+len(boxes)-remaining)
                self.lcdNumber_2.display(total_count+len(boxes)-remaining)
                self.viewCam(frame)
                
                                  
                if (recordStatus==1) & recordFlag:
                    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
                    ext=str(dt.datetime.now().minute)+str(dt.datetime.now().second)
                    out = cv2.VideoWriter('output'+ext+'.mp4', fourcc, 20.0, (1024,768))
                    recordFlag=False
                    print('Initialized')
                elif (recordStatus==1) & (not recordFlag):
                  #  recordFrame=cv2.resize(recordFrame,(1024,768))  
                    out.write(recordFrame)
                    print('Recording')
                elif (recordStatus==0) & (not recordFlag):
                    out.release()
                    recordFlag=True
                    print('Stopped')
                   
                #cv2.imshow('Video',frame)

            if cv2.waitKey(1)==ord('q'):
                break
            if stopExecution==1:
                stopExecution=0
                break
           

        cv2.destroyAllWindows()

 


    def setupUi(self, FurnaceVisionSystem):
        FurnaceVisionSystem.setObjectName("FurnaceVisionSystem")
        FurnaceVisionSystem.resize(2342, 975)
        FurnaceVisionSystem.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(FurnaceVisionSystem)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 167, 1191, 721))
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(4)
        self.label.setMidLineWidth(1)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setPixmap(QtGui.QPixmap("Desktop/Designer\\../../.designer/.designer/backup/100 (1).bmp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 201, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("100px-Danfoss.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 1551, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 164))
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(1220, 160, 641, 721))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 601, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber_2.setFont(font)
        self.lcdNumber_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_2.setAutoFillBackground(False)
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setProperty("intValue", 0)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_5.addWidget(self.lcdNumber_2)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 160, 601, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setTabletTracking(True)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 2, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 390, 601, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.dial_4 = QtWidgets.QDial(self.groupBox_4)
        self.dial_4.setMouseTracking(True)
        self.dial_4.setTabletTracking(False)
        self.dial_4.setAcceptDrops(False)
        self.dial_4.setAutoFillBackground(False)
        self.dial_4.setMaximum(2000)
        self.dial_4.setSingleStep(10)
        self.dial_4.setWrapping(False)
        self.dial_4.setNotchesVisible(True)
        self.dial_4.setObjectName("dial_4")
        self.verticalLayout_19.addWidget(self.dial_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lcdNumber_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.horizontalLayout_4.addWidget(self.lcdNumber_4)
        self.verticalLayout_19.addLayout(self.horizontalLayout_4)
        self.gridLayout_4.addLayout(self.verticalLayout_19, 0, 2, 1, 1)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.dial_5 = QtWidgets.QDial(self.groupBox_4)
        self.dial_5.setMouseTracking(True)
        self.dial_5.setTabletTracking(False)
        self.dial_5.setAcceptDrops(False)
        self.dial_5.setAutoFillBackground(False)
        self.dial_5.setMaximum(1000)
        self.dial_5.setSingleStep(10)
        self.dial_5.setWrapping(False)
        self.dial_5.setNotchesVisible(True)
        self.dial_5.setObjectName("dial_5")
        self.verticalLayout_20.addWidget(self.dial_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_3.addWidget(self.label_16)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lcdNumber_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.horizontalLayout_3.addWidget(self.lcdNumber_3)
        self.verticalLayout_20.addLayout(self.horizontalLayout_3)
        self.gridLayout_4.addLayout(self.verticalLayout_20, 0, 1, 1, 1)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.dial_6 = QtWidgets.QDial(self.groupBox_4)
        self.dial_6.setMouseTracking(True)
        self.dial_6.setTabletTracking(False)
        self.dial_6.setAcceptDrops(False)
        self.dial_6.setAutoFillBackground(False)
        self.dial_6.setMaximum(200)
        self.dial_6.setWrapping(False)
        self.dial_6.setNotchesVisible(True)
        self.dial_6.setObjectName("dial_6")
        self.verticalLayout_21.addWidget(self.dial_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.label_17)
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_2.addWidget(self.lcdNumber)
        self.verticalLayout_21.addLayout(self.horizontalLayout_2)
        self.gridLayout_4.addLayout(self.verticalLayout_21, 0, 0, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.Capture_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.Capture_2.setObjectName("Capture_2")
        self.verticalLayout_22.addWidget(self.Capture_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_22.addWidget(self.pushButton_4)
        self.horizontalLayout_9.addLayout(self.verticalLayout_22)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.Set_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.Set_3.setObjectName("Set_3")
        self.verticalLayout_23.addWidget(self.Set_3)
        self.Set_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.Set_4.setObjectName("Set_4")
        self.verticalLayout_23.addWidget(self.Set_4)
        self.horizontalLayout_9.addLayout(self.verticalLayout_23)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.Track_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.Track_3.setObjectName("Track_3")
        self.verticalLayout_24.addWidget(self.Track_3)
        self.Track_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.Track_4.setObjectName("Track_4")
        self.verticalLayout_24.addWidget(self.Track_4)
        self.horizontalLayout_9.addLayout(self.verticalLayout_24)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(760, 100, 531, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(760, 120, 531, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        FurnaceVisionSystem.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FurnaceVisionSystem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2342, 20))
        self.menubar.setObjectName("menubar")
        FurnaceVisionSystem.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FurnaceVisionSystem)
        self.statusbar.setObjectName("statusbar")
        FurnaceVisionSystem.setStatusBar(self.statusbar)

        self.Capture_2.clicked.connect(self.capture)
        self.Set_3.clicked.connect(self.set_params)
        self.Track_3.clicked.connect(self.realtime_capture)
        self.pushButton_3.clicked.connect(self.updatePartCode)
        self.Track_4.clicked.connect(self.exit_function)
        self.pushButton_4.clicked.connect(self.capture_function)
        self.Set_4.clicked.connect(self.stopSet)
        self.radioButton.toggled.connect(self.record)
     
        self.retranslateUi(FurnaceVisionSystem)
        QtCore.QMetaObject.connectSlotsByName(FurnaceVisionSystem)


    def retranslateUi(self, FurnaceVisionSystem):
        _translate = QtCore.QCoreApplication.translate
          
        date=''
        shift=''
        d=dt.datetime.now().weekday()
        if d==1:
            date="Monday"
        elif d==2:
            date="Tuesday"
        elif d==3:
            date='Wednesday'
        elif d==4:
            date='Thursday'
        elif d==5:
            date='Friday'
        elif d==6:
            date='Saturday'
        elif date==7:
            date='Sunday'
    

        date=date+', '+str(dt.datetime.now().strftime("%B"))+' '+str(dt.datetime.now().day)
        
        if (int(dt.datetime.now().hour)>=6) & (int(dt.datetime.now().hour)<14):
            shift='Morning Shift'
        elif (int(dt.datetime.now().hour)>=14) &(int(dt.datetime.now().hour)<22):
            shift='Afternoon Shift'
        else:
            shift='Night Shift'
        self.label_12.setText(str(date))
        self.label_11.setText(str(shift))

        FurnaceVisionSystem.setWindowTitle(_translate("FurnaceVisionSystem", "Furnace Vision System"))
        self.label_2.setText(_translate("FurnaceVisionSystem", "Object Detection and Tracking  Portal"))
        self.groupBox.setTitle(_translate("FurnaceVisionSystem", "Control Panel"))
        self.groupBox_2.setTitle(_translate("FurnaceVisionSystem", "Counter"))
        self.label_14.setText(_translate("FurnaceVisionSystem", "Parts produced"))
        self.groupBox_3.setTitle(_translate("FurnaceVisionSystem", "Production Update"))
        self.label_13.setText(_translate("FurnaceVisionSystem", "PartCode"))
        self.pushButton_3.setText(_translate("FurnaceVisionSystem", "Update PartCode"))
        self.pushButton_5.setText(_translate("FurnaceVisionSystem", "Clear"))
        self.groupBox_4.setTitle(_translate("FurnaceVisionSystem", "Control Panel"))
        self.radioButton_2.setText(_translate("FurnaceVisionSystem", "Disable"))
        self.radioButton.setText(_translate("FurnaceVisionSystem", "Record"))
        self.label_15.setText(_translate("FurnaceVisionSystem", "max Threshold"))
        self.label_16.setText(_translate("FurnaceVisionSystem", "min Threshold"))
        self.label_17.setText(_translate("FurnaceVisionSystem", "Adjust Brightness"))
        self.Capture_2.setText(_translate("FurnaceVisionSystem", "Capture Image"))
        self.pushButton_4.setText(_translate("FurnaceVisionSystem", "Capture"))
        self.Set_3.setText(_translate("FurnaceVisionSystem", "Set Parameters"))
        self.Set_4.setText(_translate("FurnaceVisionSystem", "Confirm"))
        self.Track_3.setText(_translate("FurnaceVisionSystem", "Start Tracking"))
        self.Track_4.setText(_translate("FurnaceVisionSystem", "Stop Tracking"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FurnaceVisionSystem = QtWidgets.QMainWindow()
    ui = Ui_FurnaceVisionSystem()
    ui.setupUi(FurnaceVisionSystem)
    FurnaceVisionSystem.show()
    sys.exit(app.exec_())


