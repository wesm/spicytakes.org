---
title: "Thread pools! How do I use them?"
date: 2016-03-27
url: https://jvns.ca/blog/2016/03/27/thread-pools-how-do-i-use-them/
slug: thread-pools-how-do-i-use-them
word_count: 1306
---


HELLO! Today we’re going to talk about THREAD POOLS and PARALLELIZING COMPUTATION. I learned a couple of things about this over the last few days. This is mostly going to be about Java & the JVM. It turns out that there are lots of things to know about concurrency on the JVM, but luckily, lots of people know those things so you can learn them!


A thread pool lets you run computations in more than one thread at the same time. Let’s say I have a Super Slow Function, and I want to run it on 10000 things, and I have 32 cores on my CPU. Then I can run my function 32 times faster! Here’s what that looks like in Python.


```
from multiprocessing.pool import ThreadPool

def slow_function():
    do_whatever
results = ThreadPool(32).map(slow_command, list_of_things)

```


This seems really simple, right? Well, I was trying to parallelize something in Java (Scala, really) the other day and it was not this simple at all. So I wanted to tell you some of the confusing things I ran into.


My task: run a Sort Of Slow Function on 60 million things. It was already parallelized, but it was only using maybe 8 of my 32 CPU cores. I wanted it to use ALL OF THEM. This task was trivially parallelizable so I thought it would be easy.


### blocked threads


One of the first things I started seeing when I looked at my program with YourKit (a super great profiler for the JVM) was something a little like this (taken from [here](http://blog.tfd.co.uk/2010/10/15/jackrabbit-performance/)):


What was this red stuff?! My threads were “blocked”. What is a blocked thread?


In Java, a thread is “blocked” when it’s waiting for a “monitor” on an object. When I originally googled this I was like “er what’s a monitor?”. It’s when you use synchronization to make sure two different threads don’t execute the same code at the same time.


```
// scala pseudocode
class Blah {
    var x = 1
    def plus_one() {
        this.synchronized {
            x += 1
        }
    }
}

```


This `synchronize` means that only one thread is allowed to run this `x += 1` block at a time, so you don’t accidentally end up in a race. If one thread is already doing `x += 1`, the other threads end up – you guessed it – BLOCKED.


The two things that were blocking my threads were:

- `lazy` vals in Scala used `synchronized` internally, and so can cause problems with concurrency
- `Double.parseDouble` in Java 7 is a synchronized method. So only one thread can parse doubles from strings at a time. Really? Really. They fixed it in Java 8 though so that’s good.


### waiting threads


So, I unblocked some of my threads. I thought I was winning. This was only sort of true. Now a lot of my threads were orange. Orange means that the threads are like “heyyyyyyy I’m ready but I have nothing to do”.


At this point my code was like:


```
def doStuff(pool: FuturePool) {
    // a FuturePool is a thread pool
    while not done {
        var lines = read_from_disk
        var parsedStuff = parse(lines)
        pool.submit(parsedSuff.map{expensiveFunction})
    }
}

```


This was a pretty good function. I was submitting work to the pool! Work was getting done! In parallel!


But my main thread was doing all the work of submitting. And you see that `parse(lines)`? Sometimes this happened:


```
main: here is work to do!
main: start parsing
thread pool: ok I'm ready for more
main: I'M STILL PARSING OK
main: ok here is more work

```


The main thread couldn’t submit more work to the thread pool because it was too busy parsing!


This is like if you get a 5 year old to mix the batter for the cake when you’re doing a Complicated Kitchen Thing and they’re like OK OK OK OK OK OK WHAT NEXT and you’re like JUST A MINUTE.


The obvious solution to here was to give the parsing work to the threads! Because threads are not 5 year olds and they can do everything the main thread can do. So I rewrote my function be more like this:


```
def doStuff(pool: FuturePool):
    // a FuturePool is a thread pool
    // make sure it only has 32 threads so it
    // does not spin up a bajillion threads
    while not done {
        var lines = read_from_disk
        pool.submit(parsedSuff.map{parse}.map{expensiveFunction})
    }

```


AWESOME. This was great, right?


Wrong. Then this happened: `OutOfMemoryError`. What. Why. This brings us to…


### Work queues


This `FuturePool` abstraction is cool. Just give the thread work and it’ll do it! Don’t worry about what’s underneath! But now we need to understand what’s underneath.


In Java, you normally handle thread pools with something called an `ExecutorService`. This keeps a thread pool (say 32 threads). Or it can be unbounded! In this case I wanted to only have as many threads as I have CPU cores, ish.


So let’s say I run `ExecutorService.submit(work)` 32 times, and there are only 32 threads. What happens the 33rd time? Well, `ExecutorService` keeps an internal queue of work to do. So it holds on to Thing 33 and does something like


```
loop {
    if(has_available_thread) {
        available_thread.submit(queue.pop())
    }
}

```


In my case, I was reading a bunch of data off disk. maybe 10GB of data. And I was submitting **all of that data** into the ExecutorService work queue. Unsurprisingly, the queue exploded and crashed my program.


I tried to fix this by changing the internal queue in ExecutorService to an `ArrayBlockingQueue` with size 100, so that it would not accept an unlimited amount of work. Awesome!


### still not done


I spend like.. 8 hours on this? more? I was trying to do a small thing at work but I ended up working on it at like midnight because it was supposed to be a minor task and I couldn’t really justify spending more work time on it. I am still confused about how to do this thing that I thought would be easy.


I think what I need to do is:

- read from disk
- submit work to the ExecutorService. But with a bounded queue!!
- catch the exception from ExecutorService when it fails to schedule work, wait, and try again
- etc etc


Or maybe there is a totally simple way and this could take me 5 minutes!


This kind of thing makes me feel dumb, but in a really good and awesome way. I now know a bunch of things I didn’t know before about Java concurrency!! I used to feel bad when I realized I didn’t know how to work with stuff like this. (“threads and work queues are not that advanced of a concept julia what if you are an awful programmer”).


Now I don’t really feel bad usually I’m just like WELL TODAY IS THE DAY WHEN I LEARN IT. And tomorrow I will be even more awesome than I am today. Which is pretty awesome =D


### Abstractions


I think the thread pool abstractions I’m working with in Scala are not the best abstractions. Not because they don’t make it easier to program with concurrency – they do!


But the best abstractions I work with (the TCP/IP network layer! unix pipes!) let me use them for years without understanding in the slightest how they worked. When working with these concurrency abstractions I end up having to worry almost immediately about what’s underneath because the underlying queue has filled up and crashed my program.


I **love** learning about what’s underneath abstractions, but it is kinda time consuming. I guess it’s hard to build abstractions over thread pools! Maybe you really just have to understand how they’re implemented to work with them effectively. Either way – now I know more, and I can work with them a little better.
