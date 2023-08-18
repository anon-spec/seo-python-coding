#!/usr/bin/python3
"""MODULE DOCSTRING"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
"""Subclass inherited from BaseGeometry"""

    def __init__(self, width, height):
        """initialization of objects"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
