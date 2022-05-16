from Crypto.Util.number import *

cipher = open("out", "r").read()

for c in cipher:
    print(chr(ord(c) - 39137), end="")

print()

c = 0x4e68d16a61bc2ea72d5f971344e84f11

print(long_to_bytes(c))
