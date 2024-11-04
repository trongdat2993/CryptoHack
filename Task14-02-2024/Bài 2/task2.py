from Crypto.Cipher import AES
def padd(pl):
    val = len(pl) % 16
    if val != 0:
        pl += '0'*(16 - val)
    return pl
key1 = b'xxxxxxxxxxxxxxxx' # key là các byte đọc được 
assert len(key1) == 16
key2 = key1[:13] + b'xxx'# key là các byte đọc được
assert len(key2) == 16
cipher1 = AES.new(key=key1, mode=AES.MODE_ECB)
cipher2 = AES.new(key=key2, mode=AES.MODE_ECB)

with open("flag.txt") as f:
    flag = f.read().strip()
ct1 = cipher1.encrypt(padd(flag).encode())
ct2 = cipher2.encrypt(ct1)
print(ct1)
print(ct2)
# b'\xe5\xf2\xa3\xc6\xdes\x9b\x91\xf5;\x0bI\x93\x08\xa1\xc0\x97]\xcc\x1a\x89\xc1\xc0h\xcc\xb0%~t\xf9\x8e\xbd'
# b'\x0bc="\xdc\xec\x90\x94d\xd4qd\xc7\xbd\x99\x0e\x97\xa3\x95\xa77\xdf\xa8"\x84g\xcf\xb3rY\xb3u'