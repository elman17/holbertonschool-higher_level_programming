#!/usr/bin/python3
"""This module defines a Rectangle class"""


class Rectangle:
    """Defines a rectangle"""
    
    number_of_instances = 0
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        
    @property
    def heigth(self):
        return self.__heigth
    
    @heigth.setter
    def heigth(self, value):
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__heigth = value
        
    def area(self):
        """Return rectangle area"""
        return self.__width * self.__heigth
    
    def perimeter(self):
        """Return rectangle perimeter"""
        if self.__heigth == 0 or self.__width == 0:
            return 0
        return 2 * (self.__heigth + self.__width)
    
    def __str__(self):
        """Return string representation using #."""
        if self.__width == 0 or self.__heigth == 0:
            return ""
        rows = []
        
        for i in range(self.__heigth):
            rows.append("#" * self.__width)
        return "\n".join(rows)
    
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__heigth)
    
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_intance -= 1
