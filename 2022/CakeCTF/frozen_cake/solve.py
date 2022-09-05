from Crypto.Util.number import *
from output import a, b, c, n

x = a * b % n

# c = m^(p*q) mod n
# x = m^(p+q) mod n

flag = x*inverse(c, n) % n
print(long_to_bytes(flag))

