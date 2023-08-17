#!/usr/bin/python3
"""
function that determines if object is instance of a class that is inherited
"""


def inherits_from(obj, a_class):
    """
    returns true or false
    """
    return issubclass(obj, a_class) and obj != a_class
