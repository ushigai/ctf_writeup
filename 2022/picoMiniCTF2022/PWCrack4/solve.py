import hashlib
from Crypto.Util.number import *

PwList = ["1c39", "ef9b", "dba8", "4e0b", "8392", "19a6", "d45b", "8dfa", "491d", "c7b3", "1201", "a2c9", "b391", "ea3a", "bd7f", "f090", "1c78", "b683", "5ccc", "e019", "cedd", "ed2a", "da9d", "dca6", "f56c", "ed57", "1b86", "c4af", "df6b", "4067", "fa42", "7c31", "b593", "de0e", "52cf", "b011", "8630", "ebb4", "e783", "df96", "defe", "4930", "2381", "a155", "3c20", "5801", "5c90", "495b", "5ae0", "42fc", "2ab0", "1ecb", "7d60", "c63e", "90ce", "10c0", "41f1", "163c", "e41e", "ce19", "7f3f", "734a", "e12f", "7bd8", "b7a1", "c51f", "a29c", "d7c1", "4fe2", "6eb3", "ac03", "b238", "7c93", "dfd7", "6495", "77f8", "afb0", "73cf", "2ced", "aa22", "cca2", "66a6", "f581", "7539", "da70", "da3d", "a99d", "e5da", "e37a", "e58b", "b753", "1280", "7831", "ec80", "dc8b", "5eb4", "9a27", "af9d", "8cf8", "d788"]

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

correct_pw_hash = open('level4.hash.bin', 'rb').read()

for i in PwList:
    if hash_pw(i) == correct_pw_hash:
        print(i)

