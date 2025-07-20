#!/usr/bin/python3
def no_c(my_string):
    remove_chars = "Cc"
    my_string = my_string.translate(str.maketrans("", "", remove_chars))
    return my_string
