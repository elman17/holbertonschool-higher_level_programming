#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """Return dict format"""
    return obj.__dict__
