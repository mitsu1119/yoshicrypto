from yoshicrypto.util.Pari import *

class Integer:
    def __init__(self, value, parent):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = value.to_Integer()
        self.__parent = parent

    # --------------------------------------------------------------------------------------------
    # Attribute Getter
    # --------------------------------------------------------------------------------------------
    def parent(self):
        return self.__parent

    def is_prime(self):
        if self.value < 2:
            return False
        if self.value == 2:
            return True
        return pari(self.value).isprime()

    def is_prime_power(self):
        if self.value < 2:
            return False
        if self.value == 2:
            return True
        if pari(self.value).isprimepower()[0] == 0:
            return False
        return True

    # --------------------------------------------------------------------------------------------
    # Arithmetic Operators
    # --------------------------------------------------------------------------------------------
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Integer(self.value + other.value, self.__parent)
        raise TypeError(f"unsupported operand for +: '{str(self.parent())}' and '{str(other.parent())}'")
    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Integer(self.value - other.value, self.__parent)
        raise TypeError(f"unsupported operand for -: '{str(self.parent())}' and '{str(other.parent())}'")
    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Integer(self.value * other.value, self.__parent)
        raise TypeError(f"unsupported operand for *: '{str(self.parent())}' and '{str(other.parent())}'")
    def __mod__(self, other):
        if isinstance(other, self.__class__):
            return Integer(self.value % other.value, self.__parent)
        raise TypeError(f"unsupported operand for %: '{str(self.parent())}' and '{str(other.parent())}'")

    # --------------------------------------------------------------------------------------------
    # Arithmetic and Assignment Operators
    # --------------------------------------------------------------------------------------------
    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.value += other.value
            return self
        raise TypeError(f"unsupported operand for +: '{str(self.parent())}' and '{str(other.parent())}'")
    def __isub__(self, other):
        if isinstance(other, self.__class__):
            self.value -= other.value
            return self
        raise TypeError(f"unsupported operand for -: '{str(self.parent())}' and '{str(other.parent())}'")
    def __imul__(self, other):
        if isinstance(other, self.__class__):
            self.value *= other.value
            return self
        raise TypeError(f"unsupported operand for *: '{str(self.parent())}' and '{str(other.parent())}'")
    def __imod__(self, other):
        if isinstance(other, self.__class__):
            self.value %= other.value
            return self
        raise TypeError(f"unsupported operand for %: '{str(self.parent())}' and '{str(other.parent())}'")

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
        return self.value

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
class IntegerRing:
    def __call__(self, value):
        if self.__convertable_from(value):
            return Integer(value, self)
        else:
            raise TypeError("Integer class must be int value")

    def __str__(self):
        return "Integer Ring"

    def __convertable_from(self, other):
        if isinstance(other, int) or hasattr(other, "to_Integer"):
            return True
        return False

ZZ = IntegerRing()
