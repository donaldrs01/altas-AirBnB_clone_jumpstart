#!/usr/bin/python3
"""
Script that starts a Flask web application.
Renders an HMTL webpage that lists all state names
as well as associated City objects.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    from models import storage
    from models.state import State
    states = storage.all('State')
    print(states) # Debugging statement
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """ Method to close current SQLAlchemy session"""
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
