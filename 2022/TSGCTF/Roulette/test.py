import numpy as np

class RNG:
    def __init__(self):
        self.p = np.random.randint(2**32)
        self.q = np.random.randint(2**32)
        self.r = np.random.randint(2**32)
        self.x = np.random.randint(2**32)
    def next(self):
        self.x = (self.p * self.x + self.q) % self.r
        return self.x

money = 5
rng = RNG()

for i in range(10000):
    g = rng.next() % 37
    h = rng.next() % 37
    j = rng.next() % 37
    if g+h+j == 0:
        print(i)


#from numpy import random as R

#for i in range(100000):
    #p = R.randint(2**32)
    #q = R.randint(2**32)
    #r = R.randint(2**32)
    #x = R.randint(2**32)
    
    #if (p * x + q) % r % 37 == 0:
            #if q % r % 37 == 0:
                #print(i)
