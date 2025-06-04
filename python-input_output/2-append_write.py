#!/usr/bin/python3
"""File writing module"""


def append_write(filename="", text=""):
    """Append a string to a text file and return the number of text added"""

    with open(filename, "a") as f:
        append_f = f.write(text)
        return append_f
