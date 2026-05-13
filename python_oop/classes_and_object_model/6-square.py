#!/usr/bin/env python3
"""Module for Square."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Init square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Area."""
        return self.__size ** 2

    def my_print(self):
        """Print square."""
        if self.__size == 0:
            print("")
            return
        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))

    def __str__(self):
        """String rep."""
        if self.__size == 0:
            return ""
        res = "\n" * self.__position[1]
        for i in range(self.__size):
            res += " " * self.__position[0] + "#" * self.__size
            if i < self.__size - 1:
                res += "\n"
        return res
