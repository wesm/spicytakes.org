---
title: "Hacking on your TI calculator"
date: 2014-02-25
url: https://drewdevault.com/2014/02/25/Hacking-on-your-TI-calculator.html
slug: Hacking-on-your-TI-calculator
word_count: 1580
---

I’ve built the  [KnightOS kernel](https://github.com/KnightOS/kernel) , an open-source OS that runs on
several TI calculator models, including the popular TI-83+ family, and recently the new TI-84+ Color
Silver Edition. I have published some information on how to build your own operating sytsems for these
devices, but I’ve learned a lot since then and I’m writing this blog post to include the lessons I’ve
learned from other attempts.

## Prerequisites

Coming into this, you should be comforable with z80 assembly. It’s possible to write an OS for these
devices in C (and perhaps other high-level languages), but proficiency in z80 assembly is still
required. Additionally, I don’t consider C a viable choice for osdev on these devices when you
consider that the available compliers do not optimize the result very well, and these devices have
very limited resources.

You will also have to be comfortable (though not neccessarily expert-level) with these tools:

* make
* The assembler of your choice
* The toolchain of your choice

I’m going to gear this post from the perspective of a Linux user, but Windows users should be able to
do fine with cygwin. If you’re looking for a good assembler, I suggest
 [sass](https://github.com/KnightOS/sass) , the assembler KnightOS uses. I built it myself to address
the needs of the kernel, and it includes several nice features that make it easier to maintain such a
large and complex codebase. Other good choices include
 [spasm](https://wabbit.codeplex.com/releases/view/45088)  and
 [brass](https://code.google.com/p/brass-assembler/) .

For your toolchain, there are a few options, but I’ve built custom tools that work well for KnightOS
and should fit into your project as well. You need to accomplish a couple of tasks:

* [Create ROM files from assembler output](https://github.com/KnightOS/MakeROM)
* [Create OS upgrades from ROM files](https://github.com/KnightOS/CreateUpgrade)

You also need the  [cryptographic signing keys](http://brandonw.net/calculators/keys/)  for any of the
calculators you intend to support. There are ways to get around using these (which you’ll need to
research for the TI-84+ CSE, for example) that you may want to look into. These keys will allow you
to add a cryptographic signature on your OS upgrades that will make your calculator think it’s an
official Texas Instruments operating system, and you will be able to send it to the device. The
CreateUpgrade tool linked above produces signed upgrade files for you, but if you choose to use other
tools you may need to find a seperate signing tool.

Additonally, if you target devices with a newer boot code, you’ll have to reflash your boot code or
use a tool like  [UOSRECV](http://brandonw.net/calcstuff/uosrecv.zip)  to send your OS to an actual
device.

## What you’re getting into

You will be replacing everything on the calculator with your own system (though if you want to retain
compatability with TIOS like  [OS2](http://brandonw.net/calculators/OS2/)  tried to, feel free). You’ll
need to do  *everything* , including common things like providing your own multiplication functions, or
drawing functions, or anything else. You’ll also be responsible for initializing the calculator and
all of the hardware you want to use (such as the LCD or keypad).

That being said, you can take some code from projects like the KnightOS kernel to help you out. The
KnightOS kernel is open sourced under the MIT license, which means you’re free to take any code from
it and use it in your own project. I also strongly suggest using it as a reference for when you get
stuck.

The advantage to taking on this task is that you can leverage the full potential of these devices.
What you’re building for is a 6/15 MHz z80 with 32K or more of RAM, plus plenty of Flash and all
sorts of fun hardware. You can also build something that frees your device of proprietary code, if
that is what you are interested in (though the proprietary boot code would remain - but that’s a
story for another day).

If you plan on making a full blown operating systems that can run arbituary programs and handle all
sorts of fun things, you’ll want to make sure you have a strong understanding of programming in
general, as well as solid algorithmic knowledge and low-level knowledge. If you don’t know how to
use pointers or bit math, or don’t fully understand the details of the device, you may want to try
again when you do. That being said, I didn’t know a lot when I started KnightOS (as the community was
happy to point out), and now I feel much more secure in my skills.

## Building the basic OS

We’ll build a simple OS here to get you started, including booting the thing up and showing a
simple sprite on the screen. First, we’ll create a simple Makefile. This OS will run on the
TI-73, TI-83+, TI-83+ SE, TI-84+, TI-84+ SE, and TI-84+ CSE, as well as the French variations
on these devices.

[Grab this tarball](/demo_os.tar.gz)  with the basic OS to get started. It looks like this:

```
.
├── build
│   ├── CreateUpgrade.exe
│   ├── MakeROM.exe
│   └── sass.exe
├── inc
│   └── platforms.inc
├── Makefile
└── src
    ├── 00
    │   ├── base.asm
    │   ├── boot.asm
    │   ├── display.asm
    │   └── header.asm
    └── boot
        └── base.asm
```

If you grab this, run  `make all`  and you’ll get a bunch of ROM files in the  `bin`  directory.
I’ll explain a little bit about how it works. The important file here is  `boot.asm` , but I
encourage you to read whatever else you feel like - especially the Makefile.

### Miscellaneous Files

Here is the purpose of each file, save for boot.asm (which gets its own section later):

* The makefile is like a script for building the OS. You should probably learn how these work
if you don’t already.
* Everything in build/ is part of the suggested toolchain.
* The inc folder can be #included to, and includes  `platforms.inc` , which defines a bunch of
useful constants for you.
* `base.asm`  is just a bunch of #include statements, for linking without a linker
* `display.asm`  has some useful display code I pulled out of KnightOS
* `header.asm`  contains the OS header and RST list

### boot.asm

The real juciy stuff is boot.asm. This file initializes everything and draws a smiley face
in the middle of the screen. Here’s what it does (in order):

1. Disable interrupts
2. Set up memory mappings
3. Create a stack and set SP accordingly
4. Initialize the LCD (B&W or color)
5. Draw a smiley face

I’m sure your OS will probably want to do more interesting things. The KnightOS kernel, for
example, adds on top of this a bunch of kernel state initialization, filesystem initialization,
and loads up a boot program.

`boot.asm`  is well-commented and I encourage you to read through it to get an idea of what
needs to be done. The most complicated and annoying bit is the color LCD initialization, which is
mostly in  `display.asm` .

I encourage you to spend some time playing with this. Bring in more things and try to build
something simple. Remember, you have no bcalls here. You need to build everything yourself.

## Resources

There are several things you might want to check out. The first and most obvious is
 [WikiTI](http://wikiti.brandonw.net/index.php?title=Calculator_Documentation) . I don’t use much
here except for the documentation on I/O ports, and you’ll find it useful, too.

The rest of the resources here are links to code in the KnightOS kernel.

The  [interrupt handler](https://github.com/KnightOS/kernel/blob/master/src/00/interrupt.asm#L19) 
is a good reference for anyone wanting to work with interrupts to do things like handle the ON
button, link activity, or timers. One good use case here (and what KnightOS uses it for) is
preemptive multitasking. Note that you might want to use  `exx`  and  `ex af, af'`  instead of
pushing all the registers like KnightOS does. Take special note of how we handle USB activity.

You might want to consider offering some sort of color LCD compatabilty mode like KnightOS does.
This allows you to treat it like a black & white screen. The relevant code is
 [here](https://github.com/KnightOS/kernel/blob/master/src/00/display-color.asm) .

If you want to interact with the keyboard, you’ll probably want to reference the KnightOS
keyboard code  [here](https://github.com/KnightOS/kernel/blob/master/src/00/keyboard.asm) . You
might also consider working out an interrupt-based keyboard driver.

If you’d like to manipulate Flash, you need to run most of it from RAM. You will probably want
to reference the  [KnightOS Flash driver](https://github.com/KnightOS/kernel/blob/master/src/00/flash.asm) .

## Skipping to the good part

It’s entirely possible to avoid writing an entire system by yourself. If you want to dive right
in and start immediately making something cool, you might consider grabbing the KnightOS kernel.
Right off the bat, you’ll get:

* A tree-based filesystem
* Multitasking and IPC
* Memory management
* A standard library (math, sorting, etc)
* Library support
* Hardware drivers for the keyboard, displays, etc
* Color and monochrome graphics (and a compatability layer)
* A font and text rendering
* [Great documentation](http://www.knightos.org/documentation.html)
* Full support for 9 calculator models

The kernel is standalone and open-source, and it runs great without the KnightOS userspace.
If you’re interested in that, you can get started  [on GitHub](https://github.com/KnightOS/kernel) .
We’d also love some contributors, if you want to help make the kernel even better.

## Closing thoughts

I hope to see a few cool OSes come into being in the TI world. It’s unfortunately sparse in that
regard. If you run into any problems, feel free to drop by #knightos on irc.freenode.net, where
I’m sure myself or someone else can help answer your questions. Good luck!
