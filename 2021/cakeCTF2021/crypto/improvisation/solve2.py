import random

def LFSR():
    r = random.randrange(1 << 64)
    while True:
        yield r & 1
        b = (r & 1) ^\
            ((r & 2) >> 1) ^\
            ((r & 8) >> 3) ^\
            ((r & 16) >> 4)
        r = (r >> 1) | (b << 63)

l = LFSR()
for i in range(10):
    for j in range(64):
        print(next(l), end="")
    print("")
