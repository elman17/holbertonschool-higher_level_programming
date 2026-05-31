#!/usr/bin/python3
"""Basic Serialization"""

import json


def serialize_and_save_to_file(data, filename):
    """Wrtite to file"""
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Read from file"""
    with open(filename, "r") as f:
        return json.load(f)
