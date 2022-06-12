#!/usr/bin/python3
def roman_to_int(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    val = 0
    if (type(s) != str or len(s) == 0):
        return 0
    size = len(s)
    val = roman[s[size - 1]]

    for i in range(size - 2, -1, -1):
        sign = 1
        if (roman[s[i]] < roman[s[i + 1]]):
            sign = -1
        val = val + roman[s[i]] * sign
    return val
