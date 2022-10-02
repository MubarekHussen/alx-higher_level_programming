#!/usr/bin/python3
"""A module for pascal triangle"""


def pascal_triangle(n):
    """Pascal Triangle"""
    if n == 0:
        return []
    li = []
    for i in range(1, n + 1):
        tmp = []
        for j in range(0, i):
            if (j == 0 or j == i - 1):
                tmp.append(1)
            else:
                k = li[len(li) - 1][j - 1] + li[len(li) - 1][j]
                tmp.append(k)
        li.append(tmp)
    return li
