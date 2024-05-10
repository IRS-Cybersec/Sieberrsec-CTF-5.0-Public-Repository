from Crypto.Util.number import getPrime, bytes_to_long

FLAG = b"REDACTED"

assert(len(FLAG) == 48)
def convert(msg):
    return 2**N.bit_length()-2**(len(msg)*8) + bytes_to_long(msg)

p = getPrime(1024)
q = getPrime(1024)
N = p*q
e = 3
c = pow(convert(FLAG), e, N)

print(f"N: {N}")
print(f"e: {e}")
print(f"c: {c}")
