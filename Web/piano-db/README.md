# piano db

flag: `sctf{0op5_un10n_4t+4ck}`

## Description

I have been learning how to play the piano, so I made a website to store some of my favourite piano covers!

## Solution

Union based sqli.

Manually send a post request (eg using burpsuite), with the payload as your sql statement.

Payload: `' UNION SELECT flag FROM flaggy_table--`

