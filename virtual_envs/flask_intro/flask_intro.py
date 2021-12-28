from flask import Flask # Importing flask class

# Create a flask object
app=Flask('__name__')

#Setup a decorator, where the function can be accessed from the URL
@app.route('/')
def welcome():
    return(' Flask Intro')

@app.route('/user/<name>')
def welcome_by_name(name):
    return f"Hello,{name}"

if __name__=='__main__':
    app.run()

