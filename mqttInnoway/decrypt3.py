# encrypt and decrypt
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from binascii import unhexlify
#--------------------------------
def hex2bin(hex):
    decimal_value = int(hex, 16)
    binary_string = bin(decimal_value)[2:]
    return binary_string
def hex2byte(hex_string):
    byte_string = unhexlify(hex_string)
    return byte_string
def hex2hexdecimal(hex_string):
    # Chuyển chuỗi hex thành danh sách các giá trị hex với định dạng \0x..
    formatted_hex = ["\\0x" + hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
    # Ghép các phần tử thành một chuỗi
    formatted_string = " ".join(formatted_hex)
    return formatted_string

#thông tin ban đầu
plaintext ="helloundefined"
key = b'sl0NFX332bJd84NJ'
print("plaintext1: ", plaintext)

#setup theo mode ECB
cipher1 =AES.new(key, AES.MODE_ECB)
cipher2 = AES.new(key, AES.MODE_ECB)

# mã hóa
ciphertext_byte = cipher1.encrypt(pad(plaintext.encode(), 16))

#print để so sánh
print("ciphertext_hex: ", ciphertext_byte.hex())
print("ciphertext_byte: ", ciphertext_byte)
print("hex2byte  : ", hex2byte(ciphertext_byte.hex()))
print("hex2hexdecimal: ", hex2hexdecimal(ciphertext_byte.hex()))

# giải mã
plaintext2 = unpad(cipher2.decrypt(ciphertext_byte), 16)
print("plaintext2: ", plaintext2.decode())
# plaintext3 = unpad(ciphertext_byte, 16)
# print("plaintext3: ", plaintext3.decode())
#________________________________


