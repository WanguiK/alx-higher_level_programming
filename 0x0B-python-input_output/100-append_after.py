#!/usr/bin/python3
"""A  function that inserts a line of text to a file."""


def append_after(filename="", search_string="", new_string=""):
    """inserts a text file after each line containina string."""
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
        file.truncate()
