---
title: "Computers are *fast*!"
date: 2014-05-12
url: https://jvns.ca/blog/2014/05/12/computers-are-fast/
slug: computers-are-fast
word_count: 765
---


So I have a computer. My computer contains hardware (like a CPU! RAM!
L1/L2 caches!) But I don’t understand very well how fast that hardware
is, what tools I have to profile it, and how much of the time that my
programs are running is split between RAM/the hard disk/the CPU.


So today I paired with
[Sasha Laundy](https://twitter.com/SashaLaundy), and we ran Serious
Investigations into how fast my computer can process a 1GB file.


**The objects:**

- An episode of The Newsroom (1GB)
- A task: add up all the bytes (mod 256)


This was basically the easiest task that I could think of that
involved processing the entire file (so nothing gets optimized out by
the compiler).


### Step 1: Write a program to add up all the bytes


I wrote a small C program to add up all the bytes in a file. It’s
called
[bytesum.c](https://github.com/jvns/howcomputer/blob/master/bytesum.c).
It reads the file in chunks of 64k, and then adds up all the bytes
into a char.


This runs pretty fast! I compiled it with `gcc -Ofast` (to make it
FASTER!) and it added up all the bytes in

- 2.5 seconds (the first time I ran the program)
- 0.6 seconds (the second time I ran the program, because it’s already
loaded into RAM)


I take this to mean that it takes 2s to read the file into memory (I
have a SSD in my computer, so 500MB/s makes sense), and then 0.6s to
do the actual adding-up-of-the bytes. Awesome! We now know that I can
read from my hard drive at 500MB/s.


### Step 2: try to use `mmap` to make it faster


This is a pretty boring step. We made it use `mmap` instead (see
[bytesum_mmap.c](https://github.com/jvns/howcomputer/blob/master/bytesum_mmap.c)),
in the hopes that it would make it faster. It took exactly the same
amount of time. NEXT.


### Step 3: use vector intrinsics!!!


Then I went and talked to [James Porter](http://jamesporter.me/), and
he told me that CPUs have special instructions for doing multiple
additions at once, and that I could maybe use them to optimize my
program! So I googled “vector intrinsics”, copied some code from Stack
Overflow, and ended up with a new version:
[bytesum_intrinsics.c](https://github.com/jvns/howcomputer/blob/master/bytesum_intrinsics.c).
I timed it, and it took **0.25 seconds**!!!


So our program now runs **twice as fast**, and we know a whole bunch
of new words (SSE! SIMD! vector intrinsics!)


### Step 4: Make it slow.


Now that we’ve written a super fast program, I wanted to understand
the CPU caches better. What if we engineered a whole bunch of cache
misses? I wrote a new version of `bytesum_mmap.c` that added up all
the bytes in an irregular way – instead of going through all the
bytes in order, it would skip from byte 1 to 2001 to 3001 to 4001 and
then loop around and access 2, 2002, 3002, …, 100002. As you might
imagine, this isn’t very efficient.


You can see the code for this in
[bytesum_stride.c](https://github.com/jvns/howcomputer/blob/master/bytesum_stride.c).
I ran it with `./bytesum_stride *.mp4 60000`, and it took about 20
seconds. So we’ve learned that **cache misses can make your code 40
times slower**.


### Step 5: where do the 0.25 seconds come from???


I still didn’t totally understand exactly how my super fast vector
intrinsic program’s performance broke down, though: how much of that
0.25 seconds was spent doing memory accesses, and how much in
numerical computation? James suggested using
[Marss](http://marss86.org/~marss86/index.php/Home) which will
apparently give you unlimited amounts of information, but I spent a
few minutes trying to get it to work and failed.


So instead I used `perf`, which is a *totally magical* performance
measurement tool for Linux. I needed to upgrade my kernel first, which
was a bit nervewracking. But I did it! And it was beautiful. There are
colours, and we got it to annotate the assembly code with performance
statistics. Here’s what I ran to do it:


```

perf record ./bytesum_intrinsics The\ Newsroom\ S01E04.mp4
perf annotate --no-source

```


And here’s the result:


![](https://jvns.ca/images/perf.png)


The `movdqa` instructions have to do with accessing memory, and it
spends 32% of its time on those instructions. So I *think* that means
that it spends 32% of its time accessing RAM, and the other 68% of its
time doing calculations. Super neat!


There are still a lot of things I don’t understand here – are my
conclusions about this program correct? Are there further things I
could be doing to optimize this?


I’m also kind of amazed by how fast C is. I’m used to writing in
dynamic programming languages, which definitely do not process 1GB
files in 0.25 seconds. Fun!
