#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """inherits from list"""

    def print_sorted(self):
        new_list = self.copy()
        new_list.sort()
        print(new_list)
        return new_list
