#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """
    This is a class that defines the Square with size
    It checks the type of the size attribute and it's value
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size**2
