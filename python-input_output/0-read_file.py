#!/usr/bin/python3
"""Read file"""

def read_file(filename=""):
    with open(filename, "r", encoding="utf8-") as f:
        print(f.read(), ends="")
