---
title: "Day 36: On programming without malloc"
date: 2013-12-03
url: https://jvns.ca/blog/2013/12/03/day-36-programming-without-malloc/
slug: day-36-programming-without-malloc
word_count: 534
---


So right now I’m working on writing a kernel in Rust. My current goal
is to press keys on the keyboard and have them echoed to the screen.
This is going okay! I anticipate being able to type by the end of the
week.


One thing that’s interesting is that my expectations around what
programs should be able to do is really different right now. Normally
I write Python or other high-level languages, so my programs don’t run
too quickly, but have tons of resources available to them (the
Internet, a standard library, memory allocation, garbage collection,
…).


Writing operating systems is totally different. This is kind of
obvious, but actually doing it is really fascinating. My OS literally
can’t allocate memory, and there’s no standard way to print (I have to
write to the VGA buffer manually). I can still write loops, though, and
in general writing Rust doesn’t feel too unfamiliar. But I expect my
code to run super fast, because it has no excuse not to :). Right now
I definitely don’t have timers or anything, so I’m looping 80,000,000
times to sleep.


A few things that I can’t do that I’m used to being able to do:

- allocate memory
- print (I can sort of do this)
- `sleep`
- run other processes (there are no other programs)
- read from stdin (I don’t have a keyboard driver yet. There is no stdin.)
- open files (there are no files)
- list files (there are no files)


(thanks to [Lea](http://instamatique.com/lea/) for “there are no
files” =D)


The only real problem with not having `malloc` is that all the memory
I use has to either be

- in the program at compile time, or
- allocated on the stack


This is less difficult than I expected it to be! We’ll see how it
continues. It does mean that I use a lot of global variables, and it’s
given me an appreciation for why there is so much use of global
variables in the Linux kernel – if just need 1 struct, it makes so
much more sense to just have 1 global struct than to keep `malloc`ing
and `free`ing it all the time.


Here’s an example of some code I have in the kernel! `main()` prints
all the ASCII characters in a loop.


```
pub unsafe fn putchar(x: u16, y: u16, c: u8) {
    let idx : uint =  (y * VGA_WIDTH * 2 + x * 2) as uint;
    // 0xb8000 is the VGA buffer
    *((0xb8000 + idx) as *mut u16) = make_vgaentry(c, Black, Yellow);
}

fn make_vgaentry(c: u8, fg: Color, bg: Color) -> u16 {
    // VGA entries are 2 bytes. The first byte is the character, the
    second is the colour
    let color = fg as u16 | (bg as u16 << 4);
    return c as u16 | (color << 8);
}

pub unsafe fn main() {
    let mut i: u32 = 0;
    let mut c: u8 = 65; // 'A'
    let N: u32 = 80000000; // big enough number so that it goes slowly
    loop {
        i += 1;
        if (i % N == 0) {
            c += 1;
            putchar(2, 4, c);
        }
    }
}

```
