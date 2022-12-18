from yoshicrypto.ring.Ring import *

# --------------------------------------------------------------------------------------------
# Type Factory
# --------------------------------------------------------------------------------------------
class PolynomialRing:
    def __init__(self, base_ring):
        if not is_ring(base_ring):
            raise TypeError("base ring of PolynomialRing must be a ring")
        self.__base_ring = base_ring

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

