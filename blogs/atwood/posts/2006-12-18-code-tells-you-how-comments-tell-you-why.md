---
title: "Code Tells You How, Comments Tell You Why"
date: 2006-12-18
url: https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/
slug: code-tells-you-how-comments-tell-you-why
word_count: 717
---

In an earlier post on [the philosophy of code comments](https://blog.codinghorror.com/when-good-comments-go-bad/), I noted that **the best kind of comments are the ones you don’t need**. Allow me to clarify that point. You should first strive to make your code as simple as possible to understand without relying on comments as a crutch. Only at the point where the code *cannot* be made easier to understand should you begin to add comments.


It helps to keep your audience in mind when you’re writing code. The classic book [Structure and Interpretation of Computer Programs](https://web.archive.org/web/20061224075206/http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-7.html), originally published in 1985, gets right to the point in the preface:


> Programs must be written for people to read, and only incidentally for machines to execute.


Knuth covers similar ground in his classic 1984 essay on [Literate Programming](http://www-cs-faculty.stanford.edu/~knuth/lp.html) ([pdf](http://www.literateprogramming.com/knuthweb.pdf)):


> Let us change our traditional attitude to the construction of programs: Instead of imagining that our main task is to instruct a computer what to do, let us concentrate rather on explaining to human beings what we want a computer to do.
> The practitioner of [literate programming](http://en.wikipedia.org/wiki/Literate_programming) can be regarded as an essayist, whose main concern is with exposition and excellence of style. Such an author, with thesaurus in hand, chooses the names of variables carefully and explains what each variable means. He or she strives for a program that is comprehensible because its concepts have been introduced in an order that is best for human understanding, using a mixture of formal and informal methods that reinforce each other.


If you write your code to be consumed by other programmers first, and by the compiler second, you may find the need for additional comments to be greatly reduced. Here’s an excellent example of [using comments as a crutch](https://web.archive.org/web/20061230025457/http://www.jtse.com/blog/2006/12/15/does-bad-writing-reflect-poor-programming-skills):

kg-card-begin: html

> This is a snippet of code from a well funded, closed-source system that has been deployed in production for years.
> float _x = abs(x - deviceInfo->position.x) / scale;
> int directionCode;
> if (0 < _x & x != deviceInfo->position.x) {
> if (0 > x - deviceInfo->position.x) {
> directionCode = 0x04 /*left*/;
> } else if (0 < x - deviceInfo->position.x) {
> directionCode = 0x02 /*right*/;
> }
> }
> This is equivalent to the following, more readable code, with a bugfix.
> static const int DIRECTIONCODE_RIGHT = 0x02;
> static const int DIRECTIONCODE_LEFT = 0x04;
> static const int DIRECTIONCODE_NONE = 0x00;
> int oldX = deviceInfo->position.x;
> int directionCode 
> = (x > oldX)? DIRECTIONCODE_RIGHT
> : (x < oldX)? DIRECTIONCODE_LEFT
> : DIRECTIONCODE_NONE;
> Note that more comments does not mean more readable code. It didn’t in this example. **The comments in the snippet above – if you even noticed them – only clutter the code even more.** Sometimes *fewer* comments makes for more readable code. Especially if it forces you to use meaningful symbol names instead.

kg-card-end: html

Although there are almost infinite opportunities to refactor and simplify code to obviate the need for comments, explaining yourself exclusively in code has its limits.


No matter how simple, concise, and clear your code may end up being, it’s impossible for code to be completely self-documenting. **Comments can never be replaced by code alone.** Just ask [Jef Raskin](https://web.archive.org/web/20131218060559/http://queue.acm.org/detail.cfm?id=1053354):

kg-card-begin: html

> Code can’t explain why the program is being written, and the rationale for choosing this or that method. Code cannot discuss the reasons certain alternative approaches were taken. For example:
> /* A binary search turned out to be slower than the Boyer-Moore algorithm for the data sets of interest, thus we have used the more complex, but faster method even though this problem does not at first seem amenable to a string search technique. */

kg-card-end: html

What is perfectly, transparently obvious to one developer may be utterly opaque to another developer who has no context. Consider [this bit of commenting advice](http://everything2.com/index.pl?node_id=1709851&displaytype=printable):


> You may very well know that
> `$string = join('',reverse(split('',$string)));`
> reverses your string, but how hard is it to insert
> `# Reverse the string`
> into your Perl file?


Indeed. It’s not hard at all. Code can only tell you *how* the program works; comments can tell you *why* it works. Try not to shortchange your fellow developers in either area.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
