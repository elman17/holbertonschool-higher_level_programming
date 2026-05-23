#!/usr/bin/python3
"""Only sub class checker"""


def inherits_from(obj, a_class):
    """Fuction for inherit checker"""

    return isinstance(obj, a_class) and type(obj) is not a_class
