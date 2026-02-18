---
title: "Sendfile (a system call for web developers to know about!)"
date: 2016-01-23
url: https://jvns.ca/blog/2016/01/23/sendfile-a-new-to-me-system-call/
slug: sendfile-a-new-to-me-system-call
word_count: 863
---


The other day I learned about a new (to me) exciting Linux system call! (for newcomers, a system call is an operation you can ask the operating system to do). This one seems really important to know about if you’re configuring a webserver! So let’s learn about it.


Before this, I knew about basic system calls like `open` and `read` for files, and `sendto` and `recvfrom` for networking. And a few fancier things like `futex` and `select` for mutexes and waiting.


### why sendfile was invented


Suppose I want to send you a big file over a network connection. Normally I’d just read the file incrementally, and then write the contents to the socket. So, at a minimum, we need to

- use `read` (requires a context switch into kernel code)
- (implicitly, copy the data from kernel memory into user memory)
- use `sendto` or `write` (another context switch)


This means we need to copy data (bad) and use two system calls instead of one (also bad).


So the idea is – this pattern of reading a file and writing to a socket is really common! So they made a system call to just do that! Then the kernel can do all the work of reading and writing, and save you CPU time. And you don’t need to copy any data around! AMAZING.


### the performance implications


I found this [google code discussion on a Python FTP library](https://code.google.com/p/pyftpdlib/issues/detail?id=152). One person says that by using the `sendfile` system call, they could transfer 1.5GB/s instead of 800MB/s! That’s pretty awesome for a small change.


[This paper from Netflix](https://people.freebsd.org/~rrs/asiabsd_2015_tls.pdf) describes using sendfile on FreeBSD to go from 6Gbps to 40Gbps of network throughput. They also talk about implementing (part of?) TLS in the kernel to improve TLS performance.


### the disasters


I then read [“The brokenness of the sendfile() system call”](https://blog.phusion.nl/2015/06/04/the-brokenness-of-the-sendfile-system-call/). Wait?! But I thought sendfile was awesome and we should always use it? Not so!


That post describes how on OS X, `sendfile` wouldn’t send **any** data until the socket was closed, causing up to 5 second delays. That’s TERRIBLE. So sendfile isn’t some kind of universal panacea, and that’s why webservers let you turn it on and off.


### some other reading on sendfile


[Rob Pike (one of the creators of Go) thinks sendfile is “bizarre”](https://groups.google.com/forum/#!msg/golang-nuts/gdp1q6T0DNY/sFaRetnWPWIJ). I find his argument in that post pretty difficult to follow (if the kernel provides a way to do something, and that way gives you better performance in practice, why not use it?). But I thought it was interesting.


[Life of a HTTP request, as seen by my toy web server](http://tia.mat.br/posts/2014/10/06/life_of_a_http_request.html) is interesting, and describes how the author uses `sendfile` for large files, but not for small files. You don’t need to write your own webserver to take advantage of this – you can configure apache and nginx to use sendfile!


[The sendfile man page](http://man7.org/linux/man-pages/man2/sendfile.2.html) is actually quite readable, and it tells you something very important! It recommends using the `TCP_CORK` TCP option for better network performance. We learned about how understanding TCP is important in [Why you should understand (a little) about TCP](http://jvns.ca/blog/2015/11/21/why-you-should-understand-a-little-about-tcp/), and that’s pretty important here as well. In this case you need to decide whether to use `TCP_CORK` and `TCP_NODELAY`. One thing I read recommended using both.


You can also use sendfile to copy files quickly! (like, think about how `cp` is implemented!) [So you want to write to a file real fast…](http://blog.plenz.com/2014-04/so-you-want-to-write-to-a-file-real-fast.html) walks through some optimizations to file copying and gets a 25% improvement by using `sendfile` and other tricks. I straced `cp` on my machine just now, and it seems like it does not use `sendfile`. It’s super interesting to me how much abstractions break down when you’re trying to really optimize performance.


### next step: `splice` & `tee`


These days `sendfile` is a wrapper around the `splice` system call, which seems to be the same thing – copy data from one file/pipe/socket to another – but with some extra options.


There’s [a neat thread on the Linux Kernel Mailing List from 2006](https://web.archive.org/web/20130521163124/http://kerneltrap.org/node/6505), just after those system calls came into existence, where Linus explains what they’re for and how to think about them.


I found this paragraph helpful:


> Anyway, when would you actually *use* a kernel buffer? Normally you’d use it
> it you want to copy things from one source into another, and you don’t
> actually want to see the data you are copying, so using a kernel buffer allows
> you to possibly do it more efficiently, and you can avoid allocating user VM
> space for it


That post also makes it clear that `sendfile` used to be a separate system call and is now just a wrapper around `splice`.


There’s also `vmsplice`, which I think is related and important. But right now my brain is full. Maybe we’ll learn about vmsplice later.


### why this is amazing


It makes me really happy when learning a new system call helps me understand how to do something really practical. Now I know that if I’m building something that serves large files and I care about the performance, I should make sure I understand if it’s using sendfile!
