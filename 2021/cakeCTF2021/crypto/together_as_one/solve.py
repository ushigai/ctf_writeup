from Crypto.Util.number import *
from output import x, y, n, c

q = GCD(x-y, n)
r = GCD((x-y) // q - 1, n)
p = n // q // r

assert p*q*r == n

phi = (p - 1) * (q - 1) * (r - 1)
e = 65537

d = inverse(e, phi)
m = pow(c, d, n)

print(long_to_bytes(m))
