import random
from secret import FLAG

def encrypt(message):
    text = list(message.encode('ascii'))
    for _ in range(100):
        a = random.randrange(1, 32)
        b = random.randrange(1, 32)
        for i in range(len(text)):
            text[i] = a ^ ((b ^ text[i]) ^ a) ^ b ^ a
    ciphertext = bytes(text)
    return ciphertext

cipher = encrypt(FLAG)
with open('ciphertext', 'wb') as f:
    f.write(cipher)
