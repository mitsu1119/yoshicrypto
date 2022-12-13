from Integer import *
from sympy import isprime

class Fp_Integer:
    def __init__(self, value, order, parent):
        if isinstance(value, int):
            self.value = value % order.value
        else:
            self.value = value.to_FiniteField(order)
        self.__order = order
        self.__parent = parent

    # --------------------------------------------------------------------------------------------
    # Attribute Getter
    # --------------------------------------------------------------------------------------------
    def parent(self):
        return self.__parent

    # --------------------------------------------------------------------------------------------
    # Arithmetic Operators
    # --------------------------------------------------------------------------------------------
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Fp_Integer((self.value + other.value) % ZZ(self.__order).value, self.__order, self.__parent)
        raise TypeError(f"unsupported operand for +: '{str(self.parent())}' and '{str(other.parent())}'")
    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Fp_Integer((self.value - other.value) % ZZ(self.__order).value, self.__order, self.__parent)
        raise TypeError(f"unsupported operand for -: '{str(self.parent())}' and '{str(other.parent())}'")
    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Fp_Integer((self.value * other.value) % ZZ(self.__order).value, self.__order, self.__parent)
        raise TypeError(f"unsupported operand for *: '{str(self.parent())}' and '{str(other.parent())}'")
    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return self * other.inv()
        raise TypeError(f"unsupported operand for /: '{str(self.parent())}' and '{str(other.parent())}'")
    def inv(self):
        return Fp_Integer(pow(self.value, -1, ZZ(self.__order).value), self.__order, self.__parent)

    # --------------------------------------------------------------------------------------------
    # Arithmetic and Assignment Operators
    # --------------------------------------------------------------------------------------------
    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.value += other.value 
            self.value %= ZZ(self.__order).value
            return self
        raise TypeError(f"unsupported operand for +: '{str(self.parent())}' and '{str(other.parent())}'")
    def __isub__(self, other):
        if isinstance(other, self.__class__):
            self.value -= other.value 
            self.value %= ZZ(self.__order).value
            return self
        raise TypeError(f"unsupported operand for -: '{str(self.parent())}' and '{str(other.parent())}'")
    def __imul__(self, other):
        if isinstance(other, self.__class__):
            self.value *= other.value 
            self.value %= ZZ(self.__order).value
            return self
        raise TypeError(f"unsupported operand for *: '{str(self.parent())}' and '{str(other.parent())}'")
    def __itruediv__(self, other):
        if isinstance(other, self.__class__):
            self.value *= other.inv().value
            self.value %= ZZ(self.__order).value
            return self
        raise TypeError(f"unsupported operand for /: '{str(self.parent())}' and '{str(other.parent())}'")

    # --------------------------------------------------------------------------------------------
    # Comparison Operators
    # --------------------------------------------------------------------------------------------
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.value == other.value)
        raise TypeError(f"unsupported operand for ==: '{str(self.parent())}' and '{str(other.parent())}'")
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return (self.value != other.value)
        raise TypeError(f"unsupported operand for !=: '{str(self.parent())}' and '{str(other.parent())}'")
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return (self.value < other.value)
        raise TypeError(f"unsupported operand for <: '{str(self.parent())}' and '{str(other.parent())}'")
    def __le__(self, other):
        if isinstance(other, self.__class__):
            return (self.value <= other.value)
        raise TypeError(f"unsupported operand for <=: '{str(self.parent())}' and '{str(other.parent())}'")
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return (self.value > other.value)
        raise TypeError(f"unsupported operand for >: '{str(self.parent())}' and '{str(other.parent())}'")
    def __ge__(self, other):
        if isinstance(other, self.__class__):
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
        if not isprime(order.value):
            raise NotImplementedError("the order of a FiniteField must be prime")
        self.__order = order

    def __call__(self, value):
        if self.__convertable_from(value):
            return Fp_Integer(value, self.__order, self)
        raise ValueError(f"the element of {self.__str__()} must be Integer")

    def __str__(self):
        return f"finite field of order {self.__order}"

    def order(self):
        return self.__order

    def __convertable_from(self, other):
        if isinstance(other, int) or hasattr(other, "to_FiniteField"):
            return True
        return False
