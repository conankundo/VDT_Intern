from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from binascii import unhexlify
from base64 import b64encode,b64decode


# Khóa mã hóa và ciphertext
def hex2byte(hex_string):
    byte_string = unhexlify(hex_string)
    return byte_string
_key = 'sl0NFX332bJd84NJ'
key =_key.encode('utf-8')

ciphertext_hex = '3A5F793D9FD9935E9E5732CE4EF75D8CE9D20A49D5141EE9A68881870EBC6B86'

ciphertext_byte = hex2byte(ciphertext_hex)

# Khởi tạo AES cipher ở chế độ ECB (hoặc chế độ bạn đã sử dụng)
cipher = AES.new(key, AES.MODE_ECB)

# Giải mã
plaintext_unpad = cipher.decrypt(ciphertext_byte)

# plaintext = unpad(cipher.decrypt(ciphertext_byte), 8, style="pkcs7")
plaintext = cipher.decrypt(ciphertext_byte)

print("plaintext2: ", plaintext)
# Loại bỏ padding nếu có và chuyển thành chuỗi
plaintext = plaintext.strip()

print("Chuỗi ban đầu có pad:", plaintext)
print("Chuỗi ban đầu unpad: ", plaintext_unpad)
