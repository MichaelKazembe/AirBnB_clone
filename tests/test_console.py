#!/usr/bin/python3
"""Tests for Console"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """Tests for the console, quit and empty"""

    def setUp(self):
        self.console = console.HBNBCommand()

    def tearDown(self):
        pass

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__('console').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        self.assertIsNotNone(console.HBNBCommand.__doc__)
        self.assertIsNotNone(console.HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(console.HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(console.HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(console.HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(console.HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(console.HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(console.HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(console.HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(console.HBNBCommand.default.__doc__)

    def test_emptyline(self):
        """Test no user input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual(f.getvalue(), '')

    def test_create(self):
        """Test cmd output: create"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create SomeClass")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")  # not used
            self.console.onecmd("create User")  # just need to create instances
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.all()")
            self.assertEqual('["[User', f.getvalue()[:7])

    def test_all(self):
        """Test cmd output: all"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all NonExistantModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Place")
            self.assertEqual("[]\n", f.getvalue())

    def test_destroy(self):
        """Test cmd output: destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy TheWorld")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 12345")
            self.assertEqual("** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.destroy('123')")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_update(self):
        """Test cmd output: update"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update You")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User 12345")
            self.assertEqual("** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User 12345")
            self.assertEqual("** attribute name missing **\n", f.getvalue())

    def test_show(self):
        """Test cmd output: show"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("SomeClass.show()")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Review")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.show('123')")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_class_cmd(self):
        """Test cmd output: <class>.<cmd>"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.count()")
            self.assertEqual(int, type(eval(f.getvalue())))


if __name__ == '__main__':
    unittest.main()
