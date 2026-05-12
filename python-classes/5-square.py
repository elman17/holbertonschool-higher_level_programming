#!/usr/bin/python3
"""Define a square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize square"""
        self.size = size

    @property
    def size(self):
        "Retrieve size"
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation"""
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return area"""
        return self.__size**2

    def my_print(self):
        """Print square with #"""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
