#!/usr/bin/env python3
"""Module pour les formes géométriques et le duck typing."""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Classe de base abstraite pour toutes les formes."""

    @abstractmethod
    def area(self):
        """Calcule l'aire de la forme."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calcule le périmètre de la forme."""
        pass


class Circle(Shape):
    """Représente un cercle."""

    def __init__(self, radius):
        """Initialise le cercle avec son rayon."""
        self.radius = radius

    def area(self):
        """Renvoie l'aire du cercle : pi * r^2."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Renvoie le périmètre du cercle : 2 * pi * r."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Représente un rectangle."""

    def __init__(self, width, height):
        """Initialise le rectangle avec largeur et hauteur."""
        self.width = width
        self.height = height

    def area(self):
        """Renvoie l'aire du rectangle : L * l."""
        return self.width * self.height

    def perimeter(self):
        """Renvoie le périmètre du rectangle : 2 * (L + l)."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Affiche l'aire et le périmètre d'une forme (Duck Typing)."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
