import os
flag = os.environ["FLAG"]


def xor(c: str, n: int) -> str:
    temp = ord(c)
    for _ in range(n):
        temp ^= n
    return chr(temp)


enc_flag = ""
for i in range(len(flag)):
    enc_flag += xor(flag[i], i)

with open("./flag", "w") as f:
    f.write(enc_flag)
