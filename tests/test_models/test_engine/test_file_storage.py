#!/usr/bin/python3
""" Run unittest for file_storage.py """
import unittest
import os
import time
import datetime
import uuid
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        """Set up method to prepare the environment before tests."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """Tear down method to clean up after tests."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test if save updates the 'updated_at' attribute."""
        bm = BaseModel()
        time.sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        """Test if consecutive saves update 'updated_at' accordingly."""
        bm = BaseModel()
        time.sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        time.sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        """Test if save method raises TypeError with an argument."""
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        """Test if save method updates the JSON file correctly."""
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_handling_BaseModel(self):
        """Test if filetstorage store the BaseModel class instances."""
        new_dict = storage.classes()
        self.assertIn("BaseModel", new_dict)

    def test_handling_User_class(self):
        """Test if filetstorage store the user class instances."""
        new_dict = storage.classes()
        self.assertIn("User", new_dict)


if __name__ == '__main__':
    unittest.main()
