#!/usr/bin/python3
""" Unittests for place.py
"""
import unittest
from time import sleep
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test suite for the Place class."""

    def test_place_inherits_from_base_model(self):
        """Test if Place class inherits from BaseModel."""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_place_attributes(self):
        """Test if Place attributes are initialized correctly."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_attribute_assignment(self):
        """Test if Place attributes can be assigned correctly."""
        place = Place()
        place.city_id = "21982198219"
        place.user_id = "76287128721"
        place.name = "John"
        place.description = "Small description"
        place.number_rooms = 4
        place.number_bathrooms = 2
        place.max_guest = 3
        place.price_by_night = 30
        place.latitude = 20.5
        place.longitude = 10.5
        place.amenity_ids = ["1662792222", "292822223", "2202989293"]
        self.assertEqual(place.city_id, "21982198219")
        self.assertEqual(place.user_id, "76287128721")
        self.assertEqual(place.name, "John")
        self.assertEqual(place.description, "Small description")
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 3)
        self.assertEqual(place.price_by_night, 30)
        self.assertEqual(place.latitude, 20.5)
        self.assertEqual(place.longitude, 10.5)
        self.assertEqual(place.amenity_ids, ["1662792222", "292822223", "2202989293"])

    def test_two_places_unique_ids(self):
        """Test if two instances of Place have unique IDs."""
        us1 = Place()
        us2 = Place()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_places_different_created_at(self):
        """Test if two instances of Place have different 'created_at'
        timestamps."""
        us1 = Place()
        sleep(0.05)  # Introduce a delay to ensure a time difference
        us2 = Place()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_places_different_updated_at(self):
        """Test if two instances of Place have different 'updated_at'
        timestamps."""
        us1 = Place()
        sleep(0.05)  # Introduce a delay to ensure a time difference
        us2 = Place()
        self.assertLess(us1.updated_at, us2.updated_at)


if __name__ == '__main__':
    unittest.main()
