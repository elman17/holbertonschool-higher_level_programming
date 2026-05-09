#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0:
        copied_list = my_list.copy()
        return copied_list
    elif idx >= len(my_list):
        copied_list = my_list.copy()
        return copied_list
    else:
        copied_list = my_list.copy()
        copied_list[idx] = element
        return copied_list
