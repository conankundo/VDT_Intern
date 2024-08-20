# form decrypt2.py
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from binascii import unhexlify


def decryptSV2UE(keyString, hexString):
    key = keyString.encode('utf-8')
    cptext_hex = unhexlify(hexString)
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = unpad(cipher.decrypt(cptext_hex),16)
    # print("Chuỗi sau khi giải mã:", padded_plaintext)
    return padded_plaintext.decode()
def check(str):
    if str[0:4] == 'step':
        # print("step:", int(str[4:]))
        return int(str[4:])
    else:
        return 0