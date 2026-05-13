#!/usr/bin/env python3
"""
Module 6-square
Définit une classe Square avec gestion de la position et affichage.
"""


class Square:
    """
    Classe Square qui définit un carré par sa taille et sa position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialise le carré avec size et position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Récupère la taille."""
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la taille avec validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Récupère la position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Définit la position avec validation (tuple de 2 entiers positifs)."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Calcule l'aire."""
        return self.__size * self.__size

    def __str__(self):
        """Définit la représentation sous forme de chaîne de l'objet."""
        if self.size == 0:
            return ""
        result = []
        result.append("\n" * self.position[1])
        for i in range(self.size):
            result.append(" " * self.position[0] + "#" * self.size)
        return "\n".join(result)

    def my_print(self):
        """Affiche le carré avec des # en respectant la position."""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
