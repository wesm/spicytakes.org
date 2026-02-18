---
title: "Day 39: Writing malloc wrong, for fun"
date: 2013-12-10
url: https://jvns.ca/blog/2013/12/10/day-39-i-wrote-a-malloc/
slug: day-39-i-wrote-a-malloc
word_count: 320
---


My major achievement for today is writing the following five lines of
code:


```
let a: ~u8 = ~('A' as u8);
stdio::putc(*a);
let b: ~u8 = ~('B' as u8);
stdio::putc(*a);
stdio::putc(*b);

```


and having them do the wrong thing. One would normally expect this to
print “AAB”. But for me, right now, until I stop goofing off, it
prints “ABB”. Why is that?


Well, it’s because my `malloc` implementation looks like this:


```
static mut base: uint = 0x200000;
pub extern "C" fn malloc(len: uint) -> *mut u8 {
    unsafe {
        let ret: uint = base;
        return base as *mut u8;
   }
}

```


This means that every time I allocate memory, I get the same pointer
back, and so `a` and `b` will always be equal no matter what. And for
that matter any variable I create will always have the same value.
This is of course a terrible idea in real life, but it is *really
fun*.


Here’s my real `malloc` function (that causes the above code to print
“AAB”, like it should):


```
pub extern "C" fn malloc(len: uint) -> *mut u8 {
    unsafe {
        let ret: uint = base;
        base += len + size_of::<uint>();

        // Align next allocation to 4-byte boundary.
        if(base % 4 != 0) {
            base += 4 - (base % 4);
        }

        *(base as *mut uint) = len;

        return (ret + size_of::<uint>()) as *mut u8;
    }
}

pub extern "C" fn free(ptr: *mut u8) {
    // meh.
}

```


The hardest part about this was not actually writing `malloc`. Writing
`malloc` is easy, as long as you never need to free memory. I also
just wrote this by copying it from a C implementation. You just need
to keep a counter and keep incrementing it.


The hard part was getting the type of the function right, because Rust
:). This is entirely made up for by being able to play silly memory
games.
