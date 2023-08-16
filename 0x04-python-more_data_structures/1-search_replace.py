#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return (my_list)
    cp_list = my_list[:]
    for i in my_list:
        if i == search:
            cp_list[i] = replace
    return (cp_list)
