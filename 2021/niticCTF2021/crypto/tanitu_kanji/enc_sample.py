import os
alphabets = "abcdefghijklmnopqrstuvwxyz0123456789{}_"
after1 = "fl38ztrx6q027k9e5su}dwp{o_bynhm14aicjgv"
after2 = "rho5b3k17pi_eytm2f94ujxsdvgcwl{}a086znq"

format = os.environ["FORMAT"]
flag = os.environ["FLAG"]

assert len(format) == 10


def conv(s: str, table: str) -> str:
    res = ""
    for c in s:
        i = alphabets.index(c)
        res += table[i]
    return res


for f in format:
    if f == "1":
        flag = conv(flag, after1)
    else:
        flag = conv(flag, after2)

with open("./flag", "w") as file:
    file.write(flag)
