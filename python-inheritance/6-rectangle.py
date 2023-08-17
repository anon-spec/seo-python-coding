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
    
    def __init__(self, width, height):
        """initialization of objects"""
        self.__width = width
        self.__height = height
        integer_validator(self.__width)
        integer_validator(self.__height)
