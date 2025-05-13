#!/usr/bin/python3
def print_list_integer(my_list=[]):
    index = 0
    while index < len(my_list):
        print("{}".format(my_list[index]))
        index = index + 1
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
