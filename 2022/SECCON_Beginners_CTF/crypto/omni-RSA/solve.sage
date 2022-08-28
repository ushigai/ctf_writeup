from Crypto.Util.number import *


rq = 7062868051777431792068714233088346458853439302461253671126410604645566438638
e = 2003
n = 140735937315721299582012271948983606040515856203095488910447576031270423278798287969947290908107499639255710908946669335985101959587493331281108201956459032271521083896344745259700651329459617119839995200673938478129274453144336015573208490094867570399501781784015670585043084941769317893797657324242253119873
s = 1227151974351032983332456714998776453509045403806082930374928568863822330849014696701894272422348965090027592677317646472514367175350102138331
cipher = 82412668756220041769979914934789463246015810009718254908303314153112258034728623481105815482207815918342082933427247924956647810307951148199551543392938344763435508464036683592604350121356524208096280681304955556292679275244357522750630140768411103240567076573094418811001539712472534616918635076601402584666


shift = 2^470
for k in range(1, e):
    print(f"[*] {k} / {e}")
    F.<x> = PolynomialRing(Zmod(n))
    f = e*(x*shift + s) - 1 + k*rq - k
    f = f.monic()
    x0 = f.small_roots(X=2^42, beta=0.20, epsylon=1/16)
    if len(x0) != 0:
        d_ = int(x0[0])*shift + s 
        print("ok")
        break


var("r")
fr = 1 + k*(r - rq - 1)*(r - 1) - e*d_
print(solve(fr, r))
# [
# r == 115782269004778310532099644136706472617339510140211345931055084365526756095881,
# r == -108719400953000878740030929903618126158486070837750092259928673760881189657241
# ]

r = 115782269004778310532099644136706472617339510140211345931055084365526756095881
q = r - rq
p = n // q // r
assert p*q*r == n

phi = (p - 1)*(q - 1)*(r - 1)
d = inverse(e, phi)
flag = pow(cipher, d, n)

print(long_to_bytes(flag))

