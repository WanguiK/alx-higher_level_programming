#!/usr/bin/python3
"""Reads a textfile."""

def read_file(filename=""):
    """Prints the content of the file"""
    
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            print(line, end="")
