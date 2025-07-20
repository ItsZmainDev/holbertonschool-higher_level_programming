#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    i = 0
    a = sorted(a_dictionary)
    while i < len(a):
        key = a[i]
        print("{}: {}".format(key, a_dictionary[key]))
        i += 1
