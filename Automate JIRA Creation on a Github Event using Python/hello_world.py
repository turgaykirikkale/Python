from flask import Flask

#creating a flask app instance 
app = Flask(__name__)


@app.route("/") #this decorator
def helloWorld():
    return "Hello World"

@app.route("/abc")
def whereAreYou():
    return "Where Are You"

app.run('0.0.0.0')