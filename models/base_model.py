#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models import storage
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if "created_at" in kwargs:
                    self.created_at = datetime.strptime(
                            kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                if "updated_at" in kwargs:
                    self.updated_at = datetime.strptime(
                            kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                if 'id' not in kwargs:
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs:
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs:
                    self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(
                type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """ return a string representation """
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__)
        dictionary.pop('_sa_instance_state', None)
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """delete current instance from storage"""
        from models import storage
        storage.delete(self)
