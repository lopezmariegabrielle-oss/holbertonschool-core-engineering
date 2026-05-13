#!/usr/bin/env python3
"""Module définissant la classe BaseGeometry."""


class BaseGeometry:
    """Classe de base pour les formes géométriques."""

    def area(self):
        """
        Calcule l'aire de la forme.

        Raises:
            Exception: Toujours, car cette méthode n'est pas implémentée
            dans la classe de base.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide qu'une valeur est un entier strictement positif.

        Args:
            name (str): Le nom de la variable (utilisé dans les erreurs).
            value (any): La valeur à valider.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieure ou égale à 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greter than 0".format(name))
