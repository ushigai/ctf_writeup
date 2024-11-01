from random import randint, shuffle
from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha256
#from secret import *
import os

#assert sha256(KEY).hexdigest().startswith('786f36dd7c9d902f1921629161d9b057')

class BBS:
    def __init__(self, bits, length):
        self.bits = bits
        self.out_length = length
        self.zero, self.one = 0, 0

    def reset_params(self):
        self.zero, self.one = 0, 0
        self.state = randint(2, 2 ** self.bits - 2)
        self.m = getPrime(self.bits//2) * getPrime(self.bits//2) * randint(1, 2)
    
    def extract_bit(self):
        self.state = pow(self.state, 2, self.m)
        return str(self.state % 2)

    def gen_output(self):
        self.reset_params()
        out = ''
        for _ in range(self.out_length):
            out += self.extract_bit()
        self.zero += 1 if "000000000000000000000000000000000000000000" in out else 0
        self.one += 1 if "111111111111111111111111111111111111111111111" in out else 0
        return out

    def encrypt(self, msg):
        out = self.gen_output()
        key = sha256(out.encode()).digest()
        iv = os.urandom(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        #return (iv.hex(), cipher.encrypt(pad(msg.encode(), 16)).hex())
        return (iv.hex(), cipher.encrypt(pad(msg.encode(), 16)).hex(), self.zero, self.one)

encryptor = BBS(512, 256)

enc_messages = []
MESSAGES = "a"*1000
zero, one = 0, 0
ans = 0
for msg in MESSAGES:
    res = encryptor.encrypt(msg)
    if res[2] or res[3]:
        ans += 1
print(ans)
#for msg in MESSAGES:
    #enc_messages.append([encryptor.encrypt(msg) for _ in range(10)])

#enc_flag = AES.new(KEY, AES.MODE_ECB).encrypt(pad(FLAG, 16))

#with open('output.txt', 'w') as f:
    #f.write(f'{enc_messages}\n')
    #f.write(f'{enc_flag.hex()}\n')


print(zero)
print(one)
