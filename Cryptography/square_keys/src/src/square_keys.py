from Crypto.Util.number import getRandomNBitInteger

FLAG = "sctf{v13ta_jump1ng_15_h4rd_274537f626465081709}"

def is_perfect_square(n):
    lo = 1
    hi = n//2
    while lo < hi:
        mid = (lo+hi)//2
        if mid**2 == n:
            return True
        elif mid**2 < n:
            lo = mid+1
        else:
            hi = mid-1
    if lo**2 == n:
        return True
    else:
        return False

a = 0
while (a.bit_length() < 2048 or a < 0):
    k = getRandomNBitInteger(1024)
    my_y = getRandomNBitInteger(512)
    my_x = getRandomNBitInteger(512)
    a = k*(my_y**2) - (k-1)*(my_x**2)
    
    
print("Let's collaborate on a key!")
print("My x:", my_x)
print("My y:", my_y)
print("k:", k)
print("a:", a)
x = int(input("Give me your x: "))

if (x.bit_length() < 1024):
    print("Sorry, your x needs to be long enough :(")
else:
    sq_y = ((k-1)*x**2 + a)//k
    if is_perfect_square(sq_y):
        print("Key collaboration successful! Here's the flag", FLAG)
    else:
        print("Sorry, the y obtained isn't valid :(")
    
