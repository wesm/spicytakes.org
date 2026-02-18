---
title: "perf top: an awesome way to spy on CPU usage"
date: 2016-02-24
url: https://jvns.ca/blog/2016/02/24/perf-top-my-new-best-friend/
slug: perf-top-my-new-best-friend
word_count: 1006
---


If you read this blog, you might know that I [love strace, so much that I wrote a zine about it](http://jvns.ca/blog/2015/04/14/strace-zine/). But strace has not ever been able to solve all my problems – it only tells me about system calls, it can slow down my code up to 50x. Not ideal!


So, enter `perf`. We [learned about perf](http://jvns.ca/blog/2014/05/13/profiling-with-perf/) a couple of years ago, when we found out that it can tell you about how many CPU cycles your program is using. That was cool, but ultimately not that useful to me right now (I’m trying to make Ruby programs fast!).


But! A couple of months ago I learned about `perf top`, which tells you which functions are in use on your computer right now (the same way `top` does for programs). I have three stories for you about how perf top is the best and has helped me solve problems.


First, I’m going to show you what `sudo perf top` gives me on my computer right now:


```
$ sudo perf top
26.63%  chrome                               [.] 0x0000000000fe202b
 2.20%  perf                                 [.] 0x00000000000523fd
 1.12%  [kernel]                             [k] _raw_spin_lock_irqsave
 1.10%  MusicManager_x86_64.nexe             [.] sqlite3VdbeExec
 0.98%  [kernel]                             [k] fget_light
 0.91%  perf-10709.map                       [.] 0x00001db39d555f0d
 0.89%  [kernel]                             [k] aes_decrypt
 0.88%  [kernel]                             [k] sock_poll
 0.82%  [kernel]                             [k] aes_encrypt
 0.78%  [kernel]                             [k] __schedule
 0.76%  .com.google.Chrome.Bc2ixX            [.] 0x000000000feda002

```


You can see that some mystery function in Chrome is responsible for 26% of CPU usage, perf itself has some overhead, `MusicManager_x86_64` is using sqlite (what? why?), and there are various things going on inside my kernel. Neat.


Now, let’s see some real examples of perf in action!


### the case of the sad Node program


I needed to debug a node program recently. It was super slow, and spending a ton of time on the CPU. I had no idea why.


Since my new hobby is to run `perf top` any time I have a question about CPU usage, I ran perf! I don’t have the real results here, but I basically saw something like this:


```
node                 [.] v8::internal::StackFrame::GetCallerState(v8::internal::StackFrame::State*) const
node                 [.] v8::internal::SemiSpace::Swap(v8::internal::SemiSpace*, v8::internal::SemiSpace*)
node                 [.] v8::internal::ScavengeVisitor::VisitPointers(v8::internal::Object**, v8::internal::Object**)
node                 [.] v8::internal::GCTracer::Start(v8::internal::GarbageCollector, char const*, char const*)
node                 [.] v8::internal::Heap::ClearJSFunctionResultCaches()
node                 [.] v8::internal::InnerPointerToCodeCache::GetCacheEntry(unsigned char*)
node                 [.] v8::internal::Runtime_AllocateInTargetSpace(int, v8::internal::Object**,

```


I didn’t know what all of it meant, but it seemed clear that the program was spending most of its time doing garbage collection. No good! We didn’t manage to figure out *why* it was garbage collecting, but it was awesome to be able to quickly triage what was going on.


### the case of the swapping computer


Today at work, I had a program that was slow. Surprise! A lot of stories these days start this way. The computer was using a lot of CPU, and I wanted to know why.


Here’s what `perf top` had to say about that:


![](https://jvns.ca/images/swap-perf.png)


This is a totally different story from our node story – in this case, the **linux kernel** is using all our CPU. What?! Why?


It turns out that the computer was swapping its memory to disk, and that the swap partition was encrypted. So every time it saved memory to disk or read it back, it needed to encrypt and decrypt all that memory. The CPU load on that machine was like 15. It was having a bad day.


We fixed the memory usage on the machine, and everything was all better ❤.


### the case of the HTTP request


Our last case is a Python mystery! This one is a fake mystery that I made up, but it illustrates a real possible slow program.


So! I ran a Python program to download several files, and it used 100% of my CPU for several seconds. What was it doing? Let’s ask perf top!!


```
24.92%  libcrypto.so.1.0.0  [.] 0x00000000001264e4
 8.88%  libcrypto.so.1.0.0  [.] EVP_DecodeUpdate
 6.23%  libc-2.15.so        [.] malloc
 5.62%  python              [.] 0x00000000000e9b5d
 4.48%  libc-2.15.so        [.] malloc_consolidate.part.3
 3.25%  python              [.] PyEval_EvalFrameEx
 2.77%  libcrypto.so.1.0.0  [.] EVP_DecodeBlock
 2.63%  libcrypto.so.1.0.0  [.] ASN1_item_ex_d2i
 2.07%  libcrypto.so.1.0.0  [.] X509_NAME_cmp
 1.62%  libc-2.15.so        [.] msort_with_tmp.part.0
 1.62%  libcrypto.so.1.0.0  [.] ASN1_item_ex_i2d

```


It seems to be doing… a lot of crypto? Why? Here’s the program:


```
import grequests

rs = (grequests.get('https://news.ycombinator.com') for i in xrange(1000))

grequests.map(rs)

```


It turns out that opening a HTTPS connection is pretty slow! You need to spend a bunch of time in crypto functions in order to be secure. And perf tells us immediately that that’s what’s going on! Awesome.


### But there’s more


So I’ve gone through a few examples of how perf can sometimes help triage what a program is spending its CPU time on, even if the program is written in node or Python or something.


There’s a limitation here that you may have noticed – perf will only tell us about C functions (like `EVP_DecodeUpdate` or something).


So you may be thinking – “my node program isn’t garbage collecting! It’s spending its time in some Javascript function! perf will not help me at all!” And what if I’m using Java, Julia? This will not help me with Java!


perf is even more magical than you might expect, though! You can **tell perf about your Java and node functions**. This blew my mind when I learned it and is continuing to blow my mind. If you want to make perf amazing for Java, read this blog post [Java in flames](http://techblog.netflix.com/2015/07/java-in-flames.html)


[Brendan Gregg’s page on perf](http://www.brendangregg.com/perf.html) has more about perf and how great it is and how to use it to help debug your node.js programs.


### a toolbox of delightful tools


I’m slowly building a toolbox of easy-to-use tools that will help me understand what my programs are doing. There are a few things that are farther down the list (ftrace and systemtap are still very confusing to me and I do not know how to use them.)


But `perf top` is so simple (just one command!), and so straightforward, and I think it deserves to go in your toolbox. It works on Linux. Try it out! See what happens! Run it everywhere! It’s safe to run in production.


`sudo perf top`
