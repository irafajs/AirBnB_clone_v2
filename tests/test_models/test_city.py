#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.state import State
from models import storage


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "Testing database storage only")
class TestCity(unittest.TestCase):
    """ Test the City class """

    @classmethod
    def setUpClass(cls):
        """ Set up the testing environment """
        # Configure the database connection
        cls.engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                   format(getenv("HBNB_MYSQL_USER"),
                                          getenv("HBNB_MYSQL_PWD"),
                                          getenv("HBNB_MYSQL_HOST"),
                                          getenv("HBNB_MYSQL_DB")),
                                   pool_pre_ping=True)
        Base.metadata.create_all(cls.engine)

    @classmethod
    def tearDownClass(cls):
        """ Remove the testing environment """
        Base.metadata.drop_all(cls.engine)

    def setUp(self):
        """ Create a new session for each test """
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        """ Remove the session after each test """
        self.session.close()

    def test_city_inherits_from_base_model(self):
        """ Test if City inherits from BaseModel """
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_has_name_attribute(self):
        """ Test if City has 'name' attribute """
        city = City(name="Test City")
        self.assertEqual(city.name, "Test City")

    def test_city_has_state_id_attribute(self):
        """ Test if City has 'state_id' attribute """
        city = City(state_id="state-123")
        self.assertEqual(city.state_id, "state-123")

    def test_city_table_name(self):
        """ Test if the table name is as expected """
        self.assertEqual(City.__tablename__, 'cities')

    def test_city_name_not_nullable(self):
        """ Test if 'name' attribute is not nullable """
        with self.assertRaises(ValueError):
            city = City()
            self.session.add(city)
            self.session.commit()

    def test_city_state_id_not_nullable(self):
        """ Test if 'state_id' attribute is not nullable """
        with self.assertRaises(ValueError):
            city = City(name="Test City")
            self.session.add(city)
            self.session.commit()

    def test_city_relationship_with_state(self):
        """ Test if City has a relationship with State """
        state = State(name="Test State")
        self.session.add(state)
        self.session.commit()

        city = City(name="Test City", state_id=state.id)
        self.session.add(city)
        self.session.commit()

        self.assertEqual(city.state, state)


if __name__ == '__main__':
    unittest.main()

