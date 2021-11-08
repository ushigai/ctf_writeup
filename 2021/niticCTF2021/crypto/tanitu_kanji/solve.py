alphabets = "abcdefghijklmnopqrstuvwxyz0123456789{}_"
after1 = "fl38ztrx6q027k9e5su}dwp{o_bynhm14aicjgv"
after2 = "rho5b3k17pi_eytm2f94ujxsdvgcwl{}a086znq"

cipher = "l0d0pipdave0dia244im6fsp8x"

def conv(s: str, table: str) -> str:
    res = ""
    for c in s:
        i = table.index(c)
        res += alphabets[i]
    return res


for i in range(2**10):
    flag = cipher
    for j in range(10):
        if i & 1:
            flag = conv(flag, after1)
        else:
            flag = conv(flag, after2)
        i >>= 1
    if "ctf{" in flag:
        print(flag)

        
