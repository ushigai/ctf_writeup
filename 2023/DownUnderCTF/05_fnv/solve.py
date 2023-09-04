def fnv1(s):
    h = 0xcbf29ce484222325
    h = 0x0000000000000001
    for b in s:
        h *= 0x00000100000001b3
        h &= 0xffffffffffffffff
        h ^= b
        print("h :", bin(h)[2:].zfill(64))
    return h


#h = fnv1([1,2,3,4,5,6,7,8,9,10,11])
h = fnv1([0,0,0,0,0,0,0,0,0,0,0,0,0])
