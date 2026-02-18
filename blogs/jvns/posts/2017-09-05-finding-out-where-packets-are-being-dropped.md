---
title: "Finding out if/why a server is dropping packets"
date: 2017-09-05
url: https://jvns.ca/blog/2017/09/05/finding-out-where-packets-are-being-dropped/
slug: finding-out-where-packets-are-being-dropped
word_count: 539
---


When packets are being dropped on a computer, they’re being dropped for
a *reason*. How do you find out whether/why packets are being dropped?


Here’s the situations we want to understand:

1. a packet enters the network stack of your computer (`RX`) (say on
port 8000). It gets dropped before the application listening on port
8000 receives it.
2. you send a packet (`TX`). Before it makes it out of your computer, it
gets dropped.


I’m not interested here in “packets are being dropped somewhere else on the
internet, let’s diagnose it with traceroute / by counting TCP retransmits”
(though that’s important too!)


### how do you even know if packets are being dropped?


I asked on Twitter and got the very useful answer “look at `netstat -i`!”
Here’s what that looks like on my laptop:


```
bork@kiwi~> sudo netstat -i
Kernel Interface table
Iface       MTU Met   RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
docker0    1500 0         0      0      0 0             0      0      0      0 BMU
enp0s25    1500 0   1235101      0    242 0        745760      0      0      0 BMRU
lo        65536 0     21558      0      0 0         21558      0      0      0 LRU
nlmon0     3776 0    551262      0      0 0             0      0      0      0 ORU

```


It looks like there are some received (`RX`) packets being lost on `enp0s25`
(my wireless card). No `TX` packets lost though!


Someone also told me that running `ethtool -S` is useful but my ethtool doesn’t have a `-S` option.


### how do you know **why** packets are being dropped


I was googling and I found this cool tool called `dropwatch`. There isn’t any Ubuntu package for it but it’s on github: [https://github.com/pavel-odintsov/drop_watch](https://github.com/pavel-odintsov/drop_watch).


Here are the instructions that worked for me to compile it:


```
sudo apt-get install -y libnl-3-dev libnl-genl-3-dev binutils-dev libreadline6-dev
git clone https://github.com/pavel-odintsov/drop_watch
cd drop_watch/src
vim Makefile # comment out the -Werror argument to gcc
make

```


And here’s the output! It tells me at which kernel function I’m losing packets. Cool!


```
sudo ./dropwatch -l kas
Initalizing kallsyms db
dropwatch> start
Enabling monitoring...
Kernel monitoring activated.
Issue Ctrl-C to stop monitoring

1 drops at tcp_v4_do_rcv+cd (0xffffffff81799bad)
10 drops at tcp_v4_rcv+80 (0xffffffff8179a620)
1 drops at sk_stream_kill_queues+57 (0xffffffff81729ca7)
4 drops at unix_release_sock+20e (0xffffffff817dc94e)
1 drops at igmp_rcv+e1 (0xffffffff817b4c41)
1 drops at igmp_rcv+e1 (0xffffffff817b4c41)

```


### monitoring dropped packets with perf


Here’s another cool way to debug what’s happening!


[thomas graf](https://twitter.com/tgraf__) told me that you can monitor the
`kfree_skb` event using perf, and that will tell you when packets are being
dropped (where in the kernel stack it happened):


```
sudo perf record -g -a -e skb:kfree_skb
sudo perf script

```


### advanced reading


There’s also these two cool articles:

- [Monitoring and Tuning the Linux Networking Stack: Receiving Data](https://blog.packagecloud.io/eng/2016/06/22/monitoring-tuning-linux-networking-stack-receiving-data/)
- [Monitoring and Tuning the Linux Networking Stack: Sending Data](https://blog.packagecloud.io/eng/2017/02/06/monitoring-tuning-linux-networking-stack-sending-data/)


I still haven’t read them in full but they are extremely detailed and cool.


### tell me if you know more!


I still haven’t ever used these tools to seriously debug a packet loss problem
yet, just wanted to write this down so that I have the notes if I do want to in
the future!


If you have better tips for debugging whether/why packets are being dropped on
a computer, let me know!
