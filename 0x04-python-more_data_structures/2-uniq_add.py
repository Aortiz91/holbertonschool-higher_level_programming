#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    uniq_values = set(my_list)
    for x in uniq_values:
        add += x
    return add
