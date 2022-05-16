import math
import hashlib
import sys
import functools

ITERS = int(2e7)
VERIF_KEY = "96cc5f3b460732b442814fd33cf8537c"
ENCRYPTED_FLAG = bytes.fromhex("42cbbce1487b443de1acf4834baed794f4bbd0dfb5df5e6f2ad8a2c32b")

def m_func(i):
    if i == 0: return 1
    if i == 1: return 2
    if i == 2: return 3
    if i == 3: return 4

    return 55692*m_func(i-4) - 9549*m_func(i-3) + 301*m_func(i-2) + 21*m_func(i-1)

def f2(n, coeff):
    p, q, r = coeff
    if n <= 3:
        return 1
    a, b, c, d = 1, 1, 1, 1
    for i in range(n - 3):
        a, b, c = b, c, d
        d = (p*c + q*b + r*a) % (10**10000)
    return d

def m_func(i):
    a, b, c, d, e = 1, 1, 2, 3, 4
    a, b, c, d, e = 1, 1, 1, 1, 1
    for i in range(i - 3):
        a, b, c, d = b, c, d, e
        d = (55692*a - 9549*b + 301*c + 21*d) % (10**10000)
    return d

def f3(n):
    F = Integers(10**10000)
    A = Matrix(F, [[21, 301, -9549, 55692], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
    return int(sum((A^(n-2))[1]))


def decrypt_flag(sol):
    sol = sol % (10**10000)
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()

    if sol_md5 != VERIF_KEY:
        print("Incorrect solution")
        sys.exit(1)

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([char ^ key[i] for i, char in enumerate(ENCRYPTED_FLAG)]).decode()
    print(flag)

if __name__ == "__main__":
    ITERS = 6
    for ITERS in range(6, 10):
        sol = m_func(ITERS)
        print(sol)
        print(f3(ITERS))
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()
    print(sol_md5 == VERIF_KEY)
    #sol = m_func(ITERS)
    #decrypt_flag(sol)
