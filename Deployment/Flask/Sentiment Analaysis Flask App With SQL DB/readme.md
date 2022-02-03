<h2> Project to run a Natural Language Processing model on Flask </h2>
<br><br><br><br>
Files : 

<br><br>
[+] labelledTrainData.csv : Used by create_model.py to train the model
<br><br>
[+] testData.tsv          : Used by create_model.py to test the model
<br><br>
[+] kill_flask.py         : Helper Python file to Kill the flask process
<br><br>[+] kill_proces.sh        : Function to kill the flask process so that we don't have to use different ports everytime
<br><br>[+] requirements.txt      : All dependencies used. Output from pip freeze
<br><br>[+] test_case.py          : test case to check if all functions are working. If it completes execution without error, it passed the test
<br><br>[+] preprocess.py         : Python class invoked for preprocessing data and prediction
<br><br>[+] create_model.py       : Used to create classifier.pkl model
<br><br>[+] count_vectorizer.pkl  : Pickled version of count vectorizer
<br><br>[+] create_bd.py          : Used to create the database using sqlite3
<br><br>[+] init.py               : The flask app file
<br><br>[+] database.db           : The database file created with sqlite3  
