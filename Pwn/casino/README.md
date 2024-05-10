# Casino

Category: pwn

Author: enxgmatic

Flag: `sctf{g4mbl1n9_15_b4d_9uy5}`

## Description

I heard that you shouldn't gamble here unless you know the casino's counting tricks.

## Solution

Integer overflow at `gamble()`.

Eg first gamble -1000 => your balance is now $-900. Then gamble -2147483648 to cause integer overflow to proc => balance is now $2147482748. Buy the flag.

You just need to take note that gamble <= balance.

See `solve.py` for script.
