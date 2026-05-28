#!/usr/bin/python3
"""Append to a file"""


def append_write(file_name="", text=""):
    """Appemd text"""
    with open(file_name, "a", encoding="utf-8") as f:
        return f.write(text)
