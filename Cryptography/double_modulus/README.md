# Double Modulus

*Creator - Iri*

## Description

Our newest RSA algorithm uses two moduli, for double the security! We're so certain that it's safe, that we'll even let you pick the modulus!

## Hints
1. How can we make N and N+17 easy to factorise?

## Solution
Solution to this challenge:
1. We want to get a nice factorisation of N and N+17. If we let N+17 = 17p, we just need 17(p-1) to have a nice factorisation to get its phi.
2. We can choose a smooth prime p, which is a prime such that the factors of p-1 are smaller than a certain bound. Code can be found online (a good place is the picoCTF challenge "Very Smooth")
3. Hence, we can obtain all the factors of N and N+17, allowing us to calculate their respective private keys.

## Flag

SCTF{sm00th_pr1me5_4re_3asy_t0_fact0r1s3_1a7304b7fc7a4b84289cbb16}