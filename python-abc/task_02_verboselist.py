#!/usr/bin/env python3
"""Duck Typing Example with Abstract Base Class"""

class VerboseList(list):
    """Class that extends list to provide verbose output on operations"""

    def append(self, item):
        """Define a method that append an item to the list and print a message"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Define a method that extend the list and print a message"""
        count = len(list(iterable))
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Define a method that print a message before removing the item"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=None):
        """Define a method that print a message before popping item from the list"""
        if index is None:
            item = super().pop()
        else:
            item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item

