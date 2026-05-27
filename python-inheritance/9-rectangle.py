#!/usr/bin/python3
"""Full Rectangle"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inheritence from BaseGeometry"""

    def __init__(self, width, height):
        """Width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Area of Rectangle"""

        return self.__height * self.__width

    def __str__(self):
        "Rectangle area for user"

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
