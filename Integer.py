
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

