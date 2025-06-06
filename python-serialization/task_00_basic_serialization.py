#!/usr/bin/python3
"""Module to serialize/deserialize data using JSON"""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize data and save to file"""
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load data from file and deserialize it"""
    with open(filename, "r") as f:
        return json.load(f)
