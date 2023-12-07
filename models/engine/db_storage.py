#!/usr/bin/python3
"""Shebang to create PY scrip
"""


from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """class DBStorage"""
    __engine = None
    __session = None
    storage_type = "db"

    def __init__(self):
        """Initializes the DBStorage instance"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', default='localhost')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, db),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database """
        from models import classes
        objects = {}

        if cls:
            query_result = self.__session.query(classes[cls]).all()
        else:
            query_result = []
            for class_ in classes.values():
                query_result.extend(self.__session.query(class_).all())

        for obj in query_result:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objects[key] = obj

        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        if not isinstance(obj, DBStorage):
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        from models import storage
        from datetime import datetime
        self.updated_at = datetime.utcnow()
        storage.new(self)
        #print(f"Saving object with sql: {str(self)}")
        #storage.save()
        #self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and create the current database session"""

        Base.metadata.create_all(self.__engine)
        #print("Table created successfuly!!!!")
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()
