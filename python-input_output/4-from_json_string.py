#!/usr/bin/python3
"""From JSON string to Object"""

import json


def from_json_string(my_obj):
    """converter to object"""
    return json.loads(my_obj)
