---
title: "I conquered thread pools! For today, at least."
date: 2016-03-29
url: https://jvns.ca/blog/2016/03/29/thread-pools-part-ii-i-love-blocking/
slug: thread-pools-part-ii-i-love-blocking
word_count: 724
---


The other day I wrote [Thread pools! How do I use them?](http://jvns.ca/blog/2016/03/27/thread-pools-how-do-i-use-them/) chronicling my Extreme Confusion about how to parallelize a task in Java/Scala. I am less confused now! Let me tell you how.


To recap: I wanted to

1. send a bunch of work to some worker threads, in parallel
2. have them do the work without anything exploding
3. that’s it


This turned out to be surprisingly difficult. A lot of people gave me a lot of suggestions about how to accomplish this. Here’s what I did!


### pipes = the best


I thought a bit about how Unix pipes are one of my favorite abstractions. You pipe stuff from `thing1` to `thing2` (`thing1 | thing2`), it works, nothing explodes. Why?


Well, pipes have an internal buffer, and when the buffer is full, `thing1` is not allowed to write to the pipe any more. It blocks. Several people pointed out to me that Go channels also work exactly this way. Super nice!


I think I want my concurrency to work like pipes (with an internal buffer that blocks). But how?


### blocking submissions to a thread pool in Java: nope


So, is there something in Java’s standard library that lets you submit to a thread pool and block if the thread pool is too busy? Spoiler: no, there is not.


I looked at the docs, I read Stack Overflow, and I watched jessitron’s fantastic [Concurrency Options on the JVM](https://www.youtube.com/watch?v=yhguOt863nw) talk (which is GREAT and you should watch it). No dice.


There is [CallerRunsPolicy](https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/ThreadPoolExecutor.CallerRunsPolicy.html) which will make the calling thread run the task if the thread pool is too busy, but that was not what I wanted.


### java concurrency in practice saves the day


Okay, so Java 7’s standard library hates me. Fine. Well, Java is Turing-complete and, besides, has all kinds of concurrency primitives. This is definitely possible to do in a nice way. But how?! I asked Kamal what he thought and he was like “wow, it’s weird that it’s not in the standard library!”.


We googled and Kamal found this gorgeous code snippet from the book [Java Concurrency in Practice](http://www.amazon.com/Java-Concurrency-Practice-Brian-Goetz/dp/0321349601?ie=UTF8&*Version*=1&*entries*=0) – [BoundedExecutor.java](http://jcip.net/listings/BoundedExecutor.java). Here it is:


```
public class BoundedExecutor {
    private final Executor exec;
    private final Semaphore semaphore;

    public BoundedExecutor(Executor exec, int bound) {
        this.exec = exec;
        this.semaphore = new Semaphore(bound);
    }

    public void submitTask(final Runnable command)
            throws InterruptedException {
        semaphore.acquire();
        try {
            exec.execute(new Runnable() {
                public void run() {
                    try {
                        command.run();
                    } finally {
                        semaphore.release();
                    }
                }
            });
        } catch (RejectedExecutionException e) {
            semaphore.release();
        }
    }
}

```


I didn’t know what a semaphore was until I read this code and I was like OH THIS IS AMAZING AND SO USEFUL AND WOW. A semaphore is just a shared int that you can decrement and increment! `acquire()` decrements, `release()` increments. And if it gets to 0, `semaphore.acquire()` will block until someone else has released it. Awesome. That *is* a great concurrency primitive!


I implemented a version of this in my code and everything worked amazingly. It all parallelized super beautifully, my main thread just delegated work, and my worker threads were all busy all the time.


I tweeted about how great Java Concurrency in Practice is and everyone was like “yeah that book was so formative for me it made me love concurrency” “seriously it’s such a great book” “it’s like K&R”. So now I’m way way way more motivated to read it.


### how to shutdown a thread pool


Here’s what I did:


```
service.shutdown()
service.awaitTermination(Long.MaxLong, TimeUnit.Seconds)

```


This tells it to stop accepting new tasks, and then wait for all the tasks to finish! This is easy but I needed to remember to do it and think through it.


### a super quick note on Python


Out of curiosity, I looked at Python’s thread pool ([ThreadPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) from `futures` in Python 2). It doesn’t even let you configure the internal submission queue on your thread pool! Luckily the implementation of ThreadPoolExecutor is [not very long](https://hg.python.org/cpython/file/3.5/Lib/concurrent/futures/thread.py) so we can always write our own or something if we are dissatisfied and brave.


### Final scores

- java standard library: 0.5 (for having the primitives I wanted)
- twitter’s FuturePool: 0 (nope.)
- Python: ???, but, not relevant
- scala streams / other parallel collections: 0
- Java Concurrency in Practice: 1
- julia & kamal: 1


WE WIN.
