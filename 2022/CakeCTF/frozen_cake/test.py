from Crypto.Util.number import getPrime
import os

flag = os.getenv("FLAG", "FakeCTF{warmup_a_frozen_cake}")
m = int(flag.encode().hex(), 16)

p = getPrime(512)
q = getPrime(512)

n = p*q

print("n =", n)
a = pow(m, p, n)
b = pow(m, q, n)
c = pow(m, n, n)

x = pow(m, p+q, n)
y = a*b%n

print("x :", x)
print("y :", y)

