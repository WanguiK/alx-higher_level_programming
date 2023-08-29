#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initiate a new Square.

        Args:
            size (int): This is the size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return (self.__size ** 2)
