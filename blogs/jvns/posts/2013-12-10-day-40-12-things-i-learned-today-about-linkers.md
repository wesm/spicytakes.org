---
title: "Day 40: 12 things I learned today about linkers."
date: 2013-12-10
url: https://jvns.ca/blog/2013/12/10/day-40-12-things-i-learned-today-about-linkers/
slug: day-40-12-things-i-learned-today-about-linkers
word_count: 346
---


I read 11 parts of
[this series on linkers](http://lwn.net/Articles/276782/) today. I
also wrote an
[epic blog post](http://jvns.ca/blog/2013/12/10/day-40-learning-about-linkers/),
but here is the tl;dr version (trying to synthesize…). This is all
about ELF. I use “ELF file” and “object file” interchangeably.


In no particular order:

1. To inspect an ELF object file, you can use `objdump`, `readelf`
and/or `nm`.
2. Executable files have **segments** and **sections**. Each segment has
many sections. The operating system looks at the segments, not the
sections. Read/Write/Execute permissions are controlled per
segment, not per section.
[[Part 8]](http://www.airs.com/blog/archives/45)
3. ELF symbols have types! And different visibility options!
[[Part 5]](http://www.airs.com/blog/archives/42)
4. The linker knows about threading, and does optimizations to make
threading easier. [[Part 7]](http://www.airs.com/blog/archives/44)
5. An object file can define two symbols with the same name and
different symbols, for backwards compatibility.
[[Part 9]](http://www.airs.com/blog/archives/46)
6. Those `.a` files? Those are just collections of `.o` object files,
and they’re called “archives”!
[[Part 11]](http://www.airs.com/blog/archives/48)
7. Linkers can work in parallel to some extent.
[[Part 10]](http://www.airs.com/blog/archives/47)
8. Linkers actually have to do fairly complicated stuff to allow the
code in a shared library to be shared between different programs
and save memory. [[Part 6]](http://www.airs.com/blog/archives/43)
for memory savings,
[[Part 4]](http://www.airs.com/blog/archives/41) for the PLT/GOT
9. There’s more than one way to link a shared library, and the choices
you make affect how quickly it loads
[[Part 4]](http://www.airs.com/blog/archives/41)
10. In the Mach-O executable format you can have assembly code for
*differrent architectures* in the same executable. Nuts. And
there’s [FatELF](https://icculus.org/fatelf/) that extends ELF to
do the same thing. (edit: and isn’t being developed anymore)
11. Every `.o` file has a “relocation table” listing every single
reference to a symbol that the linker will need to update, and how
it will need to update it.
[[Part 2]](http://www.airs.com/blog/archives/39)
12. If you’re making a speed comparison for a linker, you might
compare it to `cat`. [[Part 1]](http://www.airs.com/blog/archives/38)


I’m curious about these ELF symbol versions – they sound kind of like
polymorphism to me, and I’m wondering why people use symbol name
mangling to implement polymorphism instead of symbol versions.
Probably very good reasons!
