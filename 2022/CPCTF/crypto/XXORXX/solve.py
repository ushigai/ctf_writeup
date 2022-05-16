from Crypto.Util.number import *

cipher = b"VEVASnm%gJ$ Jv%xx`\"!\"$c&h"
cipher = list(cipher)
print(cipher)

key = 21
for c in cipher:
    print(chr(c ^ key), end="")

print("")
