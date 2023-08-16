#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    dkeys = a_dictionary.keys()
    for i in dkeys:
        new[i] *= 2
    return new
