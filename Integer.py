
class Integer:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            raise TypeError("Integer class must be int value")

    def __add__(self, other):
        return Integer(self.value + other.value)
    def __sub__(self, other):
        return Integer(self.value - other.value)
    def __mul__(self, other):
        return Integer(self.value * other.value)

    def __iadd__(self, other):
        self.value += other.value
        return self
    def __isub__(self, other):
        self.value -= other.value
        return self
    def __imul__(self, other):
        self.value *= other.value
        return self

    def __eq__(self, other):
        return (self.value == other.value)
    def __ne__(self, other):
        return (self.value != other.value)

    def __lt__(self, other):
        return (self.value < other.value)
    def __le__(self, other):
        return (self.value <= other.value)
    def __gt__(self, other):
        return (self.value > other.value)
    def __ge__(self, other):
        return (self.value >= other.value)

    def __str__(self):
        return str(self.value)

ZZ = Integer
