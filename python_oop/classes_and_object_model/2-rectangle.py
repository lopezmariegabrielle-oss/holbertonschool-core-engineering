#!/usr/bin/env python3
"""
Module 2-rectangle
Définit une classe Rectangle avec calcul d'aire et de périmètre.
"""


class Rectangle:
    """
    Classe Rectangle qui définit un rectangle par sa largeur et sa hauteur.
    """

    def __init__(self, width=0, height=0):
        """Initialise le rectangle avec largeur et hauteur."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Récupère la largeur."""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur avec validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("widht must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur."""
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur avec validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an interger")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            int: L'aire (largeur * hauteur).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            int: Le périmètre, ou 0 si une dimension est nulle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
