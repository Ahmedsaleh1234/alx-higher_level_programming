#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        a = list(a_dictionary.keys())
        return max(a)
    else:
        return None

