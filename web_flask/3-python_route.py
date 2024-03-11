#!/usr/bin/python3
"""
Script for starting a Flask web application
Contains previous 3 methods + Python method
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text_display(text):
    text = text.replace('_', ' ')
    return f'C {text}'


#  Provide route for when text is not included after 'Python'
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_display(text="is cool"):
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
