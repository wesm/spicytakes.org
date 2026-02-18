---
title: "Asking questions is a superpower"
date: 2014-06-13
url: https://jvns.ca/blog/2014/06/13/asking-questions-is-a-superpower/
slug: asking-questions-is-a-superpower
word_count: 756
---


There are all kinds of things that I think I “should” know and don’t.
A few things that I don’t understand as well as I’d like to:

- Database replication and sharding (seriously how does replication
even work)
- How fast a computer can process data (should I expect more or less
than 6GB/s if it’s a simple CPU-bound program where the data is
already in RAM?)
- How do system calls work, reeeeally? (I do not understand context
switching nearly as well as I could!)
- An truly embarrassing amount of basic statistics, even though I have
a math degree.


There are lots of much more embarrassing things that I just can’t
think of right now.


I’ve started trying to ask questions any time I don’t understand
something, instead of worrying about whether people will think I’m
dumb for not knowing it. This is *magical*, because it means I can
then learn those things!


One of my very favorite examples of this is how I started learning
about operating systems. At the beginning of Hacker School, I realized
that I legitimately did not know what a kernel was or did more than
“er, operating system stuff”.


This was super embarrassing! I’d been using Linux for 10 years, and I
didn’t really understand at all what the basic responsibilities of the
Linux kernel were. Oh no! Instead of hiding under a rock, I *asked*.
And then people told me, and I wrote
[What does the Linux kernel even do?](http://jvns.ca/blog/2013/10/02/day-3-what-does-the-linux-kernel-even-do/).


I don’t know how I would have learned without asking. Now I have given
talks about getting started with understanding the Linux kernel! So
fun!


One surprising thing about asking questions is that when I start
digging into a problem, people who I respect and who know a lot will
sometimes not know the answers at all! For instance, I’ll think that
someone totally knows about the Linux kernel, but of course they don’t
know everything, and if I’m trying to do something specific like write
a rootkit they might not know all the details of how to do it.


[aphyr](http://aphyr.com/) is a really good example of someone who
asks basic questions and gets unexpected answers. He does research
into whether distributed systems are reliable (linearizable?
consistent? / available?). The results he finds are like
[RabbitMQ might lose 40% of your data](http://aphyr.com/posts/315-call-me-maybe-rabbitmq).
Ooooops. If you don’t start asking questions about how RabbitMQ works
from the beginning (in his case, by writing a program called Jepsen
that automates this kind of reliability testing), then you’ll never
find that out. (be skeptical! Don’t believe what people say even if
they’re using fancy words!)


## “I don’t understand.”


Another hard thing is admitting that I don’t understand. I try to not
be too judgemental about this – if someone is explaining something to
me and it doesn’t make sense, it’s possible that they’re explaining it
badly! Or that I’m tired! Or any other number of reasons. But if I
don’t *tell* them I’m don’t understand, I’m never going to understand
the damn thing.


So I try to take a deep breath and say cheerfully “Nope!”, figure
exactly which aspect of the thing I don’t understand, and ask a
clarifying question.


As a side effect, when I go to a talk about a subject I’m interested in, and I
don’t understand something, I’m a lot more willing to ask questions like “so
what IS <basic concept that wasn’t explained>?”. Usually people are
really happy to answer!


## Avoiding mansplaining


A difficult thing about asking questions is that I have to be pretty
careful about asking the *right* questions and making it clear which
parts I know already. This is just good hygiene, and makes sure
nobody’s time gets wasted.


For instance, I have sometimes said things like “I don’t know anything
about statistics”, which is actually false and sometimes results in
people trying to explain basic probability theory to me, or what an
estimator is, or maybe the difference between a biased and unbiased
estimator. It turns out these are actually things I know! So I need to
be more specific, like “can we walk through some basic survival
analysis?” (actually a thing I would like to understand!)


## HUGE SUCCESS


So! Understanding and learning are more important than feeling smart.
Probably the most important thing I learned at Hacker School was how
to ask questions and admit when I don’t understand something. I know
way more things now as a result! (see: this entire blog of things I
have learned)
