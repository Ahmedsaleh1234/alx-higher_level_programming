#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cp_list = my_list[:]
    for i in my_list:
        if i == search:
            cp_list[i] = replace
    return (cp_list)
