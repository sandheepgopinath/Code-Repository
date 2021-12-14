# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:04:06 2020
#Training for Object Detection and Tracking Algorithm

@author: Sandheep Gopinath
"""





import cv2
import os
import time
import tkinter as tk
import tkinter.font as tkFont


def capture():
    
    cap = cv2.VideoCapture(0)


    while(True):
        # Capture frame-by-frame
        
        ret, frame = cap.read()
        cv2.imshow('Image',frame)
    
       ## Save image when S is pressed
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('Webcam Capture.jpg',frame)
            break


    cap.release()
    cv2.destroyAllWindows()
    


def set_params():
    global label
    def do_nothing(x):
        pass
    cv2.namedWindow('Track Bars')
    
    cv2.createTrackbar('min_blue','Track Bars',0,255,do_nothing)
    cv2.createTrackbar('min_green','Track Bars',0,255,do_nothing)
    cv2.createTrackbar('min_red','Track Bars',0,255,do_nothing)
    
    cv2.createTrackbar('max_blue','Track Bars',0,255,do_nothing)
    cv2.createTrackbar('max_green','Track Bars',0,255,do_nothing)
    cv2.createTrackbar('max_red','Track Bars',0,255,do_nothing)
    
    
    im=cv2.imread('Webcam Capture.jpg')
    im=cv2.resize(im,(640,480))
    # Converting to HSV Color Space
    
    im_HSV=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
        
    cv2.imshow('Original',im)
    cv2.imshow('HSV',im_HSV)
    #Gettingtrackbar values
    while True:
       
        min_blue=cv2.getTrackbarPos('min_blue','Track Bars')
        min_green=cv2.getTrackbarPos('min_green','Track Bars')
        min_red=cv2.getTrackbarPos('min_red','Track Bars')
    
        max_blue=cv2.getTrackbarPos('max_blue','Track Bars')
        max_green=cv2.getTrackbarPos('max_green','Track Bars')
        max_red=cv2.getTrackbarPos('max_red','Track Bars')
    
    
        mask=cv2.inRange(im_HSV,(min_blue,min_green,min_red),(max_blue,max_green,max_red))
    
        cv2.namedWindow('Image')
        cv2.imshow('Image',mask)
    
    
        if cv2.waitKey(1)==ord('q'):
            break
        
    cv2.destroyAllWindows()
    print(min_blue,min_green,min_red,max_blue,max_green,max_red)
    label=str(input('Enter label name : '))
    return min_blue,min_green,min_red,max_blue,max_green,max_red


def track(min_blue,min_green,min_red,max_blue,max_green,max_red):
    
   # min_blue,min_green,min_red=0,0,204
   # max_blue,max_green,max_red=107,35,255
    global area,label
    cap = cv2.VideoCapture(0)
    print(min_blue,min_green,min_red,max_blue,max_green,max_red)
    
    
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        im=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(im,(min_blue,min_green,min_red),(max_blue,max_green,max_red))
        contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        contours=sorted(contours,key=cv2.contourArea,reverse=True)

        try:
            if cv2.contourArea(contours[0])>area:
                x,y,w,h=cv2.boundingRect(contours[0])
                cv2.rectangle(frame,(x-15,y-15),(x+w+15,y+h+15),(0,255,0),3)
                cv2.putText(frame,str(label),(x,y-25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                #cv2.putText(frame,str(cv2.contourArea(contours[0])),(x+35,y-25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            else:
                cv2.putText(frame,'No Detection',(200,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        except:
            #cv2.putText(frame,'No Detection',(200,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            pass
        cv2.imshow('Webcam Mask',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def set_area():
    
    cap = cv2.VideoCapture(0)
    
    
    
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        im=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(im,(min_blue,min_green,min_red),(max_blue,max_green,max_red))
        contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        contours=sorted(contours,key=cv2.contourArea,reverse=True)
 
        try:
            if cv2.contourArea(contours[0])>500:
                x,y,w,h=cv2.boundingRect(contours[0])
                cv2.rectangle(frame,(x-15,y-15),(x+w+15,y+h+15),(0,255,0),3)
                cv2.putText(frame,str(cv2.contourArea(contours[0])),(x,y-25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            else:
                cv2.putText(frame,'No Detection',(200,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        except:
            cv2.putText(frame,'No Detection',(200,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.putText(frame,'Press S to save detection area',(20,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow('Webcam Mask',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return cv2.contourArea(contours[0])
    
min_blue=0
min_green=0
min_red=0
max_blue=0
max_green=0
max_red=0
area=0
label=''
message=''
#'Min Blue : '+str(min_blue)+' Min Red : '+str(min_red)+' Min Green :'+str(min_green)+ 'Max Blue : '+str(max_blue)+'  Max Red : '+str(max_red)+'  Max Green :'+str(max_green)
def main():
    global min_blue,min_green,min_red,max_blue,max_green,max_red,area
    choice=0

    while(choice!=9):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Enter 0 to Capture Image')
        print('Enter 1 to set parameters')
        print('Enter 2 Modify detection area')
        print('Enter 3 Test Tracking')
        print('Enter 4 to show set values')
        print('Enter 5 to reset parameters')
        print('Enter 9 to exit')
        
        choice=int(input('Enter choice  :  '))
        
        
        if choice==0:
            capture()
            time.sleep(1)
        elif choice==1:
            min_blue,min_green,min_red,max_blue,max_green,max_red=set_params()
            time.sleep(1)
        elif choice==2:
            area=set_area()
            time.sleep(1)
        elif choice==3:
            track(min_blue,min_green,min_red,max_blue,max_green,max_red)
            time.sleep(1)
        elif choice==4:
            print('Parameters :',min_blue,min_green,min_red,max_blue,max_green,max_red)
            print('Area: ',area)
            time.sleep(2)
        elif choice==5:
            min_blue=0
            min_green=0
            min_red=204
            max_blue=107
            max_green=35
            max_red=255
            time.sleep(1)
        elif choice==9:
            break    


class App:
    def __init__(self, root):
        #setting title
        global message
        root.title("Visual Image Callibration Portal V1.0")
        #setting window size
        width=631
        height=604
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_41=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_41["font"] = ft
        GLabel_41["fg"] = "#333333"
        GLabel_41["justify"] = "center"
        GLabel_41["text"] = "Capture an Image"
        GLabel_41.place(x=50,y=100,width=183,height=46)

        GButton_682=tk.Button(root)
        GButton_682["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_682["font"] = ft
        GButton_682["fg"] = "#000000"
        GButton_682["justify"] = "center"
        GButton_682["text"] = "Capture"
        GButton_682.place(x=380,y=100,width=121,height=46)
        GButton_682["command"] = self.GButton_682_command

        GLabel_117=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_117["font"] = ft
        GLabel_117["fg"] = "#333333"
        GLabel_117["justify"] = "center"
        GLabel_117["text"] = "Set detection parameters"
        GLabel_117.place(x=40,y=170,width=258,height=51)

        GButton_450=tk.Button(root)
        GButton_450["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_450["font"] = ft
        GButton_450["fg"] = "#000000"
        GButton_450["justify"] = "center"
        GButton_450["text"] = "Calibrate"
        GButton_450.place(x=380,y=170,width=124,height=45)
        GButton_450["command"] = self.GButton_450_command

        GLabel_25=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_25["font"] = ft
        GLabel_25["fg"] = "#333333"
        GLabel_25["justify"] = "center"
        GLabel_25["text"] = "Set detection area"
        GLabel_25.place(x=10,y=230,width=278,height=76)

        GButton_403=tk.Button(root)
        GButton_403["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_403["font"] = ft
        GButton_403["fg"] = "#000000"
        GButton_403["justify"] = "center"
        GButton_403["text"] = "Set Area"
        GButton_403.place(x=380,y=240,width=128,height=47)
        GButton_403["command"] = self.GButton_403_command

        GLabel_431=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_431["font"] = ft
        GLabel_431["fg"] = "#333333"
        GLabel_431["justify"] = "center"
        GLabel_431["text"] = "Test Tracking"
        GLabel_431.place(x=30,y=320,width=205,height=36)

        GButton_281=tk.Button(root)
        GButton_281["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_281["font"] = ft
        GButton_281["fg"] = "#000000"
        GButton_281["justify"] = "center"
        GButton_281["text"] = "Track"
        GButton_281.place(x=380,y=310,width=128,height=47)
        GButton_281["command"] = self.GButton_281_command

        GLabel_630=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_630["font"] = ft
        GLabel_630["fg"] = "#333333"
        GLabel_630["justify"] = "center"
        GLabel_630["text"] = "Reset Parameters"
        GLabel_630.place(x=20,y=390,width=268,height=37)

        GButton_373=tk.Button(root)
        GButton_373["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_373["font"] = ft
        GButton_373["fg"] = "#000000"
        GButton_373["justify"] = "center"
        GButton_373["text"] = "Reset"
        GButton_373.place(x=380,y=380,width=130,height=48)
        GButton_373["command"] = self.GButton_373_command

        GMessage_153=tk.Message(root)
        ft = tkFont.Font(family='Times',size=13)
        GMessage_153["font"] = ft
        GMessage_153["fg"] = "#333333"
        GMessage_153["justify"] = "center"
        GMessage_153["text"] = str(message)
        GMessage_153.place(x=0,y=430,width=637,height=174)

    def GButton_682_command(self):
        capture()
        time.sleep(1)

    def GButton_450_command(self):
        global min_blue,min_green,min_red,max_blue,max_green,max_red
        min_blue,min_green,min_red,max_blue,max_green,max_red=set_params()
        time.sleep(1)

    def GButton_403_command(self):
        global area
        area=set_area()
        time.sleep(1)

    def GButton_281_command(self):
        track(min_blue,min_green,min_red,max_blue,max_green,max_red)
        time.sleep(1)


    def GButton_373_command(self):
        global min_blue,min_green,min_red,max_blue,max_green,max_red
        min_blue=0
        min_green=0
        min_red=204
        max_blue=107
        max_green=35
        max_red=255
        time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
