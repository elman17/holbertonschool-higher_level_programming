#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """Writes a text file and prints it to stdout"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
