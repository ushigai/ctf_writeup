L = list(range(100))

print(L)
print("-*-*-*-*-")

for i in range(len(L) - 1):
    L[i] += L[i + 1]

print(L)
print("-*-*-*-*-")

for i in [L]:
    for j in range(len(i) - 1):
        i[-j - 2] -= i[-j - 1]

print(L)
