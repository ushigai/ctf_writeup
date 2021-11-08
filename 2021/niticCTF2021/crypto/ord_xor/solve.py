
def xor(c: str, n: int) -> str:
    temp = ord(c)
    for _ in range(n):
        temp ^= n
    return chr(temp)


cipher = "nhtjcZcsfroydRx`rl"
flag = ""

for i in range(len(cipher)):
    flag += xor(cipher[i], i)

print(flag)
