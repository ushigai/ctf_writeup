from Crypto.Util.number import inverse, GCD
from functools import reduce

def solve_M(states):
    diffs = [X_1 - X_0 for X_0, X_1 in zip(states, states[1:])]
    multiples_of_M = [T_2 * T_0 - T_1 ** 2 for T_0, T_1, T_2, in zip(diffs, diffs[1:], diffs[2:])]

    # GCD(GCD(multiples_of_M[0],multiples_of_M[1]), multiples_of_M[2])
    M = reduce(GCD, multiples_of_M)
    return M

def solve_A(states, M):
    A = (states[2] - states[1]) * inverse((states[1] - states[0]), M)
    return A

def solve_B(states, A, M):
    B = (states[1] - A * states[0]) % M
    return B


X = [1711700508854459564, 7426870668700400289, 14391986150169726378, 15369608455104884503, 9038571200792588664, 14918858422273414557, 14830307082840265622, 8720264661952989107, 11402451316050596740, 12005889711690007257]
X0 = 1711700508854459564
X1 = 7426870668700400289
X2 = 14391986150169726378
X3 = 15369608455104884503
X4 = 9038571200792588664
X5 = 14918858422273414557
X6 = 14830307082840265622
X7 = 8720264661952989107
# 11402451316050596740
# 12005889711690007257
Y1 = X1 - X2
Y2 = X2 - X3
Y3 = X3 - X4
Y4 = X4 - X5
Y5 = X5 - X6


M = solve_M([X0, X1, X2, X3, X4, X5, X6])
A = solve_A([X0, X1, X2, X3, X4, X5, X6], M)
B = solve_B([X0, X1, X2, X3, X4, X5, X6], A, M)


print("A = ", A)
print("B = ", B)
print("M = ", M)
print((A*X6 + B) % M)

