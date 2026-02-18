---
title: "Understanding pointers"
date: 2016-05-28
url: https://drewdevault.com/2016/05/28/Understanding-pointers.html
slug: Understanding-pointers
word_count: 1497
---

I was recently chatting with a new contributor to Sway who is using the project
as a means of learning C, and he had some questions about what  `void**`  meant
when he found some in the code. It became apparent that this guy only has a
basic grasp on pointers at this point in his learning curve, and I figured it
was time for another blog post - so today, I’ll explain pointers.

To understand pointers, you must first understand how memory works. Your RAM is
basically a flat array of
 [octets](https://en.wikipedia.org/wiki/Octet_(computing)) . Your compiler
describes every data structure you use as a series of octets. For the context of
this article, let’s consider the following memory:

We can refer to each element of this array by its index, or address. For
example, the value at address 0x0004 is 0x08. On this system, we’re using 16-bit
addresses to refer to 8-bit values. On an i686 (32-bit) system, we use 32-bit
addresses to refer to 8-bit values. On an amd64 (64-bit) system, we use 64-bit
addresses to refer to 8-bit values. On Notch’s imaginary DCPU-16 system, we use
16-bit addresses to refer to 16-bit values.

To refer to the value at 0x0004, we can use a pointer. Let’s declare it like so:

```
uint8_t *value = (uint8_t *)0x0004;
```

Here we’re declaring a variable named value, whose type is  `uint8_t*` . The *
indicates that it’s a pointer. Now, because this is a 16-bit system, the size of
a pointer is 16 bits. If we do this:

```
printf("%d\n", sizeof(value));
```

It will print 2, because it takes 16-bits (or 2 bytes) to refer to an address on
this system, even though the value there is 8 bits. On your system it would
probably print 8, or maybe 4 if you’re on a 32-bit system. We could also do this:

```
uint16_t address = 0x0004;
uint8_t *ptr = (uint8_t *)address;
```

In this case we’re not casting the  `uint16_t`  value 0x0004 to a  `uint8_t` , which
would truncate the integer. No, instead, we’re casting it to a  `uint8_t*` , which
is the size required to represent a pointer on this system. All pointers are the
same size.

## Dereferencing pointers

We can refer to the value at the other end of this pointer by  *dereferencing*  it.
The pointer is said to contain a  *reference*  to a value in memory. By
 *dereferencing*  it, we can obtain that value. For example:

```
uint8_t *value = (uint8_t *)0x0004;
printf("%d\n", *value); // prints 8
```

## Working with multi-byte values

Even though memory is basically a big array of  `uint8_t` , thankfully we can work
with other kinds of data structures inside of it. For example, say we wanted to
store the value 0x1234 in memory. This doesn’t fit in 8 bits, so we need to
store it at two different addresses. For example, we could store it at 0x0006
and 0x0007:

*0x0007 makes up the first byte of the value, and *0x0006 makes up the second
byte of the value.

C allows us to use pointers that refer to these sorts of composite values, like
so:

```
uint16_t *value = (uint16_t *)0x0006;
printf("0x%X\n", *value); // Prints 0x1234
```

Here, we’ve declared a pointer to a value whose type is  `uint16_t` . Note that the
size of this pointer is the same size of the  `uint8_t*`  pointer - 16 bits, or
two bytes. The value it  *references* , though, is a different type than
 `uint8_t*`  references.

## Indirect pointers

Here comes the crazy part - you can work with pointers to pointers. The address
of the  `uint16_t`  pointer we’ve been talking about is 0x0006, right? Well, we
can store that number in memory as well. If we store it at 0x0002, our memory
looks like this:

The question might then become, how do we get it out again? Well, we can use a
pointer  *to that pointer* ! Check out this code:

```
uint16_t **pointer_to_a_pointer = (uint16_t**)0x0002;
```

This code just declared a variable whose type is  `uint16_t**` , which a pointer
whose value is a  `uint16_t*` , which itself points to a value that is a
 `uint16_t` . Pretty cool, huh?  We can dereference this too:

```
uint16_t **pointer_to_a_pointer = (uint16_t**)0x0002;
uint16_t *pointer = *pointer_to_a_pointer;
printf("0x%X\n", *pointer); // Prints 0x1234
```

We don’t actually even need the intermediate variable. This works too:

```
uint16_t **pointer_to_a_pointer = (uint16_t**)0x0002;
printf("0x%X\n", **pointer_to_a_pointer); // Prints 0x1234
```

## Void pointers

The next question that would come up to your average C programmer would be,
“well, what is a  `void*` ?” Well, remember earlier when I said that all pointers,
regardless of the type of value they reference, are just fixed size integers?
In the imaginary system we’ve been talking about, pointers are 16-bit addresses,
or indexes, that refer to places in RAM. On the system you’re reading this
article on, it’s probably a 64-bit integer. Well, we don’t actually need to
specify the type to be able to manipulate pointers if they’re just a fixed size
integer - so we don’t have to. A  `void*`  stores an arbitrary address without
bringing along any type information. You can later  *cast*  this variable to a
specific kind of pointer to dereference it. For example:

```
void *pointer = (void*)0x0006;
uint8_t *uintptr = (uint8_t*)pointer;
printf("0x%X", *uintptr); // prints 0x34
```

Take a closer look at this code, and recall that 0x0006 refers to a 16-bit value
from the previous section. Here, though, we’re treating it as an 8-bit value -
the  `void*`  contains no assumptions about what kind of data is there. The result
is that we end up treating it like an 8-bit integer, which ends up being the
least significant byte of 0x1234;

## Dereferencing structures

In C, we often work with structs. Let’s describe one to play with:

```
struct coordinates {
    uint16_t x, y;
    struct coordinates *next;
};
```

Our structure describes a linked list of coordinates. X and Y are the
coordinates, and next is a pointer to the next set of coordinates in our list.
I’m going to drop two of these in memory:

Let’s write some C code to reason about this memory with:

```
struct coordinates *coords;
coords = (struct coordinates*)0x0000;
```

If we look at this structure in memory, you might already be able to pick out
the values. C is going to store the fields of this struct in order. So, we can
expect the following:

```
printf("0x%X, 0x%X", coords->x, coords->y);
```

To print out “0xDEAD, 0xBEEF”. Note that we’re using the structure dereferencing
operator here,  `->` . This allows us to dereference values  *inside*  of a
structure we have a pointer to. The other case is this:

```
printf("0x%X, 0x-X", coords.x, coords.y);
```

Which only works if  `coords`  is not a pointer. We also have a pointer within
this structure named next. You can see in the memory I included above that its
address is 0x0004 and its value is 0x0006 - meaning that there’s another  `struct coordinates`  that lives at 0x0006 in memory. If you look there, you can see the
first part of it. It’s X coordinate is 0x1234.

## Pointer arithmetic

In C, we can use math on pointers. For example, we can do this:

```
uint8_t *addr = (uint8_t*)0x1000;
addr++;
```

Which would make the value of  `addr`  0x1001. But this is only true for pointers
whose type is 1 byte in size. Consider this:

```
uint16_t *addr = (uint16_t*)0x1000;
addr++;
```

Here,  `addr`  becomes 0x1002! This is because ++ on a pointer actually adds
 `sizeof(type)`  to the actual address stored. The idea is that if we only added
one, we’d be referring to an address that is  *in the middle*  of a uint16_t,
rather than the next uint16_t in memory that we meant to refer to. This is also
how arrays work. The following two code snippets are equivalent:

```
uint16_t *addr = (uint16_t*)0x1000;
printf("%d\n", *(addr + 1));
```

```
uint16_t *addr = (uint16_t*)0x1000;
printf("%d\n", addr[1]);
```

## NULL pointers

Sometimes you need to work with a pointer that points to something that may not
exist yet, or a resource that has been freed. In this case, we use a NULL
pointer. In the examples you’ve seen so far, 0x0000 is a valid address. This is
just for simplicity’s sake. In practice, pretty much no modern computer has
any reason to refer to the value at address 0. For that reason, we use NULL to
refer to an uninitialized pointer. Dereferencing a NULL pointer is generally a
Bad Thing and will lead to segfaults. As a fun side effect, since NULL is 0, we
can use it in an if statement:

```
void *ptr = ...;
if (ptr) {
    // ptr is valid
} else {
    // ptr is not valid
}
```

I hope you found this article useful! If you’d
like something fun to read next, read about  [“three star
programmers”](http://c2.com/cgi/wiki?ThreeStarProgrammer) , or programmers who
have variables like  `void***` .
