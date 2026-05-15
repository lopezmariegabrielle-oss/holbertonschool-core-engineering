#!/usr/bin/env python3
"""Module définissant les classes Fish, Bird et FlyingFish."""


class Fish:
    """Représente un poisson."""

    def swim(self):
        """Affiche le comportement de nage du poisson."""
        print("The fish is swimming")

    def habitat(self):
        """Affiche l'habitat naturel du poisson."""
        print("The fish lives in water")


class Bird:
    """Représente un oiseau."""

    def fly(self):
        """Affiche le comportement de vol de l'oiseau."""
        print("The bird is flying")

    def habitat(self):
        """Affiche l'habitat naturel de l'oiseau."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Représente un poisson volant, héritant de Fish et Bird."""

    def fly(self):
        """Redéfinit le vol pour le poisson volant."""
        print("The flying fish is soaring!")

    def swim(self):
        """Redéfinit la nage pour le poisson volant."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Redéfinit l'habitat pour combiner les deux milieux."""
        print("The flying fish lives both in water and the sky!")
