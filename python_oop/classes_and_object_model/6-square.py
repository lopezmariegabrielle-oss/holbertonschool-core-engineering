#!/usr/bin/env python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        if self.size == 0:
            return ""
        result = []
        result.append("\n" * self.position[1])
        for i in range(self.size):
            result.append(" " * self.position[0] + "#" * self.size)
        return "\n".join(result)

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
