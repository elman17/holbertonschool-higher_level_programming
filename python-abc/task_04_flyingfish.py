#!/usr/bin/python3
"""The Enigmatic FlyingFish - Exploring Multiple Inheritance"""


class Fish:
    def swim(self):
        print("The fish is swiming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky ")


class FlyingFish(Fish, Bird):
    def swim(self):
        print("The flying fish is swiming")

    def fly(self):
        print("The flying fish is soaring")

    def habitat(self):
        print("The flying fish lives both in water and he sky!")
