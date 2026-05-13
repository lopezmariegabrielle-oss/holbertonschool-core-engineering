#!/usr/bin/env python3
"""
Module 4-square
Définit une classe Square avec des propriétés getter et setter.
"""


class Square:
    """
    Classe Square qui définit un carré par sa taille avec contrôle d'accès.

    Attributes:
        __size (int): La taille d'un côté du carré (privée).
    """

    def __init__(self, size=0):
        """
        Initialise une nouvelle instance de Square.

        Args:
            size (int): La taille du côté du carré.
        """
        self.size = size

    @property
    def size(self):
        """
        Récupère la valeur de la taille.

        Returns:
            int: La taille du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Définit la valeur de la taille avec validation.

        Args:
            value (int): La nouvelle taille à assigner.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcule l'aire du carré actuel.

        Returns:
            int: L'aire du carré.
        """
        return self.__size * self.__size
