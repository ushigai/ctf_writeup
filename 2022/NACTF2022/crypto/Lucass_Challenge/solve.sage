"""
f(x, k) = 2 * f(x - 1, k) + k * f(x - 2, k)

f(0, k) = 0
f(1, k) = 1
f(2, k) = 2 * f(2 - 1, k) + k * f(2 - 2, k) = 2*1 + k*0 = 2
f(3, k) = 2 * f(3 - 1, k) + k * f(3 - 2, k) = 2*2 + k*1 = 4 + k
f(4, k) = 2 * f(4 - 1, k) + k * f(4 - 2, k) = (4 + k)*2 + k*2

"""

from Crypto.Util.number import *
from sage.crypto.util import *


def ff(p, k, mod):
    F = Integers(mod)
    car1 = carmichael_lambda(mod)
    car2 = carmichael_lambda(car1)
    x = pow(11, p, car2)
    x = pow(11, x, car1)
    A = Matrix(F, [[2, k], [1, 0]])
    return (A^x * vector([1, 0]))[1]


F = open("enc.txt", "r").read().split("\n")
flag = ""
for f in F[:-1]:
    p, k, mod, c = map(int, f.split())
    #print(p, k, mod, c)
    #print(long_to_bytes(ff(p, k, mod) ^^ c))
    m = ff(p, k, mod)
    flag += long_to_bytes(int(m)^^c).decode()

print(flag)
