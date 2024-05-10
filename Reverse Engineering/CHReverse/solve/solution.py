key = 'THEKEY'
i = 0
flag = ''

with open('output.txt','r') as f:
    encrypted = f.read()

for char in encrypted:
    value = ord(char) ^ ord(key[i])

    i += 1
    if i > 5:
        i = 0

    if value < 65:
        value += 64
    else:
        value -= 32
    flag += chr(value)

print(flag)
