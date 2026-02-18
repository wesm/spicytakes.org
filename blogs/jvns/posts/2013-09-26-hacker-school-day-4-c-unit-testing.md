---
title: "Hacker School Day -4: unit testing in C. checkmk!"
date: 2013-09-26
url: https://jvns.ca/blog/2013/09/26/hacker-school-day-4-c-unit-testing/
slug: hacker-school-day-4-c-unit-testing
word_count: 339
---


So I’ve been accepted to the fall batch at
[Hacker School](http://hackerschool.com), which starts on Monday. I
managed to find somewhere to live in New York, so today I went to a café
to do some coding.


One of my goals for this batch is to get better at low-level programming
and managing my own memory, so I’m planning to learn C a bit, as well as
maybe Go or Rust. I’ve never really gotten further than reversing a
string in C, so.


I am also thinking of starting to write about coding on the internet, so
here this is.


Today I decided to try implementing snake in C, using ncurses. This
turned out to be easier than I thought it would be – ncurses is pretty
nice. Here’s [what I have so far on Github](http://github.com/jvns/snake). (spoiler:
not too much. But you can press arrow keys and it moves! There is as yet
no food, but you can die.)


The hardest part actually turned out to be unit testing. My friend
[Chris](http://www.sable.mcgill.ca/~cpicke/) pointed me to a unit
testing framework [check](http://check.sourceforge.net/doc/check_html/)
that he maintains. HOWEVER the tutorial starts talking about autotools.
I spent an hour or two trying to understand how to autotools and it made
me want to kill someone. So I stopped trying to use autotools, since I
just want my code to run on my computer today.


BUT THEN I found out that check comes with `checkmk`, an awk script that
turns snippets like this:


```
#test test_create_cell
    struct Snake* snake = create_cell(2, 3);
    fail_unless(snake->x == 2);
    fail_unless(snake->y == 3);

```


into tests that `check` understands. And I could just write a normal
`Makefile` and everything was great.


For some reason `checkmk` is in the source distribution for check, but
not in the Ubuntu package. Also if you download `checkmk` from
[this page](http://micah.cowan.name/projects/checkmk/), it doesn’t work.


Conclusion: snake is too easy of a thing to do, so I probably won’t take
this much further. Next coding day maybe I’ll start trying to write a
shell? We will see.
