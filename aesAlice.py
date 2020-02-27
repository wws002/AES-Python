from base64 import urlsafe_b64encode, urlsafe_b64decode
from Crypto.Cipher import AES
from Crypto import Random

#initialize padding and key
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
base64pad = lambda s: s + '=' * (4 - len(s) % 4)
base64unpad = lambda s: s.rstrip("=")
encrypt_key = 'LKHlhb899Y09olUidsv432de'

#encryption function
def encrypt(key, msg):
    iv = Random.new().read(BS)
    cipher = AES.new(key, AES.MODE_CBC, iv, segment_size=AES.block_size * 8)
    encrypted_msg = cipher.encrypt(pad(str(msg)))
    return base64unpad(urlsafe_b64encode(iv + encrypted_msg))

#get message and encrypt
hidden_msg = raw_input("enter a secret message: ")
cipher_text = encrypt(encrypt_key, hidden_msg)
print "cipher text: " + cipher_text

#write cipherText to file
f = open("cipherText.txt","w+")
f.write(cipher_text)
f.close()
