#!/usr/bin/python3
"""Improve Geometry"""


class BaseGeometry:
    """Improvment"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
