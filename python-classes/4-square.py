#!/usr/bin/python3
"""Define a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize square"""
        self.size = size

    @property
    def size(self):
        """Retrieve current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size with validation"""
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return area of square"""
        return self.__size ** 2
