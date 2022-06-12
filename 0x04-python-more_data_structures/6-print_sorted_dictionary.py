#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for j, i in enumerate(sorted(a_dictionary.keys())):
        print(i, end=": ")
        print(a_dictionary[i])
