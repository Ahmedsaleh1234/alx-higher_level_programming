#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ls = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return (ls)

    ls[idx] = element
    return (ls)
