#!/usr/bin/python3
"""
Starts Flask web application.
Uses storage engine (File or DB) to retrieve data.
Contains a route that lists states present in storage
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    from models import storage
    from models.state import State
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """ Method to close current SQLAlchemy session"""
    from models import storage
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
