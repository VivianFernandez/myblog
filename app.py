from flask import Flask, app

app = Flask(__name__)
@app.route("/")
def index():
    return "hello world"