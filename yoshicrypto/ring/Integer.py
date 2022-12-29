from yoshicrypto.util.Pari import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# self.value: int
# self.__parent: Factory Class Object
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Integer:
    def __init__(self, value, parent):
        from yoshicrypto.field.FiniteField import Fp_Integer
        if isinstance(value, self.__class__):
            self.value = value.value
        elif isinstance(value, int):
            self.value = value
        elif isinstance(value, Fp_Integer):
            self.value = value.value
        else:
            raise TypeError("unable to convert to '{value}' to an integer")
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
            return (False, 0)
        if self.value == 2:
            return (True, 1)
        X = pari(self.value).isprimepower()
        if X[0] == 0:
            return (False, 0)
        return (True, X[0])

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
# Type Factory
# --------------------------------------------------------------------------------------------
class IntegerRing:
    # --------------------------------------------------------------------------------------------
    # Structure
    # --------------------------------------------------------------------------------------------
    def is_ring(self):
        return True

    def __call__(self, value):
        return Integer(value, self)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return True
        return False

    def __str__(self):
        return "Integer Ring"

ZZ = IntegerRing()
