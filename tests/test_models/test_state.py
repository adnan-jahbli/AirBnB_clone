#!/usr/bin/python3
""" Unittests for state.py
"""
import unittest
from time import sleep
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test suite for the State class."""

    def test_state_inherits_from_base_model(self):
        """Test if State class inherits from BaseModel."""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_attributes(self):
        """Test if State attributes are initialized correctly."""
        state = State()
        self.assertEqual(state.name, "")

    def test_state_attribute_assignment(self):
        """Test if State attributes can be assigned correctly."""
        state = State()
        state.name = "Oregon"

    def test_two_states_unique_ids(self):
        """Test if two instances of State have unique IDs."""
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)

    def test_two_states_different_created_at(self):
        """Test if two instances of State have different 'created_at'
        timestamps."""
        st1 = State()
        sleep(0.05)  # Introduce a delay to ensure a time difference
        st2 = State()
        self.assertLess(st1.created_at, st2.created_at)

    def test_two_states_different_updated_at(self):
        """Test if two instances of State have different 'updated_at'
        timestamps."""
        st1 = State()
        sleep(0.05)  # Introduce a delay to ensure a time difference
        st2 = State()
        self.assertLess(st1.updated_at, st2.updated_at)


if __name__ == '__main__':
    unittest.main()
