---
title: "Nancy Drew and the Case of the Slow Program"
date: 2015-03-15
url: https://jvns.ca/blog/2015/03/15/nancy-drew-and-the-case-of-the-slow-program/
slug: nancy-drew-and-the-case-of-the-slow-program
word_count: 1452
---


Yesterday I tweeted:


> you have three slow
> programs:
> 1. CPU-bound
> 2. waiting for slow network
> responses
> 3. writing a lot to disk
> how do you tell which is
> which?— Julia Evans (@b0rk) [March 14,
> 2015](https://twitter.com/b0rk/status/576883056864288768)


I specifically wanted programming-language-independent ways to
investigate questions like this, and I guess people who follow me on
twitter get me because I got SO MANY GREAT ANSWERS. I’ll give you a list
of all the answers at the end, but first! We’re going to mount an
investigation.


Let’s start! I wrote up 3 example mystery programs, and you can find
them in this
[github repository](https://github.com/jvns/swiss_army_knife_talk).


### Mystery Program #1


Let’s investigate our first mystery slow program!


First, let’s check **how long it takes** using `time`:


```
$ time python mystery_1.py
0.09user 0.01system 0:02.11elapsed 5%CPU (0avgtext+0avgdata 52064maxresident)

```


We can already see by timing the program  that a) it takes 2 seconds and
b) it’s only on the CPU for 5% of that time. So we already know it’s
waiting for something! But what is it waiting for?


#### What is Mystery Program #1 waiting for?


First, we’ll use a rough tool: `ps` can tell us what every process is
currently waiting for. It gives you a piece of information called
`wchan`, which the internet defines as “wait channel. The address of an
event on which a particular process is waiting.”


So, let’s start the program and then call `ps -eo pid,wchan:42,cmd` to
get the PID, current waiting channel, and command for each process. (the
42 is so it doesn’t cut off any information)


I actually ran it in a loop (`ps -eopid,wchan:42,cmd; sleep 0.5` so that
I wouldn’t miss anything)


```
$ ps -eo pid,wchan:42,cmd | grep mystery_1.py
2382 sk_wait_data                               python mystery_1.py

```


