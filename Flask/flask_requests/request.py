from flask import Flask,render_template,request
app=Flask('__name__')

@app.route('/')
def home_page():
    return f"welcome to the Flask requests Library"

@app.route('/query',methods=['GET','POST'])
def requests_function():
    if request.method=='GET':
        args=request.args

    name=args['name']
    input1=args['num1']
    input2=args['num2']
    output=input1+input2

    return f"Hello, {name}, \n The Sum of the given number is {output}"


if __name__=='__main__':
    app.run()

