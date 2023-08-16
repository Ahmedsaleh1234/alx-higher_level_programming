#!/usr/bin/python3
def uniq_add(my_list=[]):
    lis = list(set(my_list))
    sum = 0
    for i in lis:
        sum += i
    return (sum)
