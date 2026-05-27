#!/usr/bin/python3
"""Inheritence class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle intheritence from BaseGeometry"""

    def __init__(self, width, height):
        """Width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
