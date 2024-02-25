from AlphabetConfig import *


class IntMod:
    MODULE = m

    def __init__(self, value):
        self.__value = value % IntMod.MODULE

    def getValue(self):  # getter bcs value is private
        return self.__value

    def __abs__(self):  # for "abs(x)"
        return abs(self.__value)

    def __add__(self, other):  # for "+"
        return IntMod((self.__value + other.__value) % IntMod.MODULE)

    def __sub__(self, other):  # for "-"
        return IntMod((self.__value - other.__value) % IntMod.MODULE)

    def __mul__(self, other):  # for "*"
        return IntMod((self.__value * other.__value) % IntMod.MODULE)

    def __floordiv__(self, other):  # for "//"
        return IntMod((self.__value * pow(other.__value, -1, IntMod.MODULE)) % IntMod.MODULE)

    def __int__(self):  # for "int(x)"
        return self.__value

    def __str__(self):  # for "str(x)" and print(x)
        return str(int(self))

    def __gt__(self, other):  # for ">"
        return True if self.__value > other.getValue() else False

    def __lt__(self, other):  # for "<"
        return True if self.__value < other.getValue() else False
