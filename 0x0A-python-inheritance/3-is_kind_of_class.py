#!/usr/bin/python3
"""same class or subclass"""


def is_kind_of_class(obj, a_class):
    """if the object is an instance of, or if it is a subclass of class"""
    return (type(obj) is a_class or issubclass(type(obj), a_class))
