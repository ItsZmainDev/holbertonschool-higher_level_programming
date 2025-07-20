#!/usr/bin/python3
"""Module to serialize python dictionnary
    and deserialize json file"""

import json


def serialize_and_save_to_file(data, filename):
    """Function to serialize in json"""
    with open(filename, "w") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Function to deserialize"""
    with open(filename, "r") as f:
        return json.load(f)
