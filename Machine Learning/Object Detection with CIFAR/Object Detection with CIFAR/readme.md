Contents of the Tar file 

: CIFAR.ipynb : The ipinb file
: CIFAR.pdf : pdf version of the above file.
: model.sav : The final model saved in pickle format
: lab1.pdf : Question
: cifar-10-batches-py : The folder with the dataset downloaded from website
: cifar.py : The python file with the cifar class which is defined

: testscript.py : The file which uses the model created to detectobjects from android camera
       : Usage : Download IP Camera from Play Store
       :       : Connect phone and laptop to same network
               : Go to the IP specified in app and test if camera is streamed
               : Change the ip address in testscript.py to the IP address assigned
               : Run the PY script in terminal
               : The live stream window will open and press q on keyboard when the object is focussed
               : The prediction will be displayed on the terminal
        : Although the predictions are not very accurate, it is able to detect the objects
        : Since we are not detecting the posityion of the image, the image has to be clibked in such a way that the object is centered


