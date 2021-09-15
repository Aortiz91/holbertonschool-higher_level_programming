#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    newdata = {key:value}
    a_dictionary.update(newdata)
    return a_dictionary
