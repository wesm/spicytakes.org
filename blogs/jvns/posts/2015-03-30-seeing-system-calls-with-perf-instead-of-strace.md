---
title: "Seeing system calls with perf instead of strace"
date: 2015-03-30
url: https://jvns.ca/blog/2015/03/30/seeing-system-calls-with-perf-instead-of-strace/
slug: seeing-system-calls-with-perf-instead-of-strace
word_count: 438
---


I’m at a local hackerspace this evening, and I decided to get `perf`
working on my computer again. You all know by now that I’m pretty into
strace, but – strace is not always a good choice! If your program runs
too many system calls, strace will slow it down. A lot.


Let’s try it and see:


```
$ time du -sh ~/work
0.04 seconds
$ time strace -o out du -sh ~/work
2.66 seconds

```


That’s 65 times slower! This is because `du` needed to use 260,000
system calls, which is uh a lot. If you strace a program with less
system calls it won’t be that big of a deal. But what if we still want
to know what `du` is doing, and `du` is actually a Really Important
Program like a database or something?


### WE’RE GOING TO USE PERF =D =D.


I’ve been eyeing Brendan Gregg’s
[page on perf](http://www.brendangregg.com/perf.html)
and the [kernel.org tutorial](https://perf.wiki.kernel.org/index.php/Tutorial)
for almost a year now, and we learned in May last year that
[perf lets you count CPU cycles](http://jvns.ca/blog/2014/05/13/profiling-with-perf/), which is
cool! But perf is capable of way more stuff.


Here’s how we record what system calls `du` is using:


```
sudo perf record -e 'syscalls:sys_enter_*' du -sh ~/work

```


This finishes right away, except that perf takes a little extra time to
write its recorded data to desk. Then we can see the system calls with
`sudo perf script`, which shows us something like this:


```
du 25156 [003] 142769.540801: syscalls:sys_enter_newfstatat:
       dfd: 0x00000006, filename: 0x021b0b58, statbuf: 0x021b0ac8, flag: 0x0
du 25156 [003] 142769.540802: syscalls:sys_enter_close:
       fd: 0x00000006
du 25156 [003] 142769.540804: syscalls:sys_enter_newfstatat: 
       dfd: 0x00000005, filename: 0x021b4708, statbuf: 0x021b4678, flag: 0x0

```


This is showing us system calls! You can see the file descriptors –
`fd: 0x00000006`. But it doesn’t give us the filename, just… the
address of the filename? I don’t know how to get the actual filename out
and that makes me sad.


It’s called `perf script` because you can write scripts with the output
(like this [flamegraph script](http://www.brendangregg.com/FlameGraphs/cpuflamegraphs.html)!).
Like maybe you could pretty it up and have a script that’s like strace
but doesn’t slow your program down so much. Apparently `perf script -g python`
will automatically generate boilerplate for a perf script in Python for
me! But it doesn’t work because I need to recompile perf. So we’ll see
about that :)


That’s all I have to say for now! Mostly I’m writing this up in the
hopes that someone will either a) tell me how to get perf to give me the
actual filename or b) tell me why it’s unreasonable to expect perf to do
that.
