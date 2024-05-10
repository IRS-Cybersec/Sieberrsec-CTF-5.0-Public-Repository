from Crypto.Util.number import bytes_to_long, getPrime

FLAG = b"3ll1p7ic_curv35_f1nd_5ma11_f4ct0r5_7961bff6dde8b67857cdb"

e = 65537
N = 1

for i in range(20):
    p = getPrime(64)
    N *= p

m = bytes_to_long(FLAG)

c = pow(m, e, N)

print("e:", e)
print("N:", N)
print("c:", c)