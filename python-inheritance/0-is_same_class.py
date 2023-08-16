#!/usr/bin/python3
    """function that determines if object is instance of specific class"""
def is_same_class (obj, a_class):
    """
    returns true or false
    """
    if isinstance(obj, a_class) == True:
        return True
    else:
        return False
