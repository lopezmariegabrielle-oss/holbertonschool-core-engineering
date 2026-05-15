#!/usr/bin/env python3
"""Module définissant une classe animale abstraite et ses sous-classes."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Classe de base abstraite représentant un animal."""

    @abstractmethod
    def sound(self):
        """Méthode abstraite que chaque sous-classe doit implémenter."""
        pass


class Dog(Animal):
    """Sous-classe représentant un chien."""

    def sound(self):
        """Renvoie le cri du chien."""
        return "Bark"


class Cat(Animal):
    """Sous-classe représentant un chat."""
    def sound(self):
        """Renvoie le cri du chat."""
        return "Meow"
