#!/usr/bin/python3
def uppercase(sentence):
    for i in sentence:
        c = chr(ord(i) - 32) if ord(i) >= 97 and ord(i) <= 122 else i
        print("{}".format(c), end="")
    print("")
