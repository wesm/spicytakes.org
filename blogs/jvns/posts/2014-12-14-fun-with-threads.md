---
title: "Diving into concurrency: trying out mutexes and atomics"
date: 2014-12-14
url: https://jvns.ca/blog/2014/12/14/fun-with-threads/
slug: fun-with-threads
word_count: 1836
---


I hadn’t written any threaded programs before yesterday. I knew sort of
abstractly about some concurrency concepts (mutexes! people say
compare-and-swap but I don’t totally get it!), but actually
understanding a Thing is hard if I’ve never done it. So yesterday I
decided to write a program with threads! In this post, we’re going to:

1. Write a threaded program that gets the wrong answer because of a race
condition
2. Fix that race condition in C and Rust, using 2 different approaches
(mutexes and atomics)
3. Find out why Rust is slower than C
4. Talk a little about the actual system calls and instructions that
make some of this work


At first I was going to write a concurrent hashmap, but
[Kamal](https://twitter.com/kamalmarhubi) wisely pointed out that I
should start with something simpler, like a counter!


So. We’re going to get 20 threads to count to 20,000,000 all together.
We’ll have a global counter variable, and increment it like this:


```
counter += 1

```


That seems so safe! What can go wrong here is that if two threads try to
increment the number at the exact same time, then it’ll only get
incremented once instead of twice. This is called a **race condition**.


### Writing a race condition


Here’s what my original C program looks like, with the bug. I wrote this
by knowing that people used a library called “pthreads” to do threads in
c, and googling “pthreads example”. I’m not going to explain it very
much, but essentially it creates 20 threads and has them all run the
`AddThings` function which increments a global counter a million times.


Full version:
[counter_race.c](https://github.com/jvns/fun-with-threads/blob/master/counter_race.c).


```
#define NUM_THREADS     20
#define NUM_INCREMENTS  1000000

int counter;

void *AddThings(void *threadid) {
   for (int i = 0; i < NUM_INCREMENTS; i++)
        counter += 1;
   pthread_exit(NULL);
}

int main (int argc, char *argv[]) {
   pthread_t threads[NUM_THREADS];
   long t;
   for(t = 0; t<NUM_THREADS; t++){
      int rc = pthread_create(&threads[t], NULL, AddThings, (void *)t);
      if (rc){
         printf("ERROR; return code from pthread_create() is %d\n", rc);
         exit(1);
      }
   }
   // Wait for threads to finish
   for (t = 0; t < NUM_THREADS; t++)
       pthread_join(threads[t], NULL);
   printf("Final value of counter is: %d\n", counter);
   pthread_exit(NULL);
}

```


This program a) runs very fast and b) returns wildly different answers
each time. We’re expecting 20,000,000. I ran it 10 times and got 10
different answers, between 2,838,838 and 5,695,671.


### First try: mutexes! (and learning that mutexes can be Really Slow)


A mutex (or **lock**) is a way to control access to a resource so that
two threads don’t change it in conflicting ways at the same time.


A typical pattern for using a lock is:


```
lock.lock();
// do something with shared state, eg counter +=1 
lock.unlock();

```


