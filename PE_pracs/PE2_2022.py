def encode_R(s1,s2,m):
    if len(s1) == 0:
        return ''
    shifter = (int(s2[0]) * m) % 26
    new_ord = ord(s1[0]) + shifter
    if new_ord < ord('a'):
        new_ord += 26
    elif new_ord > ord('z'):
        new_ord -= 26
    return chr(new_ord) + encode_R(s1[1:], s2[1:], m)

def encode_U(s1,s2,m):
    return ''.join([chr(ordi + 26) if ordi < ord('a') else chr(ordi - 26) if ordi > ord('z') else chr(ordi) for ordi in map(lambda i: ord(s1[i]) + (int(s2[i]) * m) % 26, range(len(s1)))])
