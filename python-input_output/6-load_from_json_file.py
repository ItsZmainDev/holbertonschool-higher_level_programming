#!/usr/bin/python3
"""File writing module"""

import json


def load_from_json_file(filename):
    """Return the json object from a text file"""

    with open(filename, "r") as f:
        return json.load(f)
