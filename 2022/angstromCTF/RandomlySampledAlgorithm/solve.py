from Crypto.Util.number import *

n = 133075794736862400686388110598570266808714052683651232655122797445099216964925703530068957607358890220696254013415564497625510160656547477386290353341301388957868030883484367150794172590602260618953020322190415128204088685449855108061423638905602604314199002557585876080719068735072138975699738144061697925373
e = 65537
c = 42999486939739078417543300759928045769347425010481921402117654240134870338470114310074441997014418414023223148236139895795053257877203574091454937566637813901960299427919263842462481370908334316720948794826158725807235252653149450622143783560995967869958852519888842457531188064386890082072803961804464549309
phi = 133075794736862400686388110598570266808714052683651232655122797445099216964925703530068957607358890220696254013415564497625510160656547477386290353341301365877872031151018140890962539358215097403168452396402116271802269636497626498820406125901329433708704273662567430256232652048920492894069126553095462130720

d = inverse(e, phi)

flag = pow(c, d, n)

print(long_to_bytes(flag))
