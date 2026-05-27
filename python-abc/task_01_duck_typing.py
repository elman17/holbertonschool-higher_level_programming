#!/usr/bin/python3
import math

"""Shapes, Interfaces, and Duck Typing"""
from abc import ABC, abstractclassmethod


class Shape(ABC):
    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radiaus = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return math.pi * 2 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__height = height
        self.__width = width

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    print("Area: {}".format(shape.area))
    print("Perimeter: {}".format(shape.perimeter))
