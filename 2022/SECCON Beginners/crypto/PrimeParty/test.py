from Crypto.Util.number import *
from os import urandom

N = 100
m = b"ctf4b{hogehoge_hugahuga_piyopiyo}"
m = bytes_to_long(m)
ans = [GCD(m, getPrime(10)) for i in range(N)]

print(sum(ans))
assert sum(ans) == N

