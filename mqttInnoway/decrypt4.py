from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

# Provided data
hex_string = "E8444DED87CBB93807D73C874C5D33374F2A0FDA49135BFCEFE5DB5449691006"
key = b'affzMYRLdEY97are'

# Convert the hex string to bytes
encrypted_data = binascii.unhexlify(hex_string)

# Create an AES cipher object with the given key and ECB mode
cipher = AES.new(key, AES.MODE_ECB)

# Decrypt the data
decrypted_data = cipher.decrypt(encrypted_data)

# Unpad the decrypted data
unpadded_data = unpad(decrypted_data, AES.block_size)

# Output the unpadded decrypted data
print(unpadded_data.decode('utf-8'))
