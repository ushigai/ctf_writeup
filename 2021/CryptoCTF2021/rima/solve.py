from Crypto.Util.number import *

def nextPrime(n):
    while True:
        n += (n % 2) + 1
        if isPrime(n):
            return n

def base_n(num_10,n): # https://qiita.com/ether2420/items/061c19a000c52adf7f3e
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])

g = open("g.enc", "rb").read()
h = open("h.enc", "rb").read()
g, h = bytes_to_long(g), bytes_to_long(h)
g, h = list(str(base_n(g, 5))), list(str(base_n(h, 5)))
g, h = list(map(int, g)), list(map(int, h))

for length in range(200, 1000):
    a = nextPrime(length + 1)
    b = nextPrime(a)
    c = nextPrime((length + 1) >> 2)
    if not(a == 257 and b == 263):
        continue
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
        #print("".join(list(map(str, flag))))
        print(length, a, b, c)
        print(len(flag))
        print("-*-*-*-*-*-")
        #if 2 in flag:
            #break
        #flag = int("".join(list(map(str, flag[1:]))), base=2)
        #print(long_to_bytes(flag))

a, b, c = 257, 263, 67
