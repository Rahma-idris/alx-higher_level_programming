#!/usr/bin/python3
def uppercase(str):
    """Prints upper case string"""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
            print("{}".format(c), end="")
    print("")
