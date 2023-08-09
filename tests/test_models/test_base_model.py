#!/usr/bin/python3
""" Run unittest for base_model.py """
import unittest
import time
import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class functionality."""

    def setUp(self):
        """Initialize a BaseModel instance for testing."""
        self.base_model = BaseModel()

    def test_if_id_is_string(self):
        """Check if the 'id' attribute is a string."""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_its_datetime(self):
        """Check if 'created_at' attribute is of type datetime."""
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)

    def test_updated_at_its_datetime(self):
        """Check if 'updated_at' attribute is of type datetime."""
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_if_save_updates_updated_at(self):
        """Check if 'save' method updates the 'updated_at' attribute."""
        prev_updated_at = self.base_model.updated_at
        time.sleep(1)  # To ensure time difference
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, prev_updated_at)

    def test_if_to_dict_returns_dict(self):
        """Check if 'to_dict' method returns a dictionary."""
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_if_to_dict_contains_classname(self):
        """Check if 'to_dict' contains '__class__' key with the class name."""
        obj_dict = self.base_model.to_dict()
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_if_to_dict_contains_created_at(self):
        """Check if 'to_dict' contains 'created_at' key."""
        obj_dict = self.base_model.to_dict()
        self.assertIn("created_at", obj_dict)

    def test_if_to_dict_contains_updated_at(self):
        """Check if 'to_dict' contains 'updated_at' key."""
        obj_dict = self.base_model.to_dict()
        self.assertIn("updated_at", obj_dict)

    def test_if_to_dict_contains_id(self):
        """Check if 'to_dict' contains 'id' key."""
        obj_dict = self.base_model.to_dict()
        self.assertIn("id", obj_dict)

    def test_if_to_dict_id_matches(self):
        """Check if 'to_dict' contains correct 'id' value."""
        obj_dict = self.base_model.to_dict()
        self.assertEqual(obj_dict["id"], self.base_model.id)

    def test_str_repr(self):
        """Check the string representation of the BaseModel instance."""
        str_repr = str(self.base_model)
        self.assertIn(self.base_model.__class__.__name__, str_repr)
        self.assertIn(self.base_model.id, str_repr)


if __name__ == '__main__':
    unittest.main()
