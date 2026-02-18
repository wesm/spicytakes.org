---
title: "PAPERS ARE AMAZING: Profiling threaded programs with Coz"
date: 2015-10-31
url: https://jvns.ca/blog/2015/10/31/papers-are-amazing-profiling-threaded-programs-with-coz/
slug: papers-are-amazing-profiling-threaded-programs-with-coz
word_count: 848
---


HI BLOG FRIENDS!


I usually don’t read papers. I only read [one paper](http://research.google.com/pubs/pub43146.html) so far this year (which I love). I only read it because my friend Maggie printed it out and gave it to me.


SO. Yesterday I got handed 3 (three!) printed out papers from the amazing organizers of [Papers We Love Montreal](http://www.meetup.com/Papers-We-Love-Montreal/). And I woke up this morning and started reading one (because, Saturday morning). And then I had to tell you all about it because this paper is so cool. Okay, enough backstory.


The paper we’re going to talk about is [COZ: Finding Code that Counts with Causal Profiling](https://web.cs.umass.edu/publication/docs/2015/UM-CS-2015-008.pdf) (pdf). I found it super easy to read. Here is what I got out of it so far!


## Profiling threaded applications is hard


Profiling single-threaded applications where everything happens synchronously is pretty straightforward. If one part of the program is slow, it’ll show up as taking 10% of the time or something, and then you can target that part of the program for optimization.


But, when you start to use threads, everything gets way more complicated. The paper uses this program as an example:


```
void a() { // ˜6.7 seconds
  for(volatile size_t x=0; x<2000000000; x++) {}
}
void b() { // ˜6.4 seconds
  for(volatile size_t y=0; y<1900000000; y++) {}
}
int main() {
  // Spawn both threads and wait for them.
  thread a_thread(a), b_thread(b);
  a_thread.join(); b_thread.join();
}

```


Speeding up one of `a()` or `b()` won’t help you, because they *both* need to finish in order for the program to finish. (this is totally different from if we ran `a(); b()`, in which case speeding up `a()` could give you an up to 50% increase in speed).


Okay, so profiling threaded programs is hard. What next?


## Speed up one thread to see if that thread is the problem


The core idea in this paper is – if you have a line of code in a thread, and you want to know if it’s making your program slow, speed up that line of code to see if it makes the **whole program** faster!


Of course, you can’t actually speed up a thread. But you *can* slow down all other threads! So that’s what they do. The implemention here is super super super interesting – they use the `perf` Linux system to do this, and in particular they can do it **without modifying the program’s code**. So this is a) wizardry, and b) uses `perf`


Which are both things we love here ([omg perf](http://jvns.ca/blog/2014/05/13/profiling-with-perf/)). I’m going to refer you to the paper for now to learn more about how they use perf to slow down threads, because I honestly don’t totally understand it myself yet. There are some difficult details like “if the thread is already waiting on another thread, should we slow it down even more?” that they get into.


## omg it works


The thing that really impressed me about this paper is that they showed the results of running this profiler on real programs (SQLite! Memcached!), and then they could use the profiler results to detect

- a problem with too many hash table collisions
- unnecessary / inefficient uses of locking (“this is atomic anyway! no need to lock!”)
- where it would be more efficient to move code from one thread to another


and speed up the program on the workload they were testing by, like, 10%!


They also find out places where speeding up a line of code would introduce a *slowdown* (because of increased contention around some resource). This paradoxically also helps them make code faster, because that’s a good site for figuring out why there’s a problem with contention and changing the ways the locks are set up.


Also, they claim that the overhead of this profiling is like 20%? How can this be. This seems like literally magic except that THEY EXPLAIN HOW IT WORKS. Papers. Wow.


## Actually running the code


You can actually download the code [on GitHub](https://github.com/plasma-umass/coz). I tried to compile it and it did not work the first time. I suspect this is because `perf` changes a little between different Linux versions (I get a bunch of errors about `perf.h`). It seems like this is something [they’re working on](https://github.com/plasma-umass/coz/issues/16). Maybe a future project will be to try to get it to compile and run it on a REAL PROGRAM and see if I can reproduce some of the things they talk about in the paper! We’ll see.


## Async programming?!


Now I’m really curious about if we could do something similar for profiling single-threaded but asynchronous applications (for all the javascript programmers in the world!). Like, if you identified a function call you were interested in speeding up, you could slow down everything else running in the event loop and see if it slowed down the overall program. Maybe someone has already tried this! If so I want to know about it. (I’m [@b0rk](https://twitter.com/b0rk) on twitter).


Okay, papers are cool. If you know me and want to print a paper you love and give it to me I’d be into it.
