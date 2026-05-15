#!/usr/bin/env python3
"""Module pour la classe Square."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Représente un carré héritant de Rectangle."""

    def __init__(self, size):
        """Initialise le carré."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
