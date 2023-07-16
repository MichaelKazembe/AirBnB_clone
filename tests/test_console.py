#!/usr/bin/python3
"""Tests for Console"""
import unittest
import pep8
import pycodestyle
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(TestCase):
    """Tests for the console, quit and empty"""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_pep8_console(self):
        """Pep8 test"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(
            p.total_errors,
            0,
            "Found code style errors (and warnings).")

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__('console').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_do_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_do_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_do_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_do_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 26811")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 26811")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 26811 name 'Michael Ahmad'")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_default(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('unknown command')
            output = f.getvalue().strip()
            self.assertEqual(output, '*** Unknown syntax: unknown command')


if __name__ == '__main__':
    unittest.main()
