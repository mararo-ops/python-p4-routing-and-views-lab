#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Print to console
    return f'<p>Printed: {param}</p>'

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(param + 1))
    return f'<pre>{numbers}</pre>'

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2

    return f'<p>Result: {result}</p>' if result is not None else '<p>Invalid operation or division by zero</p>'

if __name__ == '__main__':
    app.run(debug=True)

