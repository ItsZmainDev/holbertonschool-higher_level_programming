#!/usr/bin/python3
"""Module to serialize CSV into JSON"""

import json
import csv


def convert_csv_to_json(csv_filename):
    """Serialize CSV to JSON"""
    try:
        with open(csv_filename, "r") as csv_f:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", "w") as json_f:
            json.dump(csv_dict, json_f)

        return True

    except FileNotFoundError:
        return False
