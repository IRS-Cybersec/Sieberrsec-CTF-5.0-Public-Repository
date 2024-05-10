# Insider (Part 1)

Category: Forensics

Author: ljx1608

Flag: `sctf{unh4ck4bl3}`

## Description

Our employee John from Hacking Pros has been acting suspiciously lately. We managed to get a memory dump of his computer. Find out what his password is.

Flag format: `sctf{password}`

## Distribution
https://drive.google.com/file/d/11Ue988l0ujsCc1Vt7fLH-vAtjWO-PwTQ/view?usp=sharing

## Solution

Since the challenge invovles a volatile memory dump, we first use Volatility 2 to find the appropriate profile using `volatility -f JOHN-PC-20240307-103240.raw imageinfo`. Then, using the appropriate profile, we try `volatility -f JOHN-PC-20240307-103240.raw --profile Win7SP1x86 hashdump` to dump SAM hashes:

```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
John:1000:aad3b435b51404eeaad3b435b51404ee:7ae7a60f7a94521653c6f01c9e7e8caf:::
```

The format of the dump is `<username>:<RID>:<LM hash>:<NTLM hash>:<comment>:<homedir>:<shell>`. The LM hash is empty, and the NTLM hash is `7ae7a60f7a94521653c6f01c9e7e8caf`. We can use an [online hash cracker](https://crackstation.net/) to find that the password is `unh4ck4bl3`. (Alternatively, we can use `hashcat` or `john` to crack the hash with the rockyou.txt wordlist. To do that, put the NTLM hash in a file, say `hash.txt`, and run `hashcat -m 1000 -a 0 hash.txt /usr/share/wordlists/rockyou.txt` or `john --format=NT hash.txt --wordlist=/usr/share/wordlists/rockyou.txt`.)
