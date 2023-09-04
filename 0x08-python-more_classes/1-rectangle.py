#!/usr/bin/python3


"""defines class Rectangle"""


class Rectangle:
     """
    Class that defines properties of rectangle by: (based on 0-rectangle.py).

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """a function that called otomataclly

        Args:
            width(int): The width of the new rectangle.
            height(int): The height of new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width retriver.

        Returns:
            int: the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set width

        Args:
            value(int):the width of rectangle

        Raise:
            TypeError: width must be an integer
            ValueError:  width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height retriver.

        Returns:
            int: the width of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """"set height

        Args:
            value(int):the width of rectangle

        Raise:
            TypeError: width must be an integer
            ValueError:  width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
