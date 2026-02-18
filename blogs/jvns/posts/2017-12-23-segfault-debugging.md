---
title: "Debugging a segfault in my Rust program"
date: 2017-12-23
url: https://jvns.ca/blog/2017/12/23/segfault-debugging/
slug: segfault-debugging
word_count: 2277
---


Hello! Yesterday I finished debugging a segfault. It was (in retrospect) a pretty easy thing to fix
but I learned a few things from fixing it and so I thought I’d share.


I think this was a great example of Allison Kaptur’s [love your bugs](http://akaptur.com/blog/2017/11/12/love-your-bugs/) principle – it was a relatively simple
bug, but it was a new class of bug **for me** and so it was a good learning opportunity!


### why do segfaults happen?


Really quickly – a segfault is when your program tries to access an area that it’s not allowed to
happen. This can happen for a few reasons:

- You tried to dereference (“access”) a null pointer (`0x0` is an address! dereferencing it does not
work!)
- You did an out-of-bounds memory access (like you went past the end of an array) and some code
somewhere else set up “guard pages” around that memory so that your program would segfault. You can
protect memory with the [mprotect system call](https://linux.die.net/man/2/mprotect). This is a
useful thing because it’s often better to fail early than to access uninitialized memory.
- You accidentally put something into a pointer that wasn’t supposed to be a pointer (like.. just
some random bytes) and then tried to dereference that pointer
- You tried to write to a read-only part of memory


I haven’t dealt with segfaults much so having a rough categorization of the possible reasons is
really helpful to me. There are probably more reasons I don’t know about.


### why do segfaults happen in Rust?


Segfaults happen in Rust for all the same reasons, but Rust also offers compile-time guarantees that
your program won’t segfault. So, as far as I understand it, there are 2 possible reasons your
**Rust** program can segfault:

1. you wrote unsafe code in a way that violates Rust’s memory safety guarantees
2. The Rust compiler has a bug


option 1 is obviously much more likely, and of course it’s what was happening in my program: I had
some unsafe code in my program and I’d done something wrong. So it was just a matter of figuring out
what I’d done wrong exactly in my unsafe code!


### my segfault


So, I have a program that grabs a stack trace from a Ruby program. The second time it got a stack trace,
(not the first!) it was always segfaulting. here’s what that looked like in my shell (fish). I
already knew what “terminated by signal SIGSEGV” (it’s a segfault!) meant so that was good!


```
fish: Process 29420, “sudo” “sudo  ./target/debug/ruby-stack…”
terminated by signal SIGSEGV (Address boundary error)

```


I’m going to go through the steps I went through to debug this segfault. It’s artifically cleaned up
a bit to be more readable (when I was actually debugging it was a bit more confusing/chaotic), but
it’s mostly accurate.


### step 1: figure out where the segfault is happening


I started out by putting in a lot of print statements to figure out where the segfault was happening
exactly. It turned that it happened after the function [get_stack_trace returned](https://github.com/jvns/ruby-stacktrace/blob/13d61a6e2959a70f3dd11b0bab1c84f633e16bc6/src/lib.rs#L230).


I knew that in Rust, the compiler inserts code to deallocate (“drop”) any pointers that need to be
deallocated at the end of the function. So I figured that my segfault was happening during
deallocation somewhere (spoiler: this was true.)


### step 2: run valgrind


I’d never run valgrind before, but I knew it was a tool for detecting memory problems (like
use-after-free or using uninitialized memory). So I decided to run valgrind to see if it would help
me.


Here’s what the output of valgrind looked like: It’s kind of big but I think it’s interesting so I’m
going to include all of it.


```
==24054== Invalid read of size 8
==24054==    at 0x70BFAF: arena_run_size_get (arena.c:2139)
==24054==    by 0x70BFAF: arena_run_dalloc (arena.c:2158)
==24054==    by 0x70BFAF: arena_dalloc_large_locked_impl (arena.c:3059)
==24054==    by 0x70BFAF: je_arena_dalloc_large (arena.c:3076)
==24054==    by 0x15CBDD: _$LT$alloc..heap..Heap$u20$as$u20$alloc..allocator..Alloc$GT$::dealloc::hdb5e62b8e81170c3 (heap.rs:104)
==24054==    by 0x15E1CF: _$LT$alloc..raw_vec..RawVec$LT$T$C$$u20$A$GT$$GT$::dealloc_buffer::h21ec0f0ea4d7e8ea (raw_vec.rs:687)
==24054==    by 0x15F544: _$LT$alloc..raw_vec..RawVec$LT$T$C$$u20$A$GT$$u20$as$u20$core..ops..drop..Drop$GT$::drop::h680e0cd5f2ba0db0 (raw_vec.rs:696)
==24054==    by 0x15AA24: core::ptr::drop_in_place::ha5d166fd802b1dc7 (in /home/bork/work/ruby-stacktrace/target/debug/ruby-stacktrace)
==24054==    by 0x15B02E: core::ptr::drop_in_place::hba5f72a97ec2ed1d (in /home/bork/work/ruby-stacktrace/target/debug/ruby-stacktrace)
==24054==    by 0x154B17: ruby_stacktrace::stack_trace::get_stack_trace::h8cbbf1b7ce92f028 (lib.rs:237)
==24054==    by 0x136BC3: ruby_stacktrace::main::ha677e8f07d7d709d (ruby-stacktrace.rs:69)
==24054==    by 0x6FA24E: __rust_maybe_catch_panic (lib.rs:101)
==24054==    by 0x6E32D3: UnknownInlinedFun (panicking.rs:459)
==24054==    by 0x6E32D3: catch_unwind<closure,()> (panic.rs:365)
==24054==    by 0x6E32D3: std::rt::lang_start::hb3d6b270f8135e26 (rt.rs:58)
==24054==    by 0x136FBD: main (in /home/bork/work/ruby-stacktrace/target/debug/ruby-stacktrace)
==24054==  Address 0x170b02918 is not stack'd, malloc'd or (recently) free'd
==24054== 
==24054== Invalid write of size 8
==24054==    at 0x703C63: arena_run_heap_remove (arena.c:114)
==24054==    by 0x70C009: arena_run_coalesce (arena.c:2061)
==24054==    by 0x70C009: arena_run_dalloc (arena.c:2188)
==24054==    by 0x70C009: arena_dalloc_large_locked_impl (arena.c:3059)
==24054==    by 0x70C009: je_arena_dalloc_large (arena.c:3076)
==24054==    by 0x15CBDD: _$LT$alloc..heap..Heap$u20$as$u20$alloc..allocator..Alloc$GT$::dealloc::hdb5e62b8e81170c3 (heap.rs:104)
==24054==    by 0x15E1CF: _$LT$alloc..raw_vec..RawVec$LT$T$C$$u20$A$GT$$GT$::dealloc_buffer::h21ec0f0ea4d7e8ea (raw_vec.rs:687)
==24054==    by 0x15F544: _$LT$alloc..raw_vec..RawVec$LT$T$C$$u20$A$GT$$u20$as$u20$core..ops..drop..Drop$GT$::drop::h680e0cd5f2ba0db0 (raw_vec.rs:696)
==24054==    by 0x15AA24: core::ptr::drop_in_place::ha5d166fd802b1dc7 (in /home/bork/work/ruby-stacktrace/target/debug/ruby-stacktrace)
==24054==    by 0x15B02E: core::ptr::drop_in_place::hba5f72a97ec2ed1d (in /home/bork/work/ruby-stacktrace/target/debug/ruby-stacktrace)
==24054==    by 0x154B17: ruby_stacktrace::stack_trace::get_stack_trace::h8cbbf1b7ce92f028 (lib.rs:237)
==24054==    by 0x136BC3: ruby_stacktrace::main::ha677e8f07d7d709d (ruby-stacktrace.rs:69)
==24054==    by 0x6FA24E: __rust_maybe_catch_panic (lib.rs:101)
==24054==    by 0x6E32D3: UnknownInlinedFun (panicking.rs:459)
==24054==    by 0x6E32D3: catch_unwind<closure,()> (panic.rs:365)
==24054==    by 0x6E32D3: std::rt::lang_start::hb3d6b270f8135e26 (rt.rs:58)
==24054==    by 0x136FBD: main (in /home/bork/work/ruby-stacktrace/target/debug/ruby-stacktrace)
==24054== Address 0x8 is not stack'd, malloc'd or (recently) free'd

```


So there were 2 errors here: an invalid read and an invalid write. It complained about 2 addresses:
`Address 0x170b02918` and `Address 0x8`. I knew both of those were invalid addresses but I had no
idea where they were coming from.


valgrind was pretty useful though! It did confirm that the segfault was definitely happening during
deallocation – you can see `drop_in_place`, `Drop`, `dealloc_buffer`, `je_arena_dealloc_large`…
in the stack trace. So SOMETHING definitely was going wrong when deallocating this memory. But what?


### step 3: identify which deallocation exactly was the problem


A cool thing you can do in Rust is – you can run `std::mem::forget(some_variable)`. This tells Rust
basically to leak that memory and to not deallocate it. I had a variable called `cfps` that I
suspected was the problem. And sure enough, when I added `std::mem::forget(cfps)`, the segfault
stopped happening. Nice! I still didn’t know what I’d done **wrong** yet but I knew which variable
was the problem.


### step 4: try switching allocators


So I noticed that my segfault was happening inside of jemalloc somewhere. Someone on the internet
somewhere said that valgrind doesn’t work well with jemalloc (I don’t know if that’s actually
true!), so I thought I’d try switching allocators to see if valgrind would give me less confusing
results.


Here’s how you switch to the system allocator.


```
#![cfg_attr(rustc_nightly, feature(test))]
#![feature(alloc_system)]

#![feature(alloc_system)]
#![feature(global_allocator, allocator_api)]

extern crate alloc_system;

use alloc_system::System;

#[global_allocator]
static A: System = System;

```


When I switched to the system allocator a very surprising thing happened: my program didn’t segfault
anymore. What? Why????


### step 5: WHY DOES IT SEGFAULT WITH JEMALLOC BUT NOT THE SYSTEM ALLOCATOR


step 5 was not a constructive step but instead just a lot of confusion. I did not know how this
could happen and I didn’t have an idea for a next step.


I tweeted “aaa my program segfaults when I compile it with jemalloc but when I switch to the system
allocator to try to debug it works fine??”. It was like 1:30am so I went to sleep.


### step 6: reproduce my weird jemalloc problem in a minimal way


I was Very Confused at this point so I decided, well, maybe I can ask someone to help me. But in
order to ask someone for help I needed to take my chaotic mess of a program and show someone a
simple program with the same problem: “it segfaults with jemalloc but not with system malloc”.


I managed to reproduce my issue on the Rust playground in a really simple way:


Basically this program tries to cast a 560-byte vec into a vec with 7 elements, where each element
is an 80-byte struct.

- [system malloc version (no segfault)](https://play.rust-lang.org/?gist=72152fe80acd41bd68c5d0be7ca0dc10&version=nightly)
- [jemalloc version (segfaults)](https://play.rust-lang.org/?gist=ee9b04e4d74818400ac21b025d029c30&version=nightly)


Nice! I felt really happy with myself: I’d taken the weird confusing behavior that I didn’t
understand and gotten it to happen in a very small self-contained program (less than 50 lines!).


### step 7: realize what I did wrong


I started writing a question for the Rust forum to ask for help figuring out what I did wrong. As
often happens when I try to explain what’s going on in writing, halfway through writing the question
I figured it out for myself.


This is the offending code. Basically it takes a vector of 560 bytes and unsafely changes it into a
vector of 7 80-byte structs.


```
// make a vector with 560 bytes
let mut ret: Vec<u8> = Vec::with_capacity(560);
for i in 0..560 {
    ret.push(i);
}

let p = ret.as_mut_ptr();

// make a 7-element vector of 80-byte structs instead
// (7 * 80 = 560)
let rebuilt: Vec<size_80_struct> = unsafe { 
    mem::forget(ret);
    Vec::from_raw_parts(
        p as *mut size_80_struct,
        7,
        560,
        )
};

```


it turns out that there are 2 things wrong with this code

1. the third argument to `from_raw_parts` is the length, not the number of bytes (so it should be 7,
not 560)
2. I went and read the `Vec::from_raw_parts` docs for the 20th time and finally read this: **`ptr's T needs to have the same size and alignment as it was allocated with.`**. `size_80_struct` definitely does not have the same size as a byte so that’s no good.


### how I fixed it


Basically instead of trying to cast my memory by creating a new vec, I created a slice instead.


```
let mut cfps: Vec<u8> = get_cfps(&thread, source_pid);
let slice: &[rb_control_frame_struct] = unsafe { std::slice::from_raw_parts(cfps.as_mut_ptr() as *mut rb_control_frame_struct, cfps.capacity() as usize / mem::size_of::<rb_control_frame_struct>() as usize) };

```


I don’t `mem::forget` the vec anymore, I just let create a slice view of it, iterate over that slice
and then let Rust deallocate the `Vec<u8>` at the end of the function.


And my program doesn’t segfault for now! The reason this works (and is safe!) is that `Vec` are
always backed by contiguous memory – I was worried that they weren’t, but literally the first
sentence in the Rust documentation on `Vec`s says:


> A contiguous growable array type, written Vec but pronounced ‘vector’.


So since a Vec is contiguous memory I can just cast it to a slice and iterate over that slice
safely. I think.


### things I learned


**segfaulting is a feature**. When I complained that this code segfaulted with jemalloc but not libc
malloc, someone made a comment like – “yeah, jemalloc detects things that valgrind doesn’t”. So in
a way, the program that segfaulted was **better** than the program that didn’t, because it was
picking up a subtle problem that could bite me later if I didn’t fix it. I think this is the same
reason people like to use mprotect.


**asan/tsan exist**:: There are things in clang called “ThreadSanitizer/AddressSanitizer” (“tsan”/“asan”) that can do sorta the same thing as valgrind does, but with way less overhead. I did not get them to work this time around but there’s documentation about how to use them with Rust  at [https://github.com/japaric/rust-san](https://github.com/japaric/rust-san) and it seems really cool.


**leaking memory is safe**. I was kind of surprised to learn that leaking memory is safe in Rust (you
can do it on purpose with `mem::forget`!). I think usually safe Rust code won’t have leaks but it’s not a strict guarantee. Rust also **doesn’t** guarantee that you code won’t segfault if you write safe code!! (“we install a guard page after the stack to safely terminate the program with a segfault on stack overflows”) The best reference for this is in the official Rust documentation: [Behavior considered undefined](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) and [Behavior not considered unsafe](https://doc.rust-lang.org/reference/behavior-not-considered-unsafe.html).


When I originally read those docs I thought that “undefined behavior” and “unsafe” were synonyms. It
turns out “undefined behavior” and “unsafe” are closely related but not the same thing!  Manish
Goregaokar wrote a [nice explanation of the difference between undefined and unsafe](https://manishearth.github.io/blog/2017/12/24/undefined-vs-unsafe-in-rust/) in response to
this post. ([also on twitter](https://twitter.com/ManishEarth/status/944787133025411072))


This is a bit confusing to me because safe Rust programs usually **won’t** have memory leaks or
segfault, and that’s part of Rust’s memory safety. But it seems that there also aren’t strict
guarantees that segfaults/memory leaks won’t happen. I have more to learn here!


**read the docs around unsafe functions really carefully**. Using unsafe functions can be safe! You
just need to be careful to make sure to call those functions in a way that maintains the invariants
that Rust expects. Rust has really clear documentation about what the expectations of unsafe
functions are. I will try to be more careful about actually reading them in the future :)


**jemalloc does some things I don’t understand**. One of the jemalloc devs gave me this very
interesting
answer to “why does this code segfault with jemalloc but not libc malloc”: (from [this tweet](https://twitter.com/davidtgoldblatt/status/944469344934813696))


> jemalloc caches memory thread-locally, bucketed by the size reserved for it, so it doesn’t have to touch the central allocator as often (risking lock contention). We can dodge some metadata lookups if the user tells us the size of the memory being freed; if we think an N-byte allocation is really M > N bytes, then we’ll return it for an M-byte request (stomping over someone else data at bytes M-N up to N).


I think this was what was happening – I’d set the capacity of the new vector incorrectly (560
instead of 7) and so jemalloc took the (wrong) hint about the how big the allocation being freed was
and that caused a segfault somehow.


### this was cool!


this was a fun bug and I know a few more things about memory safety than I did before I ran into it.
Yay! One of my favourite things about learning more Rust is that when I run into bugs in Rust
programs, I often learn new cool things about systems (valgrind! asan/tsan! jemalloc! guard pages!).
