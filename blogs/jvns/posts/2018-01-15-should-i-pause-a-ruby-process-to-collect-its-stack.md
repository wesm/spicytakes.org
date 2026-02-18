---
title: "Should I pause a Ruby process to collect its stack?"
date: 2018-01-15
url: https://jvns.ca/blog/2018/01/15/should-i-pause-a-ruby-process-to-collect-its-stack/
slug: should-i-pause-a-ruby-process-to-collect-its-stack
word_count: 1219
---


Hello! This post is about a question about my Ruby profiler that I’ve been wondering about for a few
weeks now – when I’m collecting a stack trace from a Ruby process, should I use ptrace to pause it
first?


Today for the first time I made some progress on answering this question, so I wanted to write down
what I’ve learned so far!


As a quick refresher on “how profilers work” – basically 100% of the work the profiler does while
it’s running is collecting stack traces. It collects a stack trace, waits 10 milliseconds, and
repeats that forever until it’s asked to stop. Then it generates a useful report about what your
program is doing from all those stack traces.


So collecting stack traces correctly is very important! :)


summary of the interesting things I found out (if you don’t want to read this whole post)

- pausing a Ruby process with ptrace **doesn’t** completely prevent stack trace sampling errors in
my program
- pausing **does** reduce the error rate significantly (pausing: ~1/10,000, not pausing:
~1/1000). My sample size here is extremely small though! Also there might be more errors when not
pausing that I’m not counting.
- the errors that happen when the process is paused happen when we pause the Ruby interpreter during
functions like `vm_call_iseq_setup` and `vm_call_iseq_setup_normal_0start_0params_0locals`


### Why pause a process with ptrace?


The reason to pause a process while collecting its stack is pretty simple – what if, while I’m
collecting the process’s stack, the stack **changes**?


If the stack changes while I’m in the middle of collecting it, I might fail to get the stack. That’s
no good! Initially, it seems pretty obvious that I should pause the process somehow when collecting
the stack.


But I think there’s something interesting about profiling Ruby programs in particular which is that
Ruby programs are relatively slow! Like, trying to collect stack traces from a C program without pausing it
at all I think would be a losing battle.


But with a Ruby program, it turns out that not pausing the Ruby process isn’t completely
unreasonable! After all, my profiler in Rust is fast, so it has a pretty significant speed advantage
over the Ruby program. It’s still a race, but the profiler has a pretty good chance of winning. But
how good?


### What happens if I **don’t** pause the Ruby process I’m profiling?


I just collected 15,000 stack traces from `rubocop` (a Ruby linter) at 100 traces per second, and
while doing that got 20 errors. That’s a little more than 1 error in 1000 stacks.


I think this is already pretty interesting – an error rate of 1 in 1000 isn’t nothing, but it’s
also maybe not the end of the world! After all, not pausing the program is a good thing for
overhead, and this profiler is a statistical profiler anyway. So if I lose 1 stack trace in 1000,
that won’t change overall results much.


It’s also possible that some of those stack traces are incorrect and I’m just not noticing, which is
worrying. So I still have some work to do there.


Next, let’s talk about what happens when


### ptracing a process in Rust (it’s very easy!)


Today I did an experiment where I tried pausing the Ruby process while collecting a stack!


Using ptrace to pause a process is **really easy**. To show how easy it is: Here’s all the code I
wrote to support ptracing (I used the nix trace). The only unusual thing here is this `PtracePid`
struct and this `impl Drop` thing. What’s that?


