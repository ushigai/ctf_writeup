from Crypto.Util.number import *
import gmpy2

n = 21141157755370440356159016558867591002795131037765353220781763950242197787546988623583333748613811615876039600044067795582387314625044873018261912055648316947575307397145571269092683237196318163742534102252564452361648000741215145961263035358948910750394941304616916013217678630294578579032413375393774307079767343057241805957456859330160131811246961956716626217712879502367810458962663138839207104998925545962808329297100387478763021607429645752111666523372296094568288414788741918520918522347389517685977356020153749161423831061236785869435119648010372663034476232600939002450611487244980761240697255092515294619063
e1 = 65536
c1 = 3791139181938569737398685036032381737646987513051659017777895787043616313081106838760662536132081707503545049439606032069727376790572333643094529595081085118571506461893089039469054703087386815141490544138726142314337827447061522144729907408053083672097701520947030283539764963562701091579919487153984526052282424975277999492006498441654336183574233720547915500793830555227254993335348447191157770264921144000194606354966874727918714437428556969904356868934618577114911104025392029907939301331113924863412657322707967483351467004854177190395076310650546542866389721479249039989850401261446124771193559166329619972412
e2 = 65538
c2 = 9479987054301003593696498729807102589604512322454236806662495038269939932383233766107579478386705533651017857595249113906203900757985576318399557582785561924440535008414598465159052407108648112038858687677552218404377633749009339690058222162908839308847763582094729669124528370642665466262258176588951705959922822288462616323273663488143476234490690202535922260303842658128571121608034815328952318543895796544411651444423903851422043107669054499710424643274879906277104856140792871842468587164924689276336292808339852752054246714774764674969279059667783378523996744567909634744703888058392004064096159069736198607229

def attack(c1, c2, e1, e2, n): # ref : https://inaz2.hatenablog.com/entry/2016/01/15/011138
    gcd, s1, s2 = gmpy2.gcdext(e1, e2)
    if s1 < 0:
        s1 = -s1
        c1 = gmpy2.invert(c1, n)
    elif s2 < 0:
        s2 = -s2
        c2 = gmpy2.invert(c2, n)
    v = pow(c1, s1, n)
    w = pow(c2, s2, n)
    m = (v * w) % n
    return m


m = attack(c1, c2, e1, e2, n)
m, _ = gmpy2.iroot(m, 2)
print(long_to_bytes(int(m)))
