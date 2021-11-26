from string import ascii_lowercase, digits

CHARSET = 'DUCTF{}_!?\'' + ascii_lowercase + digits
n = len(CHARSET)

def to_num(c):
    return CHARSET.index(c)

def to_chr(x):
    return CHARSET[x]

enc = "Ujyw5dnFofaou0au3nx3Cn84"

P.<x> = PolynomialRing(GF(n))

known_pt = 'DUCTF{}'
known_ct = enc[:6] + enc[-1]
pairs = [(to_num(p), to_num(c)) for p,c in zip(known_pt, known_ct)]
f = P.lagrange_polynomial(pairs)

print(pairs)
print(f)
