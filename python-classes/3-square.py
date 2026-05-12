#!/usr/bin/python3
"""Define a square"""

class Square:
    def __init__(self, size=0):
        """Initialization square size with validation"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
        
    def area(self):
        """Return current square area"""
        return self.__size ** 2
