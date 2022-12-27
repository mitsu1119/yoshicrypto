from yoshicrypto.ring.Ring import *

# --------------------------------------------------------------------------------------------
# Type Factory
# --------------------------------------------------------------------------------------------
class PolynomialRing:
    def __init__(self, base_ring, name):
        if not is_ring(base_ring):
            raise TypeError("base ring of PolynomialRing must be a ring")
        self.__base_ring = base_ring

        s = str(name)
        if len(s) == 0:
            raise ValueError("variable name must be nonempty")
        if len(s.split()) > 1:
            raise NotImplementedError("multivariate polynomial is not implemented")
        if not s[0].isalpha():
            raise ValueError(f"variable name '{s}' is not start with an alphabet")
        self.__name = s

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
            return (self.__base_ring == other.__base_ring)
        raise TypeError(f"unsupported operand for ==: '{str(self)}' and '{str(other)}'")
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return (self.__base_ring != other.__base_ring)
        raise TypeError(f"unsupported operand for !=: '{str(self)}' and '{str(other)}'")

    def __str__(self):
        return f"univariate polynomial ring over {self.__base_ring}"

    def base_ring(self):
        return self.__base_ring

