from Integer import *
from sympy import isprime

class Fp_Integer:
    def __init__(self, value, order, parent):
        self.value = value % order
        self.__order = order
        self.__parent = parent

    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)

    def parent(self):
        return self.__parent

    def to_Integer(self, parent):
        return Integer(self.value, parent)

class FiniteField:
    def __init__(self, order):
        if not isinstance(order, Integer):
            raise TypeError(f"order mult be an Integer")
        if order < ZZ(2):
            raise ValueError("the order of a FiniteField must be at least 2")
        if not isprime(order.value):
            raise NotImplementedError("the order of a FiniteField must be prime")
        self.__order = order

    def __call__(self, value):
        if isinstance(value, Integer):
            return Fp_Integer(value, self.__order, self)
        raise ValueError(f"the element of {self.__str__()} must be Integer")

    def __str__(self):
        return f"finite field of order {self.__order}"

    def order(self):
        return self.__order
