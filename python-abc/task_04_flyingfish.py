#!/usr/bin/env python3
"""Duck Typing Example with Abstract Base Class"""

class Fish:
    """Class that represent fish"""

    def swim(self):
        """Define that fish can swim"""
        print("The fish is swimming")

    def habitat(self):
        """Define that fish live in water"""
        print("The fish lives in water")

class Bird:
    """Class that represent bird"""

    def fly(self):
        """Define that bird can fly"""
        print("The bird is flying")

    def habitat(self):
        """Define that bird can live in the sky"""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """Class that represent flying fish, which can swim and fly"""

    def swim(self):
        """Define that flyingfish can swim"""
        print("The flying fish is swimming!")

    def fly(self):
        """Define that flyingfish can fly"""
        print("The flying fish is soaring!")

    def habitat(self):
        """Define that flyingfish can live in both water and sky"""
        print("The flying fish lives both in water and the sky!")

