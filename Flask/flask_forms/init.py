from flask import Flask, render_template, request
from preprocess import *
# Creating a Flask Object

app=Flask('__name__')

@app.route('/',methods=['GET'])
@app.route('/submit',methods=['GET','POST'])
def home_page():
    if request.method=='POST':
        review=request.form['review']
        predictor=analyse(str(review))
        review=predictor.prediction
        return render_template('result.html',review=review)
    return render_template('hello.html')

if __name__=='__main__':
    app.run()
