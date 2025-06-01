#!/usr/bin/env python3
"""Duck Typing Example with Abstract Base Class"""

class CountedIterator:
    """A class that wraps an iterable and counts the number of elements consumed"""
    def __init__(self, iterable):
        """Initializes the CountedIterator with an iterable"""
        self._iter = iter(iterable)
        self._count = 0

    def __iter__(self):
        """Returns the iterator object itself"""
        return self

    def __next__(self):
        """Returns the next item from the iterator and increments the count"""
        item = next(self._iter)
        self._count += 1
        return item

    def get_count(self):
        """Returns the number of items consumed by the iterator"""
        return self._count

