#!/usr/bin/python3
"""LockedClass with no class or object attribute"""


class LockedClass:

    """prevents the user from dynamically creating new instance attributes,"""
    __slots__ = ['first_name']
