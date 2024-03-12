#!/usr/bin/python3
"""
Script that starts a Flask web application.
Renders an HMTL webpage that lists all state names
as well as associated City objects.
"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_state', strict_slashes=False)
def cities_by_state():
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
