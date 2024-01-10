from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    #printing to console
    print(parameter)

    #display in console
    return(parameter)

@app.route('/count/<int:parameter>')
def count_view(parameter):
    num = range(1, parameter +1)

    return '/n'.join(map(str,num))

@app.route('/math/<float:num1><string:operation><float:num2>')
def math(num1,num2,operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '%':
        result = num1 % num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation"
    
    return f"Result: {result}"
        
if __name__ == '__main__':
    app.run(port=5555, debug=True)
