---
title: "Async IO on Linux: select, poll, and epoll"
date: 2017-06-03
url: https://jvns.ca/blog/2017/06/03/async-io-on-linux--select--poll--and-epoll/
slug: async-io-on-linux--select--poll--and-epoll
word_count: 2023
---


This week I got a new book in the mail: [The Linux Programming Interface](https://www.nostarch.com/tlpi). My awesome coworker Arshia recommended it to me so I bought it! It’s written by the
maintainer of the [Linux man-pages project](https://www.kernel.org/doc/man-pages/), Michael Kerrisk. It talks about the Linux programming interface as of kernel 2.6.x.


Here’s the cover.


![](https://jvns.ca/images/linuxprogramming.png)


In the contributing guidelines (you can contribute to the linux man pages!! mind=blown), there’s a list of [missing man pages](https://www.kernel.org/doc/man-pages/missing_pages.html) that would be useful to contribute. It says:


> You need to have a reasonably high degree of understanding of the
> topic, or be prepared to invest the time (e.g., reading source code,
> writing test programs) to gain that understanding. Writing test
> programs is important: quite a few kernel and glibc bugs have been
> uncovered while writing test programs during the preparation of man
> pages.


I thought this was a cool reminder of how you can learn a lot by
documenting something & writing small test programs!


But today we’re going to talk about something I learned from this book:
the `select`, `poll`, and `epoll` system calls.


### Chapter 63: Alternative I/O models


This book is huge: 1400 pages. I started it at Chapter 63 (“alternative
I/O models”) because I’ve been meaning to understand better what’s up with
`select`, `poll` and `epoll` for quite some time. And writing up things
I learn helps me understand them, so here’s my attempt at explaining!


This chapter is basically about how to monitor a lot of file descriptors
for new input/output. Who needs to watch a lot of file descriptors at a
time? Servers!


For example if you’re writing a web server in node.js on Linux, it’s
actually using the `epoll` Linux system call under the hood. Let’s talk
about why, how `epoll` is different from `poll` and `select`, and about how it works!


### Servers need to watch a lot of file descriptors


Suppose you’re a webserver. Every
time you accept a connection with the `accept` system call ([here’s the man page](http://man7.org/linux/man-pages/man2/accept.2.html)),
you get a new file descriptor representing that connection.


If you’re a web server, you might have thousands of connections open at
the same time. You need to know when people send you new data on those
connections, so you can process and respond to them.


You could have a loop that basically does:


```
for x in open_connections:
    if has_new_input(x):
        process_input(x)

```


The problem with this is that it can waste a lot of CPU time. Instead of
spending all CPU time to ask “are there updates now? how about now? how
about now? how about now?”, instead we’d rather just ask the Linux kernel
“hey, here are 100 file descriptors. Tell me when one of them is
updated!”.


The 3 system calls that let you ask Linux to monitor lots of file
descriptors are `poll`, `epoll` and `select`. Let’s start with poll and
select because that’s where the chapter started.


### First way: select & poll


These 2 system calls are available on any Unix system, while `epoll` is
Linux-specific. Here’s basically how they work:

1. Give them a list of file descriptors to get information about
2. They tell you which ones have data available to read/write to


The first surprising thing I learned from this chapter are that **poll
and select fundamentally use the same code**.


I went to look at the definition of `poll` and `select` in the Linux kernel
source to confirm this and it’s true!

- here’s the [definition of the select syscall](https://github.com/torvalds/linux/blob/v4.10/fs/select.c#L634-L656) and [do_select](https://github.com/torvalds/linux/blob/v4.10/fs/select.c#L404-L542)
- and the [definition of the poll syscall](https://github.com/torvalds/linux/blob/v4.10/fs/select.c#L1005-L1055) and [do_poll](https://github.com/torvalds/linux/blob/v4.10/fs/select.c#L795-L879)


They both call a lot of the same functions. One thing that the book
mentioned in particular is that `poll` returns a larger set of possible
results for file descriptors like `POLLRDNORM | POLLRDBAND | POLLIN | POLLHUP | POLLERR` while `select` just tells you “there’s input / there’s output / there’s an error”.


`select` translates from `poll`’s more detailed results (like `POLLWRBAND`) into a general “you can write”. You can see the code where it does this in Linux 4.10 [here](https://github.com/torvalds/linux/blob/v4.10/fs/select.c#L468-L482).


The next thing I learned is that **poll can perform better than select if you have a sparse set of file descriptors** .


To see this, you can actually just look at the signatures for poll and
select!


```
int ppoll(struct pollfd *fds, nfds_t nfds,
          const struct timespec *tmo_p, const sigset_t
          *sigmask)`
int pselect(int nfds, fd_set *readfds, fd_set *writefds,
            fd_set *exceptfds, const struct timespec *timeout,
            const sigset_t *sigmask);

```


With `poll`, you tell it “here are the file descriptors I want to monitor: 1,
3, 8, 19, etc” (that’s the `pollfd` argument. With select, you tell it “I want to monitor 19 file
descriptors. Here are 3 bitsets with which ones to monitor for reads / writes / exceptions.”
So when it runs, it [loops from 0 to 19 file descriptors](https://github.com/torvalds/linux/blob/v4.10/fs/select.c#L440),
even if you were actually only interested in 4 of them.


There are a lot more specific details about how `poll` and `select` are
different in the chapter but those were the 2 main things I learned!


### why don’t we use poll and select?


Okay, but on Linux we said that your node.js server won’t use either poll or
select, it’s going to use `epoll`. Why?


From the book:


> On each call to `select()` or `poll()`, the kernel must check all of the
> specified file descriptors to see if they are ready. When monitoring a large
> number of file descriptors that are in a densely packed range, the timed
> required for this operation greatly outweighs [the rest of the stuff they have
> to do]


Basically: every time you call `select` or `poll`, the kernel needs to
check from scratch whether your file descriptors are available for
writing. The kernel doesn’t remember the list of file descriptors it’s
supposed to be monitoring!


### Signal-driven I/O (is this a thing people use?)


The book actually describes 2 ways to ask the kernel to remember the
list of file descriptors it’s supposed to be monitoring: signal-drive
I/O and `epoll`. Signal-driven I/O is a way to get the kernel to send
you a signal when a file descriptor is updated by calling `fcntl`. I’ve
never heard of anyone using this and the book makes it sound like
`epoll` is just better so we’re going to ignore it for now and talk about epoll.


### level-triggered vs edge-triggered


Before we talk about epoll, we need to talk about “level-triggered” vs
“edge-triggered” notifications about file descriptors. I’d never heard
this terminology before (I think it comes from electrical engineering
maybe?). Basically there are 2 ways to get notifications

- get a list of every file descriptor you’re interested in that is readable (“level-triggered”)
- get notifications every time a file descriptor becomes readable
(“edge-triggered”)


### what’s epoll?


Okay, we’re ready to talk about epoll!! This is very exciting to because
I’ve seen `epoll_wait` a lot when stracing programs and I often feel
kind of fuzzy about what it means exactly.


The `epoll` group of system calls (`epoll_create`, `epoll_ctl`,
`epoll_wait`) give the Linux kernel a list of file descriptors to track
and ask for updates about activity on those file descriptors.


Here are the steps to using epoll:

1. Call `epoll_create` to tell the kernel you’re gong to be epolling! It
gives you an id back
2. Call `epoll_ctl` to tell the kernel file descriptors you’re
interested in updates about. Interestingly, you can give it lots of
different kinds of file descriptors (pipes,
FIFOs, sockets, POSIX message queues, inotify instances, devices, & more), but
**not regular files**. I think this makes sense – pipes & sockets
have a pretty simple API (one process writes to the pipe, and another
process reads!), so it makes sense to say “this pipe has new data for
reading”. But files are weird! You can write to the middle of a file!
So it doesn’t really make sense to say “there’s new data available
for reading in this file”.
3. Call `epoll_wait` to wait for updates about the list of files
you’re interested in.


### performance: select & poll vs epoll


In the book there’s a table comparing the performance for 100,000
monitoring operations:


```
# operations  |  poll  |  select   | epoll
10            |   0.61 |    0.73   | 0.41
100           |   2.9  |    3.0    | 0.42
1000          |  35    |   35      | 0.53
10000         | 990    |  930      | 0.66

```


So using epoll really is a lot faster once you have more than 10 or so
file descriptors to monitor.


### who uses epoll?


I sometimes see `epoll_wait` when I strace a program. Why? There is the
kind of obvious but unhelpful answer “it’s monitoring some file
descriptors”, but we can do better!


First – if you’re using green threads or an event loop, you’re likely
using epoll to do all your networking & pipe I/O!


For example, here’s a golang program that uses epoll on Linux!


```
package main

import "net/http"
import "io/ioutil"

func main() {
    resp, err := http.Get("http://example.com/")
        if err != nil {
            // handle error
        }
    defer resp.Body.Close()
    _, err = ioutil.ReadAll(resp.Body)
}

```


Here you can see the golang run time using epoll to do a DNS lookup:


```
16016 connect(3, {sa_family=AF_INET, sin_port=htons(53), sin_addr=inet_addr("127.0.1.1")}, 16 <unfinished ...>
16020 socket(PF_INET, SOCK_DGRAM|SOCK_CLOEXEC|SOCK_NONBLOCK, IPPROTO_IP
16016 epoll_create1(EPOLL_CLOEXEC <unfinished ...>
16016 epoll_ctl(5, EPOLL_CTL_ADD, 3, {EPOLLIN|EPOLLOUT|EPOLLRDHUP|EPOLLET, {u32=334042824, u64=139818699396808}}
16020 connect(4, {sa_family=AF_INET, sin_port=htons(53), sin_addr=inet_addr("127.0.1.1")}, 16 <unfinished ...>
16020 epoll_ctl(5, EPOLL_CTL_ADD, 4, {EPOLLIN|EPOLLOUT|EPOLLRDHUP|EPOLLET, {u32=334042632, u64=139818699396616}}

```


Basically what this is doing is connecting 2 sockets (on file
descriptors 3 and 4) to make DNS queries (to 127.0.1.1:53), and then
using `epoll_ctl` to ask epoll to give us updates about them


Then it makes 2 DNS queries for example.com (why 2? nelhage suggests one
of them is querying for the A record, and one for the AAAA record!), and
uses `epoll_wait` to wait for replies


```
# these are DNS queries for example.com!
16016 write(3, "\3048\1\0\0\1\0\0\0\0\0\0\7example\3com\0\0\34\0\1", 29
16020 write(4, ";\251\1\0\0\1\0\0\0\0\0\0\7example\3com\0\0\1\0\1", 29
# here it tries to read a response but I guess there's no response
# available yet
16016 read(3,  <unfinished ...>
16020 read(4,  <unfinished ...>
16016 <... read resumed> 0xc8200f4000, 512) = -1 EAGAIN (Resource temporarily unavailable)
16020 <... read resumed> 0xc8200f6000, 512) = -1 EAGAIN (Resource temporarily unavailable)
# then it uses epoll to wait for responses
16016 epoll_wait(5,  <unfinished ...>
16020 epoll_wait(5,  <unfinished ...>

```


So one reason your program might be using epoll “it’s in Go / node.js /
Python with gevent and it’s doing networking”.


What libraries do go/node.js/Python use to use epoll?

- node.js uses [libuv](https://github.com/libuv/libuv) (which was
written for the node.js project)
- the gevent networking library in Python uses [libev/libevent](https://blog.gevent.org/2011/04/28/libev-and-libevent/)
- golang uses some custom code, because it’s Go. This [looks like it might be the implementation of network polling with epoll in the golang runtime](https://github.com/golang/go/blob/91c9b0d568e41449f26858d88eb2fd085eaf306d/src/runtime/netpoll_epoll.go) – it’s only about 100 lines which is interesting. You can see the general netpoll interface [here](https://golang.org/src/runtime/netpoll.go) – it’s implemented on BSDs with kqueue instead


Webservers also implement epoll – for example [here’s the epoll code in nginx](https://github.com/nginx/nginx/blob/0759f088a532ec48170ca03d694cc103757a0f4c/src/event/modules/ngx_epoll_module.c).


### more select & epoll reading


I liked these 3 posts by Marek:

- [select is fundamentally broken](https://idea.popcount.org/2017-01-06-select-is-fundamentally-broken/)
- [epoll is fundamentally broken part 1](https://idea.popcount.org/2017-02-20-epoll-is-fundamentally-broken-12/)
- [epoll is fundamentally broken part 2](https://idea.popcount.org/2017-03-20-epoll-is-fundamentally-broken-22/)


In particular these talk about how epoll’s support for multithreaded
programs has not historically been good, though there were some
improvements in Linux 4.5.


and this:

- [using select (2) the right way](http://aivarsk.github.io/2017/04/06/select/)


### ok that’s enough


I learned quite a few new things about select & epoll by writing this
post! We’re at 1800 words now so I think that’s enough. Looking forward
to reading more of this Linux programming interface book and finding out
more things!


Probably there are some wrong things in this post, let me know what they
are!


One small thing I like about my job is that I can expense programming
books! This is cool because sometimes it causes me to buy and read books
that teach me things that I might not have learned otherwise. And buying
a book is way cheaper than going to a conference!
