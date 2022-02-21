## Image Classification
### Image Classification

###### Requirement 
- To scrap data of Pikachu, Kanye West and cats from internet
- To train a CNN model
- To get good confusion matrix
- Bonus : To deploy the solution online

###### Data Folder : Image Classification

- Contents
 	- README.md : Details abour process and steps followed
    - <a href='https://drive.google.com/drive/folders/1n2SdiXbp4_ZAnbFXlKC8E191340qdSyY?usp=sharing'>Data</a> : Images used for training
    - Data Scraping : The code used for scraping images from Google Images and Bing
    - <a href='https://drive.google.com/drive/folders/1-rpMfLOdLmHvzle5KuPzlQVySOJ4IcRg?usp=sharing'>Models</a> : The VGG and top_layer models in h5 format
    - Notebooks : Notebooks used for model training and prediction
    - Weights : Model weights used for creating the model

### Step 1 : Data Collection

- For this we have used requests and beautiful library
- We pass a query to the function which is created,and a URL for search will be generated. 
- The URL is then executed using the requests function. 
- Image URL from the webpage ae then scrapped
- The images ae then converted into a common shape using open cv and are saved as a numpy npz file and also as images in corresponding folders
- The above function was created for Google and Bing image search. 
- After the images ae scrapped, the suplicate images and invalid images are removed manually. 
- Data Augmentation techniques are also applied on to these images to increase the size of the dataaset and to make the model resistance to change due to rotation,brightness etc

- With this around 6000 images were created for each class

### Step 2 :  Model Building
- For model building, since the dataset has close similarity with Imagenet dataset, we have used a the pretrained weights from VGG16
- We have excluded the top layer,as the classes we have are very different from the ImageNet problem
- We have created word embeddings using the VGG model and this is used as input for training the last few layers which we have created
- The VGG and top_layer which are the two seperate models used are saved as h5 files and are used for later predictions

### Step 3 : Predictions
- A seperate function has been created for prediction where the user can give a url of the image to be predicted
- The function will download this image and convert it into the standard size required for the model.
- The image is passd through the vgg layer to get the embedding
- The embedding is then passed through the top layer to get the prediction
- The image and prediction are then displayed for the user
---

##### Folders : 
- Data : Images used for training
- Data Scraping : The code used for scraping images from Google Images and Bing
- <a href='https://drive.google.com/drive/folders/1-rpMfLOdLmHvzle5KuPzlQVySOJ4IcRg?usp=sharing'>Models</a> : The VGG and top_layer models in h5 format
- Notebooks : Notebooks used for model training and prediction
- Weights : Model weights used for creating the model

