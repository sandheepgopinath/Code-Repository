from flask import Flask, render_template,request
app = Flask('__name__')

@app.route('/') # decorator to tell Flask what URL should trigger the function below
def index():
    return('Home page')


d = {'name':'Alex','location':'Sweden'}

@app.route("/data")
def data():
    return(d)


@app.route('/query-example', methods=['GET','POST'])
def json_example():
    if request.method == 'POST':
        req_data = request.get_json()
        
    if request.method == 'GET':
        req_data = request.args
        # example: http://127.0.0.1:5000/query-example?name=alex&num1=2&num2=2

        
    name = req_data['name']
    num1 = req_data['num1']
    num2 = req_data['num2']    
    res = num1+num2

    return '''
           The name value is: {}
           The added number is: {}'''.format(name,res)


if __name__ == '__main__':
    app.run()
