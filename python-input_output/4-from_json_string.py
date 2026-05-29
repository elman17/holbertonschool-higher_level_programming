#!/usr/bin/python3
"""From JSON string to Object"""

import json


def from_json_string(my_obj):
    """converter to object"""
    return json.load(my_obj)
