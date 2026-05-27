#!/usr/bin/python3
"""Abstract Animal Class and its Subclasses"""
from abc import ABC, abstractclassmethod

class Animal():
    @abstractclassmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
