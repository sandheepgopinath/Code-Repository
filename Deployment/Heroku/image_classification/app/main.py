import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from app import app
import cv2
import os
import tensorflow as tf
from tensorflow import keras

vgg=tf.keras.models.load_model('vgg_layer.h5')
top=tf.keras.models.load_model('top_layer.h5')

app = Flask(__name__)
app.secret_key = os.urandom(24)

def predict(image=None,url=None):
  # Creating a dictionary for labels
  dict={0:'Cat',1:'Pikachu',2:'Kanye West'}

  if url!=None:
    import cv2    
    import numpy as np

    cap=cv2.VideoCapture(url)
    ret,frame=cap.read()
    im=cv2.resize(frame,(250,250))
    image=np.expand_dims(np.array(im),axis=0)
    embedding=vgg.predict(image)
    embedding=np.array(embedding)
   # embedding=np.expand_dims(embedding,axis=1)
    im=cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    #plt.imshow(im)
    #plt.title(dict[np.argmax(top.predict(embedding))],fontsize=15)
    #plt.axis('off')
    print(dict[np.argmax(top.predict(embedding))])

  elif image!=None:
    import cv2
    import numpy as np

    frame=cv2.imread(image)
    im=cv2.resize(frame,(250,250))
    image_e=np.expand_dims(np.array(im),axis=0)
    embedding=vgg.predict(image_e)
    embedding=np.array(embedding)
    im=cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    cv2.rectangle(frame,(0,int(frame.shape[1]-(frame.shape[1]*0.1))),(frame.shape[0],frame.shape[1]),(255,255,255),-1)
    x=int(frame.shape[0]-(frame.shape[0]*0.8))
    y=int(frame.shape[1]-(frame.shape[1]*0.1))
    cv2.putText(frame,'This is '+str(dict[np.argmax(top.predict(embedding))]),(x,y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,2)
    cv2.imwrite(str(image),frame)
    result=str('This is '+str(dict[np.argmax(top.predict(embedding))]))
    return result

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(str(filename))
		#print('static/uploads/'+str(filename))
		result=predict(image=str(filename))
		flash(str(result))
		return render_template('upload.html', filename=filename)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.run()
