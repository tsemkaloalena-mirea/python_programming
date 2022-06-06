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
    a1 = []
    for _ in range(5):
        val, offs = parse(buf, offs, 'char')
        a1.append(val.decode())
    a1 = "".join(a1)
    a2, offs = parse_b(buf, offs)
    a3_offs, offs = parse(buf, offs, "uint32")
    a3, offs = parse_d(buf, a3_offs)
    return dict(A1=a1, A2=a2, A3=a3), offs


def parse_b(buf, offs):
    b1_size, offs = parse(buf, offs, "uint16")
    b1_offs, offs = parse(buf, offs, "uint16")
    b1 = []
    for _ in range(b1_size):
        val, b1_offs = parse_c(buf, b1_offs)
        b1.append(val)
    b2_size, offs = parse(buf, offs, "uint32")
    b2_offs, offs = parse(buf, offs, "uint16")
    b2 = []
    for _ in range(b2_size):
        val, b2_offs = parse(buf, b2_offs, "int8")
        b2.append(val)
    return dict(B1=b1, B2=b2), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, "float")
    c2, offs = parse(buf, offs, "uint8")
    return dict(C1=c1, C2=c2), offs


def parse_d(buf, offs):
    d1_size, offs = parse(buf, offs, "uint32")
    d1_offs, offs = parse(buf, offs, "uint16")
    d1 = []
    for _ in range(d1_size):
        val, d1_offs = parse(buf, d1_offs, "uint8")
        d1.append(val)
    d2_size, offs = parse(buf, offs, "uint32")
    d2_offs, offs = parse(buf, offs, "uint32")
    d2 = []
    for _ in range(d2_size):
        val, d2_offs = parse(buf, d2_offs, "int64")
        d2.append(val)
    return dict(D1=d1, D2=d2), offs


def main(buf):
    return parse_a(buf, 4)[0]


print(main(
    b'\xcaYSWkpqvi\x02\x00\x17\x00\x02\x00\x00\x00!\x00X\x00\x00\x00&\x0e\x0e\xbf9]Pi?\xdd4\xafD\x8d\x9b\x84\xa9\x84\x0b\x15\xfeT\x8a\xd1a\xf2\x8e\x99\xf7\x9b\xfdP\xa1\xd7\xa6,\xfa\x92\xe2\x0fy\xd6\xdd_\xec\xc1\xf8\x92\xcf\xb8\xe8\xb7\xd7\xfa\x16\x11A\xf3\xf7\x883\xf9\xb7n&\x05\x00\x00\x00#\x00\x06\x00\x00\x00(\x00\x00\x00'))
