#!/usr/bin/env python3

from Crypto.Util.number import *

nbit = 64

while True:
    p, q = getPrime(nbit), getPrime(nbit)
    P = int(str(p) + str(q))
    Q = int(str(q) + str(p))
    PP = int(str(P) + str(Q))
    QQ = int(str(Q) + str(P))
    NN = PP * QQ
    strn = str(p*q)
    if strn[:18] == str(NN)[:18] and \
        strn[-18:] == str(NN)[-18:]:
        pass
    else:
        print("==============")
        print("n : ", p*q)
        print("NN :                     ", str(NN)[-18:])
        print("NN :", str(NN)[:18])
    #break
    #ans1 = str(P*Q)
    #ans2 = str(n)[-]
	# if isPrime(PP) and isPrime(QQ):
		# break


print("p  :", p)
print("q  :", q)
#print("PP :", PP)
#print("QQ :", QQ)
print("P :", P)
print("Q :", Q)
#print("N :", str(P*Q)[-40:])

