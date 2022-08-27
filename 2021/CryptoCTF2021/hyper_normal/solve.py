from Crypto.Util.number import *
from output import cipher


def transpose(x):
	"""
	転置行列
	"""
	result = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
	return result


p = 8443
flag = ""
cipher = transpose(cipher)
for i in range(len(cipher)):
    c = cipher[i]
    for j in range(32, 128):
        coeff = inverse((i + 1) * j, p)
        if all(0 <= r * coeff % p <= 126 for r in c):
            flag += chr(j)
            break

print(flag)

