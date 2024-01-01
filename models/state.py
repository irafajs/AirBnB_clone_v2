#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        """getter return list of City instances"""
        city_list = []
        from models import storage
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

    def __str__(self):
        """overwritting the inherited __str__"""
        state_dict = self.to_dict()
        state_dict.pop('__class__', None)
        return "[State] ({}) {}".format(self.id, state_dict)
