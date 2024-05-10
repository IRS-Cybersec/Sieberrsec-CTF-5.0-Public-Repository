# Flag Integer Overflow

Category: Pwn

Author: enxgmatic

Flag: `sctf{b1g_numb3r5_sm4ll_numb3r5}`

## Description

Can you count the flags?

## Solution

The vulnerability is, as suggested by the challenge name, integer overflow.

Integer overflow occurs when you try to store a value that is either too large or too small for an integer type. In the context of c, the max integer value is 2147483647, and the min is -2147483648.

If you store a value that is larger than INT_MAX or smaller than INT_MIN, its value will "wrap around"

So, if you store a value that is >2147483647, its value will wrap around to -2147483648.
- So for example, if you try to store a value of 2147483648, its value will wrap around to -2147483648 (since 2147483648 is 1 greater than INT_MAX).
- If you store a value of 2147483747, its value will around around to -2147483549 (since 2147483747 is 100 greater than INT_MAX, it will wrap to -2147483648+99)

This works the other way around too, if you have a value smaller than -2147483648, it will wrap around to 2147483647
- Eg if you try to store a value of -2147483649, its value will be 2147483647
- Eg if you try to store a value of -2147483748, its value will be 2147483647-99=2147483548

In this case, we can try to make `cost` to be so large, that `balance - cost` will become smaller than INT_MIN, which will wrap around to 2147483647!

We can do that by putting `21474856`.

`balance` will become `1000 - 100*21474856 = -2147484600`, which will wrap around to `2147483647 - (2147484600 - 2147483648) + 1 = 2147482696`. Hence, getting the flag.

Other input values can also work.

See `solve.py` for script.

## References

- https://nikhilh20.medium.com/integer-overflow-vulnerability-20f9ea48aff9

