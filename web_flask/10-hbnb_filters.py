#!/usr/bin/python3
"""
Script that starts a Flask web application
Includes a route that opens the application with various web filters.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ Method to close current SQLAlchemy session"""
    from models import storage
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    
