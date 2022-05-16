from Crypto.Util.number import *

f = open('level5.hash.bin', 'rb').read()
print(f)
print(hex(bytes_to_long(f)))

