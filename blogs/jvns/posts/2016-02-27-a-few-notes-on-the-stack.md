---
title: "What is 'the stack'?"
date: 2016-02-27
url: https://jvns.ca/blog/2016/02/27/a-few-notes-on-the-stack/
slug: a-few-notes-on-the-stack
word_count: 1406
---


Last week I was at [Papers We
Love](http://www.meetup.com/Papers-We-Love-Montreal/), my new favorite meetup.
And someone mentioned “the stack” in passing, and I decided to ask – what is
that, really? I talked about it with [Julian](http://www.cipht.net) (who, like many people I know, is the best).


The basic question I want to answer here is – why do people sometimes discuss “the stack” like it’s some kind of revered fundamental object? (the answer is going to turn out to be “because it is”, and I’m going to try to make that as concrete as I can.)


### Calling a function


Let’s talk about the basics before it gets weird. Suppose you’re in a programming language. Any programming language. Most languages have the concept of a “function” and “calling a function”.


Whenever you call a function, you also need to **return** from that function. So, as a simple example –


```
def elephant(x):
  value = panda(x)
  return value + 2

def panda(y):
  return y * 3

```


So if we call `elephant(3)`, we’re going to call `panda(3)` next, and we need to remember that we were in `elephant` before.


Normally programming languages keep track of this information in a data structure called the **call stack**, which you can imagine like


```
1) elephant <-- you were here before
2) panda <-- you are here now

```


### Calling a function in C (and why C is special)


Most languages have some kind of call stack data structure. Python! Ruby! C! Java! But that could be anything, right?


For a long time I’ve been vaguely confused about this, because I often hear references to “stack smashing” or “stack overflows” or “setting a stack size”, like there’s a canonical stack that all programs have. And there is a One True Stack!


As in most cases with the One True Anything on Linux, the One True Call Stack is the C call stack.


To understand why, it helps to to look at a C program and what it compiles to. I wrote one for this blog post:


```
#include <stdio.h>

int main() {
    blah(3);
    printf("Penguin!\n");
}

int blah(int x) {
    return x;
}

```


Pretty simple! When your CPU runs programs, it’s ultimately running assembly instructions. Let’s look at the assembly instructions for this program:


```
$ gcc -o hello hello.c
$ objdump -d hello
 address       instructions (binary)   instructions (english)
00000000004004f4 <main>:
  4004f4:       55                      push   %rbp
  4004f5:       48 89 e5                mov    %rsp,%rbp
  4004f8:       bf 03 00 00 00          mov    $0x3,%edi
  4004fd:       e8 0c 00 00 00          callq  40050e <blah>
  400502:       bf 0c 06 40 00          mov    $0x40060c,%edi
  400507:       e8 e4 fe ff ff          callq  4003f0 <puts@plt>
  40050c:       5d                      pop    %rbp
  40050d:       c3                      retq   

000000000040050e <blah>:
  40050e:       55                      push   %rbp
  40050f:       48 89 e5                mov    %rsp,%rbp
  400512:       89 7d fc                mov    %edi,-0x4(%rbp)
  400515:       8b 45 fc                mov    -0x4(%rbp),%eax
  400518:       5d                      pop    %rbp
  400519:       c3                      retq   
  40051a:       90                      nop
  40051b:       90                      nop
  40051c:       90                      nop

```


Delightfully, this is very simple – all of the assembly code for both these two functions fits on a page!


We have two functions: `main` and `blah`. We’re lucky that `blah` is a Very Simple Function: it only has 4 kinds of instructions in it, `push`, `pop`, `mov`, and `retq`. This is where we get into…


### Assembly instructions and The Stack


What does `push %rbp` mean? It means “put the address in %rbp on The Stack”. But what does it mean to put something on the Stack-with-a-capital-S?


Well, this is where we get to the very important **stack pointer**. There’s a special register called `%rsp` where, conventionally, an address called the stack pointer is stored.


Imagine that I have a region in memory like this. I’ve used 64 bit increments because I have a 64-bit processor.


```
address         value
832               4
824               29328323
816               283842
808               128

```


Now suppose the address in `%rsp` is 808. Then `push 3` would mean “decrement %rsp and put 3 at the next lowest address in memory”. So we’d have


```
address          value
832               4
824               29328323
816               283842
808               128
800               3

```


This means that the `push` and `pop` instructions both make very fundamental assumptions about the memory layout of your program – that `%rsp` represents an address they can access, and that the memory there is split up into 8 byte (64 bit) chunks that represent the current stack.


Next up, we need to discuss **retq** and **callq**. `retq` needs to return to main after the function `blah()` is done running. How does that even work?


Well! When we execute the instruction `callq`, the address `0x00400502` gets pushed onto the stack (where `%rsp` is). Then when we later execute `retq`, it can look in the stack and discover that it needs to go back to the address `0x00400502` to continue program execution. If we changed that address in the stack to be something totally different, the program wouldn’t know how to execute anymore! It would do something Very Different.


I found it pretty surprising that the x86 assembly instruction set knows about the C stack pointer and how the stack in C is laid out. Of course, you could invent your own new smart stack format, but you wouldn’t be able to use the `callq` and `retq` instructions to call functions.


### Which came first, the chicken or the egg?


I just said that this is the “C stack format”, and the assembly assumes that everything is like C. But of course it could be the other away around – maybe the x86 instruction set came first, with its assumptions about how the One True Stack is organized, and then C conformed to that! And you could write a C compiler that uses a totally different stack format and is incompatible with every other program!


I don’t know. Maybe you will tell me which came first – the compilers that laid out the stack this way, or the instructions! Did all this get decided in the 80s? in the 90s? in the 70s?


In any case, it seems like we’re stuck with those choices now. Except!


### What if you wrote your own stack format?


Since we are curious experimenters, we are brought to the obvious question – what would happen if we wrote our own stack format that was incompatible with the C stack? What if we used the One True Stack Pointer `%rsp` for our own nefarious purposes?


This isn’t a theoretical question at all – [Rust](https://doc.rust-lang.org/book/ffi.html) actually has a different calling convention from C, which means it sets up its stack differently.


This isn’t a super big deal in Rust – if you want to call a C function from Rust, you can tell the compiler “hey just be normal like C for a bit, okay?”. And you can tell it to expose Rust functions like they were C functions. It’s fine.


But you do need to be aware of it, if you’re a prospective weird-stack-programming-language author or user! For instance! If you want to use gdb with Rust, and you want to get a stack trace (“what function did I call before I called this one?”) – that wouldn’t normally work. gdb would not know how to interpret the stack! But Rust implements [libbacktrace](https://github.com/rust-lang/rust/tree/master/src/libbacktrace), which tells GDB how the stack information corresponds to a stack trace.


If you read the README there carefully, you’ll notice that Rust’s libbacktrace only works with ELF binaries! This means that you can’t get Rust stack traces with gdb on OS X or Windows, only in Linux/BSDs/other operating systems that ues ELF binaries. That actually really sucks! There are consequences to having an unusual stack format, and real work you need to do to make the rest of the world understand you.


### fascinating.


I was really surprised that **assembly instructions** make assumptions about how memory is organized and what information is in which registers. This explains why people talk about The Stack like it’s this fundamental data structure instead of just one choice about how you could organize your program. It kind of is!


If you want to more fun things to read, there’s a great article [Understanding C by learning assembly](https://www.recurse.com/blog/7-understanding-c-by-learning-assembly) which discusses using GDB to inspect memory and see exactly what’s going on when you run a C program. It’s super fun.


There is so much to know! [@yrp604 on twitter](https://twitter.com/yrp604/status/704896921152921602) just told me that on ARM you can choose which direction the stack grows! Whoa.
