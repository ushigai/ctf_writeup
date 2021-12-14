# 6096359484*x^3 + 6606845234*x^2 + 1736000027*x + 5669601428

def f(x):
    a = 6096359484 
    b = 6606845234
    c = 1736000027
    d = 5669601428
    x = a*x**3 + b*x**2 + c*x**1 + d
    return x


cipher = [8194393930139798, 7130326565974613, 9604891888210928, 6348662706560873, 11444688343062563, 7335285885849258, 3791814454530873, 926264016764633, 9604891888210928, 5286663580435343, 5801472714696338, 875157765441840, 926264016764633, 2406927753242613, 5980222734708251, 5286663580435343, 2822500611304865, 5626320567751485, 3660106045179536, 2309834531980460, 12010406743573553]
table = dict()
for i in range(200):
    table[f(i)] = chr(i)

for c in cipher:
    print(table[c], end="")
print("")
