#!/usr/bin/python3
"""Defines a function that writes an object in text file."""
import json


def save_to_json_file(my_obj, filename):
    """Saves the object into a file."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
