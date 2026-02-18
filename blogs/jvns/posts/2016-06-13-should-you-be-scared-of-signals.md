---
title: "Should you be scared of Unix signals?"
date: 2016-06-13
url: https://jvns.ca/blog/2016/06/13/should-you-be-scared-of-signals/
slug: should-you-be-scared-of-signals
word_count: 1449
---


Yesterday I said I was scared of Unix signals, and some experienced people who I respect said “no, you should not be! unix signals are a very well known thing!”. I was sort of surprised because I think of signals as being a little scary! Here are some facts I have collected to try to think through this.


### what’s a unix signal?


Signals are a way for Unix processes to communicate! Except for SIGKILL. When you get sent SIGKILL nobody communicates with you, you just die immediately.


But the rest of the signals you’re allowed to install signal handlers for. So! Let’s say you want to handle SIGALRM with `my_awesome_function`


You tell the Linux kernel `signal(SIGALRM, my_awesome_function)`. It remembers. When you get sent SIGALRM:

1. the linux kernel is like “hey, a signal!”
2. It stops your process.
3. It saves all the registers in your process, and runs `my_awesome_function`
4. once `my_awesome_function` is done, it puts everything back and sends you on your way.


on its face, this seems fine. the kernel will put your program back on its feet when it’s done with the signal! no problem!


### what can go wrong if you use signals?


here are a few things. I think I am missing some.

- you need to be careful and make sure that other signals do not arrive while you are handling a signal
- if you’re doing a `read` or `write` system call, and there’s a signal, your read might be interrupted! You will get a return value `EINTR`. This is generally a normal thing that can happen but this weekend I saw a Rust program crash because it did not know how to handle EINTR.
- surprise! now you have a concurrent program! you need to be very careful if you modify anything in your signal handler code because WHO KNOWS what state that thing was in before you changed it.


This paragraph from [this article](https://ldpreload.com/blog/signalfd-is-useless) explains really wonderfully what is difficult about signal handlers:


> If you register a signal handler, it’s called in the middle of whatever code
> you happen to be running. This sets up some very onerous restrictions on what
> a signal handler can do: it can’t assume that any locks are unlocked, any
> complex data structures are in a reliable state, etc. The restrictions are
> stronger than the restrictions on thread-safe code, since the signal handler
> interrupts and stops the original code from running. So, for instance, it
> can’t even wait on a lock, because the code that’s holding the lock is paused
> until the signal handler completes. This means that a lot of convenient
> functions, including the stdio functions, malloc, etc., are unusable from a
> signal handler, because they take locks internally.


Jesse Luehrs pointed out to be that `man 7 signal` has a list of functions that it’s safe to call from signal handlers. (it is perhaps telling that functions are by default unsafe to call from signal handlers :) )


### what important programs use signals?


I wanted to feel better about using signals, so I asked on Twitter what important programs that I trust use signals really extensively.


First, **init**. That’s PID 1 on older Linux systems! It turns out when I press ctrl+alt+delete on my computer, that sends a SIGINT to the init process, which then restarts the machine. I didn’t know that! Cool! Init also responds to a few other signals in various ways.


Next, my **terminal**. You know when you resize your terminal and it reflows all the text? That’s it receiving a whole bunch of SIGWINCH (window change) signals, and updating its size and then redrawing everything accordingly. This one made me feel better because a terminal is a Complicated Program, but it is totally handling lots of signals okay all the time!


When a child process of yours exits, you get a SIGCHLD signal. I think this is how my shell knows to report to me that a process has exited.


