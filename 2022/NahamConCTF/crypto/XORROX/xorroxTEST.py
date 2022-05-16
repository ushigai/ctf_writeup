#!/usr/bin/env python3

import random

flag = b"flag{hogehoge}"

key = [random.randint(1, 256) for _ in range(len(flag))]

xorrox = []
enc = []
for i, v in enumerate(key):
    k = 1
    for j in range(i, 0, -1):
        k ^= key[j]
    xorrox.append(k)
    enc.append(flag[i] ^ v)

print("xorrox :", xorrox)
print("enc :", enc)
print("key :", key)

"""
xorrox : [1, 72, 162, 226, 228, 223, 37, 9, 36, 27, 160, 226, 183, 9]
enc : [254, 37, 139, 39, 125, 83, 149, 75, 72, 87, 212, 37, 48, 195]
key : [152, 73, 234, 64, 6, 59, 250, 44, 45, 63, 187, 66, 85, 190]
"""
