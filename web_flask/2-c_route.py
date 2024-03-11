#!/usr/bin/python3
"""
Starts a Flask web application.
Defines three routes - /, /hbnb, and /c/<text>
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
    return f'C{text}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
