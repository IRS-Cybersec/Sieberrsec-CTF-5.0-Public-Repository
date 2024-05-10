from pwn import *

elf = context.binary = ELF('./intro')

local = True

if not local:
    io = remote('EDIT', 1)
else:
    io = elf.process(stdin=PTY)


for i in range(50):
    io.recvuntil(b'n1: ')
    n1 = int(io.recvline())
    io.recvuntil(b'n2: ')
    n2 = int(io.recvline())

    print(n1,n2)
    output = n1 * n2

    io.sendline(str(output))

io.interactive()
