---
title: "Pretty Code, Ugly Code"
date: 2006-06-19
url: https://blog.codinghorror.com/pretty-code-ugly-code/
slug: pretty-code-ugly-code
word_count: 698
---

Christopher Seiwald’s [Seven Pillars of Pretty Code](https://web.archive.org/web/20060626214912/http://www.perforce.com/perforce/papers/prettycode.html) argues that **code that looks good, works good**:

1. **Code changes should blend in with the original style.**
It should not be possible to discern previous changes to a file without seeing the previous revisions. Nothing obscures the essential visual cues more than a shift in style. This practice should be applied as wide as possible: absolutely within functions, generally within a file, and if you’re lucky across the system.
2. **Keep columns narrow.**
Just as with books and magazines, code should be narrow to focus the gaze. As I mention in “Overcome Indentation,” the left edge of the code holds the structure and the right side holds the detail, and big long lines mix zones of structure and detail, confusing the reader.
3. **Break code into logical blocks so that each does a single thing or single kind of thing.**
This principle should apply within functions, and in a larger sense, among separate code blocks. A reader can only avoid a total reading if a cursory inspection can reveal the whole block’s nature.
4. **Set off code blocks with whitespace and comments that describe each block.**
Comments should rephrase what happens in the block, not be a literal translation into English. Even if your code is inscrutable and your comments jibberish, the reader can at least attempt to triangulate on the actual purpose.
5. **Reduce, reduce, reduce. Remove anything that will distract the reader.**
Use short names (like i, x) for variables with a short, local scope or ubiquitous names. Use medium length for member names. Use longer names only for global scope (like distant or OS interfaces). The tighter the scope, the shorter the name. Long, descriptive names may help the first time reader but hinder him every time thereafter.
6. **Two or more pieces of code that do the same or similar thing should be made to look the same.**
Nothing speeds the reader along better than seeing a pattern. These similar looking pieces of code should be lined up one after the other. Grouping reduces the number of entities the reader has to grasp, a critical approach to simplifying the apparent complexity of code.
7. **The left edge of the code defines its structure, while the right side holds the detail.**
You must fight indentation to safeguard this property. Code which moves too quickly from left to right (and back again) mixes major control flow with minor detail. Forcibly align the main flow of control down the left side, with one level of indentation for if/while/for/do/switch statements. Use break, continue, return, even ’goto’ to coerce the code into left-side alignment. Rearrange conditionals so that the block with the quickest exit comes first, and then return (or break, or continue) so that the other leg can continue at the same indentation level.


It’s an entirely reasonable set of advice. Until you realize that Christopher is using his very own [jam/make.c](https://web.archive.org/web/20140217161937/http://www.codinghorror.com/blog/files/make.c.htm) as a shining example of the pillars of pretty code.


And **make.c is extremely ugly to me**.


I don’t know if I’d ever consider C code *pretty*, per se. Maybe it has a nice personality. But pretty? No way. And I’m sure Ruby, Lisp, and Smalltalk aficionados feel the same way about C# code. I know most C# developers can barely force themselves to even look at VB.NET code.


Clearly, pretty code is in the eye of the beholder.


Besides the fact that it’s C, I have a few other problems with Mr. Seiwald’s make.c code:

- It embeds source control information in the comments. Isn’t this why we have source control systems?
- It uses complex, difficult to maintain block alignments in the comments, variables, and function declarations. Unless your IDE does this for you, this is the formatting equivalent of a house of cards.
- There are functions named make and make0. Ouch.


The code formatting, as promised, is pretty. But the emphasis on formatting does make me wonder – rather than focusing on the external, cosmetic attributes of the code, shouldn’t we be searching for something prettier on the *inside?* Such as a higher level language?

[clean code](https://blog.codinghorror.com/tag/clean-code/)
[code style](https://blog.codinghorror.com/tag/code-style/)
[code structure](https://blog.codinghorror.com/tag/code-structure/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
