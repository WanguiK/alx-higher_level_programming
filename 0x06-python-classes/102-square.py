#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """
    This class defines a square and provides methods to work with it.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (float or int): The size of the square's sides (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            float or int: The size of the square's sides.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The new size of the square's sides.

        Raises:
            TypeError: If the value is not a number (float or integer).
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return (self.__size ** 2)

    def __eq__(self, other):
        """
        Compare if two squares have equal areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """
        Compare if two squares have different areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are different, False otherwise.
        """
        return (self.area() != other.area())

    def __lt__(self, other):
        """
        Compare if the area of the current square is less than the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
