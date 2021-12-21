from Crypto.Util.number import *

flag = b"FLAG"
m = bytes_to_long(flag)

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e1 = 65536
e2 = 65538

print("n =", n)
print("e1 =", e1)
print("c1 =", pow(m, e1, n))
print("e2 =", e2)
print("c2 =", pow(m, e2, n))