from binascii import hexlify, unhexlify
from hashlib import sha256
from output import cipher

hint = b'Great and Noble Leader of the Tariaki'
cipher = list(unhexlify(cipher))
hint = list(hint)

def decrypt_data(cipher, k):
    m = b''
    for i in range(0, len(cipher), 32):
        chunk = cipher[i:i+32]
        for a, b in zip(chunk, k):
            m += bytes([a ^ b])
        k = sha256(k).digest()
    return m

for pad_len in range(0, 32):
    key = [x^y for x, y in \
        zip(cipher, list(b"\x00"*pad_len) + hint)]
    key = bytes(key[:32])
    m = decrypt_data(cipher, key)
    if b"HTB"in m:
        print(m)
