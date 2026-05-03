#!/usr/bin/python3
def uppercase(sentence):
    for i in sentence:
        if ord(i) >= 97 and ord(i) <= 122:
            print(chr(ord(i) - 32), end="")
        else:
            print(i, end="")     
    print("")         
