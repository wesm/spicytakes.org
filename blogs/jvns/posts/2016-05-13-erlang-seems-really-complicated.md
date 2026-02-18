---
title: "Investigating Erlang by reading its system calls"
date: 2016-05-13
url: https://jvns.ca/blog/2016/05/13/erlang-seems-really-complicated/
slug: erlang-seems-really-complicated
word_count: 731
---


I was helping debug a performance problem (this [networking puzzle](https://gist.github.com/jvns/c7e277c7a44e22ce5a6e5707febcfbf3)) in an Erlang program yesterday. I learned that Erlang is complicated, and that we can learn maybe 2 things about it by just looking at what system calls it’s running.


Now – I have never written an Erlang program and don’t really know anything about Erlang, so “Erlang seems complicated” isn’t meant as a criticism so much as an observation and something I don’t really understand. When I’m debugging a program, whether I know the programming language it’s written in or not, I often use strace to see what system calls it runs. In my few experiments so far, the Erlang virtual machine runs a TON of system calls and I’m not sure exactly what it’s doing. Here are some experimental results.


I write 4 programs: hello.c, hello,java, hello.erl, and hello.py. Here they are.


```
#include <stdio.h>
int main() {
    printf("hello!\n");
}

```


```
class Hello {
    public static void main(String[] args)  {
        System.out.println("hello!");
    }
}

```


```
-module(hello).
-export([hello_world/0]).

hello_world() ->
    io:fwrite("Hello, world!\n").⏎ 

```


```
print "hello"

```


Here are the number of system calls each of these programs made: (you can see the [full strace output here](https://gist.github.com/jvns/a5a5a39c6b79445279a7d3d03ba0c153)). You can generate this yourself with, for instance, `strace -f -o python.strace python hello.py`


```
wc -l *.strace
     38 c.strace
   1550 python.strace
   2699 java.strace
  15043 erlang.strace

```


Unsurprisingly, C comes in at the least. I was surprised that the Erlang VM runs **6 times** as many system calls as Java – I think of Java as already being pretty heavyweight. Maybe this is because Erlang starts up processes on all my cores? The variety of system calls is also interesting to see: [I put the system call frequencies in a gist too](https://gist.github.com/jvns/4b179aa7bd3e507a361f21de94e721d5).


When you look at the system call frequencies, you can see that Erlang is running significantly different **kinds** of system calls than Java and Python and C. Those 3 languages are mostly doing `open`, `read`, `lseek`, `stat`, `mmap`, `mprotect`, `fstat` – all activities around reading a bunch of files & allocating memory, which is what I think of as normal behavior when starting a program.


The top 2 syscalls for the Erlang process are `futex` and `sched_yield`. So there’s a lot of synchronization happening (the futex), and the operating system threads Erlang starts up keep scheduling themselves off the CPU “ok, I’m done, you go!”. There are also a lot of mysterious-to-me `ppoll` system calls. So Erlang seems like a programming language with really significantly different primitives.


This highly concurrent behavior is consistent with what Wikipedia article says:


> Erlang’s main strength is support for concurrency. It has a small but powerful
> set of primitives to create processes and communicate among them.


Let’s look a little more carefully at these `ppoll` system calls for a second. The story starts with


```
8682  openat(AT_FDCWD, "/sys/devices/system/node/node0", O_RDONLY|O_NONBLOCK|O_DIRECTORY|O_CLOEXEC) = 4
8703  ppoll([{fd=4, events=POLLIN|POLLRDNORM}, {fd=0, events=POLLIN|POLLRDNORM}], 2, {0, 0}, NULL, 8) = 0 (Timeout)

```


I have no idea what `/sys/devices/system/node/node0` is, but it seems to be a directory and what `ppoll` is looking for changes to? I don’t really get this at all.


One last thing – erlang runs `bind` once when it starts. Why does it need to listen on a TCP socket to run hello world? I was very confused about this and unable to figure it out. Some people on twitter thought it might have something to do with `epmd`, but `epmd` seems to be a separate process. So I don’t know what’s going on.


### <3 operating systems


I wanted to write this down because, as you all very well know, I think it’s interesting to take an operating systems-level approach to understanding what a program is doing and I thought this was a cool example of that.


I had this interesting experience yesterday where I was looking at this Erlang problem with Victor and David and they had OS X machines and I was like “dude I can’t debug anything on OS X”. So we got it working on my laptop and then I could make a lot more progress. Because now I’m pretty good at OS-level debugging tools, and I’ve spent a lot of time learning about Linux, and so I’m not super comfortable on non-Linux systems. (I know, I know, dtrace is amazing, I’m going to learn it one day soon, I promise :) )
