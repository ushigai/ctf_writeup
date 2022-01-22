from Crypto.Util.number import *
from random import randint

def nextPrime(n):
    while True:
        n += (n % 2) + 1
        if isPrime(n):
            return n


FLAG = b"CCTF{hogehoge_hugahuga_piyopiyo}"
FLAG = b"hoge"
f = [int(x) for x in bin(int(FLAG.hex(), 16))[2:]]

r = randint(300, 500)

a = nextPrime(r)
b = nextPrime(a)

g, h = [[_ for i in range(x) for _ in f] for x in [a, b]]
g_ = [f] * a
g_ = [g_[i][j] for i in range(len(g_)) for j in range(len(g_[i]))]
h_ = [f] * b
h_ = [h_[i][j] for i in range(len(h_)) for j in range(len(h_[i]))]

c = nextPrime(r >> 2)

print("length :", r)
print("a :", a)
print("b :", b)
print("c :", c)
