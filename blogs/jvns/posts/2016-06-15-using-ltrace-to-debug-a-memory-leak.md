---
title: "Using ltrace to debug a memory leak"
date: 2016-06-15
url: https://jvns.ca/blog/2016/06/15/using-ltrace-to-debug-a-memory-leak/
slug: using-ltrace-to-debug-a-memory-leak
word_count: 636
---


Yesterday, I used ltrace to debug something for the first time! I was looking at a memory leak in a Rust async library with Kamal, and it was leaking 500 bytes of memory every time we made a request to the web server that used it. Not good!


### what’s ltrace?


ltrace traces **library calls**. This is cool because there are a lot of important things that happen that don’t go through the kernel!


For example – one thing that took me a while to learn is that memory allocation with `malloc` and `free` aren’t something that your operating system handles. Your OS gives you huge chunks of memory, but the business of keeping track of which bits of it have been allocated is up to you.


Here’s a little bit of what happens when I run `ltrace ls`


```
malloc(552)      = 0xf4d010
malloc(120)      = 0xf4d240
malloc(1024)     = 0xf4d2c0
free(0xf4d2c0)   = <void>
free(0xf4d010)   = <void>
malloc(5)        = 0xf4d010
free(0xf4d010)   = <void>
malloc(120)      = 0xf4d030

```


This is neat! We can see that we allocated 1024 bytes of memory to get `0xf4d2c0` and then free that address shortly after.


### how do you find a memory leak?


A memory leak is when either you forget to free memory even though nothing refers to it anymore (pretty common in C), or when you accidentally keep a reference around to memory even though you don’t actually need it, and it’s prevented from being garbage collected (pretty common in Python).


Since this is Rust, and memory that isn’t being referred to gets freed, we probably have the second kind of problem. But where?!


We tried using valgrind to find the memory leak, but that was not super successful. It was like “dude here are some huge stack traces in this library you don’t really understand” and we were like “I don’t know what that means”.


Then I thought – ltrace! I know what ltrace is!


Since 500 bytes of memory were leaked every time we made a HTTP request to our leaking web server, we ran `ltrace` on the web server. Here’s what happened when we made the HTTP request:


```
... a bunch of mallocs and frees ...
send(7, "some string")
malloc(32)      = 0xf4d010
malloc(32)      = 0xf4d030
... a bunch of mallocs and frees ...

```


We used `grep` to find out that `0xf4d010`… never got freed! A MEMORY LEAK! WE WIN. But where? What are those 32 bytes?


There is probably a smart and clever way to figure what the 32 bytes are. Instead, we added print statements to our program to try to find the leak. This was made a lot easier because of that `send` clue – we knew the leak had to be near where we wrote to the TCP socket. After adding the print statements and experimenting a bit, the ltrace output looked like:


```
... a bunch of mallocs and frees ...
send(7, "some string")
write("this is before the leak")
malloc(32)      = 0xf4d010
malloc(32)      = 0xf4d030
write("this is after the leak")
... a bunch of mallocs and frees ...

```


Our corresponding Rust code looked like


```
println!("this is before the leak");
do_thing_1.boxed();
do_thing_2.boxed();
println!("this is after the leak");

```


Guess what `.boxed()` means in this program? It means “do an allocation and put this on the heap”! Or in other words, `malloc`. We found the leaking allocation! Yay!


In general in Rust `Box::new` is a way to allocate something on the heap.


At this point I was tired so I fell asleep. This isn’t done, of course – we still need to chase the Rust program to figure out why that allocation never gets freed. But it’s a start!


I’m always really happy when I make progress a bug using a thing in my toolkit I haven’t used properly before. Yay ltrace!
