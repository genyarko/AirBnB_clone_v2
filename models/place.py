#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            from models import storage
            from models.review import Review
            result = storage.all(Review)
            return [review_obj for review_obj in result.values()
                    if self.id == review_obj.place_id]

        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity
            result = storage.all(Amenity)
            return [amenity_obj for amenity_obj in result.values()
                    if amenity_obj.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, amenity):
            if amenity is not None:
                from models.amenity import Amenity
                if isinstance(amenity, Amenity):
                    if amenity.id not in self.amenity_ids:
                        self.amenity_ids.append(amenity.id)


class User(BaseModel, Base):
    """ User class """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', backref='user', cascade='all, delete')
    reviews = relationship('Review', backref='user', cascade='all, delete')


class City(BaseModel, Base):
    """ City class """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    places = relationship('Place', backref='cities', cascade='all, delete')
