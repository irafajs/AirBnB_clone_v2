#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    def __str__(self):
        """overwritting inherited __str__ method"""
        state_dict = self.to_dict()
        state_dict.pop('__class__', None)
        return "[City] ({}) {}".format(self.id, state_dict)
