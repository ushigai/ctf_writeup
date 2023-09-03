from Crypto.Util.number import *

primes = [2 , 3 , 19 , 31 , 83 , 3331 , 165219437 , 550618493 , 66969810339969829 , 1168302403781268101731523384107546514884411261]

N = len(primes)

p, q = 1, 1
for i in range(1, N):
    p, q = 1, 1
    p_p = primes[i:]
    p_q = primes[:i]
    for j in p_p:
        p *= j
    for j in p_q:
        q *= j
    print(long_to_bytes(p))
    print(long_to_bytes(q))

# DUCTF{is_1nt3ger_f4ct0r1s4t10n_h4rd?}
