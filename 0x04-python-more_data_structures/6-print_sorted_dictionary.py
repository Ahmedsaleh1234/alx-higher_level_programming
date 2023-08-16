#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    F = list(a_dictionary.keys())
    F.sort()
    for i in F:
        print("{}: {}".format(i, a_dictionary.get(i)))
