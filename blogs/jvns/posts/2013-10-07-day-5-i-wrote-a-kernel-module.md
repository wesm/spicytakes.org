---
title: "Day 5: I wrote a kernel module!!!"
date: 2013-10-07
url: https://jvns.ca/blog/2013/10/07/day-5-i-wrote-a-kernel-module/
slug: day-5-i-wrote-a-kernel-module
word_count: 254
---


I WROTE A KERNEL MODULE. It doesn’t do anything useful or anything, but
still! This is a pretty quick post because there was an awesome talk
today by [Mel Chua](http://blog.melchua.com/) and I need to sleep.


The source for the module is at
[https://gist.github.com/jvns/6878994](https://gist.github.com/jvns/6878994)


It intercepts any incoming packets and prints “Hello packet” to the kernel
log for each one. It uses a the Netfilter framework, which I learned
about from [this document](http://kernelnewbies.org/Networking?action=AttachFile&do=get&target=hacking_the_wholism_of_linux_net.txt).


To install it, you can run:


```
$ make
$ insmod hello-packet.ko

```


and then


```
$ rmmod hello-packet.ko

```


to remove it.


[http://kernelnewbies.org](http://kernelnewbies.org) is a fantastic
resource and I’ve been learning a lot from it.


Some more resources:

- [Instructions for writing a “hello world” kernel module](http://www.thegeekstuff.com/2013/07/write-linux-kernel-module/)
- Some examples if you’re interested in learning about rootkits: [1](http://citypw.blogspot.com/2012/11/simple-gnulinux-kernel-rootkit.html),
[2](http://memset.wordpress.com/2010/12/28/syscall-hijacking-simple-rootkit-kernel-2-6-x/),
[3](http://average-coder.blogspot.com/2011/12/linux-rootkit.html),
[4 (pdf)](http://info.fs.tum.de/images/2/21/2011-01-19-kernel-hacking.pdf)


(I think I’m going to work on writing a rootkit tomorrow. eee.)


Some things I learned along the way:

- You can’t use `malloc` inside the kernel (?!!?). This is because
anything that’s used in the kernel needs to be defined in the kernel,
and `malloc` is in glibc. This seems obvious in retrospect, but kind
of blew my mind
- Similarly, you can’t use anything from glibc in the kernel.
- There are apparently things called `kmalloc` and `vmalloc` that you
can use instead. I don’t know what these are yet.
- It is *really* easy to write a firewall that doesn’t let any packets
in or out – just replace `NF_ACCEPT` with `NF_DROP` in my kernel
module.
