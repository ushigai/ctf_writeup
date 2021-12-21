import base64

flag = b"imctf{"

def oreore_crypto(flag):
    encoded = base64.b64encode(flag)
    enc = encoded.hex()
    return enc

print("ciphertext =", oreore_crypto(flag))
