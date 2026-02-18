---
title: "A few spy tools for your operating system (other than strace!)"
date: 2015-04-06
url: https://jvns.ca/blog/2015/04/06/a-few-spy-tools-for-your-operating-system-other-than-strace/
slug: a-few-spy-tools-for-your-operating-system-other-than-strace
word_count: 983
---


There are *so many* awesome tools you can use to find out what’s going on with
your computer. Here are some that exist on Linux. They might exist on your OS
too!


### netstat


netstat tells you what ports are open on your computer. This is crazy useful if
you want to know if the service that is *supposed* to be listening on port 8080
is *actually* listening on port 8080.


```
sudo netstat -tulpn
[sudo] password for bork: 
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address       Foreign Address     State       PID/Program name
tcp        0      0 127.0.0.1:631       0.0.0.0:*           LISTEN      1658/cupsd      
tcp        0      0 127.0.0.1:5432      0.0.0.0:*           LISTEN      1823/postgres   
tcp        0      0 127.0.0.1:6379      0.0.0.0:*           LISTEN      2516/redis-server

```


If you look at the Program Name column on the right, you’ll see that
apparently I have cupsd (printing), postgres, and redis servers running
on my machine, as well as some other stuff that I redacted. I actually
have no idea why I had redis installed so uh yeah I uninstalled it.


I use netstat pretty often when I’m trying to debug “omg why is this
thing not running IT IS SUPPOSED TO BE RUNNING”. netstat tells me the
truth about whether it is running.


### dstat


Want to know how much data is actually being written to your physical hard
drive right this second? YEAH YOU DO. dstat knows that. It prints a row every
second with stats for that second. I love dstat because it’s so simple.


```
----total-cpu-usage---- -dsk/total- -net/total- ---paging-- ---system--
usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw 
 32  38  30   0   0   0|  28k   81k|   0     0 |   4B  123B| 441  2184 
 12  29  59   0   0   0|   0   184k|  66B   86B|   0     0 |1428  6031 
  9  26  65   0   0   0|   0   576k| 518B  528B|   0     0 |1157  4611 
  9  25  66   0   0   0|   0   144k|   0     0 |   0     0 |1100  5249 
 14  27  59   0   0   0|   0     0 |  60B    0 |   0     0 |1001  4285 
  9  29  62   0   0   0|   0   180k| 122B   82B|   0     0 |1166  5416

```


### lsof


lsof tells you which files every process has open right now! That’s all!
It is awesome the same way dstat and netstat are awesome – you want to
know what files are open right now, it tells you what files are open
right now, you’re done <3.


It can also tell you what position in the file the process is at, so you
can find out what kind of progress it’s making reading the file.


### ngrep / tcpdump


Okay now we’re moving from “super simple tool that does one thing” to
“tcpdump that has a billion options and also this whole BPF berkeley
packet filter business and what is this filter language even”. So I’m
not going to explain how to use tcpdump because I don’t even really
know.


Let’s say you want to

- reverse engineer a protocol
- find out if there’s *really* terrible latency or if everything is slow for some other reason
- debug why your POST request is formatted wrong in a world before google chrome dev tools


To do all of this, you need to spy on network activity! ngrep and tcpdump
capture packets, let you filter them, and show you what you’re looking for. I’m
not going to explain how to use them here but [this ngrep tutorial](http://dl.packetstormsecurity.net/papers/general/ngreptut.txt) looks
pretty useful. If you’re looking at output from tcpdump you should probably
dump it to a pcap file and use Wireshark to look at it instead. Wireshark is
the best and way easier to understand because it’s a GUI and it makes
everything pretty for you.


as always with these systems tools, ngrep / tcpdump will tell you The Truth™
about what’s going on on your network.


If you want to know how people use tcpdump, you should read [the replies to this tweet “do you use tcpdump in your day-to-day life? what do you use it for?”](https://twitter.com/b0rk/status/585234410980712448) because the people
who follow me on twitter are the best. Really go read them! There is so much
interesting stuff there.


### opensnoop & ftrace


Do you want to know every file your system is opening right now? There’s a
script in Brendan Gregg’s
[perf-tools](https://github.com/brendangregg/perf-tools) collection that does
that!


I’m mostly including this as an example to show that a lot of stuff is
*possible* to know – the scripts in that repo don’t work with every Linux kernel
version (I needed to [modify it](https://github.com/brendangregg/perf-tools/pull/24)
to get it to work with Linux 3.13). But they use a tracing framework in
the Linux kernel called ‘ftrace’ that can tell you all *kinds* of stuff.


ftrace seems like quite a bit of work to learn how to use, but also really
powerful. Basically you access it by doing various things to files in
`/sys/kernel/debug/tracing`, or by using a wrapper command called
`trace-cmd`. It’s all built into Linux!


### atop


atop is like top, but it shows you more stuff and you need to run it as
root. So it’ll show me the CPU & memory usage for each process, but also
how much disk & network I/O it’s doing. It’s neat and a little
terrifying to look at at first (SO MANY NUMBERS).


### wow


That’s all for now! If you have other tools you frequently reach for
when trying to figure out what’s going on on your system, I’d be
interested to know what they are. [@b0rk](https://twitter.com/b0rk) on
Twitter, as always :)


an aside – I’ve been thinking about man pages recently, and how you can
read the man page for tcpdump and understand individually all the words,
but it’s not a substitute for someone telling you an Awesome Story about
how they used tcpdump to debug an intermittent certificate problem or a
DNS problem and then they Saved the Day.
