#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """A function to write file"""
    with open(filename, mode="w+", encoding="utf-8") as f:
        return f.write(text)
