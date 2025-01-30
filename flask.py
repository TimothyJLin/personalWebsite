from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST' or request.method == 'GET':
        return render_template('login.html')
    else:
        return "error, wrong fetch type"

