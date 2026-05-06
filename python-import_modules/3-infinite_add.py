#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    result = 0

    i = 1
    while i < len(argv):
        result = result + int(argv[i])
        i += 1

    print(result)
