with open("flag.txt", "r") as fin:
    flag = fin.read().strip()

size = 7
flag = [flag[i:i + size] for i in range(0, len(flag), size)]  # split text into groups of size

for i in range(len(flag)):
    cur = 0
    flag[i] = flag[i][::-1]  # reverse flag[i]
    for j in flag[i]:
        cur <<= 8
        cur += ord(j)
    flag[i] = cur


def f(p, k, mod):
    # returns f(11^(11^p), k) % mod as defined in the problem statement
    pass


def generate():
    # generates appropriate p, k, and mod
    pass


with open("enc.txt", "w") as fout:
    for i in flag:
        p, k, mod = generate()
        enc = f(p, k, mod) ^ i
        fout.write(str(p) + " " + str(k) + " " + str(mod) + " " + str(enc) + "\n")
