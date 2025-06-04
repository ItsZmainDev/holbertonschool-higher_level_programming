#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """Read a text file and print its content"""

    with open(filename, "r") as f:
        print(f.read(), end="")
