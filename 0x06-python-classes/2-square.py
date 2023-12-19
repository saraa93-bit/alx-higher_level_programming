#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = self.__validate_size(size)

    def __validate_size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        return size
