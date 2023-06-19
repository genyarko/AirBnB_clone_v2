#!/usr/bin/python3
"""Unittest module for the BaseModel class"""

import unittest
from models.base_model import BaseModel
import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    """Test case for the BaseModel class"""

    def setUp(self):
        """Set up the test environment"""
        try:
            os.remove('file.json')
        except OSError:
            pass

    def tearDown(self):
        """Clean up the test environment"""
        try:
            os.remove('file.json')
        except OSError:
            pass

    def test_default(self):
        """Test the default initialization of BaseModel"""
        i = BaseModel()
        self.assertIsInstance(i, BaseModel)

    def test_kwargs(self):
        """Test initialization of BaseModel with kwargs"""
        i = BaseModel()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertIsNot(new, i)

    def test_kwargs_int(self):
        """Test initialization of BaseModel with kwargs containing int key"""
        i = BaseModel()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test the save method of BaseModel"""
        i = BaseModel()
        i.save()
        key = f"{i.__class__.__name__}.{i.id}"
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test the __str__ method of BaseModel"""
        i = BaseModel()
        expected_str = f"[BaseModel] ({i.id}) {i.__dict__}"
        self.assertEqual(str(i), expected_str)

    def test_todict(self):
        """Test the to_dict method of BaseModel"""
        i = BaseModel()
        self.assertEqual(i.to_dict(), i.__dict__)

    def test_kwargs_none(self):
        """Test initialization of BaseModel with kwargs containing None key"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    def test_kwargs_one(self):
        """Test initialization of BaseModel with kwargs containing invalid key"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = BaseModel(**n)

    def test_id(self):
        """Test the id attribute of BaseModel"""
        new = BaseModel()
        self.assertIsInstance(new.id, str)

    def test_created_at(self):
        """Test the created_at attribute of BaseModel"""
        new = BaseModel()
        self.assertIsInstance(new.created_at, datetime.datetime)

    def test_updated_at(self):
        """Test the updated_at attribute of BaseModel"""
        new = BaseModel()
        self.assertIsInstance(new.updated_at, datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertNotEqual(new.created_at, new.updated_at)


if __name__ == '__main__':
    unittest.main()
    
