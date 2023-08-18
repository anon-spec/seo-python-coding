#!/usr/bin/python3
"""MODULE DOCSTRING"""


class BaseGeometry:
    """
    finds area and value of shape
    """

    def area(self):
        """Area of self"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Subclass inherited from BaseGeometry"""

    def __init__(self, width, height):
        """initialization of objects"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Solving area of Rectangle"""
        return self.__width * self.__height

    def str(self):
        """Printing String"""
        return "[Rectangle] {}/{}".format(width, height)
