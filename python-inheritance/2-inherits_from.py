#!/usr/bin/python3
"""function that determines if object is instance of specific class"""


def inherits_from(obj, a_class):
    """
    returns true or false
    """
    return issubclass(obj, a_class) if obj != a_class
