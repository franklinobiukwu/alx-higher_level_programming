#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

""" Test Module for Rectangle Class"""


class TestRectangle(unittest.TestCase):
    """Class to test the Rectangle class"""
    def test_rec_blank(self):
        """Instantiate rectangle without any value"""
        self.assertRaises(TypeError, Rectangle)

    def test_rec_oneInt(self):
        """Instantiate rectangle with one integer"""
        self.assertRaises(TypeError, Rectangle, 20)

    def test_rec_oneStr(self):
        """Instantiate rectangle with one string"""
        self.assertRaises(TypeError, Rectangle, "hey")
