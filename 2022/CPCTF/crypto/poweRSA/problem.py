from Crypto.Util.number import getPrime, bytes_to_long
from secret import FLAG

m = bytes_to_long(FLAG)
p = getPrime(512)
q = getPrime(512)
N = p * q
e = 0x10001
r = pow(p, q, N)
c = pow(m, e, N)

print("N:", N)
print("r:", r)
print("c:", c)
