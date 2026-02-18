---
title: "Day 6: I wrote a rootkit!"
date: 2013-10-08
url: https://jvns.ca/blog/2013/10/08/day-6-i-wrote-a-rootkit/
slug: day-6-i-wrote-a-rootkit
word_count: 287
---


I made some small improvements on my kernel module from yesterday – I
made it into a rootkit!


What I mean by a “rootkit” is a kernel module that once I put it in my
kernel, any unprivileged user who knows the right incantation can become
root.


Here’s how to use it:


```
bork@kiwi > sudo insmod rootkit.ko
bork@kiwi ~/w/h/kernel-module> echo $$ # PID of my shell
17792
bork@kiwi ~/w/h/kernel-module> echo $$ > /proc/buddyinfo
root@kiwi #

```


THEN I AM ROOT. Basically it takes any integer echoed into
`/proc/buddyinfo` and makes that PID owned by root.


The code is here:
[https://gist.github.com/jvns/6894934](https://gist.github.com/jvns/6894934).
It is pretty short!


## How it works


(disclaimer: all this code is actually copied from [this rootkit here](https://github.com/mfontanini/Programs-Scripts/blob/master/rootkit/rootkit.c)
which I pretty much just read and understood a little. But mine does
less stuff!)


So apparently every file has a `struct file_operations` which controls
what happens when the file is read and written to. For example, if
you’re writing a device driver, the important device driver code goes
there. Since the kernel can do ANYTHING, it can change those file
handlers and do nefarious things.


SO. There’s already a file called `/proc/buddyinfo`. I don’t actually
know what it does. But it’s read-only. The rootkit

1. Gives a `write` file handler to `/proc/buddyinfo`
2. In the handler, get the task with the PID that was written
3. Change the owner of that task to the same owner as PID 1, which is
always `init` and owned by root
4. Print “YOU HAVE BEEN HACKED: Making PID $PID root” to the kernel log.
5. Bwahaha.


Maybe tomorrow I will improve the rootkit so that people can exploit my
computer over the network, not just when they’re logged in.
