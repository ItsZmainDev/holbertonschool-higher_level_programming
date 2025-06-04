#!/usr/bin/python3
"""Function to write in a file"""


def write_file(filename="", text=""):
    """Write a string to a text file and return the
       number of characters written"""

    with open(filename, "w") as f:
        write_f = f.write(text)
        return write_f
