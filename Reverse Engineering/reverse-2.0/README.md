# 0.2 esreveR

Category: Reverse Engineering

Author: ljx1608

Flag: `sctf{b38e902f_c0mpl1c4t3d_2dc23508_r3vers3_91ede681}`

## Description

?drowssap eht esrever su pleh uoy naC .niatbo ot deganam ew hcihw ,resrever terces repus a htiw desrever saw drowssap rieht taht dias yehT .rekcah a morf `1ede681}rs3_93ve508_r_2dc233dc0mpl1c4t902f_e{b38fsct` drowssap terces repus a niatbo ot deganam eW

## Solution

[Reverse the challenge description.](https://gchq.github.io/CyberChef/#recipe=Reverse('Character')&input=P2Ryb3dzc2FwIGVodCBlc3JldmVyIHN1IHBsZWggdW95IG5hQyAubmlhdGJvIG90IGRlZ2FuYW0gZXcgaGNpaHcgLHJlc3JldmVyIHRlcmNlcyByZXB1cyBhIGh0aXcgZGVzcmV2ZXIgc2F3IGRyb3dzc2FwIHJpZWh0IHRhaHQgZGlhcyB5ZWhUIC5yZWtjYWggYSBtb3JmIGAxZWRlNjgxfXJzM185M3ZlNTA4X3JfMmRjMjMzZGMwbXBsMWM0dDkwMmZfZXtiMzhmc2N0YCBkcm93c3NhcCB0ZXJjZXMgcmVwdXMgYSBuaWF0Ym8gb3QgZGVnYW5hbSBlVw) Load the binary into Ghidra/IDA/dogbolt.org and read the decompiled code. The sources and equivalent python script are available in [src](./src) and [solve](./solve) folders respectively.
