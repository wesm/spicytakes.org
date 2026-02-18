---
title: "fork is not my favorite syscall"
date: 2018-01-02
url: https://drewdevault.com/2018/01/02/The-case-against-fork.html
slug: The-case-against-fork
word_count: 1364
---

This article has been on my to-write list for a while now. In my opinion, fork
is one of the most questionable design choices of Unix. I don’t understand the
circumstances that led to its creation, and I grieve over the legacy rationale
that keeps it alive to this day.

Let’s set the scene. It’s 1971 and you’re a fly on the wall in Bell Labs,
watching the first edition of Unix being designed for the PDP-11/20. This
machine has a 16-bit address space with no more than 248 kilobytes of memory.
They’re discussing how they’re going to support programs that spawn new
programs, and someone has a brilliant idea. “What if we copied the entire
address space of the program into a new process running from the same spot, then
let them overwrite themselves with the new program?” This got a rousing laugh
out of everyone present, then they moved on to a better design which would
become immortalized in the most popular and influential operating system of all
time.

At least, that’s the story I’d like to have been told. In actual fact, the
laughter becomes consensus. There’s an obvious problem with this approach: every
time you want to execute a new program, the entire process space is copied and
promptly discarded when the new program begins.  Usually when I complain about
fork, this the point when its supporters play the virtual memory card, pointing
out that modern operating systems don’t actually have to copy the whole address
space. We’ll get to that, but first — First Edition Unix  *does*  copy the
whole process space, so this excuse wouldn’t have held up at the time. By Fourth
Edition Unix (the next one for which kernel sources survived), they had wisened
up a bit, and started only copying segments when they faulted.

This model leads to a number of problems. One is that the new process inherits
 *all*  of the parent’s process descriptors, so you have to close them all before
you exec another process. However, unless you’re manually keeping tabs on your
open file descriptors, there is no way to know what file handles you must close!
The hack that solves this is  `CLOEXEC` , the first of many hacks that deal with
fork’s poor design choices. This file descriptors problem balloons a bit -
consider for example if you want to set up a pipe. You have to establish a piped
pair of file descriptors in the parent, then close every fd  *but*  the pipe in
the child, then  `dup2`  the pipe file descriptor over the (now recently closed)
file descriptor 1. By this point you’ve probably had to do several non-trivial
operations and utilize a handful of variables from the parent process space,
which  *hopefully*  were on the stack so that we don’t end up copying segments
into the new process space anyway.

These problems, however, pale in comparison to my number one complaint with the
fork model. Fork is the direct cause of the  *stupidest*  component I’ve  *ever* 
heard of in an operating system: the out-of-memory (aka OOM) killer. Say you
have a process which is using half of the physical memory on your system, and
wants to spawn a tiny program. Since fork “copies” the entire process, you might
be inclined to think that this would make fork fail. But, on Linux and many
other operating systems since, it does not fail! They agree that it’s stupid to
copy the entire process just to exec something else, but because fork is
Important for Backwards Compatibility, they just fake it and reuse the same
memory map (except read-only), then trap the faults and actually copy later.
The hope is that the child will get on with it and exec before this happens.

However, nothing prevents the child from doing something other than exec -
it’s free to use the memory space however it desires! This approach now leads to
 *memory overcommittment*  - Linux has promised memory it does not have. As a
result, when it really does run out of physical memory, Linux will just kill off
processes until it has some memory back. Linux makes an awfully big fuss about
“never breaking userspace” for a kernel that will lie about memory it doesn’t
have, then kill programs that try to use the back-alley memory they were given.
That this nearly 50 year old crappy design choice has come to this astonishes
me.

Alas, I cannot rant forever without discussing the alternatives. There  **are** 
better process models that have been developed since Unix!

The first attempt I know of is BSD’s  `vfork`  syscall, which is, in a nutshell,
the same as fork but with severe limitations on what you do in the child process
(i.e. nothing other than calling exec straight away). There are  *loads*  of
problems with  `vfork` . It only handles the most basic of use cases: you cannot
set up a pipe, cannot set up a pty, and can’t even close open file descriptors
you inherited from the parent. Also, you couldn’t really be sure of what
variables you were and weren’t editing or allowed to edit, considering the
limitations of the C specification. Overall this syscall ended up being pretty
useless.

Another model is  `posix_spawn` , which is a hell of an interface. It’s far too
complicated for me to detail here, and in my opinion far too complicated to ever
consider using in practice. Even if it could be understood by mortals, it’s a
really bad implementation of the spawn paradigm — it basically operates
like fork backwards, and inherits many of the same flaws. You still have to deal
with children inheriting your file descriptors, for example, only now you do it
in the parent process. It’s also straight-up impossible to make a genuine pipe
with  `posix_spawn` . ( *Note: a reader corrected me - this is indeed possible via
posix_spawn_file_actions_adddup2* .)

Let’s talk about the good models -  `rfork`  and spawn (at least, if spawn is done
right).  `rfork`  originated from plan9 and is a beautiful little coconut of a
syscall, much like the rest of plan9. They also implement fork, but it’s a
special case of  `rfork` . plan9 does not distinguish between processes and
threads - all threads are processes and vice versa. However, new processes in
plan9 are not the everything-must-go fuckfest of your typical fork call.
Instead, you specify exactly what the child should get from you. You can choose
to include (or not include) your memory space, file descriptors, environment, or
a number of other things specific to plan9. There’s a cool flag that makes it so
you don’t have to reap the process, too, which is nice because reaping children
is another really stupid idea. It still has some problems, mainly around
creating pipes without tremendous file descriptor fuckery, but it’s basically as
good as the fork model gets. Note: Linux offers this via the  `clone`  syscall
now, but everyone just fork+execs anyway.

The other model is the spawn model, which I prefer. This is the approach I took
in my own kernel for KnightOS, and I think it’s also used in NT (Microsoft’s
kernel). I don’t really know much about NT, but I can tell you how it works in
KnightOS. Basically, when you create a new process, it is kept in limbo until
the parent consents to begin. You are given a handle with which you can
configure the process - you can change its environment, load it up with file
descriptors to your liking, and so on. When you’re ready for it to begin, you
give the go-ahead and it’s off to the races. The spawn model has none of the
flaws of fork.

Both fork and exec can be useful at times, but spawning is much better for 90%
of their use-cases. If I were to write a new kernel today, I’d probably take a
leaf from plan9’s book and find a happy medium between  `rfork`  and spawn, so you
could use spawn to start new threads in your process space as well. To the
brave OS designers of the future, ready to shrug off the weight of legacy:
please reconsider fork.
