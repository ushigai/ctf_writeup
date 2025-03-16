import os
import signal
from Crypto.Util.number import bytes_to_long

signal.alarm(30)

try:
    p, a, b = map(int, input("Enter p,a,b: ").split(","))
    assert 512 <= p.bit_length() < 1024 and 0 <= a < p and 0 <= b < p
    E = EllipticCurve(GF(p), [a, b])
    P = E.random_point()
    Q = bytes_to_long(os.getenv("FLAG").encode()) * P
    print(f"{P=}, {Q=}")
except Exception as _:
    print(":(")