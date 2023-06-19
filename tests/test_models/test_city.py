#!/usr/bin/python3
"""Unittest module for the City class"""

import unittest
from models.city import City
from models.state import State
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test case for the City class"""

    def setUp(self):
        """Set up the test environment"""
        pass

    def tearDown(self):
        """Clean up the test environment"""
        pass

    def test_state_id(self):
        """Test the state_id attribute of City"""
        new_city = City()
        self.assertIsInstance(new_city.state_id, str)

    def test_name(self):
        """Test the name attribute of City"""
        new_city = City()
        self.assertIsInstance(new_city.name, str)

    def test_inheritance(self):
        """Test inheritance of City"""
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)
        self.assertIsInstance(new_city, City)
        self.assertFalse(type(new_city) == State)


if __name__ == '__main__':
    unittest.main()
