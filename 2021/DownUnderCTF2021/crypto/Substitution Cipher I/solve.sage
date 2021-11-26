
var("x")
f = 13*x^2 + 3*x + 7
cipher = open("output.txt", "r").read().strip()
for c in cipher:
    c = ord(c)
    a, b = solve(f(x)==c, x)
    a = str(a).split()[-1]
    b = str(b).split()[-1]
    if "-" in  a:
        print(chr(int(b)), end="")
    else:
        print(chr(int(a)), end="")
    
    
