from yoshicrypto.ring.Integer import *
from yoshicrypto.util.Ntheory import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# self.value: Integer
# self.order: Integer
# self.__parent: Factory Class Object
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Fp_Integer:
    def __init__(self, value, order, parent):
        if isinstance(value, self.__class__):
            self.value = value.value % order
        elif isinstance(value, Integer):
            self.value = value % order
        elif isinstance(value, int):
            self.value = ZZ(value % order.value)
        else:
            raise TypeError(f"unable to convert '{value}' to an FiniteField eleent")
        self.__order = order
        self.__parent = parent

    # --------------------------------------------------------------------------------------------
    # Attribute Getter
    # --------------------------------------------------------------------------------------------
    def parent(self):
        return self.__parent

    # --------------------------------------------------------------------------------------------
    # Calculatable Type
    # --------------------------------------------------------------------------------------------
    def is_calcable(self, other):
        if isinstance(other, self.__class__):
            if self.__parent == other.parent():
                return True
        return False

    # --------------------------------------------------------------------------------------------
    # Arithmetic Operators
    # --------------------------------------------------------------------------------------------
    def __add__(self, other):
        if self.is_calcable(other):
            return Fp_Integer((self.value + other.value) % ZZ(self.__order), self.__order, self.__parent)
        raise TypeError(f"unsupported operand for +: '{str(self.parent())}' and '{str(other.parent())}'")
    def __sub__(self, other):
        if self.is_calcable(other):
            return Fp_Integer((self.value - other.value) % ZZ(self.__order), self.__order, self.__parent)
        raise TypeError(f"unsupported operand for -: '{str(self.parent())}' and '{str(other.parent())}'")
    def __mul__(self, other):
        if self.is_calcable(other):
            return Fp_Integer((self.value * other.value) % ZZ(self.__order), self.__order, self.__parent)
        raise TypeError(f"unsupported operand for *: '{str(self.parent())}' and '{str(other.parent())}'")
    def __truediv__(self, other):
        if self.is_calcable(other):
            return self * other.inv()
        raise TypeError(f"unsupported operand for /: '{str(self.parent())}' and '{str(other.parent())}'")
    def inv(self):
        return Fp_Integer(ZZ(pow(self.value.value, -1, self.__order.value)), self.__order, self.__parent)

    # --------------------------------------------------------------------------------------------
    # Arithmetic and Assignment Operators
    # --------------------------------------------------------------------------------------------
    def __iadd__(self, other):
        if self.is_calcable(other):
            self.value += other.value 
            self.value %= ZZ(self.__order).value
            return self
        raise TypeError(f"unsupported operand for +: '{str(self.parent())}' and '{str(other.parent())}'")
    def __isub__(self, other):
        if self.is_calcable(other):
            self.value -= other.value 
            self.value %= ZZ(self.__order).value
            return self
        raise TypeError(f"unsupported operand for -: '{str(self.parent())}' and '{str(other.parent())}'")
    def __imul__(self, other):
        if self.is_calcable(other):
            self.value *= other.value 
            self.value %= ZZ(self.__order).value
            return self
        raise TypeError(f"unsupported operand for *: '{str(self.parent())}' and '{str(other.parent())}'")
    def __itruediv__(self, other):
        if self.is_calcable(other):
            self.value *= other.inv().value
            self.value %= ZZ(self.__order).value
            return self
        raise TypeError(f"unsupported operand for /: '{str(self.parent())}' and '{str(other.parent())}'")

    # --------------------------------------------------------------------------------------------
    # Comparison Operators
    # --------------------------------------------------------------------------------------------
    def __eq__(self, other):
        if self.is_calcable(other):
            return (self.value == other.value)
        raise TypeError(f"unsupported operand for ==: '{str(self.parent())}' and '{str(other.parent())}'")
    def __ne__(self, other):
        if self.is_calcable(other):
            return (self.value != other.value)
        raise TypeError(f"unsupported operand for !=: '{str(self.parent())}' and '{str(other.parent())}'")
    def __lt__(self, other):
        if self.is_calcable(other):
            return (self.value < other.value)
        raise TypeError(f"unsupported operand for <: '{str(self.parent())}' and '{str(other.parent())}'")
    def __le__(self, other):
        if self.is_calcable(other):
            return (self.value <= other.value)
        raise TypeError(f"unsupported operand for <=: '{str(self.parent())}' and '{str(other.parent())}'")
    def __gt__(self, other):
        if self.is_calcable(other):
            return (self.value > other.value)
        raise TypeError(f"unsupported operand for >: '{str(self.parent())}' and '{str(other.parent())}'")
    def __ge__(self, other):
        if self.is_calcable(other):
            return (self.value >= other.value)
        raise TypeError(f"unsupported operand for >=: '{str(self.parent())}' and '{str(other.parent())}'")

    # --------------------------------------------------------------------------------------------
    # Other Special Method
    # --------------------------------------------------------------------------------------------
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self.value)
    def __int__(self):
        return int(self.value)

    # --------------------------------------------------------------------------------------------
    # Type Convertion
    # --------------------------------------------------------------------------------------------
    def to_Integer(self):
        return self.value
    def to_FiniteField(self, order):
        return self.value % ZZ(order).value

# --------------------------------------------------------------------------------------------
# Type Factory
# --------------------------------------------------------------------------------------------
class FiniteField:
    def __init__(self, order):
        try:
            order = ZZ(order)
        except:
            raise ValueError("the order of a FiniteField must be an Integer")

        if order < ZZ(2):
            raise ValueError("the order of a FiniteField must be at least 2")
        pw = is_prime_power(order)
        if pw[0] == False:
            raise ValueError("the order of a FiniteField must be a prime power")
        if pw[1] == 1:
            self.__order = order
        else:
            raise NotImplementedError("FiniteField the order of a prime power was not implemented")

    def __call__(self, value):
        return Fp_Integer(value, self.__order, self)

    # --------------------------------------------------------------------------------------------
    # Structure
    # --------------------------------------------------------------------------------------------
    def is_ring(self):
        return True

    # --------------------------------------------------------------------------------------------
    # Comparison Operators
    # --------------------------------------------------------------------------------------------
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.__order == other.__order)
        raise TypeError(f"unsupported operand for ==: '{str(self)}' and '{str(other)}'")
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return (self.__order != other.__order)
        raise TypeError(f"unsupported operand for !=: '{str(self)}' and '{str(other)}'")

    def __str__(self):
        return f"finite field of order {self.__order}"

    def order(self):
        return self.__order

GF = FiniteField
