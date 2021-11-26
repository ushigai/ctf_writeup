from string import ascii_lowercase, digits

CHARSET = 'DUCTF{}_!?\'' + ascii_lowercase + digits
n = len(CHARSET)

A = [1, 20, 35, 33, 42, 14, 41]

S_eq = [[i, A[i]] for i in range(7)]

print(S_eq)
P.<x> = PolynomialRing(GF(47))
f = P.lagrange_polynomial(S_eq)

assert all([f(x=i) == A[i] for i in range(7)])

table = {}
cipher = "Ujyw5dnFofaou0au3nx3Cn84"

for i in range(n):
    table[f(x=i)] = i

for c in cipher:
    c = CHARSET.index(c)
    print(CHARSET[table[c]], end="")
