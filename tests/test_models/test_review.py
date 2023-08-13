#!/usr/bin/python3
""" Unittests for review.py
"""
import unittest
from time import sleep  # Import sleep for time comparison
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test suite for the Review class."""

    def test_review_inherits_from_base_model(self):
        """Test if Review class inherits from BaseModel."""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_review_attributes(self):
        """Test if Review attributes are initialized correctly."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_attribute_assignment(self):
        """Test if Review attributes can be assigned correctly."""
        review = Review()
        review.place_id = "123456"
        review.user_id= "7891011"
        review.text = "plain text"
        self.assertEqual(review.place_id, "123456")
        self.assertEqual(review.user_id, "7891011")
        self.assertEqual(review.text, "plain text")
        
    def test_two_reviews_unique_ids(self):
        """Test if two instances of Review have unique IDs."""
        us1 = Review()
        us2 = Review()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_reviews_different_created_at(self):
        """Test if two instances of Review have different 'created_at'
        timestamps."""
        us1 = Review()
        sleep(0.05)  # Introduce a delay to ensure a time difference
        us2 = Review()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_reviews_different_updated_at(self):
        """Test if two instances of Review have different 'updated_at'
        timestamps."""
        us1 = Review()
        sleep(0.05)  # Introduce a delay to ensure a time difference
        us2 = Review()
        self.assertLess(us1.updated_at, us2.updated_at)


if __name__ == '__main__':
    unittest.main()
