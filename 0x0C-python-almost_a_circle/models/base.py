#!/usr/bin/python3
"""
Module contains class Base

Contains private class __nb_objects, and class constructor __init__
"""
class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
