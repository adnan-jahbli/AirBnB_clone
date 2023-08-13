#!/usr/bin/python3
""" Unittests for city.py
"""
import unittest
from time import sleep
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test suite for the City class."""

    def test_city_inherits_from_base_model(self):
        """Test if City class inherits from BaseModel."""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_attributes(self):
        """Test if City attributes are initialized correctly."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attribute_assignment(self):
        """Test if City attributes can be assigned correctly."""
        city = City()
        city.state_id = "903293332"
        city.name = "John"
        self.assertEqual(city.state_id, "903293332")
        self.assertEqual(city.name, "John")

    def test_two_cites_unique_ids(self):
        """Test if two instances of City have unique IDs."""
        us1 = City()
        us2 = City()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_cites_different_created_at(self):
        """Test if two instances of City have different 'created_at'
        timestamps."""
        us1 = City()
        sleep(0.05)  # Introduce a delay to ensure a time difference
        us2 = City()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_cites_different_updated_at(self):
        """Test if two instances of City have different 'updated_at'
        timestamps."""
        us1 = City()
        sleep(0.05)  # Introduce a delay to ensure a time difference
        us2 = City()
        self.assertLess(us1.updated_at, us2.updated_at)


if __name__ == '__main__':
    unittest.main()
