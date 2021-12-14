from Crypto.Util.number import *
from sympy import *
import random

def gen_sexy_primes():
    p=getPrime(256)
    q=p+6

    while((p%4!=3)or(q%4!=3)):
        p=getPrime(256)
        q=nextprime(p+1)
    return p, q

p, q = gen_sexy_primes()


def mixer(num):
    while(num>1):
        if(int(num) & 1):
            num=3*num+1
        else:
            num=num/2
    return num


print(mixer(q - p))
