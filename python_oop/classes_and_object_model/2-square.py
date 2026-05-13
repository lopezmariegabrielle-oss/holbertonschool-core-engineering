#!/usr/bin/env python3
"""
Module 2-square
Définit une classe Square avec validation de l'attribut privé size.
"""


class Square:
    """
    Classe Square qui définit un carré par sa taille avec validation.

    Attributes:
        __size (int): La taille d'un côté du carré (privée).
    """

    def __init__(self, size=0):
        """
        Initialise une nouvelle instance de Square.

        Args:
            size (int): La taille du côté du nouveau carré. 
                       Par défaut à 0.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
