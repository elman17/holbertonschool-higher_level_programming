#!/usr/bin/python3
"""Square"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square inheritance from Rectangle"""

    def __init__(self, size):
        """Size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return text"""
        return "[Square] {}/{}".format(self.__size, self.__size)
