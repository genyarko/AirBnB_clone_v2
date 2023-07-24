#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)

        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
    def cities(self):
        """
        Getter method to return the list of City objects from storage
        linked to the current State (only if the storage engine is not DBStorage)
        """
        from models import storage
        from models.city import City
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
