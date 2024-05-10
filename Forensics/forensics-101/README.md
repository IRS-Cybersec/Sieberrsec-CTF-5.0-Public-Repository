
# Title:
Forensics 101

# Description:
Aww... the cat is so cute! ...But it looks like it's hiding something.

# Hint
Have you tried searching for "png password stego"

# Flag:
sctf{d1d_y0u_3nj0y_th3_c4t_st1ck3r}

# Solution:
1. Using Hexedit or other hex editors, change the file header and trailer to png (because of IHDR which suggests its a png file)
2. In the catmemes.png, there is a passkey written in Base 64
3. Use Cyberchef or any other software to change it to text to get "theresameowinhomeowner"
4. With some Google searching on png password steganography, you can find ImageConceal and Use it with the passkey to decrypt the flag.txt file from catmemes.png