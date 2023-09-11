#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """function that returns the list of available"""
    return (dir(obj))
