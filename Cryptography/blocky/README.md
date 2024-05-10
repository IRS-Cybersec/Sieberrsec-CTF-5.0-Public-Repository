# Blocky

*Creator - Iri*

## Description

I heard that AES is pretty secure, want to try my encryption system?

Wrap the flag in SCTF{}

## Hints
1. Can we recover the characters of the flag one by one?

## Solution
Solution to this challenge:
1. We can recover characters of the flag one by one by putting the flag bytes into the same 16-byte block as the rest of our input.
2. Then, we can trial and error all the possible characters (0-9, a-z, A-Z, _) to find when the block matches, which means that the flag byte is recovered.

## Flag

SCTF{0n3_bY_0n3_4e92c}