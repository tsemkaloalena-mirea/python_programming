def main(x):
    mask_a = 0x00000003
    mask_b = 0x0000003c
    mask_c = 0x00001fc0
    mask_d = 0x000fe000
    mask_e = 0x00300000
    mask_f = 0x7fc00000
    mask_g = 0x80000000

    a = x & mask_a
    b = x & mask_b
    c = x & mask_c
    d = x & mask_d
    e = x & mask_e
    f = x & mask_f
    g = x & mask_g

    a = a << 16
    b = b << 17
    c = c << 3
    d = d >> 13
    e = e >> 13
    f = f << 1
    g = g >> 13

    return a | b | c | d | e | f | g
