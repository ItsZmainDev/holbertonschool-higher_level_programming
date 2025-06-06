#!/usr/bin/python3
"""Module to convert CSV data to JSON format"""

import json
import csv


def convert_csv_to_json(csv_filename):
    """Serialize CSV to JSON"""
    try:
        with open(csv_filename, "r") as csv_f:
            reader = csv.DictReader(csv_f)
            data = [row for row in reader]

        with open("data.json", "w") as json_f:
            json.dump(data, json_f)

        return True

    except FileNotFoundError:
        return False