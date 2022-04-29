import struct


def main(data):
    structure = dict()
    structure_a = struct.unpack('=bdH', data[3:14])
    structure['A1'] = structure_a[0]
    structure['A2'] = structure_a[1]
    structure['A3'] = structure_a[2]
    structure['A4'] = []
    start = 14
    for i in range(3):
        structure['A4'].append(dict())
        structure_b = struct.unpack('=ddb', data[start:start + 17])
        start += 17
        structure['A4'][i]['B1'] = structure_b[0]
        structure['A4'][i]['B2'] = structure_b[1]
        structure['A4'][i]['B3'] = structure_b[2]
    structure['A5'] = struct.unpack(
        '=5s', data[start:start + 5])[0].decode("utf-8")
    structure_a = struct.unpack('=II', data[start + 5:start + 13])
    structure['A6'] = dict()
    structure['A7'] = structure_a[1]
    address_c = structure_a[0]
    structure_c = struct.unpack('=BHIH', data[address_c:address_c + 9])
    structure['A6']['C1'] = structure_c[0]
    start = structure_c[2]
    finish = structure_c[2] + 2 * structure_c[1]
    structure['A6']['C2'] = list(struct.unpack
                                 (f'={structure_c[1]}H', data[start:finish]))
    address_d = structure_c[3]
    structure_d = struct.unpack('=B4HIIbqdHQ', data[address_d:address_d + 44])
    structure['A6']['C3'] = dict()
    structure['A6']['C3']['D1'] = structure_d[0]
    structure['A6']['C3']['D2'] = list(structure_d[1:5])
    start = structure_d[6]
    finish = structure_d[6] + 2 * structure_d[5]
    structure['A6']['C3']['D3'] = list(struct.unpack(
        f'={structure_d[5]}H', data[start:finish]))
    structure['A6']['C3']['D4'] = structure_d[7]
    structure['A6']['C3']['D5'] = structure_d[8]
    structure['A6']['C3']['D6'] = structure_d[9]
    structure['A6']['C3']['D7'] = structure_d[10]
    structure['A6']['C3']['D8'] = structure_d[11]
    return structure


print(main(b'PDP\x02\\\xb34\xf4\xc6\xc6\xea?\xd7\xe7\xa4\xa1u\xb8\xe4x\xed\xbf\x04\x19'
           b'RN\xa1\xb0\xd8\xbf\xbd\xb62\xd8|\xb0\x80\xea?\x90`S\xea\xae\xef\xbe?*'
           b'\x80\xdc\x1a\xf6\xa33\xaf\xbft\x86\xfePll\xe9\xbf mvwds\x8a\x00'
           b'\x00\x00\xb8\x92\xc0\xd0\xf5\xfd\x9f \xd3\xfc\xd2\ru\xee\x9cc\xa5G'
           b'\xb6\x1d\xf0\x84\x9a)\xd8\x8a\xdc\xc8\x98\x06\x00\x00\x00R\x00\x00\x00A'
           b'dV\xfc\x88\x95\xfd\xe8\xef\xe0\xc31\xcb\x9b\x16\xeb\xbf\xdeC\xebe'
           b'e\xee\x80\x1e\x03a\xa8\x02\x00N\x00\x00\x00^\x00'))
