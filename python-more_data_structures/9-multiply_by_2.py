#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    mult_dict = {}
    for key, value in a_dictionary.items():
        mult_dict[key] = value * 2
        return mult_dict
