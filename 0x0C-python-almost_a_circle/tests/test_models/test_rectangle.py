#!/usr/bin/python3
""" Test Module for Rectangle Class. Each method test for a functionality
    or feature in the rectangle module
"""


import unittest
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    """Class to test the Rectangle class"""

    # TEST CLASS INSTANTIATION
    def test_valid_instantiation(self):
        """Test instantiation with valid values"""
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)

    def test_invalid_instantiation(self):
        """Test instantiation with invalid values"""
        with self.assertRaises(TypeError):
            rectangle = Rectangle()

        with self.assertRaises(TypeError):
            rectangle = Rectangle(10)

        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 0)

        with self.assertRaises(ValueError):
            rectangle = Rectangle(0, 20)

        with self.assertRaises(TypeError):
            rectangle = Rectangle("a", 20)

        with self.assertRaises(TypeError):
            rectangle = Rectangle(10, "a")

        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 20, -1)

        with self.assertRaises(TypeError):
            rectangle = Rectangle(10, 20, "a")

        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 20, 1, -2)

        with self.assertRaises(TypeError):
            rectangle = Rectangle(10, 20, 1, "a")
        

    # TEST GET WIDTH
    def test_valid_get_width(self):
        """Test get width functionality of
            rectangle class with valid values
        """
        rectangle = Rectangle(20, 10)
        self.assertEqual(rectangle.width, 20)

    def test_invalid_get_width(self):
        """Test get width functionality of
            rectangle class with invalid values
        """
        rectangle = Rectangle(20, 10)
