from base64 import b64decode
from Crypto.Util.number import *

cipher = int("6157316a64475a374d484a6c4d484a6c58324e79655842304d4639706331397a6458426c636c397a5a574e31636d5639", 16)
cipher = long_to_bytes(cipher)
cipher = b64decode(cipher)
print(cipher)

# imctf{0re0re_crypt0_is_super_secure}

