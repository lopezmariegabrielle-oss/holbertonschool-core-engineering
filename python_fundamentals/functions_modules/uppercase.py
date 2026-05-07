#!/usr/bin/env python3
def uppercase(str):
    for c in str:
        var = ord(c)
        if var >= 97 and var <= 122:
            char = chr(var - 32) 

            print("{}".format(char), end="")
    print("")
