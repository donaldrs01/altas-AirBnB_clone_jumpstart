#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import genenv


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""
        cites = []
    
    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """Returns list of City objects from FileStorage linked to state"""
            city_objects = [city for city in storage.all(City).values()