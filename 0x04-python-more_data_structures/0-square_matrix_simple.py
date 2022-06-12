#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_sq = list(map(lambda i: list(map(lambda j: j**2, i)), matrix))
    return matrix_sq
