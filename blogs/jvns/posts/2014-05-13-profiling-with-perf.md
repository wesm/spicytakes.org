---
title: "I can spy on my CPU cycles with perf!"
date: 2014-05-13
url: https://jvns.ca/blog/2014/05/13/profiling-with-perf/
slug: profiling-with-perf
word_count: 635
---


Yesterday I talked about using `perf` to profile assembly
instructions. Today I learned how to make flame graphs with `perf`
today and it is THE BEST. I found this because
[Graydon Hoare](https://twitter.com/graydon_moz) pointed me to Brendan
Gregg’s *excellent*
[page on how to use perf](http://www.brendangregg.com/perf.html).


Wait up! What’s `perf`? I’ve talked about `strace` a lot before (in
[Debug your programs like they’re closed source](http://jvns.ca/blog/2014/04/20/debug-your-programs-like-theyre-closed-source/)).
`strace` lets you see which system calls a program is calling. But
what if you wanted to know

- how many CPU instructions it ran?
- How many L1 cache misses there were?
- profiling information for each assembly instruction?


`strace` only does system calls, and none of those things are system
calls. So it can’t tell you any of those things!


`perf` is a Linux tool that can tell you all of these things, and
more! Let’s run a quick example on the
[bytesum program from yesterday](http://jvns.ca/blog/2014/05/12/computers-are-fast/).


```

bork@kiwi ~/w/howcomputer> perf stat ./bytesum_mmap *.mp4
 Performance counter stats for './bytesum_mmap The Newsroom S01E04.mp4':

        158.141639 task-clock                #    0.994 CPUs utilized          
                22 context-switches          #    0.139 K/sec                  
                 9 CPU-migrations            #    0.057 K/sec                  
               133 page-faults               #    0.841 K/sec                  
       438,662,273 cycles                    #    2.774 GHz                     [82.43%]
       269,916,782 stalled-cycles-frontend   #   61.53% frontend cycles idle    [82.38%]
       131,557,379 stalled-cycles-backend    #   29.99% backend  cycles idle    [66.66%]
       681,518,403 instructions              #    1.55  insns per cycle        
                                             #    0.40  stalled cycles per insn [84.88%]
       130,568,804 branches                  #  825.645 M/sec                   [84.85%]
            20,756 branch-misses             #    0.02% of all branches         [83.68%]

       0.159154389 seconds time elapsed

```


This is super neat information, and there’s a lot more (see `perf list`). But we can do even more fun things!


### Flame graphs with perf


I wanted to profile my `bytesum` program. But how do you even profile
C programs? Here’s a way to do it with `perf`:


```

sudo perf record -g ./bytesum_mmap *.mp4
sudo perf script | stackcollapse-perf.pl | flamegraph.pl > flamegraph.svg

```


Here’s the SVG this gave me:


![](https://jvns.ca/images/flamegraph.svg)


This is AMAZING. But what does it mean? Basically `perf` periodically
interrupts the program and finds out where in the stack it is. The
width of each part of the stack in the graph above is the proportion
of samples that happened there. (so about 30% of the execution time
was spend in `main`). I don’t know what the colour means here.


We can see that there are 3 big parts – there’s the `mmap` call (on
the left), the main program execution (in the middle), and the
`sys_exit` part on the right. Apparently stopping my program takes a
long time! Neat!


But there’s more!


### Is it really L1 cache misses? We can find out!


So yesterday I made a program with really bad memory access patterns
([bytesum_stride.c](https://github.com/jvns/howcomputer/blob/master/bytesum_stride.c)),
and I conjectured that it was way slower because it was causing way
too many L1 cache misses.


But with `perf`, we can check if that’s actually true! Here are the
results (reformatted a bit to be more compact):


```

bork@kiwi ~/w/howcomputer> perf stat -e L1-dcache-misses,L1-dcache-loads ./bytesum_mmap *.mp4
        17,175,214 L1-dcache-misses #   11.48% of all L1-dcache hits  
       149,568,438 L1-dcache-loads
bork@kiwi ~/w/howcomputer> perf stat -e L1-dcache-misses,L1-dcache-loads ./bytesum_stride *.mp4 1000
     1,031,902,483 L1-dcache-misses #  193.16% of all L1-dcache hits  
       534,219,219 L1-dcache-loads

```


So, uh, that’s really bad. We now have **60 times more** L1 cache
misses, and also 3 times more hits.


### Other amazing things

- Go to
[Brendan Gregg’s perf page and read the whole thing](http://www.brendangregg.com/perf.html).
Also possibly everything he’s ever written. His recent post on
[strace](http://www.brendangregg.com/blog/2014-05-11/strace-wow-much-syscall.html)
is great too.
- The [perf tutorial](https://perf.wiki.kernel.org/index.php/Tutorial)
is pretty long, but I found it somewhat helpful.
- [FlameGraph!](https://github.com/brendangregg/FlameGraph)
- I spent a little bit of time running cachegrind with
`valgrind --tool=cachegrind ./bytesum_mmap my_file`
which can give you possibly even more information about CPU caches
than `perf` can. Still haven’t totally wrapped my head around this.


There are still so many things I don’t understand at all!
