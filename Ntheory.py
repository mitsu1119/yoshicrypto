from Pari import *
from Integer import *

class Euler_Totient:
    def __repr__(self):
        return "Euler's totient function φ(n)"

    def __call__(self, n):
        if n <= ZZ(0):
            return ZZ(0)
        if n <= ZZ(2):
            return ZZ(1)
        res = ZZ(int(pari(n).eulerphi()))
        return res

euler_totient = Euler_Totient()

