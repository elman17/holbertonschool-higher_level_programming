#!/usr/bin/python3
"""Converting CSV Data to JSON Format"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Converter"""
    try:
        with open(csv_filename, "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open("data.json", "w") as f:
            json.dump(data, f)

        return True
    except FileNotFoundError:
        return False