[@geofft](https://twitter.com/geofft) also said that “**the JVM** uses signal handlers to implement cross-thread stop-the-world GC”


A lot of programs (like [unicorn](http://unicorn.bogomips.org/SIGNALS.html)) handle signals like SIGHUP to **gracefully restart**. Apparently it uses `SIGTTIN` and `SIGTTOU` to increment and decrement the number of worker processes? Apparently `TTIN` stands for “teletype input”. POSIX is weird! We will never escape teletypes?


**SIGSEGV** is a very important signal. It happens when your program tries to access memory that it does not have. A normal reaction to this signal is to die. But you can also do weird stuff! The [libsigsegv library](https://www.gnu.org/software/libsigsegv/) gives a few examples of what you can use it to do:

- allocate more memory
- read some data from disk into that memory
- do something with garbage collection (but what? I’m confused about this still.)


my friend dave pointed me to [this code in an emulator that uses SEGV to notice when a video buffer is updated](https://github.com/cebix/macemu/blob/b58a9260bd1422a28e4c0b7b6bb71d26603bc3e1/BasiliskII/src/CrossPlatform/video_vosf.h).


Another really common reason to catch SIGSEGV is to not actually recover (doing this properly is tricky!), but to catch crashes to provide a better error message or get a backtrace. Here’s [example code](https://github.com/crawl/crawl/blob/master/crawl-ref/source/crash.cc) and [the debug output it produces](http://crawl.berotato.org/crawl/morgue/grandjackal/crash-grandjackal-20160608-001606.txt). Thanks to [Jesse](https://tozt.net/) for this example!


Phew. Okay, I think we believe that signals are important now.


### hundreds of signals per second


The whole reason I started thinking about signals in the first place is – I looked at the source code for [stackprof](https://github.com/tmm1/stackprof), a Ruby profiling tool. Basically what it does is it uses the `setitimer` Linux system call to say “Hi! Please send me a signal every 2 milliseconds!” and then it records a stack trace every time it gets a signal.


I thought this was cool because the C code for this program is actually pretty easy to read.


But! Getting hundreds of signals a second is really quite different from just one signal every now and then. This makes me feel worried because your program is being constantly interrupted all the time. This has some overhead, and maybe it causes problems with IO because your reads get interrupted all the time?


### signalfd


Are you scared of your program being arbitrarily interrupted at any point? In Linux, there is a thing called `signalfd` for you!.Here’s what the man page says:


> signalfd()  creates  a  file descriptor that can be used to accept
> signals targeted at the caller.  This provides an alternative to the use
> of a signal handler or sigwaitinfo(2), and has the advantage that the
> file  descriptor  may  be  monitored  by  select(2), poll(2), and
> epoll(7).


I’ve still never used this but I find the idea appealing! The idea is that you can have a thread that is constantly waiting for signals to handle.


I like this because it means you have a concurrent program (the thread is waiting for a signal), but it’s much more explicit that you’re running a concurrent program instead of having a weird signal handler that exists outside of space and time.


However apparently there are problems with signalfd and it is not a land of rainbow goodness. When I googled it I came across an article by the aforementioned @geofft called [signalfd is useless](https://ldpreload.com/blog/signalfd-is-useless) which talks about some annoying / nonobvious things about using it. The [hacker news discussion on that article](https://news.ycombinator.com/item?id=9564975) is also mostly civil & interesting.


### signals are not trivial, but it looks like they’re possible!


So after seeing how all these important programs use signals, I think I believe it’s possible to use signals for Very Important Things and still stay safe, as long as you’re careful. I still don’t feel like I know the complete list of things you need to be careful of when using signals though. If you know a good List Of What Can Go Wrong With Signals I would like to know about it!


I’m also still not sure if it’s a reasonable idea to receive hundreds of signals a second. Though stackprof does mostly work, so I guess it can’t be that unreasonable!


### don’t be afraid! be careful!


I find topics like this interesting because – I don’t like having Fears and Uncertainties about things that I can’t base in fact. Like – it’s unreasonable to say “threads are hard! never use threads! it is scary”. Threads are important! Sometimes you need to use them! It is possible to write correct threaded programs! Instead it is better to say “this code is not thread safe because of SPECIFIC REASON! it will not work!”.


I feel like getting one bajillion replies on twitter helped a bit with creating facts out of my fears about signals :)
