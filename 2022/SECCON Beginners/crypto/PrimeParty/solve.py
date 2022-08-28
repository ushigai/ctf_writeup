from Crypto.Util.number import *

n = 178846388997216303715324153141838504003016418851292634742753578454485646720639916499779812225291101109653406078996218604427343541609942612772911790627024410990857513342854440983604186542335668029589847253852978692348236477713723237771432908829786352167840948665719726850714699820681384415188349276825761601946764237397853702940931185202203811617595950497923622020665965918938218841058740480054638732025184164831356747218114628857562050624283343956599233295481517
e = 65537
cipher = 122335582115854131041204881945410154379105215140510832597034121195514778324761929803452646784073884484726324022016133776522171011038025147692827538027909300105961756614227254932737776675941866945229307131604285421777412599987923549611084220901143256189238791328117065281855896949367780873366170826522857346463675049589707840426897571976323627611915708906039539647722427200922762856864063827946491173886190995810459498587855347282835963487238970889982282489313411
p = 7125542541015089382665540838109147669178367364945725639475647981053827179059524720886882567884452880517281519977560328608747082652488826892110086607334999

phi = p - 1
d = inverse(e, phi)
m = pow(cipher, d, p)

print(long_to_bytes(m))
