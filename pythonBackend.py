from flask import Flask, request, render_template
import pythonBackend

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
    
@app.route('/login/validation', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST' or request.method == 'GET':
        pass
    
        #pythonBackend.attemptLogIn("username", "password")
    else:
        return "error, wrong fetch type"

@app.route('/create-account', methods = ['GET', 'POST'])
def createAccount():
    if request.method == 'POST' or request.method == 'GET':
        return render_template('create-account.html')
    else:
        return "error, wrong fetch type"


if __name__ == '__main__':
    app.run(debug=True) 