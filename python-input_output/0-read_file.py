#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, "r", encoding="utf8-") as f:
        print(f.read(), end="")
