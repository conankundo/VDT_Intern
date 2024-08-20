from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode,b64decode

_key = "sl0NFX332bJd84NJ"
_ciphertext = "2D2A33D0C73D3A30C87FFE0BA99FD3A49547CBA05B5691E8B5CE23E36FB4BAF3"
key0= bytes(_key, 'utf-8')
key1 = get_random_bytes(32)
print("key1: ",key1)
print("key0: ",key0)
def encrypt(plaintext,key):
    cipher = AES.new(key,AES.MODE_ECB)
    return b64encode(cipher.encrypt(pad(plaintext.encode(),16))).decode()
def decrypt(ciphertext,key):
    cipher = AES.new(key,AES.MODE_ECB)
    return unpad(cipher.decrypt(b64decode(ciphertext.encode())),16).decode()