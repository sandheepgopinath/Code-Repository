from flask import Flask, render_template, request
from preprocess import *
import sqlite3 as sql

# Creating a Flask Object

app=Flask('__name__')

@app.route('/',methods=['GET'])
@app.route('/submit',methods=['GET','POST'])
def home_page():
    if request.method=='POST':
        og_review=request.form['review']
        predictor=analyse(str(og_review))
        review=predictor.prediction
        
        with sql.connect('database.db') as connection:
            cursor=connection.cursor()
            cursor.execute("INSERT INTO review (review,sentiment) VALUES (?,?)",(og_review,review))
            connection.commit()
        return render_template('result.html',review=review)
    return render_template('hello.html')
        
@app.route('/data')
def database():
    connection=sql.connect('database.db')
    connection.row_factory=sql.Row

    cursor=connection.cursor()
    cursor.execute('select * from review')

    rows=cursor.fetchall()
    connection.close()
    return render_template('data.html',rows=rows)

if __name__=='__main__':
    app.run()
