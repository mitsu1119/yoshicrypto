from yoshicrypto.Pari import *
from yoshicrypto.Integer import *

class Euler_Totient:
    def __repr__(self):
        return "Euler's totient function φ(n)"

    def __call__(self, n):
        if ZZ(n) <= ZZ(0):
            return ZZ(0)
        if ZZ(n) <= ZZ(2):
            return ZZ(1)
        res = ZZ(int(pari(n).eulerphi()))
        return res

euler_totient = Euler_Totient()

