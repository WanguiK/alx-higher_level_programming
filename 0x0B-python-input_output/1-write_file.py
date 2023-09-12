#!/usr/bin/python3
"""Writes a string to a text file."""


def write_file(filename="", text=""):
    """PPrints the number of characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
