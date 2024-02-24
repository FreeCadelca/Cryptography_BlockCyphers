from AlphabetConfig import *


class IntMod:
    MODULE = m

    def __init__(self, value):
        self.__value = value % IntMod.MODULE

    def getValue(self):
        return self.__value

    def __abs__(self):
        return abs(self.__value)

    def __add__(self, other):
        return IntMod((self.__value + other.__value) % IntMod.MODULE)

    def __sub__(self, other):
        return IntMod((self.__value - other.__value) % IntMod.MODULE)

    def __mul__(self, other):
        return IntMod((self.__value * other.__value) % IntMod.MODULE)

    def __floordiv__(self, other):
        return IntMod((self.__value * pow(other.__value, -1, IntMod.MODULE)) % IntMod.MODULE)

    def __int__(self):
        return self.__value

    def __str__(self):
        return str(int(self))

    def __gt__(self, other):
        if self.__value > other.getValue():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__value < other.getValue():
            return True
        else:
            return False
