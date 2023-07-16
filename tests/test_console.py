#!/usr/bin/python3
"""Tests for Command Console"""
import unittest
from unittest.mock import patch
import os
import console
import tests
from console import HBNBCommand
from io import StringIO


class TestConsole(unittest.TestCase):
    """tests for the console, quit and empty"""

    @classmethod
    def setUpClass(cls):
        """setup console class for test"""
  
