#!/usr/bin/python3
"""File writing module"""

import json


def save_to_json_file(my_obj, filename):
    """Dump an object to a text file using json format"""

    with open(filename, "w") as f:
        json.dump(my_obj, f)
