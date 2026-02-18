---
title: "Day 41: Linkers are upsetting"
date: 2013-12-12
url: https://jvns.ca/blog/2013/12/12/day-41-linkers-are-still-upsetting/
slug: day-41-linkers-are-still-upsetting
word_count: 109
---


Today I spent pretty much the whole day trying to figure out what’s
going on with a
[linker problem I’m having](http://jvns.ca/blog/2013/12/06/day-38-after-7-days/).
I’ve fixed it, but I don’t understand *why* it’s fixed, and I am
having no luck.


[Allison](http://akaptur.github.io/) and I paired on it for a bit, and
we discovered that if we order the sections `.text .rodata .data .bss`, then the ELF file works correctly, but if they’re in any other
order it doesn’t work.
[There’s a gist](https://gist.github.com/jvns/ec07560a4484edd30d70)
with the offending linker scripts.


I also created
[a StackOverflow question](http://stackoverflow.com/questions/20526765/linker-scripts-strategies-for-debugging)
but it is not getting any love.


To compensate, I wrote a
[tiny start of a tutorial about binary formats](http://gist.io/7923908).
