from Crypto.Util.number import *
from output import p, cipher, vs

F = GF(p)
PR.<a,b,g0> = PolynomialRing(F)

f1, f2, f3, f4 = PR(0), PR(0), PR(0), PR(0)

f1 = a^5*g0 + a^4*b + a^4*g0 + 2*a^3*b + a^3*g0 + 3*a^2*b + a^2*g0 + 4*a*b + a*g0 + 5*b + g0
f2 = 32*a^5*g0 + 32*a^4*b + 16*a^4*g0 + 48*a^3*b + 8*a^3*g0 + 56*a^2*b + 4*a^2*g0 + 60*a*b + 2*a*g0 + 62*b + g0
f3 = 243*a^5*g0 + 243*a^4*b + 81*a^4*g0 + 324*a^3*b + 27*a^3*g0 + 351*a^2*b + 9*a^2*g0 + 360*a*b + 3*a*g0 + 363*b + g0
f4 = 1024*a^5*g0 + 1024*a^4*b + 256*a^4*g0 + 1280*a^3*b + 64*a^3*g0 + 1344*a^2*b + 16*a^2*g0 + 1360*a*b + 4*a*g0 + 1364*b + g0

f1 -= vs[0][1]
f2 -= vs[1][1]
f3 -= vs[2][1]
f4 -= vs[3][1]

I = ideal([f1, f2, f3, f4])
#print(I)
B = I.groebner_basis()
a_b_g0 = []
for b in B:
    b = b.univariate_polynomial()
    #print(b.roots())
    a_b_g0.append(b.roots()[0][0])

a, b, g0 = a_b_g0

# ====================

a, b, x = int(a), int(b), int(g0)
print("a =", a)
print("b =", b)
print("g0 =", x)

def g():
    global a, b, x
    x = (a*x + b) % p
    return x

PR.<X> = PolynomialRing(GF(p))
f = g0 + g()*X + g()*X**2 + g()*X**3 + g()*X**4 + g()*X**5

vs_ = [(i, f(i)) for i in range(1, 5)]

assert vs == vs_

print((f - cipher).roots())
flag = (f - cipher).roots()[0][0]
print(long_to_bytes(flag))

