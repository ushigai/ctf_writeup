import gmpy2, binascii
from output import *

# CakeCTF{*****}
def culc(v1, v2): # https://gist.github.com/AkashiSN/81df83a26fd7c38efd55c5a2515ea9ff#file-common_modulus_attack-py
    n = p
    e1 = 101
    e2 = v2
    c1 = ciphers[3]
    c2 = v1
    val = gmpy2.gcdext(e1,e2)
    if val[1] < 0:
        a = -val[1]
        b = val[2]
        c1_inv = gmpy2.invert(c1,n)
        c1a = pow(c1_inv, a, n)
        c2b = pow(c2, b, n)
    else:
        a = val[1]
        b = -val[2]
        c2_inv = gmpy2.invert(c2,n)
        c1a = pow(c1, a, n)
        c2b = pow(c2_inv, b, n)
    m = (c1a * c2b)%n
    m,result = gmpy2.iroot(m,val[0])
    return m

ans = culc(ciphers[0], 67)
for cipher in ciphers:
    for i in range(200):
        if culc(cipher, i) == ans:
            print(chr(i), end="")
            break
    else:
        print("e", end="")

print("")

# CakeCTF{4h4_p14in73x7_5p4c3_i5_7000000_5m411}
