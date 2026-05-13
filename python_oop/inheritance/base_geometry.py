#!/usr/bin/env python3
"""Module pour la classe BaseGeometry."""


class BaseGeometry:
    """Classe de base pour les formes géométriques."""

    def area(self):
        """Lève une exception car l'aire n'est pas implémentée ici."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide que 'value' est un entier strictement positif.

        Args:
            name (str): Le nom de la variable.
            value (int): La valeur à vérifier.

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur est <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
