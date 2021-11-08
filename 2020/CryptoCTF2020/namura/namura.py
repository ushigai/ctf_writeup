#!/usr/bin/python3

from Crypto.Util.number import *
from math import gcd
import random
from flag import flag

def xgcd(a, b):
    assert gcd(a, b) == 1
    if a == 1:
        return (1, 0)
    if b == 1:
        return (0, 1)
    x = +inverse(+a, b)
    y = -inverse(-b, a)
    return int(x), int(y)

def CRT(pairs):
    (a, m) = pairs[0]
    for (b, p) in pairs[1:]:
        k = ((b - a) * xgcd(m, p)[0]) % p
        a = (a + m * k) % (m * p)
    return (a, m)

def keygen(nbit, n, u):
	SP, SQ = [], []

	for i in range(n, u, -1):
		z = getRandomNBitInteger(nbit)
		s = 2 ** u * z
		SP = [s] + SP
		while True:
			s = getRandomNBitInteger(nbit + n - i + 1)
			if s > sum(SQ[i - n:]): # there is a bottleneck here :/
				SQ = [s] + SQ
				break

	for i in range(u, 0, -1):
		while True:
			z = getRandomNBitInteger(nbit + u - i + 1)
			if z % 2 == 1:
				break
		s = 2 ** (i - 1) * z
		SP = [s] + SP
		SQ = [getRandomNBitInteger(nbit + n - u)] + SQ

	while True:
		P, Q = getRandomRange(sum(SP) + 1, int(1.01 * sum(SP))), getRandomRange(sum(SQ) + 1, int(1.01 * sum(SQ)))
		if gcd(P, Q) == 1:
			N = P * Q
			break

	S = []
	for i in range(n):
		S.append(CRT([(SP[i], P), (SQ[i], Q)])[0])

	Sn = list(range(n))
	random.shuffle(Sn)

	pubkey = [0] * n
	for i in range(n):
		pubkey[i] = S[Sn[i]]

	return pubkey

def encrypt(pubkey, msg):
	C = 0
	for i in range(n):
		C += pubkey[i] * int(msg[i])
	return C

flag = flag.lstrip('CCTF{').rstrip('}')
bflag = bin(bytes_to_long(flag.encode('utf-8')))[2:]
n = len(bflag)
u = n - 30

pubkey = keygen((n+1) // 3, n, u)

print('pubkey =', pubkey)
enc = encrypt(pubkey, bflag)
print('enc =', enc)