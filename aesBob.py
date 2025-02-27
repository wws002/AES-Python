from base64 import urlsafe_b64encode, urlsafe_b64decode
from Crypto.Cipher import AES
from Crypto import Random

#set up padding and key
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
base64pad = lambda s: s + '=' * (4 - len(s) % 4)
base64unpad = lambda s: s.rstrip("=")
encrypt_key = 'LKHlhb899Y09olUidsv432de'

#read cipherText
f = open("cipherText.txt", "r")
cipherText = f.read()
f.close()

# when incorrect encryption key is used, `decrypt` will return empty string
def decrypt(key, msg):
    decoded_msg = urlsafe_b64decode(base64pad(msg))
    iv = decoded_msg[:BS]
    encrypted_msg = decoded_msg[BS:]
    cipher = AES.new(key, AES.MODE_CBC, iv, segment_size=AES.block_size * 8)
    return unpad(cipher.decrypt(encrypted_msg))

#print cipherText and decrypt
print cipherText
print decrypt(encrypt_key, cipherText)
