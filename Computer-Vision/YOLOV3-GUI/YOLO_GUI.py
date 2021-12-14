# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:27:46 2020

@author: Sandheep Gopinath
"""

import cv2
import time
import numpy as np
import tkinter as tk
import tkinter.font as tkFont
message='YOL Algorithm Tester'





def yolo():
    
    global message
    
    with open('yolo-coco-data/coco.names') as file:
        labels=[lab.strip() for lab in file]
        
    network=cv2.dnn.readNetFromDarknet('yolo-coco-data/yolov3.cfg','yolo-coco-data/yolov3.weights')
    

    
    layers_names=network.getLayerNames()
    
    output_layers=[layers_names[int(i-1)] for i in network.getUnconnectedOutLayers()]
    
    min_probability=0.88
    
    threshold=0.3
    

    cap=cv2.VideoCapture(0)
    
    ret=True

    
    while ret:
        ret,frame=cap.read()
        frame=cv2.resize(frame,(1024,780))
        cv2.imshow('Press C to capture',frame)
        h,w=frame.shape[:2]
        ifblob=cv2.dnn.blobFromImage(frame,1/255,(416,416),swapRB=False,crop=False)
        # IFBLOB is a 4 dimensional array
        im=ifblob[0,:,:,:].transpose(1,2,0)
        
        
        if cv2.waitKey(1) & 0xFF == ord('c'):
            break
        
    cap.release()
    network.setInput(ifblob)
    start=time.time()
    model_output=network.forward(output_layers)
    
    bounding_boxes=[]
    confidences=[]
    class_numbers=[]
    
    for result in model_output:
       for detected_object in result:
            scores=detected_object[5:]
            class_current=np.argmax(scores)
            confidence_current=scores[class_current]
            if confidence_current>min_probability:
                
                
                box=detected_object[0:4]*np.array([w,h,w,h])
                xc,yc,bw,bh=box
                xmin=int(xc-(bw/2))
                ymin=int(yc-(bh/2))
                boxwidth=int(bw)
                boxheight=int(bh)
                bounding_boxes.append([xmin,ymin,boxwidth,boxheight])
                confidences.append(float(confidence_current))
                class_numbers.append(class_current)
                
  
                 #Non Max Supression
                results=cv2.dnn.NMSBoxes(bounding_boxes,confidences,min_probability,threshold)
                
                if len(results)>0:
                    for i in results.flatten():
                        print(i)
                        xm,ym,wm,hm=bounding_boxes[i][0],bounding_boxes[i][1],bounding_boxes[i][2],bounding_boxes[i][3]
                        cv2.rectangle(frame, (xm, ym), (xm + wm, ym+hm),(0,255,0), 2)
                        cv2.putText(frame,str(labels[class_numbers[i]]),(xm,ym),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
                        cv2.putText(frame,str(np.round(confidences[i]*100,2))+'%',(xm,ym-30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
                        
    cv2.imshow('Press Q to Quit',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      cv2.destroyAllWindows()
 

def yolo_video():
    
    global message
    
    with open('yolo-coco-data/coco.names') as file:
        labels=[lab.strip() for lab in file]
        
    network=cv2.dnn.readNetFromDarknet('yolo-coco-data/yolov3.cfg','yolo-coco-data/yolov3.weights')
    
    
    layers_names=network.getLayerNames()
    
    output_layers=[layers_names[int(i-1)] for i in network.getUnconnectedOutLayers()]
    
    min_probability=0.50
    
    threshold=0.3
    
    
        
    fourcc=cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter('videos/result-traffic-cars.mp4', fourcc, 30,(1280,720), True)
    
    cap=cv2.VideoCapture('videos/traffic-cars.mp4')
    
    ret=True
    start=time.time()
    
    while ret:
        ret,frame=cap.read()
        
            
        if not ret:
            break
        
        h,w=frame.shape[:2]
       
       

        ifblob=cv2.dnn.blobFromImage(frame,1/255,(416,416),swapRB=False,crop=False)
        # IFBLOB is a 4 dimensional array
        im=ifblob[0,:,:,:].transpose(1,2,0)
        
        network.setInput(ifblob)
      
        model_output=network.forward(output_layers)
        
        bounding_boxes=[]
        confidences=[]
        class_numbers=[]
        
        for result in model_output:
            
            
           for detected_object in result:
               
                scores=detected_object[5:]
                
                class_current=np.argmax(scores)
                
                confidence_current=scores[class_current]
                
                
                
                
                
                
                
                
                if confidence_current>min_probability:
                    fstart=time.time()
              
           
                    box=detected_object[0:4]*np.array([w,h,w,h])
                    xc,yc,bw,bh=box
                    xmin=int(xc-(bw/2))
                    ymin=int(yc-(bh/2))
                    boxwidth=int(bw)
                    boxheight=int(bh)
                    bounding_boxes.append([xmin,ymin,boxwidth,boxheight])
                    
                    
                    confidences.append(float(confidence_current))
                    class_numbers.append(class_current)
    
                  
        
                    results=cv2.dnn.NMSBoxes(bounding_boxes,confidences,min_probability,threshold)
                    print(len(results))
                    if len(results)>0:
                        for i in results.flatten():
                            xm,ym,wm,hm=bounding_boxes[i][0],bounding_boxes[i][1],bounding_boxes[i][2],bounding_boxes[i][3]
                            cv2.rectangle(frame, (xm, ym), (xm + wm, ym+hm),(0,255,0), 2)
                            cv2.putText(frame,str(labels[class_numbers[i]]),(xm,ym),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)
                            cv2.putText(frame,str(np.round(confidences[i]*100,2))+'%',(xm,ym-30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)
                            writer.write(frame)
                            cv2.imshow('Processed',frame)
                            #print(time.time()-fstart)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()
    
    print('Toal Time',time.time()-start)
    

def yolo_webcam():
    
    global message
    
    with open('yolo-coco-data/coco.names') as file:
        labels=[lab.strip() for lab in file]
        
    network=cv2.dnn.readNetFromDarknet('yolo-coco-data/yolov3.cfg','yolo-coco-data/yolov3.weights')
    
    
    layers_names=network.getLayerNames()
    
    output_layers=[layers_names[int(i-1)] for i in network.getUnconnectedOutLayers()]
    
    min_probability=0.50
    
    threshold=0.3
    
    
 
    cap=cv2.VideoCapture(0)
    
    ret=True
    
    while ret:
        ret,frame=cap.read()
        
            
        if not ret:
            break
        
        h,w=frame.shape[:2]
       
       

        ifblob=cv2.dnn.blobFromImage(frame,1/255,(416,416),swapRB=False,crop=False)
        # IFBLOB is a 4 dimensional array
        im=ifblob[0,:,:,:].transpose(1,2,0)
        
        network.setInput(ifblob)
      
        model_output=network.forward(output_layers)
        
        bounding_boxes=[]
        confidences=[]
        class_numbers=[]
        
        for result in model_output:
            
            
           for detected_object in result:
               
                scores=detected_object[5:]
                
                class_current=np.argmax(scores)
                
                confidence_current=scores[class_current]
                
                
                
                
                
                
                
                
                if confidence_current>min_probability:
              
           
                    box=detected_object[0:4]*np.array([w,h,w,h])
                    xc,yc,bw,bh=box
                    xmin=int(xc-(bw/2))
                    ymin=int(yc-(bh/2))
                    boxwidth=int(bw)
                    boxheight=int(bh)
                    bounding_boxes.append([xmin,ymin,boxwidth,boxheight])
                    
                    
                    confidences.append(float(confidence_current))
                    class_numbers.append(class_current)
    
                  
        
                    results=cv2.dnn.NMSBoxes(bounding_boxes,confidences,min_probability,threshold)
                    print(len(results))
                    if len(results)>0:
                        for i in results.flatten():
                            xm,ym,wm,hm=bounding_boxes[i][0],bounding_boxes[i][1],bounding_boxes[i][2],bounding_boxes[i][3]
                            cv2.rectangle(frame, (xm, ym), (xm + wm, ym+hm),(0,255,0), 2)
                            cv2.putText(frame,str(labels[class_numbers[i]]),(xm,ym),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)
                            cv2.putText(frame,str(np.round(confidences[i]*100,2))+'%',(xm,ym-30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)
                            cv2.imshow('Processed',frame)
                            #print(time.time()-fstart)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()
    

class App:
    def __init__(self, root):
        #setting title
        root.title("YOLO Tester Toolkit 1.0")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_434=tk.Button(root)
        GButton_434["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_434["font"] = ft
        GButton_434["fg"] = "#000000"
        GButton_434["justify"] = "center"
        GButton_434["text"] = "Object detection with Photos"
        GButton_434.place(x=70,y=110,width=153,height=63)
        GButton_434["command"] = self.GButton_434_command

        GMessage_141=tk.Message(root)
        ft = tkFont.Font(family='Times',size=13)
        GMessage_141["font"] = ft
        GMessage_141["fg"] = "#333333"
        GMessage_141["justify"] = "center"
        GMessage_141["text"] = "Message"
        GMessage_141.place(x=320,y=80,width=177,height=122)

        GButton_409=tk.Button(root)
        GButton_409["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_409["font"] = ft
        GButton_409["fg"] = "#000000"
        GButton_409["justify"] = "center"
        GButton_409["text"] = "Object Detection on Video"
        GButton_409.place(x=70,y=220,width=155,height=66)
        GButton_409["command"] = self.GButton_409_command

        GMessage_117=tk.Message(root)
        ft = tkFont.Font(family='Times',size=13)
        GMessage_117["font"] = ft
        GMessage_117["fg"] = "#333333"
        GMessage_117["justify"] = "center"
        GMessage_117["text"] = "Message"
        GMessage_117.place(x=370,y=240,width=80,height=25)

        GButton_454=tk.Button(root)
        GButton_454["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_454["font"] = ft
        GButton_454["fg"] = "#000000"
        GButton_454["justify"] = "center"
        GButton_454["text"] = "Object detection on Webcam"
        GButton_454.place(x=70,y=330,width=157,height=60)
        GButton_454["command"] = self.GButton_454_command

        GMessage_780=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_780["font"] = ft
        GMessage_780["fg"] = "#333333"
        GMessage_780["justify"] = "center"
        GMessage_780["text"] = "Message"
        GMessage_780.place(x=360,y=350,width=80,height=25)

    def GButton_434_command(self):
        yolo()


    def GButton_409_command(self):
        yolo_video()


    def GButton_454_command(self):
        yolo_webcam()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


