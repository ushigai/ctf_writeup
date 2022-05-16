from Crypto.Util.number import *


e = 65537
N = 90155872626109118751539082340637664291284739918666752584753399796834394108934269799361082409068780300733478243187803947914852201275756546305701601038245062017076328987708208192044674964106835923338854908195583033310310682803512196201848036103484667516142174036453910627093541752413321035733931243762833992113
r = 9322793222533738919136767770062343847990445869750540466031127454552421896606703877767352447027469817530156341564290950012563071681611937229761941420331277
c = 6146682863326523930660780475800345684609346868118904988599020801137516078990162263453764612248242206809400248946028976662634601168167123937919798903932765746347318386910880849642655181553179504240263695508893635468417428856823495012423849224891599994895553098814398443037416874773801965115317240666818199846

p = GCD(N, r)
q = N // p

assert p * q == N

phi = (p - 1)*(q - 1)
d = inverse(e, phi)

flag = pow(c, d, N)
print(long_to_bytes(flag))