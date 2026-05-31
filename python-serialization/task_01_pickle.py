#!/usr/bin/python3
"""Pickling Custom Classes"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print object"""
        print("Name: {}".format(self.name))
        print("Age {}".format(self.age))
        print("Is student {}".format(self.is_student))

    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None
