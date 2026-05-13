#!/usr/bin/env python3
"""
Module 5-square
Définit une classe Square capable de s'imprimer avec des #.
"""

class Square:
    """
    Classe Square qui définit un carré et peut l'afficher.

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
            value (int): La nouvelle taille.

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
        Calcule l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Affiche le carré dans la sortie standard en utilisant le caractère #.
        Si la taille est 0, affiche une ligne vide.
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
