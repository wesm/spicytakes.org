---
title: "Debugging netlink requests"
date: 2017-09-03
url: https://jvns.ca/blog/2017/09/03/debugging-netlink-requests/
slug: debugging-netlink-requests
word_count: 1099
---


This week I was working on a Kubernetes networking problem. Basically
our container network backend was reporting that it couldn’t delete
routes, and we didn’t know why.


I started reading the code that was failing, and it was using a library
called “netlink”. I’d never heard of that before this week.


### what’s netlink?


Wikipedia says:


> Netlink socket family is a Linux kernel interface used for
> inter-process communication (IPC) between both the kernel and
> userspace processes, and between different userspace processes, in a
> way similar to the Unix domain sockets.


The program I was debugging was creating/deleting routes from the route table.
It seems like netlink is capable of doing lots of things (communicate kernel
<-> userspace and userspace <-> userspace), but in this case what was happening
was pretty simple

1. userspace program creates a netlink socket
2. userspace program sends a message with that socket asking the kernel
to delete a route
3. kernel deletes the route (or in our case, fails and returns an error message)


### how to see netlink messages with strace


Let’s create some netlink messages! Luckily this is easy: if we use the
`ip` tool to create and delete a route, it uses netlink.


```
ip route add 172.16.5.0/24 via 127.0.0.1 dev lo
ip route del 172.16.5.0/24 via 127.0.0.1 dev lo

```


Cool, let’s strace it! Here’s the command:


```
strace -s 100 -f -o out -x ip route add 172.16.5.0/24 via 127.0.0.1 dev lo

```


and the output:


```
socket(PF_NETLINK, SOCK_RAW|SOCK_CLOEXEC, NETLINK_ROUTE) = 3
bind(3, {sa_family=AF_NETLINK, pid=0, groups=00000000}, 12) = 0
getsockname(3, {sa_family=AF_NETLINK, pid=13058, groups=00000000},
sendmsg(3, {msg_name(12)={sa_family=AF_NETLINK, pid=0, groups=00000000},
    msg_iov(1)=[{"\x34\x00\x00\x00\x18\x00\x05\x06\x6e\xbc\xac\x59\x00\x00\x00\x00\x02\x18\x00\x00\xfe\x03\x00\x01\x00\x00\x00\x00\x08\x00\x01\x00\xac\x10\x05\x00\x08\x00\x05\x00\x7f\x00\x00\x01\x08\x00\x04\x00\x01\x00\x00\x00",
    52}], msg_controllen=0, msg_flags=0}, 0) = 52
recvmsg(3, {msg_name(12)={sa_family=AF_NETLINK, pid=0,
    msg_iov(1)=[{"\x24\x00\x00\x00\x02\x00\x00\x00\x6e\xbc\xac\x59\x02\x33\x00\x00\x00\x00\x00\x00\x34\x00\x00\x00\x18\x00\x05\x06\x6e\xbc\xac\x59\x00\x00\x00\x00",
    32768}], msg_controllen=0, msg_flags=0}, 0) = 36


```


So we see that it:

- creates the netlink socket & binds to it
- sends a message (`\x34\x00...`)
- receives a response


Okay, but what does that message **say**? Here’s the message again:


```
\x34\x00\x00\x00\x18\x00\x05\x06\x9e\xbc\xac\x59\x00\x00\x00\x00\x02\x18\x00\x00\xfe\x03\x00\x01\x00\x00\x00\x00\x08\x00\x01\x00\xac\x10\x05\x00\x08\x00\x05\x00\x7f\x00\x00\x01\x08\x00\x04\x00\x01\x00\x00\x00

```


Not super understandable, right? Well, luckily there’s a Python tool
that can help us understand it! We’ll save this to a file called
`message`.


### decoding netlink messages with pyroute2


