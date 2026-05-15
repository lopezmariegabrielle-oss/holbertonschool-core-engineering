#!/usr/bin/env python3
"""Module pour la classe Square."""
Rectangle = __import__('1-rectangle').Rectangle


class Square(Rectangle):
    """Représente un carré qui hérite de Rectangle."""

    def __init__(self, size):
        """Initialise le carré avec size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calcule l'aire du carré (héritée ou redéfinie)."""
        return self.__size ** 2

    def __str__(self):
        """Description du carré."""
        return f"[Square] {self.__size}/{self.__size}"
