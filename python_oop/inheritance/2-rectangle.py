#!/usr/bin/env python3
"""Module pour la classe Rectangle."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Représente un rectangle héritant de BaseGeometry."""
    def __init__(self, width, height):
        """Initialise le rectangle avec validation."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calcule et renvoie l'aire du rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Définit la représentation sous forme de chaîne."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
