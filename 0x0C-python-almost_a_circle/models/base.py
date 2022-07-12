#!/usr/bin/python3
"""
Module contains class Base

Contains private class __nb_objects, and class constructor __init__
"""
class Base:
    """
    defines class Base
    Class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