#       self.assertEqual(r.width, "w")
        with self.assertRaises(TypeError):
            rectangle.width()

    # TEST SET WIDTH
    def test_valid_set_width(self):
        """Test set width functionality of
            rectangle class with valid values
        """
        rectangle = Rectangle(20, 10)
        rectangle.width = 5
        self.assertEqual(rectangle.width, 5)
        rectangle.width = (5)
        self.assertEqual(rectangle.width, 5)

    def test_invalid_set_width(self):
        """Test get width functionality of rectangle class with string"""
        rectangle = Rectangle(20, 10)
        with self.assertRaises(TypeError):
            rectangle.width = "a"

        with self.assertRaises(ValueError):
            rectangle.width = 0 

        with self.assertRaises(ValueError):
            rectangle.width = -1 

        with self.assertRaises(TypeError):
            rectangle.width = (5, 10)

        with self.assertRaises(TypeError):
            rectangle.width = {5, 10}

        with self.assertRaises(TypeError):
            rectangle.width = {"num1": 5, "num2": 10}

        with self.assertRaises(TypeError):
            rectangle.width = [5, 10]

        with self.assertRaises(TypeError):
            rectangle.width = None 

        with self.assertRaises(TypeError):
            rectangle.width = float('inf') 

    # TEST GET HEIGHT
    def test_valid_get_height(self):
        """Test get height functionality of rectangle class"""
        rectangle = Rectangle(20, 10)
        self.assertEqual(rectangle.height, 10)

    def test_invalid_get_height(self):
        """Test get width functionality of
            rectangle class with invalid values
        """
        rectangle = Rectangle(20, 10)
        with self.assertRaises(TypeError):
            rectangle.height()

    # TEST SET HEIGHT
    def test_valid_set_height(self):
        """Test set height functionality of
            rectangle class with valid values
        """
        rectangle = Rectangle(20, 10)
        rectangle.height = 15
        self.assertEqual(rectangle.height, 15)

    def test_invalid_set_height(self):
        """Test set height functionality of
            rectangle class with invalid values
        """
        rectangle = Rectangle(20, 10)
        with self.assertRaises(TypeError):
            rectangle.height = "a"

        with self.assertRaises(ValueError):
            rectangle.height = 0 

        with self.assertRaises(ValueError):
            rectangle.height = -1 

        with self.assertRaises(TypeError):
            rectangle.height = 1.5

        with self.assertRaises(TypeError):
            rectangle.height = (5, 10)

        with self.assertRaises(TypeError):
            rectangle.height = {5, 10}

        with self.assertRaises(TypeError):
            rectangle.height = {"num1": 5, "num2": 10}

        with self.assertRaises(TypeError):
            rectangle.height = [5, 10]

        with self.assertRaises(TypeError):
            rectangle.height = None 

        with self.assertRaises(TypeError):
            rectangle.height = float('inf') 

    # TEST GET X
    def test_valid_get_x(self):
        """Test get X functionality"""
        rectangle = Rectangle(20, 10)
        self.assertEqual(rectangle.x, 0)
        rectangle = Rectangle(20, 10, 6)
        self.assertEqual(rectangle.x, 6)

    def test_invalid_get_x(self):
        """Test get x functionality"""
        rectangle = Rectangle(20, 10)
        with self.assertRaises(TypeError):
            rectangle.x()

    # TEST SET X
    def test_valid_set_x(self):
        """Test set x functionality with valid values"""
        rectangle = Rectangle(10, 5)
        self.assertEqual(rectangle.x, 0)

        rectangle.x = 15
        self.assertEqual(rectangle.x, 15)

        rectangle.x = 0
        self.assertEqual(rectangle.x, 0)


    def test_invalid_set_x(self):
        """Test set x functionality with invalid values"""
        
        rectangle = Rectangle(20, 10)
        with self.assertRaises(TypeError):
            rectangle.x = "a"

        with self.assertRaises(ValueError):
            rectangle.x = -1 

        with self.assertRaises(TypeError):
            rectangle.x = 1.5

        with self.assertRaises(TypeError):
            rectangle.x = (5, 10)

        with self.assertRaises(TypeError):
            rectangle.x = {5, 10}

        with self.assertRaises(TypeError):
            rectangle.x = {"num1": 5, "num2": 10}

        with self.assertRaises(TypeError):
            rectangle.x = [5, 10]

        with self.assertRaises(TypeError):
            rectangle.x = None 

        with self.assertRaises(TypeError):
            rectangle.x = float('inf') 


    # TEST GET Y
    def test_valid_get_y(self):
        """Test get y functionality"""
        rectangle = Rectangle(20, 10)
        self.assertEqual(rectangle.y, 0)
        rectangle = Rectangle(20, 10, 6, 6)
        self.assertEqual(rectangle.y, 6)

    def test_invalid_get_y(self):
        """Test get y functionality"""
        rectangle = Rectangle(20, 10)
        with self.assertRaises(TypeError):
            rectangle.y()


    # TEST SET Y
    def test_valid_set_y(self):
        """Test set y functionality with valid values"""
        rectangle = Rectangle(10, 5)
        self.assertEqual(rectangle.y, 0)

        rectangle.y = 15
        self.assertEqual(rectangle.y, 15)

        rectangle.y = 0
        self.assertEqual(rectangle.y, 0)


    def test_invalid_set_y(self):
        """Test set y functionality with invalid values"""
        
        rectangle = Rectangle(20, 10)
        with self.assertRaises(TypeError):
            rectangle.y = "a"

        with self.assertRaises(ValueError):
            rectangle.y = -1 

        with self.assertRaises(TypeError):
            rectangle.y = 1.5

        with self.assertRaises(TypeError):
            rectangle.y = (5, 10)

        with self.assertRaises(TypeError):
            rectangle.y = {5, 10}

        with self.assertRaises(TypeError):
            rectangle.y = {"num1": 5, "num2": 10}

        with self.assertRaises(TypeError):
            rectangle.y = [5, 10]

        with self.assertRaises(TypeError):
            rectangle.y = None 

        with self.assertRaises(TypeError):
            rectangle.y = float('inf') 


    # TEST FOR AREA
    def test_area(self):
        """Test area functionality of Rectangle.
            This should return the area of the Rectangle instance
        """
        rectangle = Rectangle(20, 10)
        self.assertEqual(rectangle.area(), 200)

    # TEST FOR DISPLAY
    def test_display(self):
        """Test for display method of the Rectangle instance.
            This should print to stdout in character '#', the
            instance of Rectangle.
        """
        rectangle = Rectangle(20, 10)
        self.assertEqual(rectangle.display(), '\n'.join(['#' * rectangle.width for _ in range(rectangle.height)]))
