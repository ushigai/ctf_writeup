from Crypto.Util.number import *

#10 834277 × 10 848931

p, q = 10834277, 10848931
n = p * q
e = 65537
ct = 73443041533799

phi = (p - 1)*(q - 1)

d = inverse(e, phi)
m = pow(ct, d, n)
print(m)

