from Crypto.Util.number import bytes_to_long

FLAG = b"REDACTED"

assert len(FLAG) == 60

e = 65537
m1 = bytes_to_long(FLAG[:30])
m2 = bytes_to_long(FLAG[30:])

N = int(input("Choose your modulus: "))

if abs(N.bit_length() - 2048) > 10:
    print("Sorry, your modulus isn't the right size!")
else:
    c1 = pow(m1, e, N)
    c2 = pow(m2, e, N+17)

    print("First half:", c1)
    print("Second half:", c2)
