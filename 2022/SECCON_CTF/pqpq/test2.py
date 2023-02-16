from Crypto.Util.number import *

p = getPrime(512)
q = getPrime(512)

flag = bytes_to_long(b"SECCON{hogehoge_fugafuga_hogehoge_fugafuga}")
print(flag.bit_length())
e = 65537

r = pow(p, e, n)
s = (pow(p, e, n) - pow(q, e, n)) % n

print("p :", p)
print("q :", q)
print("s :", s)

#cipher = pow(flag, e, p)

#print(cipher)

#phi = p - 1
#d = inverse(e, phi)
#mm = pow(cipher, d, p)

#print(long_to_bytes(mm))
