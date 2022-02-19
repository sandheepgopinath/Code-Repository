## Image Classification

### Step 1 : Data Collection

- For this we have used requests and beautiful library
- We pass a query to the function which is created,and a URL for search will be generated. 
- The URL is then executed using the requests function. 
- Image URL from the webpage ae then scrapped
- The images ae then converted into a common shape using open cv and are saved as a numpy npz file and also as images in corresponding folders
- The above function was created for Google and Bing image search. 
- After the images ae scrapped, the suplicate images and invalid images are removed manually. 
- Data Augmentation techniques are also applied on to these images to increase the size of the dataaset and to make the model resistance to change due to rotation,brightness etc
- 