---
title: "Understanding how killall works using strace"
date: 2013-12-22
url: https://jvns.ca/blog/2013/12/22/fun-with-strace/
slug: fun-with-strace
word_count: 607
---


Right now I’m on a million-hour train ride from New York to Montreal.
So I’m looking at the output of `strace` because, uh, `strace` is
cool, and it is teaching me some things about how the command line
tools I
use all the time work.


What `strace` does is capture every single system call that gets
called when executing a program. System calls are the interface
between userspace programs and the kernel, so looking at the output
from `strace` is a fun way to understand how Linux works, and what’s
really involved in running a program.


For example! `killall`! I ran


`strace killall ruby1.9.1 2> killall-log`.


This starts with


```
execve("/usr/bin/killall", ["killall", "ruby1.9.1"], [/* 48 vars */]) = 0

```


Every time you run a program, `execve` gets called to start, so
`execve` will always be the first line.


Then this happens A WHOLE BUNCH OF TIMES:


```
open("/proc/4526/stat", O_RDONLY)       = 3
fstat(3, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7febbb269000
read(3, "4526 (chrome) S 4521 2607 2607 0"..., 1024) = 374
close(3)                                = 0
munmap(0x7febbb269000, 4096)            = 0

```


with different PIDs.


What’s going on here is that it goes through every PID. To find the
PIDs, it opens the `/proc` directory. There’s a directory in `/proc`
for each PID.


```
bork@kiwi ~/w/homepage> ls /proc
1      1495   2408   2780   3278  8065         fb
10006  1498   2409   2782   3281  8066         filesystems
10152  1500   2410   2795   3283  8068         fs
10158  1504   2411   28     3317  8069         interrupts
1021   1513   2412   2802   35    8070         iomem

```


The system call that does this is:


`openat(AT_FDCWD, "/proc", O_RDONLY|O_NONBLOCK|O_DIRECTORY|O_CLOEXEC) = 3`


Once it’s done that, then it iterates through all the PIDs, opens
`/proc/$PID/stat`, and checks to see if the process has the right
name. The kernel isn’t involved in seeing whether or not the process
has the right name, so we don’t see that in the `strace` output.


Once it finds a PID that it wants to kill, it runs something like


```
kill(11510, SIGTERM)

```


to kill it. SIGTERM isn’t a very serious killing-y signal – it’s
signal 15, and processes can ignore it or save their state before they
stop. If you run `killall -9`, it will sent `SIGKILL` to all the
matching processes and it will kill them dead.


This is really neat! I never thought of `killall` as having to do an
exhaustive search through all PIDs before, but it makes sense.


After all of that, if there was something to kill, the only thing left
is `exit_group(0)`. `man 2 exit_group` tells me that this exits all
threads in a process, and that this system call is called at the end
.of every process


If we run `killall blah`, and there was no `"blah"` process to kill,
instead we see:


```
write(2, "blah: no process found\n", 23blah: no process found) = 23
exit_group(0) 

```


because it needs to write “no process found” to stderr.


**Edit:**


I have learned a couple of new things, from people’s responses to this
post!


If you want to see the library calls instead of the system calls, and
want to see where it does the string comparisons, you can use
`ltrace`!


For `killall`, finding `python3` and killing it looks like:


```
__asprintf_chk(0x7fff195b6988, 1, 0x403fd9, 15499, 0x7f31d919e700) = 16
fopen("/proc/15499/stat", "r")              = 0x208f8f0
free(0x0208f8d0)                            = <void>
fscanf(0x208f8f0, 0x403fe7, 0x7fff195b71b0, 0x7f31d8fa5728, 0) = 1
fclose(0x208f8f0)                           = 0
strcmp("python3", "python3")                = 0
kill(15499, 15)                             = 0

```


And you can attach `strace` or `ptrace` to an already-running process
to see what it’s up to. [@zbrdge](https://twitter.com/zbrdge/) said
that he sometimes uses it to see which files Apache is accessing
during a HTTP request.
