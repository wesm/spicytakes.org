---
title: "What's a network interface?"
date: 2017-09-03
url: https://jvns.ca/blog/2017/09/03/network-interfaces/
slug: network-interfaces
word_count: 1233
---


I’ve been working with container networking a bunch this week. When learning
about new unfamiliar stuff (like container networking / virtual ethernet
devices / bridges / iptables), I often realize that I don’t fully understand
something much more fundamental.


This week, that thing was: network interfaces!!


You know, when you run `ifconfig` and it lists devices like `lo`, `eth0`,
`br0`, `docker0`, `wlan0`, or whatever. Those.


This is a thing I **thought** I understood but it turns out there are at least
2 things I didn’t know about them.


I’m not going to try to give you a crisp definition, instead we’re going to
make some observations, do some experiments, ask some questions, and make some
guesses.


### What happens if you don’t have any network interfaces?


I was messing around with network namespaces, and I created a new one with:


`sudo ip netns add ns1`


It turns out that when you create a new network namespace, it doesn’t have any
network interfaces at all! What does that mean?  Let’s explore and see what it
looks like:


We can run commands inside this new network namespace with `sudo ip netns exec ns1 COMMAND`. I’m just going to run a shell inside this network namespace, and then
try out some things.


So let’s start with `sudo ip netns exec ns1 bash`


```
$ sudo ip netns exec ns1 bash
$ ifconfig
(no output)

```


That makes sense, this is a new network namespace so there are no network
interfaces set up yet. Still inside that network namespace, let’s try to make a
webserver and connect to it.


```
$ nc -l 8900 & # make a server on port 8900
$ netstat -tulpn # list open ports
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address   PID/Program name
tcp        0      0 0.0.0.0:8900    2918/nc 
$ curl localhost:8900
curl: (7) Couldn't connect to server

```


Okay, so this is sort of interesting. I can create a server on port 8900 with
`nc -l 8900`. And netstat shows that that server exists. But when I try to
`curl localhost:8900`, nothing happens!


What if I try to create a server listening on 127.0.0.1?


```
sudo nc -l 127.0.0.1 8080
nc: Cannot assign requested address

```


Doesn’t work. Makes sense.


I think what’s happening here is:

- `nc -l 8900` is listening on 0.0.0.0:8900, which means “all network interfaces”
- but there are no network interfaces
- so when we do `curl localhost:8900`, no packets actually get sent (when I ran tcpdump, no packets show up)
- so `nc` never receives any packets


Let’s do an experiment to try to confirm our hypotheses: let’s add a network
interface! The idea is that if we have a `lo` network interface, then `curl localhost:8900` will actually send packets, `nc` will receive them, and
everything will work.


```
$ ip link set dev lo up # this sets uo the 'lo' loopback interface
$ curl localhost:8900                                                                               
# BAM! this totally works! 
# the backgrounded netcat prints out this output:
GET / HTTP/1.1
User-Agent: curl/7.35.0
Host: localhost:8900
Accept: */*

```


This is rad. What we know now:

- if you don’t have any network interfaces, you can’t do any networking (but you can start servers on 0.0.0.0 and netstat shows those servers)
- when we add a network interface, our server starts working right away (without having to restart the server)


### A packet can appear multiple times in tcpdump


Something I’ve been observing recently but haven’t fully understood is – sometimes I’ll be on a machine which has

- virtual network interfaces for each container (`vethXXXXXXX`)
- a bridge interface (`cni0`)
- and a “real” network interface to the outside world (`eth0`)


When containers send packets to the outside world and I’m running `sudo tcpdump -i any`, I’ll see those packets **3 times**.


I know a few more things about how tcpdump works:

1. I can run `sudo tcpdump -i cni0` to listen on a specific interface. When I do that, the packets appear only once
2. tcpdump happens at the “beginning” of the network stack. I think that means that packets are captured by tcpdump when packets enter a network interface


What does “enter a network interface” actually mean, though? I tried to look at
[this 20,000 word article on the linux network stack](https://blog.packagecloud.io/eng/2016/06/22/monitoring-tuning-linux-networking-stack-receiving-data/)
and I think I have a workable theory!


### What happens when a packet is created?


Okay, so I skimmed [Monitoring and Tuning the Linux Networking Stack: Receiving Data](https://blog.packagecloud.io/eng/2016/06/22/monitoring-tuning-linux-networking-stack-receiving-data/) and I think I have a working hypothesis for how packets

- get assigned network interfaces
- get captured by tcpdump
- can be assigned more than one network interface


First thing first, this document refers to “network interfaces” as “network devices”. I think those are the same thing.


So!! Let’s say I create a packet on my computer.


**step 0**: iptables prerouting rules


**step 1**: the packet gets **routed**.


Routing a packet means “assigning it a network device”.


Let’s do a tiny experiment in routing – I have 3 interfaces on my computer right now


```
$ ifconfig
docker0   Link encap:Ethernet  HWaddr 02:42:ef:ab:0d:ac  
          inet addr:172.17.0.1  Bcast:0.0.0.0  Mask:255.255.0.0

enp0s25   Link encap:Ethernet  HWaddr 3c:97:0e:55:b3:7g  
          inet addr:192.168.1.213  Bcast:192.168.1.255  Mask:255.255.255.0

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0

```


and here are the routes:


```
$ sudo ip route list table all
default via 192.168.1.1 dev enp0s25  proto static  metric 100 
169.254.0.0/16 dev docker0  scope link  metric 1000 linkdown 
172.17.0.0/16 dev docker0  proto kernel  scope link  src 172.17.0.1 linkdown 
192.168.1.0/24 dev enp0s25  proto kernel  scope link  src 192.168.1.213  metric 100 
local 127.0.0.0/8 dev lo  table local  proto kernel  scope host  src 127.0.0.1 
local 127.0.0.1 dev lo  table local  proto kernel  scope host  src 127.0.0.1 
local 172.17.0.1 dev docker0  table local  proto kernel  scope host  src 172.17.0.1 

```


So – if I make a request to 172.17.0.1 (`curl 172.17.0.1:8080`), it seems like that would end up on the
`docker0` device. Right? Wrong, apparently.


If I run `tcpdump -i lo` packets to 172.17.0.1 show up, and if I run `tcpdump -i docker0`,
the packets don’t show up. So it seems right now, on my machine,
packets sent to 172.17.0.1 go through the `lo` device.


The reason they get sent to `lo` instead of `docker0` is that there’s a route
for 172.17.0.1  in my route table that says `local` – the same reasons that
packets to `127.0.0.1` get sent to `lo`.


**step 2** tcpdump gets the packet


This is pretty straightforward – once there’s a network device attached to the
packet, then tcpdump gets the packet.


That’s all I know for now!


### ok so what do we know about network interfaces?


Here’s what I think so far:

- they can be physical network interfaces (like `eth0`) or virtual interfaces (like `lo` and `docker0`)
- you can list them with `ifconfig` or `ip link list`
- if you don’t have any network interfaces, your packets don’t enter the linux network stack at all really. To go through the network stack you need network interfaces.
- When you send a packet to an IP address, your **route table** decides which network interface that packet goes through. This is one of the first things that happens in the network stack.
- tcpdump captures packets after they’re routed  (assigned an interface) Though there’s a `PREROUTING` chain in iptables that happens before routing!`


Some of this is probably wrong, let me know what! I’m on Twitter as always ([https://twitter.com/b0rk](https://twitter.com/b0rk))
