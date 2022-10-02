#!/usr/bin/python3
"""Write a function that writes the JSON representation of
an object (string) to a file"""


def save_to_json_file(my_obj, filename):
    """Dumps obj to json and write it to a file"""
    import json
    with open(filename, mode='w', encoding='utf-8') as fd:
        return json.dump(my_obj, fd)
