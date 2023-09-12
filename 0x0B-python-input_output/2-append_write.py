#!/usr/bin/python3
"""A function that appends a string at the end of a text file."""


def write_file(filename="", text=""):
    """Returns the number of characters added."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
