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

    def test_rec_getW(self):
        """Test get width functionality of rectangle class"""
        r = Rectangle(20, 10)
        self.assertEqual(r.width, 20)

    def test_rec_setW_int(self):
        """Test get width functionality of rectangle class integer"""
        r = Rectangle(20, 10)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_rec_setW_str(self):
        """Test get width functionality of rectangle class with string"""
        r = Rectangle(20, 10)
        r.width = "hey"
        self.assertEqual(r.width, "hey")

    def test_rec_setH_int(self):
        """Test get width functionality of rectangle class"""
        r = Rectangle(20, 10)
        r.height = 15
        self.assertEqual(r.height, 15)
