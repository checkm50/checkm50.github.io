from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = 'Typing Cat on'
    msgToReturn = msg + host
    return msgToReturn
