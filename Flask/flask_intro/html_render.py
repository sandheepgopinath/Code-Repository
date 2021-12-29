from flask import Flask,render_template

# Creating a flask object
app=Flask('__name__')

@app.route('/')
def home_page():
    return render_template('hello.html')

if __name__=='__main__':
    app.run()
