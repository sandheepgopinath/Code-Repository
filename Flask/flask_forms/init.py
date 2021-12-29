from flask import Flask, render_template, request
from preprocess import *
import sqlite3 as sql

# Creating a Flask Object

app=Flask('__name__')
global reviews
global predictions
@app.route('/',methods=['GET'])
@app.route('/submit',methods=['GET','POST'])
def home_page():
    global reviews,predictions
    if request.method=='POST':
        og_review=request.form['review']
        predictor=analyse(str(og_review))
        review=predictor.prediction 
        reviews=og_review
        predictions=review

        with sql.connect('database.db') as connection:
            cursor=connection.cursor()
            cursor.execute("INSERT INTO reviews (review,sentiment) VALUES (?,?)",(og_review,review))
            connection.commit()
        return render_template('result.html',review=review)
    return render_template('hello.html')
        
@app.route('/data')
def database():
    connection=sql.connect('database.db')
    connection.row_factory=sql.Row

    cursor=connection.cursor()
    cursor.execute('select * from reviews')

    rows=cursor.fetchall()
    connection.close()
    return render_template('data.html',rows=rows)

@app.route('/updatefalse',methods=['GET','POST'])
def update_true():
    global reviews
    if request.method=='GET':
        with sql.connect('database.db') as connection:
            cursor=connection.cursor()
            cursor.execute('UPDATE reviews SET status="True" WHERE review="'+str(reviews)+'"')
            connection.commit()

    return render_template('hello.html')        


@app.route('/updatetrue',methods=['GET','POST'])
def update_false():
    global reviews,predictions
    if request.method=='GET':
        print(reviews,predictions)  
        with sql.connect('database.db') as connection:
            cursor=connection.cursor()
            cursor.execute('UPDATE reviews SET status="False" WHERE review="'+str(reviews)+'"')
            connection.commit()

    return render_template('hello.html')

if __name__=='__main__':
    app.run()

