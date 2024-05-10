from Crypto.Util.number import bytes_to_long, getPrime

FLAG = b"REDACTED"

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
