from Crypto.Util.number import *

flag = bytes_to_long(b"hogehoge")
p, q = getPrime(128), getPrime(128)
n = p * q
phi = (p - 1) * (q - 1)
d = inverse(flag, phi)

c = pow(3, flag, n)

print("c =", c)

print("m =", pow(c, d, n))



