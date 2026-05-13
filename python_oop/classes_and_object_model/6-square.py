#!/usr/bin/env python3
"""Module for Square class."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position with strict validation.

        Args:
            value (tuple): tuple of 2 positive integers.

        Raises:
            TypeError: if not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Returns the area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with # and spaces."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """String representation of the square for print()."""
        res = ""
        if self.__size == 0:
            return res

        for _ in range(self.__position[1]):
            res += "\n"
        for i in range(self.__size):
            res += " " * self.__position[0] + "#" * self.__size
            if i < self.__size - 1:
                res += "\n"
        return res
