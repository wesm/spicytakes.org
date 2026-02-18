---
title: "Recovering files using /proc (and spying, too!)"
date: 2014-03-23
url: https://jvns.ca/blog/2014/03/23/recovering-files-using-slash-proc-and-other-useful-facts/
slug: recovering-files-using-slash-proc-and-other-useful-facts
word_count: 785
---


I’ve had a vague idea for years that /proc was a way the Linux kernel
exposed its internals, and that I could look there to find things.


Then I learned this:


> TIL!!! If you
> accidentally delete a file that a process still has open, you can
> recover it with cat /proc/$pid/fd/$file_descriptor. so
> easy!— Julia Evans (@b0rk) [March 19,
> 2014](https://twitter.com/b0rk/statuses/446291944575352833)


Suddenly it was like `/proc` was turned into a magical unicorn! I can
use it to recover my files?! ★★Amazing★★.


Let’s explain why this works. When a process opens a file (including
sockets), it gets a *file descriptor* for that file, which is a number
starting at 0.


### File descriptors and investigations on std{in,out,err}


0, 1, and 2 are always the stdin, stdout, and stderr of the process.
For example, if I look at the file descriptors for a Google Chrome
process I have, I see:


```

$ ls /proc/4076/fd
0  10  12  14  16  18  2   21  23  26  28  3   31  34  36  38  4   41  43  5   6  72  8
1  11  13  15  17  19  20  22  25  27  29  30  32  35  37  39  40  42  44  53  7  74  9

```


That’s pretty opaque! Let’s take a closer look.


```

$ ls -l /proc/4076/fd/{0,1,2}
lr-x------ 1 bork bork 64 Mar 22 22:38 /proc/4076/fd/0 -> /dev/null
l-wx------ 1 bork bork 64 Mar 22 22:38 /proc/4076/fd/1 -> /dev/null
l-wx------ 1 bork bork 64 Mar 22 22:38 /proc/4076/fd/2 -> /home/bork/.xsession-errors

```


Neat, the numbers 0, 1, and 2 are just symbolic links! It looks like
Chrome doesn’t have any stdin or stdout, which makes sense, but the
stderr is `/home/bork/.xsession-errors`. I didn’t know that! It turns
out this is also a great way to find out where a process that you
didn’t start is redirecting its output.


Where else do my programs redirect their stderr? Let’s see! I looked
at everything’s stderr, got awk to pull out just the file, and ran
`uniq` to get the counts.


```

$ ls -l /proc/*/fd/2 | awk '{print $11}' | sort | uniq -c
      42 /dev/null
      2 /dev/pts/0
      1 /dev/pts/1
      3 /dev/pts/2
      2 /dev/pts/3
      2 /dev/pts/4
      5 /dev/pts/5
      1 /dev/pts/7
     25 /home/bork/.xsession-errors

```


So mostly /dev/null, some of them are running on terminals
(`/dev/pts/*`), and the rest to `~/.xsession-errors`. No huge
surprises here.


What else could we use these file descriptors for? Someone on Twitter
suggested this:


> [@b0rk](https://twitter.com/b0rk) When I was
> making my first Tarsnap backup, I used `readlink
> /proc/<TARSNAP>/fd/7` in a loop to find out what file it was
> on. — Matthew Frazier (@LeafStorm) [March
> 23, 2014](https://twitter.com/LeafStorm/statuses/447564888198885376)


This works because when you open different files again and again in a
loop, it will usually end up with the same file descriptor. You could
also do the same thing by running `strace -etrace=open -p$TARSNAP_PID`
to see which files Tarsnap is opening.


Okay, now we know that we can use /proc to learn about our processes'
files! What else?


### Spy on your processes with /proc/$pid/status


If you look at the file `/proc/$pid/status`, you can find out all
sorts of information about your processes! You can look at this for
any process.


Here’s a sample of what’s in that file:


```

Name:   chrome
Groups: 4 20 24 27 30 46 104 109 124 1000 
VmPeak:   853984 kB
VmSize:   670392 kB
VmData:   323264 kB
VmExe:     96100 kB
Threads:        3
Cpus_allowed_list:      0-7

```


So we can see there’s some information about the memory, its name, its
groups, its threads, and which CPUs it’s allowed to run on.


But wait! We could have found out a lot of this information with `ps aux`. How does `ps` do it? Let’s find out!


```

$ strace -f -etrace=open ps aux
...
open("/proc/30219/stat", O_RDONLY)      = 6
open("/proc/30219/status", O_RDONLY)    = 6
open("/proc/30219/cmdline", O_RDONLY)   = 6
...

```


So `ps` gets its information from `/proc`! Neat.


### I’m sold. What else is there?!!


I tweeted asking for suggestions of things to find in `/proc/`, and
someone replied linking to the
[/proc man page](http://linux.die.net/man/5/proc). I thought they were
trolling me, but then I clicked on it and it was actually useful!


A few more things I need to investigate:

- the `procps` and `sysstat` utilities
- a ton of wonderful suggestions by Keegan McAllister on the
[Ksplice blog](https://blogs.oracle.com/ksplice/entry/solving_problems_with_proc)
(including how to force a program to take stdin if it doesn’t take
stdin)
- `/sys` replaces part of `/proc`’s functionality.
- Plan 9 / Inferno took this “everything is a file” business even more
seriously than Linux does
- [debugfs](https://en.wikipedia.org/wiki/Debugfs) / ftrace.
[An example someone linked to.](http://thread.gmane.org/gmane.linux.kernel.mmc/4248/focus=4400)


I still feel like there are concrete uses for `/proc/` that I don’t
know about, though. What are they?
