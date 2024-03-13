#!/usr/bin/python3
"""
Script that starts a Flask web application.
Contains route '/states' that will list all State objects in DBStorage.
Contains second route '/states/<id>:
If object found with this ID, will open page with state and all linked cities.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    from models import storage
    from models.state import State
    states = storage.all('State').values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    from models import storage
    from models.state import State

    states = storage.all(State).values()
    #  generator expression to find valid cases of state.id == id
    state = next((state for state in states if state.id == id), None)

    if state:
        return render_template('9-states_id.html', state=state, not_found=False)
    else:
        return render_template('9-states_id.html', not_found=True)


@app.teardown_appcontext
def teardown(exception):
    """ Method to close current SQLAlchemy session"""
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
