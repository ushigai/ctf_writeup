from Crypto.Util.number import *


def pgcd(f, g):
    while g:
        f, g = g, f % g
    return f


N = 131524088884825815804488932464729357040334400654894482058463384631465646564218562087397372641691153724192714309237816737178676891008253858742684770007206270690351261617425456727727358875299906146914830254560972052930255319744195538734348410986466067329708785605858045414804679488686183262367088579297015291141
e = 3
c1 = 53446890814226238195814900775610146361354688642953984822875182297861976571235892581728318314459205473773163777796449566433544434134073179844466939691972553393776130664306258111549148944010961079361802647342130537687069419065674984241592765378827102906801889899262139334877519178755098426417577535191788787887
c2 = 53446890814226238195814900775610146361354688642953984822875182321385725425008957482596867857544541131433772697093663878596038952458110930478268276653144018403231153004739183129121025413011758697599979926904528387653993851636222310955660828650069081991070148602980332627389671548440711748081532341124803683994


delta_bits = 96

PR.<x, y> = PolynomialRing(Zmod(N))
PRS.<xs> = PolynomialRing(Zmod(N))

g1 = x^e - c1
g2 = (x + y)^e - c2

gg1 = g1.change_ring(PRS)
gg2 = g2.change_ring(PRS)
h = gg2.resultant(gg1)
h = h.univariate_polynomial().subs(y=xs).monic()

delta_ans = h.small_roots(epsilon=1/60)
if len(delta_ans):
    if 2**delta_bits + 1 < delta_ans[0]:
        print("Diff :", int(delta_ans[0]) - N)
    else:
        print("Diff :", delta_ans[0])
else:
    exit("uwa")

# Franklin-Reiter Related Message Attack
PR.<x> = PolynomialRing(Zmod(N))
g1 = x^e - int(c1)
g2 = (x + int(delta_ans[0]))^e - int(c2)

ph = pgcd(g1, g2)
ph = ph.monic()
flag = -ph[0] >> delta_bits

print(long_to_bytes(int(flag)))
