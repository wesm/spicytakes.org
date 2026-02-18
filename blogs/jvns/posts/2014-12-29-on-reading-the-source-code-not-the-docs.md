---
title: "On reading the source code, not the docs"
date: 2014-12-29
url: https://jvns.ca/blog/2014/12/29/on-reading-the-source-code-not-the-docs/
slug: on-reading-the-source-code-not-the-docs
word_count: 572
---


In my first programming job, I worked at a [web development company](http://evolvingweb.ca)
and wrote modules for [Drupal](https://drupal.org) sites.


Every so often, I’d need to understand some specific Drupal edge case
(say, how the text in the tabs on a search page was determined). And it
wouldn’t be documented. And Stack Overflow didn’t have any answers about
it, and my [colleagues](http://twitter.com/tavarm) didn’t know. I like
to think of this as a “oh right I actually need to know how to program”
moment – nobody’s going to tell me what to do, I just need to figure it
out.


The consultancy’s cofounder was [Alex Dergachev](https://twitter.com/dergachev),
and he taught me a really important thing! Whenever I had a question
like this, he’d tell me to just read Drupal’s source code, and then I’d
know the answer. This is pretty obvious in retrospect, but it wasn’t
obvious to me at the time.


I originally felt like Drupal was too complicated to understand (it’s a
big codebase!), but it turned out that if I tried I could usually figure
out what I needed to know.


This works particularly well when I understand pretty well what the code
I’m using is doing, but am just unsure about some particular detail.
For example “will this button appear for all users, or only admin
users?” I use this all the time at work, and most of you probably do
too! There are always details about code that aren’t exhaustively
documented, and using grep to find answers is incredibly helpful.


### But sometimes reading the code doesn’t work.


Recently I was writing a map reduce job, and there was an out of memory
error. And it wasn’t really obvious why, and I tried to look at the
stack trace and read some relevant parts of the source code. And it
just. did not. help. at. all.


It turned out that I was doing a join, and the rows on the right side of
the join were too big, and this was causing
[Cascading](http://www.cascading.org/) to be sad. But to understand
that, it was important to understand how Cascading joins worked! And I
didn’t know that at all. Thankfully I work with
[people](https://twitter.com/avibryant)
[who](https://twitter.com/jeffbalogh)
[know](https://twitter.com/colinmarc)
[things](https://twitter.com/DanielleSucher)
I don’t know about Hadoop and they could help figure it out.


So it seems like there are a few different levels of bug difficulty:

1. It’s immediately obvious to you what’s wrong
2. You Google the exception, read some documentation or Stack Overflow,
and then it’s immediately obvious what’s wrong
3. You don’t know what’s wrong, but you know more or less where in the
(open source) library code you’re using to look, and you can read the
code to figure it out
4. You’re missing some bigger-picture of knowledge about the code you’re
running that you need to understand the bug (like me not
understanding how joins work in Cascading).


I still struggle with approaching problems in #4 (especially if I
don’t know that I don’t know the Thing That I’m Missing). For now, I
just [ask](http://jvns.ca/blog/2014/06/13/asking-questions-is-a-superpower/),
and often the people I work with have answers, and are really helpful.


I think if I couldn’t do this, I’d read a lot of documentation and hope
that some of it was relevant. I’d love more ideas, though. Or if you
disagree with my hierarchy of bug difficulty that I made up 10 minutes
ago and have your own, I’d love to know that too :) :)
