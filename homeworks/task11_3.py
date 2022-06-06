from struct import *

FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d'
)


def parse(buf, offs, ty):
    return unpack_from(FMT[ty], buf, offs)[0], offs + calcsize(FMT[ty])


def parse_a(buf, offs):
    a1, offs = parse(buf, offs, "int8")
    a2 = []
    for _ in range(5):
        val, offs = parse(buf, offs, 'char')
        a2.append(val.decode())
    a2 = "".join(a2)
    a3_size, offs = parse(buf, offs, "uint32")
    a3_offs_for_offs, offs = parse(buf, offs, "uint32")
    a3 = []
    for _ in range(a3_size):
        a3_offs, a3_offs_for_offs = parse(buf, a3_offs_for_offs, "uint32")
        val, a3_offs = parse_b(buf, a3_offs)
        a3.append(val)
    a4, offs = parse(buf, offs, "uint64")
    a5, offs = parse(buf, offs, "int16")
    a6_offs, offs = parse(buf, offs, "uint32")
    a6, offs = parse_c(buf, a6_offs)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, "float")
    b2, offs = parse(buf, offs, "uint64")
    return dict(B1=b1, B2=b2), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, "uint8")
    c2 = []
    for _ in range(8):
        val, offs = parse(buf, offs, 'float')
        c2.append(val)
    c3 = []
    for _ in range(3):
        val, offs = parse(buf, offs, 'uint32')
        c3.append(val)
    c4, offs = parse_d(buf, offs)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4), offs


def parse_d(buf, offs):
    d1 = []
    for _ in range(3):
        val, offs = parse(buf, offs, 'double')
        d1.append(val)
    d2, offs = parse(buf, offs, "int16")
    return dict(D1=d1, D2=d2), offs


def main(buf):
    return parse_a(buf, 4)[0]


print(main(
    b'MWD\xfe\xc4wvxon\x05\x00\x00\x00\\\x00\x00\x00\xa9\xb8a\xcfM+\xfa\x7fj"p\x00\x00\x00\xd3\xbb#?\x8b?\x9fM\x9c\x83;&%\xd7%?\xbeA\xbbi]-\x08-U=g\xbf0\x96=\t\x9b\x9a\xa3\xd4\xe9K\xad>\xf4\x08\xb8\xcaP\xae7S\xea52\xbf\xdf>\xea\x03\xf5$\xb0< \x00\x00\x00,\x00\x00\x008\x00\x00\x00D\x00\x00\x00P\x00\x00\x00b9\xaa\x08?S\xf3\x04?\xe7\xda\x16>b\xb9\xdd>\xec\x88-\xbd\xc4\x88\x11?\xe3\xd1\xf6\xbdT]n\xbf\xa4N\xbc\x14"\xef\xe7#\xa4\\\xe7K\x8a\xae:\xe1\x86\x80\xe5?`|\xc9\xaeF=\xab\xbf\xe0\x00\xc3\x87x\x98\xca\xbf\xcah'))
