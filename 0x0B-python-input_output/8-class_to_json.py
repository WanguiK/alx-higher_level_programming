#!/usr/bin/python3
"""Defines a function that serialization in JSON object."""
import json


def class_to_json(obj):
    """Returns dictionary description with simple data structure."""
    return obj.__dict__
