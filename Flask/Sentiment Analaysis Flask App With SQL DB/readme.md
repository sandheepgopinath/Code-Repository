<h2> Project to run a Natural Language Processing model on Flask </h2>

Files : 
[+] labelledTrainData.csv : Used by create_model.py to train the model
[+] testData.tsv          : Used by create_model.py to test the model
[+] kill_flask.py         : Helper Python file to Kill the flask process
[+] kill_proces.sh        : Function to kill the flask process so that we don't have to use different ports everytime
[+] requirements.txt      : All dependencies used. Output from pip freeze
[+] test_case.py          : test case to check if all functions are working. If it completes execution without error, it passed the test
[+] preprocess.py         : Python class invoked for preprocessing data and prediction
[+] create_model.py       : Used to create classifier.pkl model
[+] count_vectorizer.pkl  : Pickled version of count vectorizer
[+] create_bd.py          : Used to create the database using sqlite3
[+] init.py               : The flask app file
[+] database.db           : The database file created with sqlite3  
