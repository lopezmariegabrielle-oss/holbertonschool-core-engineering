#!/usr/bin/env python3
"""Module définissant des Mixins et une classe Dragon."""


class SwimMixin:
    """Ajoute la capacité de nager."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Ajoute la capacité de voler."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Un dragon qui peut nager, voler et rugir."""
    def roar(self):
        """Affiche le rugissement du dragon."""
        print("The dragon roars!")
