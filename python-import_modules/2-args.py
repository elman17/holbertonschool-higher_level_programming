#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    number_of_args = len(argv) - 1

    if number_of_args == 0:
        print("0 arguments.")
    elif number_of_args == 1:
        print("1 argument:")
    else:
        print(f"{number_of_args} arguments:")

    i = 1
    while i < len(argv):
        print(f"{i}: {argv[i]}")
        i += 1
