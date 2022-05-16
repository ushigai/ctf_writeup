from Crypto.Util.number import *

c = 810
e = 5
p = 487
q = 853

n = p * q
phi = (p - 1)*(q - 1)
d = inverse(e, phi)
flag = pow(c, d, n)
flag = str(flag)

print(flag)
