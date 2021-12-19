class cifar():
    def __init__(self,filepath):
        """ This initialises the filepath to the directory where the files are present """
        self.filepath=filepath
        self.batch1=None
        self.batch2=None
        self.map=dict()
        self.map_labels()
        self.n_labels=len(self.map)
        self.model=None

    def load_best_model(self):
        """ The function will load the model from the folder thus making it easier to do predictions and testing"""
        import pickle
        self.model=pickle.load(open('cnnModel81.sav','rb'))
      
    def test_prediction(self,array):
        """ The function takes as input an image, does the prediction 
      and the prints the image along with the predicted label thus helping to make testing easier

      If the model has to be changed to a custom model, do
      cf.model=<newmodel>
      to restore the best model do
      cf.load_best_model()"""
        import numpy as np
        self.plot(array,self.label_decode(np.argmax(self.model.predict(array.reshape(1,32,32,3)))))

      
    def map_labels(self):
        """ The function reads the batches.meta file and converts the lists and labels to a dictionary for 
        easy access later """
        content=self.unpickle('batches.meta')
        content=content[b'label_names']
        for i,number in enumerate(content):
            self.map[i]=number.decode('utf-8')
            
    def label_decode(self,id):
        """ Returns the Label name of the ID which is being passed into the function"""
        return self.map[id]
        
    def unpickle(self,filename):
        """ The function takes a filename and returns the dictionary of data inside the file. 
            The data is pickled and stored in the files and hence this function helps to unpack
            the data. 

            Usage : data=unpickle('batches.meta')
            Return : Dictionary of data
            Data inside the dictionary can be explored using data.keys and other dictionary functions """

        filepath=self.filepath+filename
        import pickle
        with open(filepath,'rb') as foo:
            dict=pickle.load(foo,encoding='bytes')
        return dict
    
    def convert_to_rgb(self,array):
        """ The function takes a flattened array as input and converts it into a RGB Image.
        It normalises the image by didving by 255 and then stacks it depth wise to get an RGB Image. """
    
        import numpy as np
        r=array[0:1024].reshape(32,32)/255
        g=array[1024:2048].reshape(32,32)/255
        b=array[2048:].reshape(32,32)/255
        im=np.dstack((r,g,b))
        return im

    
    def read_batch_data(self,id):
        """ Function takes as input the number of the batch file to be read
            It then reads the data and corresponding label of the data from the file
            and then converts it into RGB images. 
            The function return the images and labels which can later be used for training 
            or validation. 
            """
        import numpy as np
        filename='data_batch_'+str(id)
        data=self.unpickle(filename)
        y=data[b'labels']
        x=data[b'data']
        images=[]
        for image in x:
            images.append(self.convert_to_rgb(image))
        return np.array(images),np.array(y)
    
    
    def read_test_batch(self):
        """ The function already has a set of testing data file. Calling this function would
        read the corresponding testing file and would then convert the data into images and labels
        in the same way as in the read-batch-data function. 
        The function then returns the images and its associated labels which are later used as test data 
        during the process
        """
        import numpy as np
        filename='test_batch'
        data=self.unpickle(filename)
        y=data[b'labels']
        x=data[b'data']
        images=[]
        for image in x:
            images.append(self.convert_to_rgb(image))
        return np.array(images),np.array(y)
    
    def OHE(self,list_of_values):
        """ Since the output columns are label encoded, invoking the OHE function 
        would convert the label encoded outputs to One Hot Encoded Outputs and returns the same
        The function takes as input a list of the labels 
        """
        import numpy as np
        result=np.zeros((len(list_of_values),self.n_labels))
        for i in range(len(list_of_values)):
            result[i][list_of_values[i]]=1
        return result

    def plot(self,array,label):
        """ A helper function to plot an image""" 
        import matplotlib.pyplot as plt
        print(label)
        plt.imshow(array)
