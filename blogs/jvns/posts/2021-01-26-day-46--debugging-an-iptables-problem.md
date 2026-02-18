---
title: "Day 46: debugging an iptables problem"
date: 2021-01-26
url: https://jvns.ca/blog/2021/01/26/day-46--debugging-an-iptables-problem/
slug: day-46--debugging-an-iptables-problem
word_count: 618
---


I spent a lot of my brain energy yesterday debugging an iptables mystery.


### the iptables mystery


I needed to be able to ping the host’s IP (like `192.168.1.23`) from inside a
container. This was working 100% totally fine on my laptop. Then I tried the
exact same thing on my server, and it didn’t work at all!


At first I thought that maybe I didn’t understand something about how bridges
work, and I spent some time reading about bridges. I think I learned a tiny bit
more about bridges but this didn’t really help.


Then Kamal said “well, maybe it’s iptables” and so I spent some time looking
into that. I really didn’t think it was iptables because I didn’t think there
were any special iptables rules except the Docker rules, and the Docker rules
were working fine on my laptop.


### some adventures in iptables tracing


I tried to trace some specific iptables rules that I thought might potentially
be the problem (with `-j TRACE`) following this very good blog post [How do I see what iptables is doing? ](https://www.opsist.com/blog/2015/08/11/how-do-i-see-what-iptables-is-doing.html)


This ultimately didn’t really help, but at some point that blog post suggested
running `iptables -L -n -v --line-numbers` and I noticed something!!!


### what was happening: iptables was dropping some packets


When I ran `iptables -L -n -v` and I saw something like this:


```
$ iptables -L -n -v 
Chain INPUT (policy DROP 2 packets, 120 bytes)
 pkts bytes target     prot opt in     out     source               destination         
   18  1288 ufw-before-logging-input  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
   18  1288 ufw-before-input  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
    2   120 ufw-after-input  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
    2   120 ufw-after-logging-input  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
    2   120 ufw-reject-input  all  --  *      *       0.0.0.0/0            0.0.0.0/0           
    2   120 ufw-track-input  all  --  *      *       0.0.0.0/0            0.0.0.0/0         

```


`policy DROP 2 packets`! That is suspicious! I double checked that this was
100% definitely the problem by running `iptables -Z` to reset all of iptables'
counts and tried again. Same result! Hooray!


I looked into these `ufw` rules and I found out that `ufw` is a firewall that
often gets installed in Ubuntu machines. I tried to track down which exact rule
was causing the problem, but I didn’t really figure it out.


But I tried completely disabling the firewall with `ufw disable`, and it fixed the problem!


### solution: disable the ufw firewall


DigitalOcean comes with an external firewall anyway and I didn’t really see why
I also needed an extra iptables firewall running on my machine, so I decided to just
run `ufw disable` to disable that firewall completely.


I added some extra rules to the external firewall to block all TCP ports except
22 and 80.


### some experiments with ignite


On the weekend I spent some time experimenting with reimplementing my
Firecracker VM API using [ignite](https://github.com/weaveworks/ignite).


So far I’ve learned that:

- ignite turns Docker containers into VM images
- it uses `dmsetup` to set up a device mapper so that it doesn’t need to make a copy of the image every time it starts a VM
- this *doesn’t* mean that 2 images that share some container layers share space on disk though – for every different tag it makes a copy of the whole image


I wrote a hacky HTTP API [ignite-manager.go](https://gist.github.com/jvns/67841b47ec7e4bf5f27c0e0389cbcd92) that just
shells out to the ignite command line tool a lot.


### working on startup speed


Right now the Ignite VMs are taking 15-20 seconds to start on my DigitalOcean
droplet.  I think this is kind of too slow (I want to be done in 5 seconds at
most!) so I’m going to spend some more time learning about this device mapper
thing.
