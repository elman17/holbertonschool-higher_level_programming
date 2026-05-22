#!/usr/bin/python3
"""This module defines MyList class"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))