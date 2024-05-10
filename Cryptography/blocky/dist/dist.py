from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

FLAG = "REDACTED"
key = b"REDACTED"

assert len(FLAG) == 16
assert len(key) == 16

def encrypt(key, pt):
    pt = pad(pt, 16)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pt)

print("Welcome to our encryption demo!")
print("We will show you the result of your input in our encryption system, as well as our own (unrecoverable) secret!")
s1 = input("What do you want to encrypt? ")

message = s1 + FLAG
message1 = bytes(message,'utf-8')
cipher = encrypt(key, message1)
cipher = cipher.hex()
print("Here's your result:", cipher)


