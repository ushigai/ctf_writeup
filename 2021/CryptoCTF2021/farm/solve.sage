from sage.all import *
import string, base64, math

S = string.printable[:62] + '\\='
F = list(GF(64))
PKEY = list(GF(64))
enc = "805c9GMYuD5RefTmabUNfS9N9YrkwbAbdZE0df91uCEytcoy9FDSbZ8Ay8jj"
known = "Q0NURn"

def maptofarm(c):
    assert c in S
    return F[S.index(c)]


# enc += ALPHABET[F.index(pkey * maptofarm(chr(m)))]
#tmp = chr(m)
#tmp = maptofarm(tmp)

#tmp = pkey * tmp

#tmp = F.index(tmp)
#tmp = ALPHABET[tmp]
#enc += tmp

ind = S.index("8")
f1 = F[ind]

f2 = maptofarm("Q")

for pkey in PKEY:
    if f1 * pkey == f2:
        flag = ""
        for c in enc:
            tmp = S.index(c)
            f1 = F[tmp]
            f2 = f1 * pkey
            flag += S[F.index(f2)]
        break

print(base64.b64decode(flag.encode()))
            