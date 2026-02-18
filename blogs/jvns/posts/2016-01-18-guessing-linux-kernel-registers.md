---
title: "Guessing Linux kernel registers"
date: 2016-01-18
url: https://jvns.ca/blog/2016/01/18/guessing-linux-kernel-registers/
slug: guessing-linux-kernel-registers
word_count: 761
---


I have a long-standing project to try to learn to use ftrace, a Linux kernel tracing tool. As usual when I want to learn more, I turned to one of [Brendan Gregg](http://brendangregg.com)’s tools – the [perf-tools](https://github.com/brendangregg/perf-tools/) repo on Github. There’s a whole delightful directory of [examples](https://github.com/brendangregg/perf-tools/blob/master/examples/). It’s the best.


He has a lot of tools that are ready to use and easy to understand – for instance, you can use execsnoop to see every program that’s being executed. Those are awesome.


Then there are some that require… more work. I was interested in ftrace, and I was using his kprobe script to trace system calls and their arguments.


I started out by running `sudo kernel/kprobe 'p:SyS_read'` to tell me every time the `read` system call happened. This gives me output like


```
 Chrome_ChildIOT-8978  [000] d...  7402.349880: SyS_read: (SyS_read+0x0/0xa0)
 Chrome_ChildIOT-4102  [002] d...  7402.349922: SyS_read: (SyS_read+0x0/0xa0)
            Xorg-1853  [001] d...  7402.349962: SyS_read: (SyS_read+0x0/0xa0)
            Xorg-1853  [001] d...  7402.349969: SyS_read: (SyS_read+0x0/0xa0)
 Chrome_IOThread-4092  [003] d...  7402.349974: SyS_read: (SyS_read+0x0/0xa0)

```


But WHAT FILE DID IT READ? This is not good at all.


In the [example](https://github.com/brendangregg/perf-tools/blob/master/examples/kprobe_example.txt#L108-L127), he says, on the open system call.


> Here I guessed that the mode was in register %cx, and cast it as a 16-bit
> unsigned integer (":u16"). Your platform and kernel may be different, and the
> mode may be in a different register. If fiddling with such registers becomes
> too painful or unreliable for you, consider installing kernel debuginfo and
> using the named variables with perf_events “perf probe”.


This was wizardry. How could he *guess* that the mode of a file was in the register `%cx`? What even are the registers? This makes no sense.


I partly figured this out and got more information about the `read` system calls, so I will now tell you!


### what even is a register


I know that registers are what the CPU uses to store data in when calculating things. But how many even are there? How do I guess which one is right?


First, I found [this page describing x86 registers](http://www.eecg.toronto.edu/~amza/www.mindsec.com/files/x86regs.html). It tells me that there are


```
General registers
EAX EBX ECX EDX

Segment registers
CS DS ES FS GS SS

Index and pointers
ESI EDI EBP EIP ESP

```


From the description, the segment registers seem safe to ignore! Awesome. The instruction pointer and the stack pointer tell me what instruction is running right now and where the stack is. I also don’t care about that. So that leaves me with only 7 registers to worry about (eax, ebx, ecx, edx, esi, edi, and ebp). That’s way better.


### printing the registers


So before we were running `sudo kernel/kprobe 'p:SyS_read'`. We can also print the registers for the read system call! Here goes. For some reason we need to take off the `e`.


```
sudo kernel/kprobe 'p:SyS_read ax=%ax bx=%bx cx=%cx dx=%dx si=%si di=%di' | grep chrome-4095
          chrome-4095  [001] d...  7665.279404: SyS_read: (SyS_read+0x0/0xa0) ax=0 bx=2cb4726adec0 cx=0 dx=2 si=7fff1282f70e di=9
          chrome-4095  [001] d...  7665.279562: SyS_read: (SyS_read+0x0/0xa0) ax=0 bx=2cb4726adec0 cx=0 dx=2 si=7fff1282f70e di=9
          chrome-4095  [002] d...  7665.400594: SyS_read: (SyS_read+0x0/0xa0) ax=0 bx=2cb4726adec0 cx=0 dx=2 si=7fff1282f70e di=9

```


Let’s compare this to the output of strace:


```
sudo strace -e read -p 4095
Process 4095 attached - interrupt to quit
read(9, "!", 2)                         = 1
read(9, "!", 2)                         = 1
read(9, "!", 2)                         = 1

```


Ok, awesome! In the output of `strace`. I know that `9` is the file descriptor, 2 is the length to read, and the middle value is the string. This must mean that `%di` is the file descriptor, and `%dx` is the amount of data to read!


I can label those now and be a register-guessing-wizard like Brendan Gregg!


```
sudo kernel/kprobe 'p:julia_smart_read SyS_read fd=%di:u16 bytes_to_read=%dx' | grep chrome-4095
          chrome-4095  [003] d...  7854.905089: julia_smart_read: (SyS_read+0x0/0xa0) fd=9 bytes_to_read=2
          chrome-4095  [003] d...  7854.945585: julia_smart_read: (SyS_read+0x0/0xa0) fd=9 bytes_to_read=2
          chrome-4095  [002] d...  7854.945852: julia_smart_read: (SyS_read+0x0/0xa0) fd=9 bytes_to_read=2

```


So now I know which file descriptors are being read!


The advantage of using ftrace instead of strace is that the overhead is way lower: when I strace `find` it makes it 20x slower, but with ftrace it’s totally okay. I’m still not sure where the string that we read is (I think it’s in `%si`, though!)


Now I am one step closer to being able to trace system calls with less overhead. Guessing registers is really tedious but it seems to be totally possible!


**update**: turns out you don’t have to guess at all! the registers used for system calls are always the same :D. [here is a table with all the answers ❤](http://blog.rchapman.org/post/36801038863/linux-system-call-table-for-x86-64)
