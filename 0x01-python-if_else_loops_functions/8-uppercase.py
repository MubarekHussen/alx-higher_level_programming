#!/usr/bin/python3
def uppercase(str):
    for up_chr in str:
        up = ord(up_chr)
        if(up >= 97 and up < 123):
            up = up - 32
            up_chr = chr(up)
        print("{}".format(up_chr), end="")
    print("{}".format(""))
