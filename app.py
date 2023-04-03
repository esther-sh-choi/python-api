from flask import flask


app = Flask(__name__)

@app.route('/')
def hello_ghw():
    return "<p>Hello, API Week Hackers!</p>"