---
title: "Day 37: After 5 days, my OS doesn't crash when I press a key"
date: 2013-12-04
url: https://jvns.ca/blog/2013/12/04/day-37-how-a-keyboard-works/
slug: day-37-how-a-keyboard-works
word_count: 548
---


Right now I’m working towards being able to:

1. press keys on my keyboard
2. having the OS not crash
3. and have the key I pressed be echoed back


I just achieved step 2, and this has been kind of a saga, so here’s an
explanation of the blood and tears involved. First up, some resources
that really helped me out:

- The fantastic [OSDev wiki](http://wiki.osdev.org/Main_Page).
- This
[tutorial on how to make a basic x86 kernel](http://www.osdever.net/bkerndev/Docs/idt.htm),
especially the IDT page.
- This [other Rust kernel](https://github.com/pcmattman/rustic/),
mostly for Rust coding style.
- Most of all: the OSDev wiki page
[“I Can’t Get Interrupts Working”](http://wiki.osdev.org/I_Cant_Get_Interrupts_Working).
Read this three times every time you have a problem. For real.


So here’s how I did it. There were a lot of pitfalls. Notably absent
are the hours I spent in the Rust IRC channel being confused about
types.


### How To Get Interrupts Working, Julia’s Way

1. Create a Global Descriptor Table (GDT) and load it ([source](https://github.com/jvns/rustboot/blob/b845c49358e6f789636a0ce763406fa5200403a5/src/loader.asm#L67))
2. [Switch from Real Mode to Protected Mode](http://wiki.osdev.org/Protected_mode).
This involves turning interrupts off (`cli`).
3. Create a Interrupt Descriptor Table (IDT) and load it.
4. Put interrupt handlers into my table.
5. Press keys. Nothing happens. Hours pass. Realize interrupts are
turned off and I need to turn them on.
6. Turn interrupts on (`sti`).
7. Press a key. The OS crashes. Continue experimenting in this
vein for some time. Still crashing.
8. Take the advice from [“I Can’t Get Interrupts Working”](http://wiki.osdev.org/I_Cant_Get_Interrupts_Working)
and trigger the interrupts **manually** (with `int 1`) before
turning interrupts back on and trying it for real. Get my interrupt
descriptor table not broken. Sweet.
9. Turn interrupts on (`sti`).
10. The OS AGAIN crashes every time i press a key. Read “I Can’t
Get Interrupts Working” again. This is called “I’m receiving EXC9
instead of IRQ1 when striking a key?!” Feel on top of this.
11. [Remap the PIC](http://wiki.osdev.org/PIC) so that interrupt `i`
gets mapped to `i + 32`, because of an Intel design bug. This
*basically* looks like just typing in a bunch of random numbers,
but it works.
12. THE OS IS STILL CRASHING WHEN I PRESS A KEY. This continues for 2
days.
13. Remember that now that I have remapped interrupt 1 to interrupt 33
and I need to update my IDT.
14. Update my IDT.
15. Press a key. My interrupt handler runs. Practically faint with joy.
16. But it only runs the first time I press a key, not the second
time. This is the section “I can only receive one IRQ”


As far as I can tell this is all totally normal and just how OS
programming is. Or something. Hopefully by the end of the week I will
get past “I can only receive one IRQ” and into “My interrupt handler
is the bomb and I can totally write a keyboard driver now”.


Then I’m going to write a keyboard driver where in addition to doing
normal keyboard driver things, it changes the screen colour every time
I press a key. ([Kate](http://kate.io)’s idea)


I’m seriously amazed that operating systems exist and are available
for free.


**Edit:** Thanks for all the help everyone! I’ve solved “It only runs
the first time I press a key” now and moved on to new problems :)
