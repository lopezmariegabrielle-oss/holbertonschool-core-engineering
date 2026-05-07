#!/usr/bin/env python3

def uppercase(str):
    for char in str:
        var = ord(char)
        if var >= 97 and var <= 122:
            char = chr(var - 32)

            print("{}".format(char), end="")
    print("")
