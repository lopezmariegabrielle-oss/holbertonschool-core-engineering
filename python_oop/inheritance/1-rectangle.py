#!/usr/bin/env python3
"""Module pour la classe Rectangle."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Représente un rectangle héritant de BaseGeometry."""

    def __init__(self, width, height):
        """Initialisation du rectangle avec validation.

            Args:
                width (int): La largeur.
                height (int): La hauteur.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calcule l'aire du rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Définit la représentation en chaîne du rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
