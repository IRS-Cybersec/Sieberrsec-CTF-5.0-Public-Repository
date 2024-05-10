
# Expected Twist
Category: misc

Creator: yeobl

Flag: `sctf{m3r53nn3_7w1573r_un7w1573r}`

## Description
I have an array a containing 625 uniformly distributed 32-bit numbers. You can ask me at most 624 queries about the array. For each query, you have to give me 2 numbers l and r such that 1 <= l <= r <= 625. I will respond with the range XOR of the array within the range [l, r] inclusive. Formally, I will output a_l ^ a_(l+1) ^ a_(l+2) ^ ... ^ a_(r-2) ^ a_(r-1) ^ a_r. After you are done asking the queries, guess my array and output it.

## Solution

From the source code, it can be seen that the Python Random library was used to generate juryAns. The random library uses the Mersenne Twister algorithm to generate the "random" bits. A possible solution is this: https://github.com/eboda/mersenne-twister-recover
