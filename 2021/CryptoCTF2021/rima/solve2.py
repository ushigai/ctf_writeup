from Crypto.Util.number import *
from gL import g
from hL import h

length = 255
a = 257
b = 263
c = 67
g_, h_ = g[:], h[:]
for i in [g_, h_]:
    for j in range(len(i) - c):
        i[-c - j - 1] -= i[-j - 1]

if sum(g_[:c]) + sum(h_[:c]) == 0:
    g__, h__ = g_[c:], h_[c:]
    assert g__[:length + 1] == h__[:length + 1]
    flag = g__[:length + 1]
    for i in range(length):
        flag[-i - 2] -= flag[-i - 1]
    print(long_to_bytes(int("".join(list(map(str, flag[1:]))), 2)))

