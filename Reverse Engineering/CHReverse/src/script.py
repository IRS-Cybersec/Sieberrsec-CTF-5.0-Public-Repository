
flag = 'sctf{r3v3rsing_th3_c0d3}'
key = 'THEKEY'
i = 0

encrypted = ''

for char in flag:
    value = ord(char)
    if value < 97:
        value += 32
        value = value ^ ord(key[i])
        encrypted += chr(value)
    else:
        value -= 64
        value = value ^ ord(key[i])
        encrypted += chr(value)
    i += 1
    if i > 5:
        i = 0

print(encrypted)
with open("output.txt", "w") as f:
    f.write(encrypted)
