import struct


def main(data):
    structure = dict()

    structure_a = struct.unpack('=bQIIHHHd', data[4:35])
    structure['A1'] = structure_a[0]
    structure['A2'] = structure_a[1]
    structure['A3'] = dict()
    structure['A4'] = dict()
    structure['A5'] = structure_a[4]
    structure['A6'] = [structure_a[5], structure_a[6]]
    structure['A7'] = structure_a[7]

    address_b = structure_a[2]
    structure_b = struct.unpack('=IIIi', data[address_b:address_b + 16])
    structure['A3']['B1'] = ''
    for i in range(structure_b[0]):
        start = structure_b[1] + i
        symbol = struct.unpack('=c', data[start:start + 1])[0].decode("utf-8")
        structure['A3']['B1'] += symbol
    structure['A3']['B2'] = dict()
    structure['A3']['B3'] = structure_b[3]
    address_c = structure_b[2]
    structure_c = struct.unpack('=fibB', data[address_c:address_c + 10])
    structure['A3']['B2']['C1'] = structure_c[0]
    structure['A3']['B2']['C2'] = structure_c[1]
    structure['A3']['B2']['C3'] = structure_c[2]
    structure['A3']['B2']['C4'] = structure_c[3]
    structure['A4'] = dict()
    address_d = structure_a[3]
    structure_d = struct.unpack('=QHQ', data[address_d:address_d + 18])
    structure['A4']['D1'] = structure_d[0]
    structure['A4']['D2'] = structure_d[1]
    structure['A4']['D3'] = structure_d[2]
    structure['A4']['D4'] = []
    for i in range(5):
        structure['A4']['D4'].append(dict())
        start = address_d + 10 * i
        structure_e = struct.unpack('=IHI', data[start + 18:start + 28])
        structure['A4']['D4'][i]['E1'] = []
        start = structure_e[1]
        finish = structure_e[1] + structure_e[0]
        e_massive_structure = struct.unpack(f'={structure_e[0]}b',
                                            data[start:finish])
        structure['A4']['D4'][i]['E1'] = list(e_massive_structure)
        structure['A4']['D4'][i]['E2'] = structure_e[2]
    return structure


print(main((b'ZLQM\x08I\xb8\x8cv\r\x97\x8d\xf1/\x00\x00\x00K\x00\x00\x00\x9e:\xd7'
            b'\x1eG#\xa8\xb8\x1e\xbc\x8eR\xca?zz\xe6\x1c;\xbe\xfd?\x12\x7f\xbc\xe5\x02'
            b'\x00\x00\x00#\x00\x00\x00%\x00\x00\x00\xd9\n:\x8c0\x14\xbb\x927\x86reI'
            b'T\x14B6\xa8\xd3pT=\n\x1c\xb0I\xa1\x97I1\xedR\xe9\xed\x02\x00\x00'
            b'\x00?\x00\xa2iMX\x02\x00\x00\x00A\x00e\x1f\x81\xe6\x03\x00\x00\x00C\x00\x16'
            b'+\xe0\xdd\x03\x00\x00\x00F\x00\xd9W\x14\x08\x02\x00\x00\x00I\x00\xef'
            b'\xc7m\xcc')))

print(main(b'ZLQMr\xf7\xd5\xb3\xe9\xe4#=\xa10\x00\x00\x00L\x00\x00\x00\xff\tZ9\xb1\xc8<'
           b'J\x11\x9a\xdd\x93\xeb\xbftkiFB\x01=\xf2\xc8\x9d"\xbf{\x03\x00\x00\x00'
           b'#\x00\x00\x00&\x00\x00\x00@N(\x8cD\xe78c\x96\x03\xc4\x9f+*\xb7[W\xaf\xf9\x9d'
           b'\xe2\x0c\x80O\xf9M\xe4\x1e\x9f\xab\xc5\x9e+\xa8\x02\x00\x00\x00@\x00\'b\xa3"'
           b'\x03\x00\x00\x00B\x00\x14\x18\x80\xdb\x02\x00\x00\x00E\x00P\t\xb5\x82'
           b'\x02\x00\x00\x00G\x00Gi\x13=\x03\x00\x00\x00I\x007\x94\x14\x14'))

print(main((b"ZLQM\x94\x80\x0e\xb4\xc6\xc8s\xe9'/\x00\x00\x00L\x00\x00\x00\xdd\x04\t\xa7s*\xc0"
            b"\x96^\x8bS_\x9f\xbfoaNA=?s\xf9\xc3\xeb\xc6\xcc\x02\x00\x00\x00#\x00\x00\x00%\x00"
            b"\x00\x007{s\xdb\xfe\xf6\xffe4\xd0\xe8f\xe9\xd3\x97'\x9c\xf9|\xa1B,\t+\xa1\x0c\x87"
            b"\x8f\xc4\xc1P\xa1\xf0(T\x02\x00\x00\x00?\x00b4\xdf\x9b\x03\x00\x00\x00A\x00!\\\x8d"
            b"\x1f\x03\x00\x00\x00D\x00\x04io\xf0\x02\x00\x00\x00G\x00\x00\xd7\xf4O\x03\x00\x00"
            b"\x00I\x00\xc1t\x1fB")))
