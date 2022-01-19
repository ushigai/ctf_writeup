from Crypto.Util.number import *

cipher = "27282a3d2f"
for i in range(0, len(cipher), 2):
    c = int(cipher[i:i+2], base=16)
    print(chr(c ^ 105), end="")

cipher = "327c27793d217a3b1679277a162b303d7a3a163d217a162d3c3a3d34"
for i in range(0, len(cipher), 2):
    c = int(cipher[i:i+2], base=16)
    print(chr(c ^ 73), end="")

print("")
# a = [print(cipher[i:i+2]) for i in range(0, len(cipher), 2)]

