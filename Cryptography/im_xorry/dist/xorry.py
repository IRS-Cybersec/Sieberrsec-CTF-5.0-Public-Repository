import os

flag="Redacted"
key=os.urandom(6)

def encrypt(flag,key):
    key_long=(key * (len(flag)//len(key)))[:len(flag)]
    encrypted=result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key_long))

    return encrypted
result="".join(encrypt(flag,key))
print(f'Output: {result}') #Cough cough Output: c917f4ab15f28b15e9a300f6e25fe18d0ff6ce15e3a605ff
    
    
    
