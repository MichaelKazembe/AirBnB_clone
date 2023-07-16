#!/usr/bin/python3
"""Tests for Command Console"""
import unittest
import os
import console
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """tests for the console, quit and empty"""

    @classmethod
    def setUpClass(cls):
        """setup console class for test"""
  
