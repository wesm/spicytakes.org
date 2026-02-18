---
title: "Day 41: Trying to understand what a bridge is"
date: 2021-01-19
url: https://jvns.ca/blog/2021/01/19/day-41--trying-to-understand-what-a-bridge-is/
slug: day-41--trying-to-understand-what-a-bridge-is
word_count: 1274
---


Hello! Yesterday I spent a lot of time trying to understand what a bridge is so
here are my notes. I’m only going to talk about bridges as applied to
container / VM networking because that’s what I’m trying to do and also I’ve
also never seen a bridge used for anything else.


Some things in this post are almost certainly wrong.


### why I’m doing this: trying to set up Firecracker networking


I’ve been setting up some VMs using AWS Firecracker (which is amazing and lets
you start up VMs in like ONE SECOND, it’s extremely fast, and I will write
about it in the future because I really love it). Yesterday morning
I was trying to configure the VM’s networking so that I could connect to the
outside internet from inside the VM. I was googling how to do it and there were
all these references to “make a bridge”, so I figured I needed to use a bridge.


I’ve been avoiding understanding what a bridge is for years because it seemed
confusing, but I copied and pasted some things from Github issues / various
blog posts and none of them did what I wanted.


So I figured the “blindly copy and paste” approach wasn’t really going to work
and decided OKAY TODAY IS THE DAY I WILL LEARN WHAT A BRIDGE IS.


I’m going to use a bunch of Docker examples in this post even though I’m not
planning to use Docker because it’s already set up on my computer, it basically
does what I want to do (but using a veth instead of a tap device), and I’m more familiar with it.


### some blog posts that helped me


I asked on Twitter for help understanding Docker container networking and
people linked me to 2 really good blog posts that helped me:

- [container networking is simple](https://iximiuz.com/en/posts/container-networking-is-simple/) is a
very clear explanation of how docker’s default container networking works
with great examples
- [Tracing a packet journey using Linux tracepoints, perf and eBPF](https://blog.yadutaf.fr/2017/07/28/tracing-a-packet-journey-using-linux-tracepoints-perf-ebpf/)
explains how to use `perf trace` an eBPF. The perf trace example in
particular is super easy to use and it helped me feel more confident about
what was going on


### a bridge is a layer 2 network interface


One thing I learned is that a bridge is a layer 2 (ethernet) device that can
have an arbitrary number of network interfaces attached to it.


My understanding of how it works is:

1. You send a packet to the bridge
2. If the bridge has a network interface attached to it with a MAC address
matching the destination MAC address on your packet, it sends it to that
network interface
3. if there’s no matching interface or the packet is a broadcast packet (?)
then it sends it to all of the interfaces


### tap devices and veths are also layer 2 devices


Docker uses veth pairs and the VM setup I’m using right now is using taps.
These are also both layer 2 network interfaces. So they just sort of send
packets on blindly and something else is responsible for setting the correct
MAC addresses on packets.


### your computer finds container MAC addresses with ARP


One question I had was – if you’re sending a packet to a container and it
needs to have the right MAC address on it to make it through the bridge, how
does it know what the right MAC address is? I think the answer is the same as
in a physical network: ARP!


So your computer sends an ARP request like “hey who’s 172.17.0.8” and the
container sends an ARP reply back like “it’s me! here’s my MAC address”. The
bridge gets involved here because it needs to send the ARP request to the container and the ARP reply back to the host.


I’m not 100% sure about this but I saw some ARP requests/replies being sent
back and forth and it makes sense. I think this is really funny because – all
of this information is on the same computer and it doesn’t feel like it should
need to use ARP to look up MAC addresses, like it has all the information
already! But I guess it just literally pretends like it’s a physical network.


### you need to set up the route table correctly


I think the most important thing with bridges is to set up the route tables
correctly. So far my understanding is that there are 2 route table entries you
need to set:


**route entry 1: on the host**


The first route entry that needs to be set is on the host, to make sure that
everything on the bridge subnet gets sent to the bridge. Here’s what that looks
like in Docker’s default networking setup.


```
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 

```


**route entry 2: inside the container/VM**


In the container/VM, the system’s *gateway* needs to be set to the bridge


For example, in a Docker container, you’ll see this:


```
$ ip route list
default via 172.17.0.1 dev eth0 
172.17.0.0/16 dev eth0 proto kernel scope link src 172.17.0.2 

```


This `default via 172.17.0.1 dev eth0`  line means that all packets going
outside the container subnet should be first sent to 172.17.0.1, which is the
`docker0` bridge (actually it’s a veth pair which leads to the docker0 bridge)


### you need an SNAT rule on the host


The third thing I need if I want the containers to be able to talk to the wider
internet is an SNAT iptables rule on the host. Here’s what that looks like in Docker’s default setup.


```
$ sudo iptables-save
-A POSTROUTING -s 172.17.0.0/16 ! -o docker0 -j MASQUERADE

```


### now I can access the internet from my VM!


I’m still not 100% on bridges but I *did* manage to configure a bridge so that
when I ssh into my Firecracker VM I can access the internet! I am extremely delighted by this.


Right now I’m reusing the `docker0` bridge which I’ll probably stop doing, but
it does work.


My understanding of all the steps to get a Docker-like setup where you can access a VM and it can access the outside internet are:

1. create the VM network interface (either a `tap` device or a veth) (`ip tuntap add dev "$TAP_DEV" mode tap`)
2. put the VM network interface behind the bridge (`sudo brctl addif docker0 $TAP_DEV`)
3. bring up the VM network interface (`ip link set dev "$TAP_DEV" up`)
4. set the VM’s gateway to be the bridge IP (via the kernel boot args, which I talk about below)
5. setup the host’s route table to route packets on the bridge’s subnet to the bridge (I think I’d do this when creating the bridge, which I didn’t do in this case because I’m reusing the docker bridge)
6. add an SNAT rule to the host to NAT packets coming out of the bridge (with `iptables`)
7. Change `/etc/resolv.conf` to say `nameserver 8.8.8.8` because I don’t have a working local resolver inside the VM


Here’s a snippet from my script that starts a firecracker VM. I modified it from the [firecracker-demo](https://github.com/firecracker-microvm/firecracker-demo) code.


I might post the whole thing later after I clean it up and stop using the docker bridge.


```
CONTAINER_IP=172.17.0.33
GATEWAY_IP=172.17.0.1
DOCKER_MASK_LONG=255.255.255.0
ip tuntap add dev "$TAP_DEV" mode tap
sudo brctl addif docker0 $TAP_DEV
ip link set dev "$TAP_DEV" up
# I'm not sure what these two are for exactly
sysctl -w net.ipv4.conf.${TAP_DEV}.proxy_arp=1 > /dev/null
sysctl -w net.ipv6.conf.${TAP_DEV}.disable_ipv6=1 > /dev/null

```


I also had to set `ip=${CONTAINER_IP}::${GATEWAY_IP}:${DOCKER_MASK_LONG}::eth0:off` in the kernel boot args. to set the VM’s gateway.
