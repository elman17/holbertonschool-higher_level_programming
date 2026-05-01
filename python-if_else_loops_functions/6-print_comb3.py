#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i+1, 10):
        if i < 99:
             print("{:02d}, ".format(i), end="")
        else:
             print("{:02d}".format(i))
