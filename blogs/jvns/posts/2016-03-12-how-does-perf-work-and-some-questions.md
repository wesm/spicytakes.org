---
title: "How does perf work? (in which we read the Linux kernel source)"
date: 2016-03-12
url: https://jvns.ca/blog/2016/03/12/how-does-perf-work-and-some-questions/
slug: how-does-perf-work-and-some-questions
word_count: 928
---


perf is a profiling tool for Linux, that I’ve written about [a few times](https://jvns.ca/categories/perf) on this blog before. I was interviewed on [a podcast](http://embedded.fm/episodes/141) recently where the host asked me “so, julia, tell me how perf works!” and I gave a sort of unsatisfying answer “you know, sampling?”.


So it turns out I don’t really know how perf works. And I like knowing how stuff works. Last week I read some of the [man page for `perf_event_open`](http://man7.org/linux/man-pages/man2/perf_event_open.2.html), the system call that perf uses. It’s 10,000 words but pretty helpful! I’m still quite confused about perf, so I’m going to tell you, fair reader, what I know, and then maybe you can help me out with my questions.


There is not a lot of documentation for perf. The best resource I know is on [Brendan Gregg’s site](http://www.brendangregg.com/perf.html), but it does not answer all the questions I have! To answer some of these questions, we’re going to read the Linux kernel source code. Because it’s Saturday night.


### Hardware counters


So, let’s imagine you want to know exactly how many CPU instructions happen when you run `ls`. It turns out that your CPU stores information about this kind of thing! And perf can tell you. Here’s what the answer looks like, from `perf stat`.


```
$ sudo perf stat ls
         1,482,453 instructions              #    0.48  insns per cycle        


```


But how does that *work*? Well, the [Wikipedia page on hardware performance counters](https://en.wikipedia.org/wiki/Hardware_performance_counter) mentions


> One of the first processors to implement such counter and an associated
> instruction `RDPMC` to access it was the Intel Pentium, but they were not
> documented until Terje Mathisen wrote an article about reverse engineering
> them in Byte July 1994: [1]


We can use [http://livegrep.com](https://livegrep.com/search/linux) to search the Linux kernel for the `rdpmc` instruction. Here’s it being used in a cryptic [header file called msr.h](https://github.com/torvalds/linux/blob/v4.3/arch/x86/include/asm/msr.h#L158-L164)


```
static inline unsigned long long native_read_pmc(int counter)
{
    DECLARE_ARGS(val, low, high);

    asm volatile("rdpmc" : EAX_EDX_RET(val, low, high) : "c" (counter));
    return EAX_EDX_VAL(val, low, high);
}

```


This is AWESOME. Maybe this is how Linux reads hardware counters and gives them back to us in `perf stat`!! Further grepping for uses of `native_read_pmc` reveals that we read hardware counters via `rdpmcl` in [x86/kernel/cpu/perf_event.c](https://github.com/torvalds/linux/blob/v4.3/arch/x86/kernel/cpu/perf_event.c#L84).


This code is a little impenetrable to me, but here’s a hypothesis for how this could work. Let’s say we’re running `ls`. This code might get scheduled on and off the CPU a few times.


So! Here’s what I think this looks like.


```
kernel: ok let's run ls for a while
kernel: CPU! Start counting CPU instructions!
CPU: <complies silently>
kernel: <runs ls>
ls: yayyyyyyyyyy
kernel: <stops running ls>
kernel: CPU! How many instructions was that! (`rdpmc`)
CPU: 10,200!
kernel: <increments counter by 10,200>

```


One important outcome of this, if I understand correctly is – hardware counters are exact counters, and they’re low enough overhead that the kernel can just always run `rdpmc` every time it’s done running a piece of code. There’s no sampling or approximations involved.


### Sampling software events


The core of perf events looks like it’s in [kernel/events/core.c](https://github.com/torvalds/linux/blob/v4.3/kernel/events/core.c). This file includes the definition of the [`perf_event_open`](https://github.com/torvalds/linux/blob/v4.3/kernel/events/core.c#L8107) system call, on line 8107. Files with 10,000 lines of C code are not my specialty, but I’m going to try to make something of this.


My goal: understand how perf does sampling of CPU events. For the sake of argument, let’s pretend we only wanted to save the state of the CPU’s registers every time we sample.


We know from the [`perf_event_open` man page](http://man7.org/linux/man-pages/man2/perf_event_open.2.html) that perf writes out events to userspace (“hi! I am in julia’s awesome function right now!”). It writes events to a mmap’d *ring buffer*. Which is some data structure in memory. Okay.


Further inspection of this 10,000 line `core.c` file reveals that the code outputs data to userspace in the `perf_event_update_userpage` function.


So, let’s find the code that copies all the x86 registers into userspace! It turns out it’s not too hard to find – it’s in this file called [perf_regs.c](https://github.com/torvalds/linux/blob/v4.3/arch/x86/kernel/perf_regs.c#L114-L118). There are like 15 registers to copy! Neat.


In this case it makes sense that we sample – we definitely couldn’t save all the registers every instruction. That would be way too much work!


So now I can see a little tiny bit of the code that perf uses to do sampling. This isn’t terribly enlightening, but it does make me feel better.


### Questions

- when does perf do its sampling? is it when the process gets scheduled onto the CPU? how is the sampling triggered? I am completely confused about this.
- what is the relationship between perf and kprobes? if I just want to sample the registers / address of the instruction pointer from `ls`’s execution, does that have anything to do with kprobes? with ftrace? I think it doesn’t, and that I only need kprobes if I want to instrument a kernel function (like a system call), but I’m not sure.
- are kprobes and ftrace the same kernel system? I feel like they are but I am confused.


### reading kernel code: not totally impossible


I probably skimmed like 4000 lines of Linux kernel code (the perf parts!) to write this post, in 3 hours. There are definitely at least 20,000 lines of code related to perf. Maybe 100,000? I do not have the Linux source on my computer – I used livegrep and github to look at it.


I only understood probably 10% of what I looked at, but I still learned some things about how perf works internally! This is neat.
