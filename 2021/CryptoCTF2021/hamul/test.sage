#!/usr/bin/env python3

from Crypto.Util.number import *

nbit = 64
print("hoge")

while True:
    p, q = getPrime(nbit), getPrime(nbit)
    P = int(str(p) + str(q))
    Q = int(str(q) + str(p))
    PP = int(str(P) + str(Q))
    QQ = int(str(Q) + str(P))
    break
    #ans1 = str(P*Q)
    #ans2 = str(n)[-]
	# if isPrime(PP) and isPrime(QQ):
		# break

NN = PP * QQ

print("p  :", p)
print("q  :", q)
#print("PP :", PP)
#print("QQ :", QQ)
print("P :", P)
print("Q :", Q)
print("n :", p*q)
print("N :", str(P*Q)[-42:])
print("NN :", str(NN)[-42:])

