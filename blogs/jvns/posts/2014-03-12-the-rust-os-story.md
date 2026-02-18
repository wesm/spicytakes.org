---
title: "Writing an OS in Rust in tiny steps (Steps 1-5)"
date: 2014-03-12
url: https://jvns.ca/blog/2014/03/12/the-rust-os-story/
slug: the-rust-os-story
word_count: 1509
---


I’m giving a talk tomorrow on writing a kernel in Rust.


My experience of writing a kernel that it was like jumping in puddles:
it’s a lot of fun, and there are a lot of mishaps:


![](https://jvns.ca/images/puddle.gif)


Here are a few of the tiny steps I took. There are more, but those
will have to wait for the evening.


### Step 1: copy some code from the internet


I didn’t know what I was doing, so I didn’t want to start from
scratch! So I started with something that already existed! Behold
[rustboot](https://github.com/charliesome/rustboot), a tiny 32-bit
kernel written in Rust.


Rustboot does only two things, but it does them well!

1. Turn the screen red
2. Hang


Of course what it actually does is a bit more complicated – there’s

- a loader written in assembly
- a Makefile that lets you run it with `qemu`
- Some Rust code to clear the screen


Here’s the code that clears the screen:


```
unsafe fn clear_screen(background: Color) {
    range(0, 80*25, |i| {
        *((0xb8000 + i * 2) as *mut u16) = (background as u16) << 12;
    });
}

```


What does this mean? The key part here is that the address of the VGA
buffer is `0xb8000`, so we’re setting some bytes there. And there’s a
loop.


### Step 2: Turn the screen blue instead.


The first thing I did was:

1. Make sure I could run `rustboot`.
2. Change ‘red’ to ‘blue’ and run it again


This sounds silly, but psychologically it’s an important step! It
forced me to look at the code and understand how it worked, and it was
really exciting that it worked right away.


### Step 3: Start writing I/O functions


The next obvious step now that I had a blue screen was to try to write
a `print` function.


Here’s what it looked like!


```
pub fn putchar(x: u16, y: u16, c: u8) {
    let idx : uint =  (y * VGA_WIDTH * 2 + x * 2) as uint;
    unsafe {
        *((VGA_ADDRESS + idx) as *mut u16) = make_vgaentry(c, fg_color, bg_color);
    }
}

```


I didn’t explain the `unsafe` block before. Everything inside
`unsafe{}` is *unsafe* code. This particular code is unsafe because it
accesses a memory address directly. Wrapping it in an unsafe block
tells Rust “okay, I checked and I promise this code is actually doing
the right thing and won’t blow anything up”.


We can also look at `make_vgaentry`:


```
fn make_vgaentry(c: u8, fg: Color, bg: Color) -> u16 {
    let color = fg as u16 | (bg as u16 << 4);
    return c as u16 | (color << 8);
}

```


In the VGA buffer, each character is represented by 2 bytes (so a
`u16`). The lower 8 bits are the ASCII character, and the upper 8 bits
are the foreground and background colour (4 bits each). `Color` here
is an enum so that I can refer to Red or Green directly.


I found this part pretty approachable and it didn’t take too long.
Which isn’t to say that I didn’t have problems! I had SO MANY
PROBLEMS. Most of my problems were to do with arrays and string and
iterating over strings. Here’s some code that caused me much pain:


```
pub fn write(s: &str) {
    let bytes : &[u8] = as_bytes(s);
    for b in super::core::slice::iter(bytes) {
        putc(*b);
    }
}

```


This code looks simple! It is a lie.
Friends. Here were some questions that I needed to ask to write this code.

- How do I turn a string into a byte array? (`as_bytes()`)
- What is the type of a byte array? (`&[u8]`)
- How do I iterate over a byte array? (+ “it still doesn’t work!”, 4 times)


Also, what is this `super::core::slice::iter` business? This brings us
to a fairly long digression, and an important point


### Why you can’t write a kernel in Python


So you want to write an operating system, let’s say for x86. You need
to write this in a programming language!


Can you write your operating system in Python (using CPython, say)?
You cannot. This is not being curmudgeonly! It is actually just not
possible.


What happens when you write `print "Hello!"` in Python?


Well, many things happen. But the *last* thing that happens is that
the CPython interpreter will do something like `printf("Hello")`. And
you might think, well, maybe I could link against the code for
`printf` somehow!


But what `printf` does is it calls the `write()` system call. The
`write()` system call is implemented IN YOUR KERNEL.


OH WAIT YOU DON’T HAVE A KERNEL YET. YOU ARE WRITING ONE.


This also means that you can’t write a kernel as a “normal” C program
which includes C libraries. Any C libraries. All C libraries for Linux
are built on top of some version of `libc`, which makes calls to the
Linux kernel! So if you’re *writing* a kernel, this doesn’t work.


### Why you *can* write a kernel in Rust


Writing Rust code has many of the same problems, of course! By
default, if you compile a Rust program with a print statement, it will
call your kernel’s equivalent to `write`.


But! Unlike with Python, you can put `#[no_std]` at the beginning of
your Rust program.


You lose a lot! You can no longer

- allocate memory
- do threading
- print anything
- many many more things


It’s still totally fine to define functions and make calculations,
though. And you can of course define your own functions to allocate
memory.


You also lose things like Rust’s iterators, which is sad!


### rust-core


[rust-core](https://github.com/thestinger/rust-core) is “a standard
library for Rust with freestanding support”. What this means is that
if you’re writing an OS, `rust-core` will provide you with all kinds
of helpful data structures and functions that you lost when you wrote
`#[no_std]`.


I found using this library pretty confusing, but the author hangs out
in IRC all the time and was really friendly to me, so it wasn’t a huge
problem.


So back to `super::core::slice::iter`! This says “iterate over this
using an iteration function from `rust-core`”


### Step 4: keyboard interrupts!


So it took me a few days to learn how to print because I needed
to learn about freestanding mode and get confused about rust-core and
at the same time I didn’t really understand Rust’s types very well.


Once that was done, I wanted to be able to do the following:

1. Press a key (‘j’ for example)
2. Have that letter appear on the screen.


I thought this wouldn’t be too hard. I was pretty wrong.


I wrote about what went wrong in
[After 5 days, my OS doesn’t crash when I press a key](http://jvns.ca/blog/2013/12/04/day-37-how-a-keyboard-works/).


It lists all my traumas in excruciating detail and I won’t repeat them
here. Go read it. It’s kinda worth it. I’ll wait.


### Step 5: malloc!


After I’d done that, I thought it might be fun to be able to allocate
memory.


You may be surprised at this point. We have printed strings! We have
made our keyboard work! Didn’t we need to allocate memory? Isn’t
that… *important*?


It turns out that you can get away without doing it pretty easily!
Rust would automatically create variables on the stack for me, so I
could use local variables. And for anything else I could use global
variables, and the space for those was laid out at compile time.


But allocating memory seemed like a fun exercise. To allocate
something on the heap in Rust, you can do


`let a = ~2`


This creates a pointer to a `2` on the heap. Of course, we talked
before about how there is no malloc! So I wrote one, and then made
sure that Rust knew about it.


You can see the `malloc` function I wrote in
[Writing malloc wrong, for fun](http://jvns.ca/blog/2013/12/10/day-39-i-wrote-a-malloc/)


The hardest parts of this were not writing the function, but

- getting the type right
- Understanding how Rust’s language features can be turned on and off.


WHAT DO YOU MEAN TURNED ON AND OFF, you may ask!


So in `rust-core`, if you go to
[heap.rs](https://github.com/thestinger/rust-core/blob/85c28bb64ec093aff9e3f81110200793c6291467/core/heap.rs#L32),
you’ll see this code:


```
#[lang = "exchange_malloc"]
pub unsafe fn alloc(size: uint) -> *mut u8 {
    if size == 0 {
        0 as *mut u8
    } else {
        let ptr = malloc(size);
        if ptr == 0 as *mut u8 {
            out_of_memory()
        }
        ptr
    }
}

```


This weird-looking `#[lang = "exchange_malloc"]` bit means “Code like
`let x = ~2` is now allowed to work”. It requires there to be an
implementation of `malloc`, which I wrote. It also needs implements of
`realloc` and `free`, but I left those blank :)


Before seeing that, Rust would not compile code that allocated memory.


I think this language feature gating is really cool: it means that you
can write Rust programs that can allocate memory, but not do
threading. Or that can do hardly anything at all!


I need to get up now.


**Next up:** running problems! AND SOMETHING IS ERASING MY PROGRAM WHILE
IT IS RUNNING.
