---
title: "Writing a kernel using rustboot & rust-core"
date: 2013-11-29
url: https://jvns.ca/blog/2013/11/29/writing-an-os-using-rustboot-and-rust-core/
slug: writing-an-os-using-rustboot-and-rust-core
word_count: 553
---


Here I am again using the word “kernel” in a fairly broad sense :)


So today [Lindsey Kuper](http://www.cs.indiana.edu/~lkuper/), one of
the residents for next week, came by Hacker School! I spent some time
a while ago trying to learn some Rust, but got discouraged by the
scary pointers and ran away.


But today she pointed out that Rust is for systems programming, and
right now I *am* trying to write an operating system, and this would
be the perfect time to pick it up again!


So I started playing with
[rustboot](https://github.com/charliesome/rustboot), which is a 32-bit
kernel which turns the screen red and hangs. So far I’ve made some
minor changes – it now turns the screen *green* and hangs.


But slightly more seriously, I also added a function to print
characters to the screen!


![](https://jvns.ca/images/rustboot1.png)


Here’s the new code I added to do that:


```
unsafe fn putchar(x: u16, y: u16, c: u8) {
    let idx : uint = (y * VGA_WIDTH * 2 + x) as uint;
    // 0xb8000 is the VGA buffer
    *((0xb8000 + idx) as *mut u16) = make_vgaentry(c, Black, Yellow);
}

fn make_vgaentry(c: u8, fg: Color, bg: Color) -> u16 {
    // Details of how VGA colours are stored
    let color = fg as u16 | (bg as u16 << 4);
    return c as u16 | (color << 8);
}

unsafe fn write(s: &str, x: u16, y: u16) {
    let bytes : &[u8] = to_bytes(s);
    let mut ix = x;
    let mut iy = y;
    let mut i = 0;
    for b in core::slice::iter(bytes) {
        putchar(ix, iy, *b);
        if (ix > VGA_WIDTH * 2) {
            // line wrap
            ix = ix - VGA_WIDTH * 2;
            iy += 1;
        }
        i += 1;
        ix += 2;
    }
}


#[no_mangle]
pub unsafe fn main() {
    clear_screen(Green);
    write("Hello!aaa", 2, 3);
}

```


I like that I can write a loop like `for b in core::slice::iter(bytes) {`. I still don’t know how string length is determined – it seems
like instead of having null-terminated strings, Rust stores the size
separately. I think.


It’s nice that I can write code like this without having an OS in the
background. As I mentioned before, there were quite a few gotchas –
for example, when I was trying to get the iterator to work, I got the
cryptic error message `error: unreachable pattern`, which meant that I
needed to add `use core::option::None`.


In all to get iterators to work I need to add:


```
use core::mem::transmute; // for to_bytes()
use core::slice::iter; // for the iterator
use core::iter::Iterator; // for the loop
use core::option::{Some, Option, None}; // for the loop
mod core;

```


This small amount of accomplishment wouldn’t have been remotely
possible without the help of the lovely people on the #rust IRC
channel – I had tons of issues using freestanding rust and rust-core,
and the [rust-core maintainer](https://github.com/thestinger) answered
every single one of my questions. <3.


If you wanted to do this yourself, you could do something like:


```

sudo apt-get install qemu nasm
git clone https://github.com/jvns/rustboot.git
cd rustboot
git checkout 1e0f2b02f45096e5300faf9e
git clone https://github.com/thestinger/rust-core.git ~/rust-core
ln -s ~/rust-core/core .
make run

```


Oh! Also! That code prints 9 characters to the VGA buffer correctly,
but if I try printing 10 characters, it doesn’t work. I have no idea
why. That will be for tomorrow.