Mutexes are often implemented on Linux systems with the [`futex` system
call](http://man7.org/linux/man-pages/man2/futex.2.html). Basically it’s
a way of saying “hey, kernel! This lock is closed, so I’d like to stop
running. Can you please wake me up when it’s available again?”.


I learned during these explorations that all this making system calls
and going to sleep and waking up again is actually pretty expensive. But
let’s do performance numbers first!


So the C pthread library has a mutex implementation like this. Let’s
implement our counter with it! You can see the full implementation t
[counter_with_mutex.c](https://github.com/jvns/fun-with-threads/blob/master/counter_with_mutex.c).
It’s a pretty small change: we need to add


```
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

```


at the beginning, and replace `counter += 1` with


```
pthread_mutex_lock(&mutex);
counter += 1;
pthread_mutex_unlock(&mutex);

```


If we run our new program, it calculates the correct answer every time!
Amazing! What does the performance of this look like? I’m going to do
all my profiling with `perf stat` (perf is an amazing program that you
can read more about in [I can spy on my CPU cycles with perf!](http://jvns.ca/blog/2014/05/13/profiling-with-perf/))


```
$ perf stat ./counter_with_mutex
Final value of counter is: 20000000
       3.134196432 seconds time elapse

```


Our original counter with the race condition took more like 0.08
seconds. This is a really big performance hit, even if it means that we
have a program that works instead of a program that doesn’t!


### Mutexes in Rust, too! (it’s even slower!)


I decided to implement the same thing in Rust because, well, Rust is
fun! You can see it at
[rust_counter_mutex.rs](https://github.com/jvns/fun-with-threads/blob/master/rust_counter_mutex.rs).


We create a mutex with


```
let data = Arc::new(Mutex::new(0u));

```


and increment it with


```
for _ in range(0u, NUM_INCREMENTS) {
   let mut d = data.lock();
    *d += 1;
}

```


I basically got this to work by [copying the Rust mutex
documentation](http://doc.rust-lang.org/std/sync/struct.Mutex.html). I’m
pretty impressed by how much Rust’s documentation has improved in the
last year.


I ran this, and I was expecting it to perform about as well as my C code.
It didn’t.


```
$ perf stat ./rust_counter_mutex
       8.842611143 seconds time elapsed

```


My first instinct was to profile it! I used Brendan Gregg’s excellent
[flame graph library](https://github.com/brendangregg/FlameGraph), and ran


```
$ sudo perf record ./rust_counter_mutex
$ sudo perf script | stackcollapse-perf.pl | flamegraph.pl > rust_mutex_flamegraph.svg

```


What is even going on here?! These two graphs look exactly the same. Why
does the Rust one taking longer?


So, off to the races in the #rust IRC channel! Fortunately, the people
in #rust are the Nicest People. You can see them helping me out [in the
logs](https://botbot.me/mozilla/rust/2014-12-13/?msg=27485007&page=27)
=D.


After a while, someone named Sharp explains that Rust’s mutexes are
implemented in a Slow Way using channels. This seems to make sense, but
then why couldn’t I see that from the flamegraph? He explains helpfully
that channels in Rust are also implemented with the `futex` syscall, so
it’s spending all of its time in the same syscalls, just doing it less
efficiently. COOL.


Sharp also suggests using an atomic instead of a mutex, so that’s the next
step!


### Making it fast with atomics in Rust


This one is at
[rust_counter_atomics.rs](https://github.com/jvns/fun-with-threads/blob/master/rust_counter_atomics.rs).
I did this without actually understanding what an atomic even is, so I’m not
going to explain anything yet.


Basically we replace our mutex with a


```
let counter = Arc::new(AtomicUint::new(0));

```


and our loop with


```
for _ in range(0u, NUM_INCREMENTS) {
    counter.fetch_add(1, Relaxed);
}

```


I’m not going to talk about the `Relaxed` right now (because I don’t understand it as well as I’d like), but basically this increments our counter in a threadsafe way (so that two threads can’t race).


And it works! And it’s fast!


```
perf stat ./rust_counter_atomics
20000000
       0.556901591 seconds time elapsed

```


Here’s the new flamegraph:


You can see from the new flamegraph that it’s definitely not using
mutexes at all. But we still don’t know how these atomics work, which is
troubling. Let’s implement the same thing in C, to see if it makes it a
little clearer.


### Atomics in C: even faster!


To use atomics in our C program, I replaced


```
for (int i = 0; i < NUM_INCREMENTS; i++) {
    pthread_mutex_lock(&mutex);
    counter += 1;
    pthread_mutex_unlock(&mutex);
}

```


with something called `__sync_add_and_fetch`:


```
   for (int i = 0; i < NUM_INCREMENTS; i++) {
       __sync_add_and_fetch(&counter, 1);
   }

```


You might have noticed that the `fetch_add` in Rust is suspiciously
similar to `__sync_add_and_fetch`. This is a special GCC [atomic builtin](https://gcc.gnu.org/onlinedocs/gcc-4.1.2/gcc/Atomic-Builtins.html)
which generates assembly instructions to safely increment our counter.


That GCC documentation page is pretty readable! One interesting thing is
this:


> All of the routines are described in the Intel documentation to take
> “an optional list of variables protected by the memory barrier”. It’s
> not clear what is meant by that; it could mean that only the following
> variables are protected, or it could mean that these variables should
> in addition be protected. At present GCC ignores this list and
> protects all variables which are globally accessible. If in the future
> we make some use of this list, an empty list will continue to mean all
> globally accessible variables.


It’s sort of refreshing to hear the people who write GCC (who I think of
as MAGICAL WIZARDS WHO KNOW EVERYTHING) say that they read some Intel
documentation and it was not clear what it meant! This stuff must really
not be easy.


This C program is a little faster than the Rust version, clocking in at
around 0.44 seconds on my machine. I don’t know why.


### What actual CPU instructions are involved?


I don’t really read assembly, so we’ll need some help to see which are
the Magical Safe Instructions. `perf` is the best program in the
universe, and it can help us with this! `perf record` and `perf annotate` together let us see which instructions in our program are
taking the most time.


```
$ perf record ./counter_with_atomics
$ perf annotate --no-source
       │    ↓ jmp    21 
  0.03 │15:   lock   addl   $0x1,counter
 99.43 │      addl   $0x1,-0x4(%rbp)
  0.13 │21:   cmpl   $0xf423f,-0x4(%rbp)
  0.41 │    ↑ jle    15  

```


and we can try it with the Rust program, too:


```
$ perf record ./rust_counter_atomics
$ perf annotate --no-source
       │       nop
  0.05 │ 50:   mov    0x20(%rbx),%rcx
  0.02 │       lock   incq 0x10(%rcx)
 99.93 │       dec    %rax
       │     ↑ jne    50  

```


So we can see that there’s a `lock` instruction prefix that increments a
variable in each case. Googling for “lock instruction finds us this [x86 instruction set reference](http://x86.renejeschke.de/html/file_module_x86_id_159.html):


> In a multiprocessor environment, the LOCK# signal insures that the
> processor has exclusive use of any shared memory while the signal is
> asserted.


In both cases over 99% of the run time is spent in the instruction right
after that instruction. I’m not totally sure why that is, but it could
be that the `lock` itself is fast, but then once it’s done the memory it
updated needs to be synchronized and the next instruction needs to wait
for that to happen. That’s mostly made up though. If you want to explain
it to me I would be delighted.


(If you’ve heard about compare-and-swap, that’s a similar instruction
that lets you update variables without creating races)


### We are now slightly closer to being concurrency wizards


This was really fun! In January I was talking to a (super nice!) company
that built distributed systems about interviewing there, and they sent
me some questions to answer. One of the questions was something like
“can you discuss the pros and cons of using a lock-free approach for
implementing a thread-safe hashmap?”


My reaction at the time was WHAT ARE YOU EVEN ASKING ME HELP. But these
concurrency explorations make me feel like that question is a lot more
reasonable! Using atomic instructions in this case was way faster than
using a mutex, and I feel like I have a slightly better sense of how all
this works now.


Also when I see a process waiting in a `futex(...` system call when I
strace it, I understand what’s going on a little better! This is
wonderful.


Thanks are due to [Kamal](https://twitter.com/kamalmarhubi) for having
lots of wonderful suggestions, and the people of the ever-amazing #rust
IRC channel. You can see all the code for this post at
[https://github.com/jvns/fun-with-threads/](https://github.com/jvns/fun-with-threads/).
