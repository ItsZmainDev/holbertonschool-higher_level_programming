#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    i = 0
    new_dict = {}
    key = list(a_dictionary.keys())
    while i < len(key):
        keys = key[i]
        new_dict[keys] = a_dictionary[keys] * 2
        i += 1
    return new_dict
