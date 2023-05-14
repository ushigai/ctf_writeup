from Crypto.Util.number import *
from random import getrandbits


class RSA:
    def __init__(self, bits):
        assert bits % 2 == 0
        self.gen_new_key(bits)

    def gen_new_key(self, bits):
        self.p = getPrime(bits // 2)
        self.q = getPrime(bits // 2)
        self.N = self.p * self.q
        self.N = 88514316563512879494623038195836664351937567894693534710038379189014201738600441320930701787465333959723689879136504359256101701497215740395585980297980037308246431410913892443941861931264280677081787414747628772470500268453262104902273750184435639148584505036960489689277592575246284187355445145185298950547
        self.N = 131524088884825815804488932464729357040334400654894482058463384631465646564218562087397372641691153724192714309237816737178676891008253858742684770007206270690351261617425456727727358875299906146914830254560972052930255319744195538734348410986466067329708785605858045414804679488686183262367088579297015291141
        self.e = 3
        phi = (self.p - 1) * (self.q - 1)
        self.d = inverse(self.e, phi)

    def encryption(self, m):
        c = pow(m, self.e, self.N)
        return c

    def pgcd(self, f, g):
        while g:
            f, g = g, f % g
        return f

    def shortpadAttack(self, c1, c2):
        PR.<x, y> = PolynomialRing(Zmod(self.N))
        PRS.<xs> = PolynomialRing(Zmod(self.N))
        
        g1 = x^self.e - c1
        g2 = (x + y)^self.e - c2

        gg1 = g1.change_ring(PRS)
        gg2 = g2.change_ring(PRS)
        h = gg2.resultant(gg1) # 終結式の計算
        h = h.univariate_polynomial().subs(y=xs).monic()

        delta_ans = h.small_roots(epsilon=1/60) # なんとなく1/60
        if len(delta_ans):
            if 2**delta_bits + 1 < delta_ans[0]: # 負の値の場合それを環から戻す
                print("Diff :", int(delta_ans[0]) - self.N)
            else:
                print("Diff :", delta_ans[0])
        else:
            return "Diff not found..."

        # Franklin-Reiter Related Message Attack
        PR.<x> = PolynomialRing(Zmod(self.N)) # yを消したので多項式環をまた用意
        g1 = x^self.e - int(c1)
        g2 = (x + int(delta_ans[0]))^self.e - int(c2)

        ph = self.pgcd(g1, g2)
        ph = ph.monic()
        return int(-ph[0])


bits = 1024
e = 3
r = RSA(bits)
delta_bits = floor(bits / (e^2) / 2)
r1 = ZZ.random_element(2^delta_bits)
r2 = ZZ.random_element(2^delta_bits)
delta = r2 - r1
print("Diff 1 :", delta)

M = bytes_to_long(b"Coppersmiths_shortpad_attack!!!!!!!!!!!!!!!!!!!")
m1 = 2**delta_bits*M + r1
m2 = 2**delta_bits*M + r2

c1 = r.encryption(m1)
c2 = r.encryption(m2)

N = 88514316563512879494623038195836664351937567894693534710038379189014201738600441320930701787465333959723689879136504359256101701497215740395585980297980037308246431410913892443941861931264280677081787414747628772470500268453262104902273750184435639148584505036960489689277592575246284187355445145185298950547
e = 3
c1 = 27962784309136702827078425255662563529771454120801846586316474175920891882897399697532160136134305562402000873419407805988912396878983267355448671983874127533624353009062811512922588478877693162951414889231084998608048780806278652796744546133371271501977858188616434486932456489240359031033397239428954927263
c2 = 71134590510821103274291289760747463716022331508477046378755631215525590015440656167203580720397866851660348920265543172428820230666288397747757378382183302803514748428047655413523613772375373880953912213943275224259975495443032538947913983560135891639017264504473841493065901709877437510532248929962088576516

N = 131524088884825815804488932464729357040334400654894482058463384631465646564218562087397372641691153724192714309237816737178676891008253858742684770007206270690351261617425456727727358875299906146914830254560972052930255319744195538734348410986466067329708785605858045414804679488686183262367088579297015291141
e = 3
c1 = 53446890814226238195814900775610146361354688642953984822875182297861976571235892581728318314459205473773163777796449566433544434134073179844466939691972553393776130664306258111549148944010961079361802647342130537687069419065674984241592765378827102906801889899262139334877519178755098426417577535191788787887
c2 = 53446890814226238195814900775610146361354688642953984822875182321385725425008957482596867857544541131433772697093663878596038952458110930478268276653144018403231153004739183129121025413011758697599979926904528387653993851636222310955660828650069081991070148602980332627389671548440711748081532341124803683994


delta_bits = 96

print("-*-*-*-*-*-*-*-*-*-*-*-")

print(long_to_bytes(r.shortpadAttack(c1, c2) >> delta_bits))

