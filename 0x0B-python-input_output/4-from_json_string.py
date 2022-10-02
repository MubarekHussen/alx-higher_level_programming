#!/usr/bin/python3
"""Write a function that returns the obj representation of
a json"""
import json


def from_json_string(my_str):
    """loads obj from json"""
    return json.loads(my_str)
