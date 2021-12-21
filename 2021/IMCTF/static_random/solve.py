import random

cipher = "ilYqdtO1m&k6C,(]3_*h.V=-VA\\nf\\f*w"

def decoder(inputtext: str):
    random.seed("we wish a merry xmas")
    encoded: str = ""
    for item in inputtext:
        encoded += chr(ord(item) + random.randint(0, 10))
    return encoded

print(decoder(cipher))
# imctf{V3n0m:L3+_7h3r3_B3_Carnag3}
