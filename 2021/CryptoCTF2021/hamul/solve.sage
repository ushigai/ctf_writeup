from Crypto.Util.number import *

n = 98027132963374134222724984677805364225505454302688777506193468362969111927940238887522916586024601699661401871147674624868439577416387122924526713690754043
c = 42066148309824022259115963832631631482979698275547113127526245628391950322648581438233116362337008919903556068981108710136599590349195987128718867420453399

n_upper = str(n)[:18]
n_lower = str(n)[-18:]

for i in range(1000):
    d = str(i).zfill(3)
    print("[+] COUNT :", d)
    n = int(n_upper + d + n_lower)
    ans = list(factor(n))
    if len(ans) != 2:
        #print("[+] Not two factors.")
        continue
    p, q = ans
    p, q = p[0], q[0]
    P = int(str(p) + str(q))
    Q = int(str(q) + str(p))
    PP = int(str(P) + str(Q))
    QQ = int(str(Q) + str(P))
    if isPrime(PP) and isPrime(QQ):
        print("OK")
        break

