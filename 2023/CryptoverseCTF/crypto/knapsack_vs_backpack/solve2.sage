from pwn import *
from Crypto.Util.number import *
from math import log2

io = remote("67.205.179.135", int(7272))

def knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    selected = [[-1] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for j in range(capacity + 1):
            if j >= weight:
                if dp[i - 1][j] < dp[i - 1][j - weight] + value:
                    dp[i][j] = dp[i - 1][j - weight] + value
                    selected[i][j] = i - 1
                else:
                    dp[i][j] = dp[i - 1][j]
                    selected[i][j] = selected[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
                selected[i][j] = selected[i - 1][j]

    j = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if selected[i][j] != selected[i - 1][j]:
            selected_items.append(selected[i][j])
            j -= items[selected[i][j]][0]
    selected_items = selected_items[::-1]
    return selected_items, dp[-1][-1]


for _ in range(10):
    res = io.recv(4096).decode().split("\n")
    exec("W = " + res[1])
    exec("P = " + res[2])
    A = int(res[3].split()[-1])
    N = 64
    items = [(w, p) for w, p in zip(W, P)]
    capacity = A
    selected_items, dp = knapsack(items, capacity)
    ans = " ".join(list(map(str, selected_items)))+"\n"

    io.send(ans.encode())

res = io.recvline(4096).decode()
print(res)

# challenge2

def create_matrix(pub, c):
    N = len(pub)
    m_id = matrix.identity(N) * 2
    m = matrix(ZZ, 1, N + 1, pub[:] + [-c])
    B = m_id.augment(matrix(ZZ, N, 1, [-1] * N))
    m = m.stack(B)
    return m

def shortest_vector(matrix):
    for i in matrix.columns():
        if not(i[0]) and all([(j == -1 or j == 1) for j in i[1:]]):
            return i

for _ in range(10):
    res = io.recv(4096).decode().split("\n")
    print(res)
    exec("pub_key = " + res[1])
    cipher = int(res[2].split()[-1])
    d = len(pub_key) / log2(max(pub_key))
    print("d =", d)

    M = create_matrix(pub_key, cipher)
    LLL_M = M.transpose().LLL().transpose()
    V = shortest_vector(LLL_M) 

    plane = "".join(list(map(str, V)))
    plane = plane.replace("0", "")
    plane = plane.replace("-1", "0")

    print("plane :", long_to_bytes(int(plane, base=2)))
    ans = str(int(plane, base=2)) + "\n"
    io.send(ans.encode())

res = io.recv(4096).decode()
print(res)
