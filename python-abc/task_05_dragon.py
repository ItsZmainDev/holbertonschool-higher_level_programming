#!/usr/bin/env python3
"""Duck Typing Example with Abstract Base Class"""

class SwimMixin:
    """Class that adds swim method"""

    def swim(self):
        """Define that the creature can swim"""
        print("The creature swims!")

class FlyMixin:
    """Class that adds fly method"""

    def fly(self):
        """Define that the creature can fly"""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Class that represents a dragon, which can swim, fly, and roar"""

    def roar(self):
        """Define that the dragon can roar"""
        print("The dragon roars!")

