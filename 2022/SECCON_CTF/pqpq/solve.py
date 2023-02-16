from Crypto.Util.number import *

e = 131074
n = 587926815910957928506680558951380405698765957736660571041732511939308424899531125274073420353104933723578377320050609109973567093301465914201779673281463229043539776071848986139657349676692718889679333084650490543298408820393827884588301690661795023628407437321580294262453190086595632660415087049509707898690300735866307908684649384093580089579066927072306239235691848372795522705863097316041992762430583002647242874432616919707048872023450089003861892443175057
c1 = 92883677608593259107779614675340187389627152895287502713709168556367680044547229499881430201334665342299031232736527233576918819872441595012586353493994687554993850861284698771856524058389658082754805340430113793873484033099148690745409478343585721548477862484321261504696340989152768048722100452380071775092776100545951118812510485258151625980480449364841902275382168289834835592610827304151460005023283820809211181376463308232832041617730995269229706500778999
c2 = 46236476834113109832988500718245623668321130659753618396968458085371710919173095425312826538494027621684566936459628333712619089451210986870323342712049966508077935506288610960911880157875515961210931283604254773154117519276154872411593688579702575956948337592659599321668773003355325067112181265438366718228446448254354388848428310614023369655106639341893255469632846938342940907002778575355566044700049191772800859575284398246115317686284789740336401764665472
cm = 357982930129036534232652210898740711702843117900101310390536835935714799577440705618646343456679847613022604725158389766496649223820165598357113877892553200702943562674928769780834623569501835458020870291541041964954580145140283927441757571859062193670500697241155641475887438532923910772758985332976303801843564388289302751743334888885607686066607804176327367188812325636165858751339661015759861175537925741744142766298156196248822715533235458083173713289585866

p = GCD(n, c1+c2)
q = GCD(n, c1-c2)
r = n // p // q

assert n == p*q*r

phi = (p - 1)*(q - 1)*(r - 1)
phi2 = phi
while phi2 % 2 == 0:
    phi2 //= 2

d = pow(e, -1, phi2)
X = pow(cm, d, n)

for i in range(2, e):
    x = X * pow(i, int(phi2), n) % n
    s = long_to_bytes(x)
    if b"SECCON" in s:
        print(s)
        break

