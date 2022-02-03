
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
import sys
import tensorflow as tf
import numpy as np
from PIL import Image
from object_detection import ObjectDetection



value=0
params=cv2.SimpleBlobDetector_Params() 
params.filterByArea=True

params.maxArea=3000
params.minArea=90

brightnessThreshold=2
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




MODEL_FILENAME = 'model.pb'
LABELS_FILENAME = 'labels.txt'


class TFObjectDetection(ObjectDetection):
    """Object Detection class for TensorFlow"""

    def __init__(self, graph_def, labels):
        super(TFObjectDetection, self).__init__(labels)
        self.graph = tf.compat.v1.Graph()
        with self.graph.as_default():
            input_data = tf.compat.v1.placeholder(tf.float32, [1, None, None, 3], name='Placeholder')
            tf.import_graph_def(graph_def, input_map={"Placeholder:0": input_data}, name="")

    def predict(self, preprocessed_image):
        inputs = np.array(preprocessed_image, dtype=np.float)[:, :, (2, 1, 0)]  # RGB -> BGR

        with tf.compat.v1.Session(graph=self.graph) as sess:
            output_tensor = sess.graph.get_tensor_by_name('model_outputs:0')
            outputs = sess.run(output_tensor, {'Placeholder:0': inputs[np.newaxis, ...]})
            return outputs[0]


def predictCups(image_filename):
    # Load a TensorFlow model
    graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile(MODEL_FILENAME, 'rb') as f:
        graph_def.ParseFromString(f.read())

    # Load labels
    with open(LABELS_FILENAME, 'r') as f:
        labels = [l.strip() for l in f.readlines()]

    od_model = TFObjectDetection(graph_def, labels)

    image = Image.open(image_filename)
    predictions = od_model.predict_image(image)
    return predictions


print(predictCups('Webcam Capture.jpg'))