Well – I wanted to make absolutely sure that after I stopped the Ruby process, I restarted it
again. Implementing a custom `Drop` trait on a struct in Rust means that when that struct goes out
of scope for any reason, the `drop()` method will be called. I believe this pattern is called
[RAII](https://rustbyexample.com/scope/raii.html). So that’s what I did!


Here’s the implementation of my tiny struct and the `Drop` trait:


```
struct PtracePid {
    pid: pid_t,
}

impl PtracePid {
    fn attach(&self) {
        // ATTACH attaches to the process and pauses it
        nix::sys::ptrace::ptrace(ptrace::PTRACE_ATTACH, nix::unistd::Pid::from_raw(self.pid), 0 as * mut c_void, 0 as * mut c_void);
    }

    fn detach(&self) {
        // DETACH detaches and lets the process keep going 
        nix::sys::ptrace::ptrace(ptrace::PTRACE_DETACH, nix::unistd::Pid::from_raw(self.pid), 0 as * mut c_void, 0 as * mut c_void);
    }
}

impl Drop for PtracePid {
    fn drop(&mut self) {
        self.detach();
    }
}

```


And here’s how I called the code:


```
{
    let ptrace_struct = PtracePid{pid: pid};
    ptrace_struct.attach();
    /* 
      code to get a stack trace goes here
    */
    // .detach() gets called automatically when this is done
}

```


So easy!


### Pausing the Ruby process doesn’t completely prevent errors!


This was the most surprising thing to me! I thought that if I paused my process before collecting a
stack trace, it would always Just Work. Instead, I still got a small number of errors! Why??


I went and took a shower to think about it, and then came up with a way to figure out why!


Since we’re ptracing the process (it’s stopped!), we can get the instruction pointer of the Ruby
process to see what instruction it’s running.


Here’s what that looks like (just 3 lines of code, using the nix and libc crates! Very easy!). We
use ptrace and the `PTRACE_GETREGS` request to get the instruction pointer and print it out.


```
let mut regs = unsafe {std::mem::zeroed::<libc::user_regs_struct>() };
nix::sys::ptrace::ptrace(ptrace::PTRACE_GETREGS, nix::unistd::Pid::from_raw(pid), 0 as * mut c_void, &mut regs as *mut user_regs_struct as * mut c_void);
println!("instruction pointer: {:x}", regs.rip);

```


Once I had the instruction pointer (`0x5647fbb7bcbf` for example), I attached to the process with gdb instead and ran


```
(gdb) x/10x 0x5647fbb7bcbf
0x5647fbb7bcbf <vm_call_iseq_setup+351>:	0xd0588949	0x00e48e0f	0x29480000	0xf10148d1
0x5647fbb7bccf <vm_call_iseq_setup+367>:	0x3ce1c148	0x3fe9c148	0x41f93944	0x41cf470f

```


That’s interesting! I know that an `iseq` is a thing I need to , so it makes sense that if it’s
running some sort of “iseq setup” then maybe the stack in memory is not in a totally valid state
yet?


I ran the experiment a couple more times and got similar answers:


```
(gdb) x/10x 0x5636be0c4cb3
0x5636be0c4cb3 <vm_call_iseq_setup+339>:	0xe870894d	0xf840c749	0x00000000	0xd0588949
0x5636be0c4cc3 <vm_call_iseq_setup+355>:	0x00e48e0f	0x29480000	0xf10148d1	0x3ce1c148
0x5636be0c4cd3 <vm_call_iseq_setup+371>:	0x3fe9c148	0x41f93944

```


```
(gdb) x/5x 0x5622c3d02417
0x5622c3d02417 <vm_call_iseq_setup_normal_0start_0params_0locals+87>:	0xe042894c	0xe852894c	0xf842c748	0x00000000

```


So that’s in `vm_call_iseq_setup_normal_0start_0params_0locals` and `vm_call_iseq_setup`. This is
still confusing to me – I’ve spent half an hour trying to read the Ruby interpreter code to see why
the stack during these code paths might be invalid, but haven’t figured it out yet – I understand
how in `vm_push_frame` the stack could be invalid at some points (because it’s putting a new stack frame onto the
stack), but neither of these addresses are in `vm_push_frame`.


It does definitely seem like there are points during execution of the Ruby interpreter when the
stack is not valid though. That’s fine! I can just drop a few stack traces, say “whoops, those
didn’t work”, and move on. That is the joy of having a sampling profiler.


### that’s all for now


Will keep trying to figure this out and I’ll post more if I figure out more! Also if you understand
this better and want to tell me about it I’d be happy to hear from you!
