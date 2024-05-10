cipher='2b3b2a38236d693f73366d693f27365e733f2c5928392c696d30653f6d2b21'[::-1]
plain=''.join([cipher[n:n+2][::-1] for n in range(0,len(cipher),2)])
decoded=bytearray.fromhex(plain).decode()
flag=''.join([chr((126-ord(x)+32)) for x in decoded][::-1])
print(flag)
