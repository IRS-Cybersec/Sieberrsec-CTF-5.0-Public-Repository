# Multiprime

*Creator - Iri*

## Description

My RSA encryption uses multiple primes, wouldn't it be so much more secure than using 2 primes only?

## Hints
1. What ways are there to factorise N if we know all the primes are small?

## Solution
Solution to this challenge:
1. By using the elliptic curve factorisation method, we can find all the prime factors of N, and hence calculate phi.
2. We can then solve RSA normally.

## Flag

SCTF{3ll1p7ic_curv35_f1nd_5ma11_f4ct0r5_7961bff6dde8b67857cdb}