# I'm Xorry

*Creator - landen*

## Description
Hmmm... Seems we found some kind of password. I'm xorry, i can't seem to crack it though.

## Hints (Optional)
1. What are common vulneribilites of a XOR cipher? | 10


## Distribution (Optional)

- xorry.py

## Solution
Solution to this challenge
1. Known plaintext attack. Knowing the first 5 characters of the flag will be 'sctf{' and the last character is '}'(this only works because the full length of the flag is a multiple of 6), run an XOR cipher on 'sctf{}' and the output in the comments.
2. Set the found key as the key variable in xorry.py and the output as the flag variable to get the whole flag.

## Flag
`sctf{p1ainntX+a@attackk}`
