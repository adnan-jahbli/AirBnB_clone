#!/usr/bin/python3
""" Unittests for user.py
"""
import unittest
from time import sleep  # Import sleep for time comparison
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test suite for the User class."""

    def test_user_inherits_from_base_model(self):
        """Test if User class inherits from BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_attributes(self):
        """Test if User attributes are initialized correctly."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attribute_assignment(self):
        """Test if User attributes can be assigned correctly."""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_two_users_unique_ids(self):
        """Test if two instances of User have unique IDs."""
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_users_different_created_at(self):
        """Test if two instances of User have different 'created_at'
        timestamps."""
        us1 = User()
        sleep(0.05)  # Introduce a delay to ensure a time difference
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_users_different_updated_at(self):
        """Test if two instances of User have different 'updated_at'
        timestamps."""
        us1 = User()
        sleep(0.05)  # Introduce a delay to ensure a time difference
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)


if __name__ == '__main__':
    unittest.main()
