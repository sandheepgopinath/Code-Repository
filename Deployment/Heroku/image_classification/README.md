    # Hosting Flask app on Heroku

    Requirement : 
    - To host an image classification app on Heroku

    ###### Data Folder : Part 2 : Heroku App
    - Contents
        - Pipfile : File with all dependencies: Created automatically from requirements.tx when below command is executed

                pipenv install flask gunicorn
        - Procfile : Details about app to invoke
        - requirements.txt : Used for creatin of Pipfile. Not used iin Heroku. Heorku uses Pipfile
        - runtime.txt : specifies the version of python
        - static : folder to store uploaded images
        - templates : html pages for flask app
        - models: stoired in drive https://drive.google.com/drive/folders/10ZrX58Y0vm4VjRsRJ8kAX4Etur_DetaF?usp=sharing
            - contains vgg layer for creating emnedding and top_layer.h5 for predictions. 
