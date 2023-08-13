#!/usr/bin/python3
""" Unittests for amenity.py
"""
import unittest
from time import sleep
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test suite for the Amenity class."""

    def test_amenity_inherits_from_base_model(self):
        """Test if Amenity class inherits from BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_attributes(self):
        """Test if Amenity attributes are initialized correctly."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_attribute_assignment(self):
        """Test if Amenity attributes can be assigned correctly."""
        amenity = Amenity()
        amenity.name = "John"
        self.assertEqual(amenity.name, "John")

    def test_two_amenities_unique_ids(self):
        """Test if two instances of Amenity have unique IDs."""
        us1 = Amenity()
        us2 = Amenity()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_amenities_different_created_at(self):
        """Test if two instances of Amenity have different 'created_at'
        timestamps."""
        us1 = Amenity()
        sleep(0.05)  # Introduce a delay to ensure a time difference
        us2 = Amenity()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_amenities_different_updated_at(self):
        """Test if two instances of Amenity have different 'updated_at'
        timestamps."""
        us1 = Amenity()
        sleep(0.05)  # Introduce a delay to ensure a time difference
        us2 = Amenity()
        self.assertLess(us1.updated_at, us2.updated_at)


if __name__ == '__main__':
    unittest.main()
