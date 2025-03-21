from output import hint, cipher
from binascii import hexlify, unhexlify
from Crypto.Cipher import AES
from hashlib import sha256

for h in hint:
    for iv, cipher in h:
        iv, cipher = unhexlify(iv), unhexlify(cipher)
        out = b"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
        out = b"0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        key = sha256(out).digest()
        aes = AES.new(key, AES.MODE_CBC, iv)
        message = aes.decrypt(cipher)
        print(message)

m1 = b'Welcome! If you see this you have successfully decrypted the first message. To get the symmetric key that decrypts the flag you need to do the following:\n\n1. Collect all 5 shares from these messages\n2. Use them to interpolate the polynomial in a finite field that will be revealed in another message\n3. Convert the constant term of the polynomial to bytes and use it to decrypt the flag. Here is your first share!\n\nShare#1#: (1, 27006418753792019267647881709336369603809025474153761185424552629526746515909)'
m2 = b'Keep up the good work! Offered say visited elderly and. Waited period are played family man formed. He ye body or made on pain part meet. You one delay nor begin our folly abode. By disposed replying mr me unpacked no. As moonlight of my resolving unwilling. Turned it up should no valley cousin he. Speaking numerous ask did horrible packages set. Ashamed herself has distant can studied mrs.\n\nShare#2#: (2, 76590454267924193303526931251420387908730989759486987968207839464816350274449)'
m3 = b'Only a few more are left! Of be talent me answer do relied. Mistress in on so laughing throwing endeavor occasion welcomed. Gravity sir brandon calling can. No years do widow house delay stand. Prospect six kindness use steepest new ask. High gone kind calm call as ever is. Introduced melancholy estimating motionless on up as do. Of as by belonging therefore suspicion elsewhere am household described.\n\nShare#3#: (3, 67564500698667187837224046797217120599664632018519685208508601443605280795068)'
m4 = b'You are almost there! Not him old music think his found enjoy merry. Listening acuteness dependent at or an. Apartments thoroughly unsatiable terminated sex how themselves. She are ten hours wrong walls stand early. Domestic perceive on an ladyship extended received do. Why jennings our whatever his learning gay perceive. Is against no he without subject. Bed connection unreserved preference partiality not unaffected.\n\nShare#4#: (4, 57120102994643471094254225269948720992016639286627873340589938545214763610538)'
m5 = b'Congratulations!!! Not him old music think his found enjoy merry. Listening acuteness dependent at or an. Apartments thoroughly unsatiable terminated how themselves. She are ten hours wrong walls stand early. Domestic perceive on an ladyship extended received do. You need to interpolate the polynomial in the finite field GF(88061271168532822384517279587784001104302157326759940683992330399098283633319).\n\nShare#5#: (5, 87036956450994410488989322365773556006053008613964544744444104769020810012336)'


m = m1 + m2 + m3 + m4 + m5
m = m.decode()
print(m)

"""
$ python3 solve.py
Welcome! If you see this you have successfully decrypted the first message. To get the symmetric key that decrypts the flag you need to do the following:

1. Collect all 5 shares from these messages
2. Use them to interpolate the polynomial in a finite field that will be revealed in another message
3. Convert the constant term of the polynomial to bytes and use it to decrypt the flag. Here is your first share!

Share#1#: (1, 27006418753792019267647881709336369603809025474153761185424552629526746515909)Keep up the good work! Offered say visited elderly and. Waited period are played family man formed. He ye body or made on pain part meet. You one delay nor begin our folly abode. By disposed replying mr me unpacked no. As moonlight of my resolving unwilling. Turned it up should no valley cousin he. Speaking numerous ask did horrible packages set. Ashamed herself has distant can studied mrs.

Share#2#: (2, 76590454267924193303526931251420387908730989759486987968207839464816350274449)Only a few more are left! Of be talent me answer do relied. Mistress in on so laughing throwing endeavor occasion welcomed. Gravity sir brandon calling can. No years do widow house delay stand. Prospect six kindness use steepest new ask. High gone kind calm call as ever is. Introduced melancholy estimating motionless on up as do. Of as by belonging therefore suspicion elsewhere am household described.

Share#3#: (3, 67564500698667187837224046797217120599664632018519685208508601443605280795068)You are almost there! Not him old music think his found enjoy merry. Listening acuteness dependent at or an. Apartments thoroughly unsatiable terminated sex how themselves. She are ten hours wrong walls stand early. Domestic perceive on an ladyship extended received do. Why jennings our whatever his learning gay perceive. Is against no he without subject. Bed connection unreserved preference partiality not unaffected.

Share#4#: (4, 57120102994643471094254225269948720992016639286627873340589938545214763610538)Congratulations!!! Not him old music think his found enjoy merry. Listening acuteness dependent at or an. Apartments thoroughly unsatiable terminated how themselves. She are ten hours wrong walls stand early. Domestic perceive on an ladyship extended received do. You need to interpolate the polynomial in the finite field GF(88061271168532822384517279587784001104302157326759940683992330399098283633319).

Share#5#: (5, 87036956450994410488989322365773556006053008613964544744444104769020810012336)
"""
