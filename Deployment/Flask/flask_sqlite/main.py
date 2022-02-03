from flask import Flask,render_template,request
import sqlite3 as sql

app=Flask('__name__')


@app.route('/')
def home():
    return(render_template('home.html'))


@app.route('/send',methods=['POST','GET'])
def enter():
    msg='Nothing Happened'
    try:
        if request.method=='POST':
            name=request.form['name']
            age=request.form['age']
            print(name,age)
            with sql.connect('test_database.db') as con:
                cursor=con.cursor()
                cursor.execute('INSERT INTO Something\
                                (Name,Age)\
                                VALUES (?,?)',(name,age))
                cursor.commit()
        msg='Data Posted'
     
    except:
        msg='Process Failed'
    finally:
        return(render_template('success.html',msg=msg))
        

@app.route('/list')
def data():
    con=sql.connect('test_database.db')
    con.row_factory=sql.Row
    
    cursor=con.cursor()
    cursor.execute('Select * from Something')
    rows=cursor.fetchall()
    return render_template('list.html',rows=rows)

if __name__=='__main__':
    app.run()