I googled how to decode netlink messages and I found this great page:
[http://docs.pyroute2.org/debug.html](http://docs.pyroute2.org/debug.html).


Decoding my netlink message turned out to be pretty simple: I just had
to run this:


```
pip install pyroute2
wget https://raw.githubusercontent.com/svinota/pyroute2/72e444714f37a313fb15bdb22734e517feefa9e9/tests/decoder/decoder.py
python decoder.py pyroute2.netlink.rtnl.rtmsg.rtmsg message

```


Here’s the output!


```
{'attrs': [('RTA_DST', '172.16.5.0'),
           ('RTA_GATEWAY', '127.0.0.1'),
           ('RTA_OIF', 1)],
 'dst_len': 24,
 'family': 2,
 'flags': 0,
 'header': {'flags': 1541,
            'length': 52,
            'pid': 0,
            'sequence_number': 1504493250,
            'type': 24},
 'proto': 3,
 'scope': 0,
 'src_len': 0,
 'table': 254,
 'tos': 0,
 'type': 1}

```


I don’t understand all of this but we’re just going to focus on this part:


```
{'attrs': [('RTA_DST', '172.16.5.0'),
           ('RTA_GATEWAY', '127.0.0.1'),
           ('RTA_OIF', 1)],

```


The dst and gateway fields are pretty easy to understand there!


### why the program I was debugging wasn’t working


You see this `RTA_OIF` field? This field is a **network interface id**. For
example, on my laptop right now I have 5 network interfaces, numbered 1 through
5. The (correct) message above has `RTA_OIF` set to 1, for the `lo` loopback interface.


```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: enp0s25: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 3c:97:0e:55:b3:7f brd ff:ff:ff:ff:ff:ff
3: wlp3s0: <BROADCAST,MULTICAST> mtu 1500 qdisc mq state DOWN mode DORMANT group default qlen 1000
    link/ether 60:67:20:eb:7b:bc brd ff:ff:ff:ff:ff:ff
4: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default 
    link/ether 02:42:a0:c5:c1:be brd ff:ff:ff:ff:ff:ff
5: nlmon0: <NOARP,UP,LOWER_UP> mtu 3776 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1
    link/netlink 

```


But in our errant program, the `RTA_OIF` field was set to 0! 0 is not even a
valid value for this field, I don’t think! (0 is not a valid network interface ID)


### pyroute2 is great


pyroute2 is really cool, if I wanted to write a quick script to understand
what’s going on with my network interfaces & routes I would 100% definitely try
pyroute2. There are a lot of [great examples here](http://docs.pyroute2.org/general.html#rtnetlink-sample).


For example! If I want to run the equivalent of `ip route add 172.16.5.0/24 via 127.0.0.1 dev lo`, that’s:


```
from pyroute2 import IPRoute
ip = IPRoute()
ip.route('add',
         dst='172.16.0.0/24',
         gateway='127.0.0.1',
         oif=1)

```


Super simple! `oif=1` means the same as `dev lo`.


### other ways to capture netlink messages: tcpdump + wireshark


You can also use tcpdump to capture netlink messages! here’s how:


```
# create the network interface
sudo ip link add  nlmon0 type nlmon
sudo ip link set dev nlmon0 up
sudo tcpdump -i nlmon0 -w netlink.pcap # capture your packets
wireshark netlink.pcap # look at the results with wireshark

```


I tried this but had trouble for a couple reasons

1. It didn’t work for me on the server I was working on (though it works on my laptop now)
2. I actually found it harder to work with than the strace method – it captured too many packets and I found it hard to filter them in Wireshark.


### ip monitor


You can also run `ip monitor` and it’ll tell you some netlink requests. when I run it it prints out this stuff:


```
$ sudo ip monitor
fd68:29:f8f6::1 dev enp0s25 lladdr c4:6e:1f:95:d8:3e router STALE
fe80::c66e:1fff:fe95:d83e dev enp0s25 lladdr c4:6e:1f:95:d8:3e router STALE
192.168.1.144 dev enp0s25 lladdr 14:30:c6:ba:e4:6c STALE
192.168.1.144 dev enp0s25 lladdr 14:30:c6:ba:e4:6c PROBE
192.168.1.144 dev enp0s25 lladdr 14:30:c6:ba:e4:6c STALE
192.168.1.144 dev enp0s25 lladdr 14:30:c6:ba:e4:6c REACHABLE
fd68:29:f8f6::1 dev enp0s25 lladdr c4:6e:1f:95:d8:3e router PROBE
fd68:29:f8f6::1 dev enp0s25 lladdr c4:6e:1f:95:d8:3e router REACHABLE
fe80::c66e:1fff:fe95:d83e dev enp0s25 lladdr c4:6e:1f:95:d8:3e router PROBE
fe80::c66e:1fff:fe95:d83e dev enp0s25 lladdr c4:6e:1f:95:d8:3e router REACHABLE

```


It didn’t give me the information I wanted though.


### nltrace


There’s also [nltrace](https://github.com/socketpair/nltrace) (for instance `nltrace ip route list`) but in this case it didn’t give me the information I wanted. It’s not a maintained project but looks maybe useful!


### that’s all!


It always makes me happy when I learn about a NEW LINUX THING during the course
of my job. When I was in the middle of this I tweeted


> kubernetes is cool but definitely not easy, my experience is definitely like
> “learn how all the networking works in excruciating detail”


which definitely feels true, it’s less like “set up networking and it works”
and more like “pick a networking backend, wait a month, discover weird
problems, strace it, learn things about netlink and what a `RTA_OIF` is, fix
the bugs, eventually it works”. Maybe that isn’t everyone’s experience but that
is my experience so far!
