#!/usr/bin/python3
"""
Module that prepares a Flask web application
When accessed via the root URL (/), app should display a message
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
