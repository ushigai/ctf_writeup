from Crypto.Util.number import *
from gmpy2 import iroot

n = 24687942429563213485113614973398575979224882414140275678483908060230982339365458771775886355173330426545249659378353471615636913048013698628526849769487397836762704759055715596619041262549929970659958110275314464182704905740984011365177514377251506100833255729778583220109029332089938659816281985642695802990443892006390573088872073364023123814188372748169032649205343879031108339419425151202580942955801610585366884703098020059331742928223147332462659757470742403707485302638724396296944052380813139297737775900497672892426312301200024887514403148226675349979705318695092904092545179891047022476012717633609476912681
e = 3
ct = 26480272848384180570411447917437668635135597564435407928130220812155801611065536704781892656033726277516148813916446180796750368332515779970289682282804676030149428215146347671350240386440440048832713595112882403831539777582778645411270433913301224819057222081543727263602678819745693540865806160910293144052079393615890645460901858988883318691997438568705602949652125

m, _ = iroot(ct, e)
m = int(m)

print(m)
print(long_to_bytes(m))

