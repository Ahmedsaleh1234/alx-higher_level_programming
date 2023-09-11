#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """True if the object is exactly an instance of the class"""

    return (type(obj) is a_class)
