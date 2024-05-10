# Y3K

Author: samuzora

Difficulty: Medium

It's the year 3000, who cares about efficient memory usage? My program allocates huge chunks to prevent any heap
overflows (whatever that is). The bigger the chunk, the safer it is right?

## Solution

Libc 2.35
PIE disabled
Full RELRO

We are constrained to chunks of size 0x1008. Therefore, tcache/fastbin is not an option. Chunks will only land in
unsorted/large bin.

We have an easy-to-spot UAF. Use this + view for our libc leak.

Since free does a few checks on unsorted chunks to ensure the double-linked list isn't corrupted, it's slightly hard to
pivot from the UAF to write primitive as we can't overwrite fd/bk to our target directly. One way to exploit unsorted is
as follows:

```c
    /* consolidate backward */
    if (!prev_inuse(p)) {
      prevsize = prev_size (p);
      size += prevsize;
      p = chunk_at_offset(p, -((long) prevsize));
      if (__glibc_unlikely (chunksize(p) != prevsize))
        malloc_printerr ("corrupted size vs. prev_size while consolidating");
      unlink_chunk (av, p);
    }
```

The above segment is called when the previous chunk was previously freed. This is most commonly seen in House of
Einherjar, but we don't have overflow Einherjar is not possible. However, we do have control over fd and bk, which is
used in `unlink_chunk`:

```c
/* Take a chunk off a bin list.  */
static void
unlink_chunk (mstate av, mchunkptr p)
{
  if (chunksize (p) != prev_size (next_chunk (p)))
    malloc_printerr ("corrupted size vs. prev_size");

  mchunkptr fd = p->fd;
  mchunkptr bk = p->bk;

  if (__builtin_expect (fd->bk != p || bk->fd != p, 0))
    malloc_printerr ("corrupted double-linked list");

  fd->bk = bk;
  bk->fd = fd;
  if (!in_smallbin_range (chunksize_nomask (p)) && p->fd_nextsize != NULL)
    {
      if (p->fd_nextsize->bk_nextsize != p
	  || p->bk_nextsize->fd_nextsize != p)
	malloc_printerr ("corrupted double-linked list (not small)");

      if (fd->fd_nextsize == NULL)
	{
	  if (p->fd_nextsize == p)
	    fd->fd_nextsize = fd->bk_nextsize = fd;
	  else
	    {
	      fd->fd_nextsize = p->fd_nextsize;
	      fd->bk_nextsize = p->bk_nextsize;
	      p->fd_nextsize->bk_nextsize = fd;
	      p->bk_nextsize->fd_nextsize = fd;
	    }
	}
      else
	{
	  p->fd_nextsize->bk_nextsize = p->bk_nextsize;
	  p->bk_nextsize->fd_nextsize = p->fd_nextsize;
	}
    }
}
```

Once the self-reference check is passed, `fd->bk` and `bk->fd` are overwritten. We thus have a sort of arbitrary write
here. 

Note:
1. Since we're dealing with largebin sizes, we also need to pass nextsize and prevsize checks.
2. 2.35 doesn't allow for `__free_hook`, and we only have 1 leak so we can't attack `exit_funcs`. We can attack stderr
   file struct which doesn't require any leaks other than libc base.

Exploit is as follows:

1. Malloc 2 chunks and free the 1st. 1st is victim chunk.
2. Forge fake chunk exactly at start of data segment of victim chunk. `fd` is -0x18 from pointer to victim and `bk` is
   -0x10 from pointer to victim. `fd_nextsize` (since `fd` and `bk` are overwritten before largebin checks) is -0x28
   from the other pointer to victim (`last_chunk`), and `bk_nextsize` is -0x20 from that other pointer.
3. At the end of fake chunk, set the `prev_size` of chunk 2 to align with fake chunk.
4. Free chunk 2 triggering unlink mechanism. Chunk array is now corrupted.
5. Overwrite `chunks[0]` to desired write address while preparing for House of Apple.
6. Attack stderr and perform House of Apple.
