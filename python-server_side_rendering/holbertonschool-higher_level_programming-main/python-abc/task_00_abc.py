#!/usr/bin/python3
"""Define an Animal Class"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Class Animal"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Class Dog inherit from Animal"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Class Cat inherit from Animal"""
    def sound(self):
        return "Meow"
