from Crypto.Util.number import *
from output import cipher

for c in cipher:
    ans = 0
    for i in c:
        ans += 1 if i % 67 == 0 else 0
    print(ans)



