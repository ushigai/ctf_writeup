import dis
import marshal
import struct

with open('run.pyc', 'rb') as f:
    f.seek(16)
    print(dis.dis(marshal.load(f)))

#f = open('solve.pyc', 'rb')
#magic,tstamp = struct.unpack('<ll', f.read(8))
#print(magic & 0xFFFF, tstamp)

#f = open('run.pyc', 'rb')
#magic,tstamp = struct.unpack('<ll', f.read(8))
#print(magic & 0xFFFF, tstamp)
