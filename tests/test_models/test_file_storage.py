#!/usr/bin/env python3
"""A unit test module for testing file_storage.py"""
import unittest
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    """class that tests basic features of FileStorage class"""

    def test_all_method(self):
        """testing dictionary returned by all() method"""
        self.assertEqual(type(storage.all()), dict)

    def test_new_method(self):
        """testing creation of new class instance"""
        base1 = BaseModel()
        fetch_all = str(storage.all())
        base2 = BaseModel()
        self.assertNotEqual(fetch_all, str(storage.all()))

    def test_save(self):
        """tests save method of FileStorage class"""
        storage = FileStorage()
        storage.reload()
        initial_file = str(storage.all())
        base1 = BaseModel()
        storage.save()
        storage.reload()
        new_file = str(storage.all())
        self.assertNotEqual(initial_file, new_file)

    def test_reload(self):
        """tests reload method"""
        storage = FileStorage()
        storage.reload()
        initial_file = str(storage.all())
        base1 = BaseModel()
        base1.save()
        storage.reload()
        new_file = str(storage.all())
        self.assertNotEqual(initial_file, new_file)