[The internet](http://askubuntu.com/questions/19442/what-is-the-waiting-channel-of-a-process)
tells us that `sk_wait_data` means “Wait for some data on a network
socket.”. So it seems likely that it’s slow because it’s waiting for a
network response! AWESOME.


You can see [the source for mystery_1.py](https://github.com/jvns/swiss_army_knife_talk/blob/master/slow_client.py) if you want to know what it’s actually doing.


## Mystery Program #2


`time`, again, is a great place to start.


```
$ time python mystery_2.py
2.74user 0.00system 0:02.74elapsed 99%CPU (0avgtext+0avgdata 18032maxresident)k

```


This program is spending all of its runtime on the CPU (2.74/2.74
seconds), and it’s all in user functions. The operating system won’t
have anything new to tell us here (no IO! No network!), and since it’s
Python (and not, say, C++) it’s actually going to be best to just use a
Python profiler.


It’s important to know when you *shouldn’t* use fancy operating systems
tools to debug performance, and I think this is one of those cases.


You can see [the source for mystery_2.py](https://github.com/jvns/swiss_army_knife_talk/blob/master/adder.py)
if you want to know what it’s actually doing.


## Mystery program #3


```
time python mystery_3.py 
0.08user 1.03system 0:10.61elapsed 10%CPU (0avgtext+0avgdata 18176maxresident)k

```


This one is waiting for 9 seconds. What’s going on?! I actually
originally thought I understood this one but I TOTALLY DIDN’T.


To thicken the plot, if we run the program twice in a row, it takes
drastically different amounts of time:


```
$ time python mystery_3.py 
0.01user 0.40system 0:00.61elapsed 69%CPU (0avgtext+0avgdata 18176maxresident)k
0inputs+585944outputs (0major+1239minor)pagefaults 0swaps
$ time python mystery_3.py 
0.01user 0.34system 0:10.55elapsed 3%CPU (0avgtext+0avgdata 18176maxresident)k
24inputs+585944outputs (0major+1238minor)pagefaults 0swaps

```


It just went from 0.6 seconds to 10 seconds! What in the world is going on?


I tried this `wchan` trick again, and ran our mystery program a few times


```
$ for i in `seq 1 100`
do
    ps -eo pid,wchan:42,cmd | grep mystery_3; sleep 0.5
end

11285 -                                          python mystery_3.py
11285 sleep_on_buffer                            python mystery_3.py
11285 sleep_on_buffer                            python mystery_3.py
11285 sleep_on_buffer                            python mystery_3.py
11410 sleep_on_page                              python mystery_3.py
11438 sleep_on_shadow_bh                         python mystery_3.py

```


All of this buffer and page business is enough for me to conclude that
there’s **something** going on with IO. But what, and why does it run so
much more slowly the second time? I was actually totally confused about
this, even though I knew what the program was doing.


Here’s the program. It’s writing 287MB to `/tmp/fake.txt`.


```
line = 'a' * 30000
filename = '/tmp/fake.txt'

with open(filename, 'w') as f:
    for i in xrange(10000):
        f.write(line)

```


The whole point of this exercise is to debug using our operating system,
so we need to get a better picture of what the OS is doing! Let’s use
`dstat`, which gives us snapshots every second of what network, IO, and
CPU activity is happening (SO GREAT)


```
$ dstat
----total-cpu-usage---- -dsk/total- -net/total- ---paging-- ---system--
usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw 
 14   5  78   3   0   0|  46k  342k|   0     0 |   0  1629B| 374  1282 
  3   1  95   1   0   0|   0   232k|   0     0 |   0     0 | 606  2807 
  3   2  95   0   0   0|   0     0 | 164B  204B|   0     0 | 444  2093 

```


I’m going to just show you the disk stats using `dstat -d` for clarity. It prints a new line every second.


```
$ dstat -d 
-dsk/total-
 read  writ
   0   136k
   0    56M <-- when I start python mystery_3.py. It finishes immediately
   0    46M <-- but it's still writing data!
   0    32M <-- still writing...
   0    52M <-- still writing...
   0    70M <-- still writing...
   0    32M <-- still writing...
   0   148k <-- okay it's done
   0     0 
   0   144k
   0     0 
   0   144k^

```


So we see that the OS is writing data even after the program is
finished. For 5 whole seconds! This was when a lightbulb went off in my
head going OH FILESYSTEM CACHES RIGHT. Writing to disks is **super
slow**, and the kernel loves you and wants you to not have to wait. So
it says “okay, got it!”, but doesn’t actually write the data to disk
until a little later.


When the filesystem cache runs out of space, it says “okay you need to
stop writing now” and actually writes the data to disk and makes you
wait until it’s done. Of course, sometimes you want your data to be
*actually for serious written before you keep on going (for example if
you’re a database!!). This is why the second run of our program takes so
long! It needs to wait for the writes from the previous run to finish,
and also catch up on its own.


[Kamal](https://twitter.com/kamalmarhubi) wisely suggested that I could
force the kernel to do finish all the writes before the program
finishes:


```
import os
line = 'a' * 30000
filename = '/home/bork/fake.txt'

with open(filename, 'w') as f:
    for i in xrange(10000):
        f.write(line)
    f.flush()
    os.fsync(f.fileno())

```


```
time python writes2.py 
0.02user 0.32system 0:06.70elapsed 5%CPU (0avgtext+0avgdata
18192maxresident)k

```


Surprise: it takes about 6.5 seconds. every time. Which is exactly what
we’d expect from looking at our dstat output above! I have other
Serious Questions about why my hard drive only writes at 40MB/s but that
will be for another time.


## All of the performance tools


I got SO MANY ANSWERS. holy crap you guys. I’m going to write down every
tool someone recommended here so I don’t forget them, though you can
also just [read the Twitter replies](https://twitter.com/b0rk/status/576883056864288768).

- `nethogs`, `nettop`, and `jnettop` for network performance
- `iotop` is top, but for IO! Awesome!
- `iostat` and `lsof` too for seeing what’s up with IO and files right now
- `top` and `htop` for CPU stats, of course (pro tip: use htop instead of top)
- `strace` because [we <3 strace](http://jvns.ca/categories/strace/)
- `perf` is [a magical tool that can do anything](http://www.brendangregg.com/perf.html)
- `atop` which I don’t even understand what it is
- `pidstat` is an amazing program for looking at both CPU and disk activity which we’re going to explain a little more later
- `ps xaopid,wchan:42,cmd` is this amazing `ps` incantation [Aria Stewart](https://twitter.com/aredridel) told me which tells you what *every process is currently doing*. whoa.
- vmstat which I’m not totally sure what it is yet
- `dstat` is like iotop and nethogs and top all rolled into one and I’m
super into it.
- [Brendan Gregg’s great picture of Linux observability tools](http://www.brendangregg.com/Perf/linux_observability_tools.png)
which is awesome as a reference but honestly I have a really hard time learning new things from it. I need examples!


Twitter is the bomb and I learned about at least 5 awesome tools I
hadn’t heard of before (nethogs, iotop, pidstat, dstat, and this `ps -eo wchan` business)


### that’s all for now!


I’m working on a talk about this for PyCon 2015 next month, so there
should be more posts along these lines coming your way :) :) :)


many many thanks to Aria Stewart, Brendan Gregg, Kamal Marhubi, and
others for telling me about some of these amazing tools!
