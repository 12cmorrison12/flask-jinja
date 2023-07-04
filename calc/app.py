from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def to_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('a'))
    result = add(a,b)

    return str(result)

@app.route('/sub')
def to_sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('a'))
    result = sub(a,b)

    return str(result)

@app.route('/mult')
def to_mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('a'))
    result = mult(a,b)

    return str(result)

@app.route('/div')
def to_div():
    a = int(request.args.get('a'))
    b = int(request.args.get('a'))
    result = div(a,b)

    return str(result)