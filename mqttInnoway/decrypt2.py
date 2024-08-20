## Cắt chuỗi hex làm 2
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from binascii import unhexlify

#packed to def
def decryptSV2UE(keyString, hexString):
    key = keyString.encode('utf-8')
    cptext_hex = unhexlify(hexString)
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = unpad(cipher.decrypt(ciphertext_hex),16)
    print("Chuỗi sau khi giải mã:", padded_plaintext)

# Ciphertext đã mã hóa (ở dạng hex string)
decrypted = ['6C489B01F6AE89EABA0D044A10FDD414',
             'FED9ED17C388160855AA4ABD0883B07353BAFC95CC18D1B12931441F303C4CDD7523BED8EAAEAF0DD260D5DA37E79563',
             'A1639DC90242ADDA5322AB44CD981BF510FA5BC507822ADE9F9A8AE7C5FB3051']  #lenHex = 64, str ban đầu 30 kí tự
ciphertext_hex = unhexlify(decrypted[0])
# print (len(ciphertext_hex))
_key = ['sl0NFX332bJd84NJ','pA2WG0J4g8XYR71z']
key = _key[1].encode('utf-8')

##______________________________________
## Cách 2
cipher = AES.new(key, AES.MODE_ECB)
padded_plaintext = unpad(cipher.decrypt(ciphertext_hex),16)
print("Chuỗi sau khi giải mã:", padded_plaintext)
print("Chuỗi sau khi giải mã + decode:", padded_plaintext.decode())

##______________________________________
# #Cach 1: ngu vcl
# #cắt đôi chuỗi hex
# mid_index = len(ciphertext_hex)//2
# end_index = len(ciphertext_hex)
# c_hex=[]
# c_hex.append(ciphertext_hex[0:(mid_index)])
# c_hex.append(ciphertext_hex[(mid_index):(end_index + 1)])
# # print(unhexlify('19A2B860AB0E1632D4651F1BA64A0EF66').decode('utf-8'))
# print(ciphertext_hex)
# for i, value in enumerate(c_hex):

#     # Khởi tạo AES cipher ở chế độ ECB
#     cipher = AES.new(key, AES.MODE_ECB)

#     # Giải mã ciphertext
#     padded_plaintext = cipher.decrypt(value)

#     # Loại bỏ padding để khôi phục chuỗi ban đầu
#     plaintext = padded_plaintext
#     print("Chuỗi",i,"sau khi giải mã:", plaintext)



