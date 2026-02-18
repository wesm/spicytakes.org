---
title: "Spooky action at a distance"
date: 2021-01-19
url: https://drewdevault.com/2021/01/19/Spooky-code-at-a-distance.html
slug: Spooky-code-at-a-distance
word_count: 535
---

Einstein famously characterized the strangeness of quantum mechanics as “spooky
action at a distance”, which, if I had to pick one phrase about physics to be my
favorite, would be a strong contender. I like to relate this to programming
language design: there are some language features which are similarly spooky.
Perhaps the most infamous of these is operator overloading. Consider the
following:

```
x + y
```

If this were written in C, without knowing anything other than the fact that
this code compiles correctly, I can tell you that x and y are numeric types, and
the result is their sum. I can even make an educated guess about the CPU
instructions which will be generated to perform this task. However, if this were
a language with operator overloading… who knows? What if x and y are some kind
of some Vector class? It could compile to this:

```
Vector::operator_plus(x, y)
```

The performance characteristics, consequences for debugging, and places to look
for bugs are considerably different than the code would suggest on the surface.
This function call is the “spooky action” — and the distance between the
“+” operator and the definition of its behavior is the “distance”.

Also consider if x and y are strings: maybe “+” means concatenation?
Concatenation often means allocation, which is a pretty important side-effect to
consider. Are you going to thrash the garbage collector by doing this?  *Is* 
there a garbage collector, or is this going to leak? Again, using C as an
example, this case would be explicit:

```
char *new = malloc(strlen(x) + strlen(y) + 1);
strcpy(new, x);
strcat(new, y);
```

If the filename of the last file you had open in your text editor ended in
 `.rs` , you might be frothing at the mouth after reading this code. Strictly for
the purpose of illustrating my point, however, consider that everything which
happens here is explicit, opt-in to the writer, and obvious to the reader.

That said, C doesn’t get off scott-free in this article. Consider the
following code:

```
int x = 10, y = 20;
int z = add(x, y);
printf("%d + %d = %d\n", x, y, z);
```

You may expect this to print out  `10 + 20 = 30` , and you would be forgiven for
your naivety.

```
$ cc -o test test.c
$ ./test
30 + 20 = 30
```

The savvy reader may have already figured out the catch: add is not a function.

```
#define add(x, y) x += y
```

The spooky action is the mutation of x, and the distance is between the apparent
“callsite” and the macro definition. This is spooky because it betrays the
reader’s expectations: it looks and smells like a function call, but it does
something which breaks the contract of function calls. Some languages do this
better, by giving macros an explicit syntax like  `name!(args...)` , but,
personally, I still don’t like it.

Language features like this are, like all others, a trade-off. But I’m of the
opinion that this trade is unwise: you’re wagering readability, predictability,
debuggability, and more. These features are toxic to anyone seeking stable,
robust code. They certainly have no place in systems programming.
