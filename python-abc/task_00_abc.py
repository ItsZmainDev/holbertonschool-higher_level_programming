#!/usr/bin/env python3
"""Abstract Base Class Example"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Define the sound an animal makes"""
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
