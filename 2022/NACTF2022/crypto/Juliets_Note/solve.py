S = "18 5 7 24 10 23 9 9 29 19 25 16 5 24 9 22 5 16 16 13 11 5 24 19 22".split()
S = list(map(int, S))

for s in S:
    print(chr(s + 60), end="")

print("")
