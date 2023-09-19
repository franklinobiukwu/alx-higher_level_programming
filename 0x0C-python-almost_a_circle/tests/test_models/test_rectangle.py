#!/usr/bin/python3
""" Test Module for Rectangle Class. Each method test for a functionality
    or feature in the rectangle module
"""


import unittest
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    """Class to test the Rectangle class"""

    # TEST CLASS INSTANTIATION
    def test_rec_blank(self):
        """Instantiate rectangle without any value"""
        self.assertRaises(TypeError, Rectangle)

    def test_rec_oneInt(self):
        """Instantiate rectangle with one integer"""
        self.assertRaises(TypeError, Rectangle, 20)

    def test_rec_oneStr(self):
        """Instantiate rectangle with one string"""
        self.assertRaises(TypeError, Rectangle, "hey")

    # TEST GET WIDTH
    def test_rec_getW(self):
        """Test get width functionality of rectangle class"""
        r = Rectangle(20, 10)
        self.assertEqual(r.width, 20)

    def test_rec_getW(self):
        """Test get width functionality of rectangle class"""
        r = Rectangle("w", "h")
        self.assertEqual(r.width, "w")

    # TEST SET WIDTH
    def test_rec_setW_int(self):
        """Test set width functionality of rectangle class integer"""
        r = Rectangle(20, 10)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_rec_setW_str(self):
        """Test get width functionality of rectangle class with string"""
        r = Rectangle(20, 10)
        r.width = "hey"
        self.assertEqual(r.width, "hey")

    # TEST GET HEIGHT
    def test_rec_getH(self):
        """Test get height functionality of rectangle class"""
        r = Rectangle(20, 10)
        self.assertEqual(r.height, 10)

    def test_rec_getW(self):
        """Test get height functionality of rectangle class"""
        r = Rectangle("w", "h")
        self.assertEqual(r.height, "h")

    # TEST SET HEIGHT
    def test_rec_setH_int(self):
        """Test set height functionality of rectangle class"""
        r = Rectangle(20, 10)
        r.height = 15
        self.assertEqual(r.height, 15)

    def test_rec_setH_int(self):
        """Test set height functionality of rectangle class"""
        r = Rectangle(20, 10)
        r.height = "h"
        self.assertEqual(r.height, "h")

    # TEST GET X
    def test_getX(self):
        """Test get X functionality"""
        r = Rectangle(20, 10)
        self.assertEqual(r.x, 0)
        r = Rectangle(20, 10, 6)
        self.assertEqual(r.x, 6)
        r = Rectangle(20, 10, -4)
        self.assertEqual(r.x, -4)
        r = Rectangle(20, 10, "x")
        self.assertEqual(r.x, "x")
        r = Rectangle(20, 10, (2, "ram"))
        self.assertEqual(r.x, (2, "ram"))
        r = Rectangle(20, 10, {2, -1})
        self.assertEqual(r.x, {2, -1})
        r = Rectangle(20, 10, [3, "box"])
        self.assertEqual(r.x, [3, "box"])
        r = Rectangle(20, 10, float('inf'))
        self.assertEqual(r.x, float('inf'))

    # TEST SET X
    def test_setX(self):
        """Test set x functionality"""
        r = Rectangle(10, 5, 2.3)
        self.assertEqual(r.x, 2.3)
        r.x = 15
        self.assertEqual(r.x, 15)
        r.x = -4
        self.assertEqual(r.x, -4)
        r.x = float('inf')
        self.assertEqual(r.x, float('inf'))
        r.x = "x"
        self.assertEqual(r.x, "x")

    # TEST GET Y
    def test_getY(self):
        """Test get Y functionality"""
        r = Rectangle(20, 10)
        self.assertEqual(r.y, 0)
        r = Rectangle(20, 10, 6, 4)
        self.assertEqual(r.y, 4)
        r = Rectangle(20, 10, -4, -3)
        self.assertEqual(r.y, -3)
        r = Rectangle(20, 10, "x", "y")
        self.assertEqual(r.y, "y")
        r = Rectangle(20, 10, 3, (2, "ram"))
        self.assertEqual(r.y, (2, "ram"))
        r = Rectangle(20, 10, {}, {2, -1})
        self.assertEqual(r.y, {2, -1})
        r = Rectangle(20, 10, [], [])
        self.assertEqual(r.y, [])
        r = Rectangle(20, 10, 20220202, float('inf'))
        self.assertEqual(r.y, float('inf'))

    # TEST SET Y
    def test_setY(self):
        """Test set Y functionality"""
        r = Rectangle(2, 1, 3, 4)
        r.y = 0
        self.assertEqual(r.y, 0)

    def test_setY_none(self):
        """Test set Y functionality"""
        r = Rectangle(2, 1, 3, 4)
        r.y = None
        self.assertEqual(r.y, None)

    def test_setY_inf(self):
        """Test set Y functionality"""
        r = Rectangle(2, 1, 3, 4)
        r.y = float('inf')
        self.assertEqual(r.y, float('inf'))

    def test_setY_nve(self):
        """Test set Y functionality"""
        r = Rectangle(2, 1, 3, 4)
        r.y = -2
        self.assertEqual(r.y, -2)

    def test_setY_str(self):
        """Test set Y functionality"""
        r = Rectangle(2, 1, 3, 4)
        r.y = "str"
        self.assertEqual(r.y, "str")

    def test_setY_tup(self):
        """Test set Y functionality"""
        r = Rectangle(2, 1, 3, 4)
        r.y = (0, 3)
        self.assertEqual(r.y, (0, 3))

    def test_setY_list(self):
        """Test set Y functionality"""
        r = Rectangle(2, 1, 3, 4)
        r.y = [1, 3, "q"]
        self.assertEqual(r.y, [1, 3, "q"])

    def test_setY_dict(self):
        """Test set Y functionality"""
        r = Rectangle(2, 1, 3, 4)
        r.y = {"name": "Frank", "age": 600}
        self.assertEqual(r.y, {"name": "Frank", "age": 600})

    def test_setY_set(self):
        """Test set Y functionality"""
        r = Rectangle(2, 1, 3, 4)
        r.y = {"Frank", 600}
        self.assertEqual(r.y, {"Frank", 600})
