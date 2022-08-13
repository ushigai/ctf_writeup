from Crypto.Util.number import *
from output import p, cipher, vs

def exploit():
    F = GF(p)
    PR.<a,b,g0> = PolynomialRing(F)
    gs = []
    for i in range(6):
        b_coef = F(0)
        for j in range(i):
            b_coef += a^j
        gs.append(a^i * g0 + b_coef * b)

    print(gs)
    print("-*-*-*-*-*-*-*-*-*-")

    fs = []
    for i in range(1, 5):
        f = PR(0)
        for j in range(6):
            g = gs[j]
            f += g * i**j
        v = vs[i-1][1]
        f -= F(v)
        fs.append(f)

    f1, f2, f3, f4 = fs
    print(fs)
    print("-*-*-*-*-*-*-*-*-*-")

    univar_polys = []
    I = ideal([f1, f2, f3, f4])
    print(I)
    B = I.groebner_basis()
    for b in B:
        b = b.univariate_polynomial()
        #print(b.roots())


if __name__ == "__main__":
    exploit()
