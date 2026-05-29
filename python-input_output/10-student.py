#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            result = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    result[key] = value
            return result
        return self.__dict__
