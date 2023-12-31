#!/usr/bin/python3

"""Module for rectangle class: Defines attributes and
    methods of a rectangle.
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class. Extends the Base class. Contains attributes
        and methods for rectangle instances."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instances of class"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return the value of Rectangle width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the value of Rectangle width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """return the value of Rectangle height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set the value of Rectangle height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """return the value of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set the value of x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """return the value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set the value of y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints Rectangle instance with character '#' to stdout"""
        charX = " " * self.__x
        display = '\n'.\
            join([charX + '#' * self.__width for _ in range(self.__height)])
        for _ in range(self.__y):
            print("")
        print(display)

    def __str__(self):
        """override the __str__ method and return string below"""
        if (type(self).__name__ == "Square"):
            str = \
                f"[{type(self).__name__}] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}"
        else:
            str = \
                f"[{type(self).__name__}] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

        return str

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            for attr, value in kwargs.items():
                self.__setattr__(attr, value)

    def to_dictionary(self):
        """returns a dictionary representation of a Rectangle"""
        if (type(self).__name__ == "Square"):
            class_dict =\
                {"id": self.id, "size": self.height, "x": self.x, "y": self.y}
        else:
            class_dict =\
                {"id": self.id, "width": self.width,
                 "height": self.height, "x": self.x, "y": self.y}
        return class_dict
