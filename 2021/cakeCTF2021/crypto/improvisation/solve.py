from Crypto.Util.number import *


def LFSR(r):
    while True:
        yield r & 1
        b = (r & 1) ^\
            ((r & 2) >> 1) ^\
            ((r & 8) >> 3) ^\
            ((r & 16) >> 4)
        r = (r >> 1) | (b << 63)


cipher = 0x58566f59979e98e5f2f3ecea26cfb0319bc9186e206d6b33e933f3508e39e41bb771e4af053
cipher = int(bin(cipher)[2:][::-1], 2) << 1
prefix = bytes_to_long("CakeCTF{"[::-1].encode())
lfsr = LFSR((cipher & (2**64 - 1)) ^ prefix)
length = cipher.bit_length()

key = 0
for i in range(length):
    key += next(lfsr) * 2**i

m = key ^ cipher
print(long_to_bytes(m).decode()[::-1])
