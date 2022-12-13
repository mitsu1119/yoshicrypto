
class Integer(int):
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            raise TypeError("Integer class must be int value")

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Integer(self.value + other.value)
        raise TypeError(f"{type(other)}")
    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Integer(self.value - other.value)
        raise TypeError(f"{type(other)}")
    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Integer(self.value * other.value)
        raise TypeError(f"{type(other)}")
    def __mod__(self, other):
        if isinstance(other, self.__class__):
            return Integer(self.value % other.value)
        raise TypeError(f"{type(other)}")

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.value += other.value
            return self
        raise TypeError(f"{type(other)}")
    def __isub__(self, other):
        if isinstance(other, self.__class__):
            self.value -= other.value
            return self
        raise TypeError(f"{type(other)}")
    def __imul__(self, other):
        if isinstance(other, self.__class__):
            self.value *= other.value
            return self
        raise TypeError(f"{type(other)}")
    def __imod__(self, other):
        if isinstance(other, self.__class__):
            self.value %= other.value
            return self
        raise TypeError(f"{type(other)}")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.value == other.value)
        raise TypeError(f"{type(other)}")
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return (self.value != other.value)
        raise TypeError(f"{type(other)}")

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return (self.value < other.value)
        raise TypeError(f"{type(other)}")
    def __le__(self, other):
        if isinstance(other, self.__class__):
            return (self.value <= other.value)
        raise TypeError(f"{type(other)}")
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return (self.value > other.value)
        raise TypeError(f"{type(other)}")
    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return (self.value >= other.value)
        raise TypeError(f"{type(other)}")

    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self.value)

ZZ = Integer
