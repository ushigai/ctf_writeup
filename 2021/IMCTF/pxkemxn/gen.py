import secrets
import random

# 参考 : https://qiita.com/srtk86/items/609737d50c9ef5f5dc59
def is_prime(n):
    if n == 2: return True
    if n == 1 or n & 1 == 0: return False

    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for k in range(100):
        a = random.randint(1, n - 1)
        t = d
        y = pow(a, t, n)

        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1

        if y != n - 1 and t & 1 == 0:
            return False

    return True

class LCG:
    def __init__(self, S):
        self.A = secrets.randbits(256)
        self.B = secrets.randbits(256)

        while True:
            self.M = secrets.randbits(256)
            if is_prime(self.M):
                break
        
        self.x = S % self.M

    def next(self):
        self.x = ((self.A * self.x) + self.B) % self.M
        return self.x

lcg = LCG(secrets.randbits(256))
print("M : " + str(lcg.M))

cnt = 100
for i in range(cnt):
    x = lcg.next()
    if i in [0, 1, 2]:
        print("X[{}] : {}".format(i, x))

print("X[{}] : ?".format(cnt))
