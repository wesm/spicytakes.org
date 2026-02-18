---
title: "Day 38: After 6 days, I have problems that I can't understand at all"
date: 2013-12-06
url: https://jvns.ca/blog/2013/12/06/day-38-after-7-days/
slug: day-38-after-7-days
word_count: 402
---


tl;dr: I expect `NUMS[2]` to equal `NUMS[keycode]` when `keycode == 2`. This doesn’t appear to be the case, and I don’t understand how
this is possible.


I’m trying to set up keycode handling in my kernel, and I’m having a
strange problem with array indexing that I can’t really fathom at all
(except “something is wrong”).


When I run this code, and press `1` several times, it prints `|2C |2C |2C |2C |2C |2C |2C |2C |2C `.


I am expecting it to print `|2C2|2C2|2C2|2C2|2C2|2C2|2C2|2C2|2C2|`.


Here is the code:


```
// some imports removed
static NUMS: &'static [u8] = bytes!("01234567890");

#[no_mangle]
pub unsafe fn _interrupt_handler_kbd() {
    let keycode: u8 = inb(0x60);
    if (keycode == 2 || keycode == 3) {
        stdio::putc(NUMS[2]); // should be '2'. It is.
        stdio::putc(65 + keycode); // should be 'C' (keycode = 2), because 'A' is 65 
        stdio::putc(NUMS[keycode]); // should be '2', BUT IT ISN'T. IT IS SOMETHING ELSE. HOW IS THIS HAPPENING. 
        stdio::putc(124); /// this is '|', just as a delimiter.
    }
    outb(0x20, 0x20); // Tell the interrupt handler that we're done.
}

```


To summarize:

- the `2` is printed by `putc(NUMS[2])`
- the `C` is printed by `putc(65 + keycode)`. This implies that `keycode == 2`, since 65 is ‘A’
- the blank space is printed by `putc(NUMS[keycode])`. I would expect this to print `2`. But no.


For bonus points, if I replace `if (keycode == 2 || keycode == 3) {`
with `if(keycode == 2) {`, then it prints
`|2C2|2C2|2C2|2C2|2C2|2C2|2C2|2C2|2C2|`, which is right. I think this
is because of a compiler optimization replacing `keycode` with `2`.


If you have `qemu` and a nightly build of `rust` installed, you can
run this code by doing


```
git clone git@github.com:jvns/rustboot.git
cd rustboot
git checkout origin/compiler-nonsense
git submodule init
git submodule update
make run

```


Some hypotheses:

- There’s something wrong with the Rust compiler
- There’s something wrong with the stack and how I’m calling
`_interrupt_handler_kbd`
- ?????????


I also can’t yet find the address of `_interrupt_handler_kbd` to look
at the assembly to debug. It’s in the symbol table of the original
object file (`main.o`), but after linking it’s not in `main.bin`, so I
can’t set a breakpoint in gdb.


Ack.


**Edit:** [Brian Mastenbrook](http://brian.mastenbrook.net/) suggested
to link using ELF and then use objcopy to create a binary, and that
somehow magically fixed the problem
([this commit](https://github.com/jvns/rustboot/commit/2dab3a8ca693a1754b498f05472670e15343bb07)).
If anyone can explain why, I would be Extremely Interested.
