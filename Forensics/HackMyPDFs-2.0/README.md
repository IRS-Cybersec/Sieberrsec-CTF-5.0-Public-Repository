
# Title
HackMyPDFs 2.0

# Description
My PDF should be harder to hack now!

# Hint
Have you seen the previous versions of this PDF?

# Flag
sctf{h0w_d1d_y0u_f1nd_m3}

# Solution
1. After some looking around in hexedit, there are 2 %%EOF
2. PDFs keep the previous version and show the new version even after it has been written over so what is shown is the second part after the first %%EOF 
3. Hence, delete the second part after the %%EOF to get the original pdf
4. The many numbers if you copy them down left to right up to down, it will be in hexadecimal
5. Put the hexadecimal through Cyberchef to get the flag