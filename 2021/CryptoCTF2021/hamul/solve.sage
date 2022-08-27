from Crypto.Util.number import *

n = 98027132963374134222724984677805364225505454302688777506193468362969111927940238887522916586024601699661401871147674624868439577416387122924526713690754043
c = 42066148309824022259115963832631631482979698275547113127526245628391950322648581438233116362337008919903556068981108710136599590349195987128718867420453399
e = 65537

n_upper = str(n)[:18]
#n_upper = str(980271329633741342)
#n_upper = str(980271329633741341)
n_lower = str(n)[-18:]


for i in range(1000):
    d = str(i).zfill(2)
    print("[+] COUNT :", d)
    nn = int(n_upper + d + n_lower)
    ans = list(factor(nn))
    if len(ans) != 2:
        print("[+] Not two factors.")
        continue
    p, q = ans
    p, q = p[0], q[0]
    print("[+] factor :", p, q)
    P = int(str(p) + str(q))
    Q = int(str(q) + str(p))
    PP = int(str(P) + str(Q))
    QQ = int(str(Q) + str(P))
    if not(isPrime(PP) and isPrime(QQ)):
        print("[+] `PP` or `QQ` is not a prime number.")
        continue
    phi = (PP - 1)*(QQ - 1)
    d = inverse(e, phi)
    flag = long_to_bytes(pow(c, d, n))
    print(flag)
    break

