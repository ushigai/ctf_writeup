from Crypto.Util.number import *
from gmpy2 import iroot

flag = ""
flag = int(flag, base=16)
c = "e607cdfc66cb35fb929214d4dfba94627f7ef42e658e6ae3531324ed589010409fe85077b875cb668018597f5057c90ee50b90e6e7657146b16a1d66e66b494"
m = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
m = bytes_to_long(bytes.fromhex(m)) ** 2

n = m - int(c, base=16)
print(n)

def FermatsMethod(n):
    i = iroot(n, 2)[0] + 1
    j = iroot(i**2 - n, 2)[0]
    Z = i**2 - n - j**2
    
    return int(i + j), int(i - j)

p, q = FermatsMethod(n)

assert isPrime(p) and isPrime(q)

for i in range(10**5):
    flag_ = long_to_bytes(int(iroot(flag, 2)[0]))
    if b"nite{" in flag_:
        print(flag_)
    flag += n

