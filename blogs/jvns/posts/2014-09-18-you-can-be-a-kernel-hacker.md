---
title: "You can be a kernel hacker!"
date: 2014-09-18
url: https://jvns.ca/blog/2014/09/18/you-can-be-a-kernel-hacker/
slug: you-can-be-a-kernel-hacker
word_count: 3050
---


This blog post is adapted from a talk I gave at Strange Loop
2014 with the same title. [Watch the video!](https://www.youtube.com/watch?v=0IQlpFWTFbM)


When I started [Hacker School](https://hackerschool.com), I wanted to
learn how the Linux kernel works. I’d been using Linux for ten years,
but I still didn’t understand very well what my kernel did. While
there, I found out that:

- the Linux kernel source code isn’t all totally impossible to
understand
- kernel programming is not just for wizards, it can also be for me!
- systems programming is REALLY INTERESTING
- I could write toy kernel modules, for fun!
- and, most surprisingly of all, all of this stuff was *useful*.


I hadn’t been doing low level programming at all – I’d written a
little bit of C in university, and otherwise had been doing web
development and machine learning. But it turned out that my newfound
operating systems knowledge helped me solve regular programming tasks
more easily.


I also now feel like if I were to be put on *Survivor: fix a bug in my
kernel’s USB driver*, I’d stand a chance of not being immediately
kicked off the island.


This is all going to be about Linux, but a lot of the same concepts
apply to OS X. We’ll talk about

- what even is a kernel?
- why bother learning about this stuff?
- A few strategies for understanding the Linux kernel better, on your own
terms:
  - strace all the things!
  - Read some kernel code!
  - Write a fun kernel module!
  - Write an operating system!
  - Try the Eudyptula challenge
  - Do an internship.


### What even is a kernel?


In a few words:


**A kernel is a bunch of code that knows how to interact with your hardware**.


Linux is mostly written in C, with bit of assembly. Let’s say you go
to [http://google.com](http://google.com) in your browser. That requires typing, sending
data over a network, allocating some memory, and maybe writing some
cache files. Your kernel has code that

- interprets your keypresses every time you press a key
- speaks the TCP/IP protocol, for sending information over the network
to Google
- communicates with your hard drive to write bytes to it
- understands how your filesystem is implemented (what do the bytes on
the hard drive even mean?!)
- gives CPU time to all the different processes that might be running
- speaks to your graphics card to display the page
- keeps track of all the memory that’s been allocated


and much, much more. All of that code is running all the time you’re
using your computer!


This is a lot to handle all at once! The only concept I want to you to
understand for the rest of this post is **system calls*. System calls
are your kernel’s API – regular programs that you write can interact
with your computer’s hardware using system calls. A few example system
calls:

- `open` opens files
- `sendto` and `recvfrom` send and receive network data
- `write` writes to disk
- `chmod` changes the permissions of a file
- `brk` and `sbrk` allocate memory


So when you call the `open()` function in Python, somewhere down the
stack that eventually uses the `open` system call.


That’s all you need to know about the kernel for now! It’s a bunch of
C code that’s running all the time on your computer, and you interact
with it using system calls.


### Why learn about the Linux kernel, anyway?


There are some obvious reasons: it’s really fun! Not everyone knows
about it! Saying you wrote a kernel module for fun is cool!


But there’s a more serious reason: learning about the interface
between your operating system and your programs will **make you a
better programmer**. Let’s see how!


#### Reason 1: strace


Imagine that you’re writing a Python program, and it’s meant to be
reading some data from a file `/user/bork/awesome.txt`. But it’s not
working!


A pretty basic question is: is your program even opening the right
file? You could start using your regular debugging techniques to
investigate (print some things out! use a debugger!). But the amazing
thing is that on Linux, the *only way* to open a file is with the
`open` system call. You can get a list of all of these calls to `open`
(and therefore every file your program has opened) with a tool called
strace.


Let’s do a quick example! Let’s imagine I want to know what files
Chrome has opened!


```
$ strace -e open google-chrome
[... lots of output omitted ...]
open("/home/bork/.config/google-chrome/Consent To Send Stats", O_RDONLY) = 36
open("/proc/meminfo", O_RDONLY|O_CLOEXEC) = 36
open("/etc/opt/chrome/policies/managed/lastpass_policy.json", O_RDONLY) = 36

```


This is a really powerful tool for observing the *behavior* for a
program that we wouldn’t have if we didn’t understand some basics
about system calls. I use strace to:

- see if the file I *think* my program is opening is what it’s
*really* opening (system call: `read`)
- find out what log file my misbehaving poorly documented program is
writing to (though I could also use `lsof`) (system call: `write`)
- spy on what data my program is sending over the network (system
calls: `sendto` and `recvfrom`)
- find out every time my program opens a network connection (system
call: `socket`)


I love strace so much I gave a lightning talk about just strace:
[Spying on your programs with strace](https://www.youtube.com/watch?v=4pEHfGKB-OE).


#### Reason 2: `/proc`


`/proc` lets you **recover your deleted files**, and is a great
example of how understanding your operating system a little better is
an amazing programming tool.


How does it do that? Let’s imagine that we’ve written a program
[smile.c](https://gist.github.com/jvns/a5c1ac3c141a6a6e782f), and
we’re in the middle of running it. But then we accidentally delete the
binary!


The PID of that process right now is `8604`. I can find the
executable for that process at `/proc/8604/exe`:


```
 /proc/8604/exe -> /home/bork/work/talks/2014-09-strangeloop/smile (deleted)

```


It’s `(deleted)`, but we can still look at it!
`cat /proc/8604/exe > recovered_smile` will recover our executable. Wow.


There’s also a ton of other really useful information about processes
in `/proc`. (like which files they have open – try `ls -l/proc/<pid>/fd`)


You can find out more with `man proc`.


#### Reason 3: ftrace


ftrace is totally different from strace. strace traces **system
calls** and ftrace traces **kernel functions**.


I honestly haven’t had occasion to do this yet but it is REALLY COOL
so I am telling you about it. Imagine that you’re having some problems
with TCP, and you’re seeing a lot of TCP retransmits. ftrace can give
you information about every time the TCP retransmit function in the
kernel is called!


To see how to actually do this, read Brendan Gregg’s post
[Linux ftrace TCP Retransmit Tracing](http://www.brendangregg.com/blog/2014-09-06/linux-ftrace-tcp-retransmit-tracing.html).


There also appear to be some articles about ftrace on
[Linux Weekly News!](https://www.google.ca/search?q=lwn+ftrace)


I dream of one day actually investigating this :)


#### Reason 4: perf


Your CPU has a whole bunch of different levels of caching (L1! L2!)
that can have really significant impacts on performance. `perf` is a
great tool that can tell you

- how often the different caches are being used (how many L1 cache
misses are there?)
- how many CPU cycles your program used (!!)
- profiling information (how much time was spent in each function?)


and a whole bunch of other insanely useful performance information.


If you want to know more about awesome CPU cycle tracking, I wrote
about it in
[I can spy on my CPU cycles with perf!](http://jvns.ca/blog/2014/05/13/profiling-with-perf/).


#### Convinced yet?


Understanding your operating system better is *super useful* and will
make you a better programmer, even if you write Python. The most
useful tools for high-level programming I’ve found `strace` and
`/proc`. As far as I can tell ftrace and perf are mostly useful for
lower-level programming. There’s also `tcpdump` and `lsof` and
`netstat` and all kinds of things I won’t go into here.


Now you’re hopefully convinced that learning more about Linux is worth
your time. Let’s go over some strategies for understanding Linux
better!


### Strategy 1: strace all the things!


I mentioned `strace` before briefly. `strace` is literally my favorite
program in the universe. A great way to get a better sense for what
your kernel is doing is – take a simple program that you understand
well (like `ls`), and run `strace` on it.


This will show you at what points the program is communicating with
your kernel. I took a 13 hour train ride from Montreal to New York
once and
[straced killall](http://jvns.ca/blog/2013/12/22/fun-with-strace/) and
it was REALLY FUN. Let’s try `ls`!


I ran `strace -o out ls` to save the output to a file. strace will
output a
[WHOLE BUNCH OF CRAP](https://gist.github.com/jvns/291a4de261cb326585c7).
It turns out that starting up a program is pretty complicated, and in
this case most of the system calls have to do with that. There’s a lot
of

- opening libraries: `open("/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC)`
- putting those libraries into memory: `mmap(NULL, 2126312, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7faf507fc000 `


and a bunch of other things I don’t really understand. My main
strategy when stracing for fun is to ignore all the crap at the
beginning, and just focus on what I understand. It turns out that `ls`
doesn’t need to do a lot!


```
openat(AT_FDCWD, ".", O_RDONLY|O_NONBLOCK|O_DIRECTORY|O_CLOEXEC) = 3
getdents(3, /* 5 entries */, 32768)     = 136
getdents(3, /* 0 entries */, 32768)     = 0
close(3)                                = 0
fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 12), ...}) = 0
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7faf5104a000
write(1, "giraffe  out  penguin\n", 22) = 22
close(1)                                = 0
munmap(0x7faf5104a000, 4096)            = 0
close(2)                                = 0
exit_group(0)                           = ?

```


This is awesome! Here’s what it needed to do:

1. Open the current directory: `openat(AT_FDCWD, ".", O_RDONLY|O_NONBLOCK|O_DIRECTORY|O_CLOEXEC)`
2. Get the contents of that directory: `getdents(3, /* 5 entries */, 32768) = 136`. Looks like it was 136 bytes of stuff!
3. Close the directory: `close(3)`
4. Write the files to standard out: `write(1, "giraffe out penguin\n", 22) = 22`
5. Close a bunch of things to clean up.


That was really simple, and we already learned a new system call! That
mmap in the middle there? No idea what that does. But it’s totally
fine! STRACE IS THE BEST.


So! Running strace on random processes and looking up the
documentation for system calls you don’t recognize is an easy way to
learn a ton!


**Warning**: **Don’t** strace processes
that you actually need to run efficiently! strace is like putting a
huge stopsign in front of your process every time you use a system
call, which is **all the time**. Brendan Gregg has a
[great post about strace which you should read](http://www.brendangregg.com/blog/2014-05-11/strace-wow-much-syscall.html).
Also you should probably read everything he writes.


### Strategy 2: Read some kernel code!


Okay, let’s imagine that we’ve gotten interested in `getdents` (the
system call to list the contents of a directory), and we want to
understand better what it actually does. There’s this fantastic tool
called [livegrep](http://livegrep.com) that lets you search through
kernel code. It’s by [Nelson Elhage](http://twitter.com/nelhage) who
is pretty great.


So let’s use it to find the source for `getdents`, which lists all the
entries in a directory! I searched for it
using livegrep, and found
[the source](https://github.com/torvalds/linux/blob/v3.13/fs/readdir.c#L192-L223).


On line 211, it calls `iterate_dir`. So let’s look that up! It’s
[here](https://github.com/torvalds/linux/blob/v3.13/fs/readdir.c#L23-L48).
Honestly this code makes no sense to me (maybe `res = file->f_op->iterate(file, ctx)` is what’s iterating over the directory?).


But it’s neat that we can look at it!


If you want to know about current Linux kernel development,
[Linux Weekly News](http://lwn.net/) is a great resource. For example,
here’s an interesting article about the
[btrfs filesystem!](http://lwn.net/Articles/342892/)


### Strategy 3: Write a fun kernel module!


Kernel modules sound intimidating but they’re actually really
approachable! All a kernel module is fundamentally is

1. An `init` function to run when the module is loaded
2. A `cleanup` function to run when the module is unloaded


You load kernel modules with `insmod` and unload them with `rmmod`.
Here’s a working “Hello world” kernel module!


```
#include <linux/module.h>    // included for all kernel modules
#include <linux/kernel.h>    // included for KERN_INFO
#include <linux/init.h>      // included for __init and __exit macros

static int __init hello_init(void)
{
    printk(KERN_INFO "WOW I AM A KERNEL HACKERl!!!\n");
    return 0;    // Non-zero return means that the module couldn't be loaded.
}

static void __exit hello_cleanup(void)
{
  printk(KERN_INFO "I am dead.\n");
}

module_init(hello_init);
module_exit(hello_cleanup);

```


That’s it! `printk` writes to the system log, and if you run `dmesg`,
you’ll see what it printed!


Let’s look at another fun kernel module! I gave a talk about kernel
hacking at [CUSEC](http://2014.cusec.net) in January, and I needed a
fun example. My friend [Tavish](https://twitter.com/tavarm) suggested
“hey julia! What if you made a kernel module that rick rolls you every
time you open a file?” And my awesome partner
[Kamal](https://twitter.com/kamalmarhubi) said “that sounds like fun!”
and inside a weekend he’d totally done it!


You can see the *extremely* well-commented source here:
[rickroll.c](https://github.com/jvns/kernel-module-fun/blob/master/rickroll.c).
Basically what it needs to do when loaded is

- find the system call table (it turns out this is not trivial!)
- Disable write protection so that we’re actually allowed to modify it
(!!)
- Save the old `open` so we can put it back
- Replace the `open` system call with our own `rickroll_open` system
call


That’s it!


Here’s the relevant code:


```
sys_call_table = find_sys_call_table();
DISABLE_WRITE_PROTECTION;
original_sys_open = (void *) sys_call_table[__NR_open];
sys_call_table[__NR_open] = (unsigned long *) rickroll_open;
ENABLE_WRITE_PROTECTION;
printk(KERN_INFO "Never gonna give you up!\n");

```


The `rickroll_open` function is also pretty understandable. Here’s a
sketch of it, though I’ve left out some important implementation
details that you should totally read: [rickroll.c](https://github.com/jvns/blob/master/rickroll.c)


```
static char *rickroll_filename = "/home/bork/media/music/Rick Astley - Never Gonna Give You Up.mp3";
asmlinkage long rickroll_open(const char __user *filename, int flags, umode_t mode) {
    if(strcmp(filename + len - 4, ".mp3")) {
        /* Just pass through to the real sys_open if the extension isn't .mp3 */
        return (*original_sys_open)(filename, flags, mode);
    } else {
        /* Otherwise we're going to hijack the open */ fd =
        (*original_sys_open)(rickroll_filename, flags, mode); return
        fd; } }

```


SO FUN RIGHT. The source is super well documented and interesting and
you should
[go read it](https://github.com/jvns/kernel-module-fun/blob/master/rickroll.c).
And if you think “but Kamal must be a kernel hacking wizard! I could
never do that!”, it is not so! Kamal is pretty great, but he had never
written kernel code before that weekend. I understand that he googled
things like “how to hijack system call table linux”. You could do the
same!


Kernel modules are an especially nice way to start because writing toy
kernel modules plays nicely into writing real kernel modules like
hardware drivers. Or you could start out writing drivers right away!
Whatever floats your boat :) The reference for learning about writing
drivers is called [Linux Device Drivers](http://lwn.net/Kernel/LDD3/)
or “LDD3”. The fabulous
[Jessica McKellar](http://web.mit.edu/jesstess/www/) is writing the
new version, LDD4.


### Strategy 4: Write an operating system!


This sounds really unapproachable! And writing a full-featured
operating system from scratch is a **ton** of work. But the great
thing about operating systems is that yours don’t need to be full-featured!


I wrote a [small operating system](https://github.com/jvns/puddle)
that basically only has a keyboard driver. And doesn’t compile for
anyone except me. It was 3 weeks of work, and I learned SO MUCH.
There’s a [super great wiki](http://wiki.osdev.org/Main_Page) with
lots of information about making operating system.


A few of the blog posts that I wrote while working on it:

- [Writing an OS in Rust in tiny steps](http://jvns.ca/blog/2014/03/12/the-rust-os-story/)
- [After 5 days, my OS doesn’t crash when I press a key](http://jvns.ca/blog/2013/12/04/day-37-how-a-keyboard-works/)
- [SOMETHING IS ERASING MY PROGRAM WHILE IT’S RUNNING (oh wait oops)](http://jvns.ca/blog/2013/12/16/day-43-hopefully-the-last-day-spent-fixing-linker-problems/)


I learned about linkers and bootloaders and interrupts and memory
management and how executing a program works and so many more things!
And I’ll never finish it,
[and that’s okay](http://jvns.ca/blog/2014/03/21/my-rust-os-will-never-be-finished/).


### Strategy 5: Do the Eudyptula challenge


If you don’t have an infinite number of ideas for hilarious kernel
module pranks to play on your friends (I certainly don’t!), the
[Eudyptula Challenge](http://eudyptula-challenge.org/) is specifically
built to help you get started with kernel programming, with
progressively harder steps. The first one is to just write a
“hello world” kernel module, which is pretty straightforward!


They’re pretty strict about the way you send email (helping you
practice for the linux kernel mailing list, maybe!). I haven’t tried
it myself yet, but [Alex Clemmer](http://nullspace.io) tells me that
it is hard but possible. Try it out!


### Strategy 6: Do an internship


If you’re really serious about all this, there are a couple of
programs I know of:

- Google Summer of Code, for students
- The GNOME outreach program for women


The GNOME outreach program for women (OPW) is a great program that
provides mentorship and a 3-month paid internship for women who would
like to contribute to the Linux kernel.
[More than 1000 patches](http://sage.thesharps.us/2014/08/27/2014-kernel-internship-report-opw/)
from OPW interns and alumni have been accepted into the kernel.


In the application you submit a simple patch to the kernel (!!), and
it’s very well documented. You don’t need to be an expert, though you
do need to know some C.


**You can apply now!** The application deadline for the current round
is October 31, 2014, and you can find more information on the
[kernel OPW website](http://kernelnewbies.org/OPWIntro).


### Resources


To recap, here are a few super useful resources for learning that I’ve
mentioned:

- Previous writing:
[4 paths to being a kernel hacker](http://jvns.ca/blog/2014/01/04/4-paths-to-being-a-kernel-hacker/),
everything I’ve written about [kernels](http://jvns.ca/categories/kernel/)
- I learned all of this at [Hacker School](https://www.hackerschool.com/)
- [LXR](http://lxr.linux.no/linux+v3.12.6/) and
[http://livegrep.com/](http://livegrep.com/search/linux) are great
for searching the Linux kernel
- [Linux Device Drivers 3](http://lwn.net/Kernel/LDD3/) is available
free online.
- The [OPW internship for the Linux kernel](http://kernelnewbies.org/OPWIntro)
- Linux Weekly News
([here’s an index](http://lwn.net/Archives/GuestIndex/))
- [Brendan Gregg](http://brendangregg.com/) has a ton of extremely
useful writing about performance analysis tools like `perf` and
`ftrace` on Linux.


### You can be a kernel hacker


I’m not a kernel hacker, really. But now when I look at awesome actual
kernel hackers like [Valerie Aurora](http://valerieaurora.org/) or
[Sage Sharp](http://sage.thesharps.us/), I no longer think that
they’re wizards. I now think those are people who worked really hard
on becoming better at kernel programming, and did it for a long time!
And if I spent a lot of time working on learning more, I could be a
kernel hacker too.


And so could you.
