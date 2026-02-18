---
title: "How to call Rust from assembly, and vice versa"
date: 2013-12-01
url: https://jvns.ca/blog/2013/12/01/how-to-call-rust-from-assembly/
slug: how-to-call-rust-from-assembly
word_count: 753
---


In the last few days I’ve been working on a kernel in Rust. This has
entailed learning about linkers and foreign function interfaces and
all kinds of things.


To learn this stuff, I read
[this guide to linkers](http://www.lurklurk.org/linkers/linkers.html), looked
at the
[Rust foreign function interface tutorial](http://static.rust-lang.org/doc/master/tutorial-ffi.html),
and asked a million questions on the Rust IRC channel.


Disclaimer: even more than usual, some of this is probably wrong.


So. Linkers.


I have assembly functions that I need to call from Rust, and Rust
functions I need to call from assembly. Everything gets compiled to
assembly eventually, so this is a reasonable thing to do. As far as I
understand it, a function call is just jumping to an address in memory
and putting some stuff on the stack and in registers, and the code
doesn’t care at all if that address in memory comes from Rust or C or
assembly or what.


Some terminology:

- A **calling convention** is about how exactly the stuff gets put on
the stack and in the registers. Rust and C have different calling
conventions.
- An **object file** is what you get when you compile some source code
to a library (using `gcc` or `nasm` or `rustc`). It ends in `.o`
- A **symbol** is an identifier in a program, like a variable or
function name. Object files have a **symbol table** and can refer to
symbols in other object files.
- A **linker** (like `ld`) combines several object files into one
binary, matching up their symbol tables.


### Calling Rust from assembly


So here’s an assembly function that calls a Rust function:


```
global  _interrupt_handler_kbd_wrapper
extern _interrupt_handler_kbd

_interrupt_handler_kbd_wrapper: 
    pushad
    call    _interrupt_handler_kbd
    popad
    iret

```


`extern` says that `_interrupt_handler_kbd` isn’t actually defined in
this file, but that `nasm` shouldn’t worry about it when assembling –
it’ll be fixed later. This is like a function declaration in C, except
without the types.


I haven’t tested this yet so there’s probably something wrong with it.
But it compiles.


### Calling assembly from Rust


External functions are defined in Rust again using the `extern`
keyword (sound familiar? =D).


I need to get the address of the `_interrupt_handler_kbd_wrapper` and
`idt_load` functions in Rust, so I defined them like this:


```
extern {
    fn _interrupt_handler_kbd_wrapper ();
    fn idt_load(x: *IDTPointer);
}

```


You’ll notice that I needed to specify the types of the function’s
arguments. These don’t have return values, but if they did I’d need to
write those types too.


The type of `_interrupt_handler_kbd_wrapper` is `extern "C" unsafe fn()`. That’s pretty complicated, but let’s break it down:

- `extern` means it’s defined in another object file.
- `"C"` is the *calling convention* which we mentioned before.
- We have no idea what the function could be doing, so it’s `unsafe`.


Then I can just call my `extern` functions like normal Rust functions.


### Putting it together: the linker


I have a file named `linker.ld` that contains:


```
ENTRY(start)
OUTPUT_FORMAT(binary)

SECTIONS {
    . = 0x7e00;

    .text : {
        *(.text)
    }
}

```


Then I run


`i386-elf-ld -T linker.ld runtime.o main.o isr_wrapper.o -o main.bin`


where `main.o` is my Rust file and `isr_wrapper.o` is my assembly
file. You’ll notice that now they have a `.o` extension – now they’re
“object files” and they’re all assembly code.


This `ld` command puts `main.o`, `runtime.o`, and `isr_wrapper.o`
together into one binary. Basically this matches up symbols with the
same name and makes it work. If an `extern` function I declare in a
file doesn’t exist, then I’ll get a linker error like this:


```
main.o: In function `main':
main.rc:(.text+0x1db): undefined reference to `_interrupt_handler_kbd_wrapper'

```


But this kind of linker error isn’t scary any more! It just means that
`_interrupt_handler_kbd_wrapper` isn’t in the symbol table of any of
the other object files we’re linking.


### How to look at an object file’s symbol table


To see the symbols that are defined in `isr_wrapper.o`, I can use
`objdump` like this:


```
bork@kiwi ~/w/h/rustboot> objdump -t isr_wrapper.o

isr_wrapper.o:     file format elf32-i386

SYMBOL TABLE:
00000000 l    df *ABS*  00000000 isr_wrapper.asm
00000000 l    d  .text  00000000 .text
00000000         *UND*  00000000 _interrupt_handler_kbd
00000000 g       .text  00000000 _interrupt_handler_kbd_wrapper
00000008 g       .text  00000000 idt_load

```


You can see here that I’ve defined `_interrupt_handler_kbd_wrapper`
and `idt_load`, but that `_interrupt_handler_kbd` is undefined and
needs to be defined in another file.


You can also use `objdump -T` to look at a dynamically linked `.so`
file’s symbol table. We’re not talking about dynamic linking today =).
For example `objdump -T  /usr/lib32/libm.so` shows me the math
library’s symbol table. COOL.


That’s all!
