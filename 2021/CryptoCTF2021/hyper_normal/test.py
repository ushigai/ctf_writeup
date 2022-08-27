#!/usr/bin/env python3

import random

p = 8443

def transpose(x):
    """
    転置行列
    """
    result = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
    return result

def vsum(u, v):
    """
    u,vの内積
    """
    assert len(u) == len(v)
    l, w = len(u), []
    for i in range(l):
        w += [(u[i] + v[i]) % p]
    return w

def sprod(a, u):
    """
    あれ
    """
    w = []
    for i in range(len(u)):
        w += [a*u[i] % p]
    return w

def encrypt(msg):
    l = len(msg)
    hyper = [ord(m)*(i+1) for (m, i) in zip(list(msg), range(l))]
    # FLAG{} => [ord("F")*0, ord("L")*1, ord("A")*2, ...]

    V, W = [], []
    for i in range(l):
        v = [0]*i + [hyper[i]] + [0]*(l - i - 1)
        V.append(v)
    print(*V, sep="\n")
    print("-*-*-*-*-")
    random.shuffle(V)
    print(*V, sep="\n")

    for _ in range(l):
        R, v = [random.randint(0, 126) for _ in range(l)], [0]*l
        print("R :", R)
        for j in range(l):
            r = sprod(R[j], V[j])
            v = vsum(v, r)
        W.append(v)
    print(*W, sep="\n")
    random.shuffle(transpose(W))
    return W

FLAG = "FLAG"
enc = encrypt(FLAG)
print("-*-*-*-*-")
print(*enc, sep="\n")
