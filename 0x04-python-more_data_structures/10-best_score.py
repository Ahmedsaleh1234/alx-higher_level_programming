#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        a = list(a_dictionary.keys())
        return max(a)
    elif not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
