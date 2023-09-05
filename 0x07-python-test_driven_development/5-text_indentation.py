#!/usr/bin/python3

"""
    This module prints a text with 2 new lines after each of these
    characters: ., ? and : using the following methods:
    text_indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for char in text:
        print(char, end="")
        if char in [".", "?", ":"]:
            print("\n\n", end="")
