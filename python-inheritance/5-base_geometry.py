#!/usr/bin/python3
"""
function for empty class BaseGeometry
"""


class BaseGeometry:
    """ empty """
    def area(self):
        """Area of self"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
