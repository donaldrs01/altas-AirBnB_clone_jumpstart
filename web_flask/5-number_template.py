#!/usr/bin/python3
"""
Script that starts a Flask web application. 
Contains previous routes as well as a route that renders
HTML template containing H1 tag with n=number.
"""
from flask import Flask, render_template


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


#  Specify that n must be an integer
@app.route('/number/<n>', strict_slashes=False)
def number_display(n):
    if isinstance(n, int):
        return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_number_template(n):
    if isinstance(n, int):
        #  Use render_template function import to display page
        return render_template('5-number.html', n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)