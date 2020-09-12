from flask import Flask

app = Flask(__name__)

@app.route('/' ) # http://www.google.com/
def home(): # whatever the function does it has to return a response to the browser
    return 'Hello, world!'

@app.route('/easy/' ) # http://www.google.com/
def easy(): # whatever the function does it has to return a response to the browser
    return 'This is easy!'

app.run(port=5000)
