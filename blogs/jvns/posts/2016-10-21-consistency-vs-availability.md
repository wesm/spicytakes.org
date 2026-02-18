---
title: "Consistency vs availability (wat?)"
date: 2016-10-21
url: https://jvns.ca/blog/2016/10/21/consistency-vs-availability/
slug: consistency-vs-availability
word_count: 1332
---


HELLO! I think I just understood something about consistency vs
availability for the first time today.


I always feel kind of dumb writing this stuff because I’ve been reading
[aphyr’s amazing blog](https://aphyr.com/) for like 2 years, and
watching his talks, and I feel like I understand them sometimes! But at
the same time I feel like I barely understand the basic concepts.


So! I was writing a blog post about work today, and we were talking
about a System (database) that we run. In the past, the system was
having availablity problems. I remember pretty distinctly being paged at
midnight one day and being like UGH THE SYSTEM IS DOWN WHAT’S HAPPENING.


At the time, I did not really understand why the System was down, it was
maintained by other people, and they brought it back up, and then it
totally stopped going down and now everything is fine.


But why did the System stop going down? Today I learned why!


LET ME TELL YOU A STORY ABOUT CONSISTENCY AND AVAILABILITY. This
is kind of a dangerous blog post to write because I know practically
nothing about distributed systems but maybe some of you beginners like
me will learn something.


## the CAP theorem (& intuition)


This is not going to be a blog post about the CAP theorem. I have never
read the CAP theorem. Martin Kleppmann says he [doesn’t even believe the CAP theorem is useful](http://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html) (see [a critique of the CAP theorem for more](https://arxiv.org/abs/1509.05393)).


I still have honestly not fully understood that blog post by Kleppmann.
I still need to read it 3 more times but I’ve learned some things from
it and I think it’s interesting.


Anyway the point of “consistency vs availability” to me is not the CAP
theorem. I think there’s just like this.. general idea that, in
distributed systems, there is a conflict between consistency and
availability.


I majored in math! I proved theorems for like 5 years. One thing I
learned while proving theorems is – it’s really useful to have
**intuitions** about the formal systems you’re working with. If you have
intuition, you can say “hmm, that smells like consistency, and that
smells like availability, maybe those two things are in conflict!” And
then you can go take your fuzzy idea and actually go make a precise
statement and prove it.


I think taking fuzzy ideas about how real-world systems operate and
translating them into actual theorems that you can use to reason with is
what distributed systems researchers do. Anyway, I’m not a distributed
systems researcher and I don’t know hardly anything about distributed
systems theory. So we’re just going to talk about fuzzy feelings.


## what is availability


Disclaimer: We’re going with fuzzy “smells like consistency/availability”
definitions here. If you’re like “julia, all your definitions are stuff
you made up just now”, you will be right. You should go read aphyr or
Martin Kleppmann if you want real definitions. Their writing is real
good and they have done a ton of work to make it accessible to mere
mortals like us.


So, I know what availability is! It means I don’t get paged because the
system is down. Basically it means if you ask, you can always get an
answer! I like that. What’s wrong with that?


## wtf is consistency


So! let’s say we have 100 computers in a “cluster”. I think
“consistency” kinda means “if you query any computer in the cluster at
the same time it will tell you the same thing”.


The C in CAP actually means “linearizability” and there’s a great
explanation of it in [that Kleppmann blog post](http://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html).


## why are consistency and availability in conflict?


Well, let’s suppose we define availability as “any machine of the 100
machines can always give me an answer” and consistency as “every machine
should always give me the same answer”.


Then it’s kind of obvious that these are in conflict, right? For the
machines to all agree (especially if their state is being updated!),
they need to **communicate with each other**. And we know that networks
are unstable! So if Machine 1 and Machine 2 can’t talk to each other,
how can they give me the same answer? That doesn’t make sense!


When i write this blog I don’t really fact check that carefully. I’m
just like “y’all anything i write here i could be wrong”. That makes it
really easy to post stuff like this quickly! I think that’s kind of the
same tradeoff :)


so:


## building consistent systems is hard


If your system only runs on one machine, building consistent systems is
easy! But if you want it to run on a lot of machines, it gets
complicated fast.


The simplest algorithm I know of for building consistent systems is
[Raft](https://raft.github.io/raft.pdf). This algorithm is really
complicated! There is a paper and it has ALL THESE PAGES. WHAT DO THEY
EVEN SAY. People have implemented Raft! [etcd is a key-value store that uses Raft](https://aphyr.com/posts/316-jepsen-etcd-and-consul).


So if you want one of these algorithms in your life that is a thing you
can have.


## building available systems is easy


Let’s say I have a database, and I replicate writes to a bunch of
secondary machines. I can make my system distributed and available
pretty easily! I can just put it on a lot of machines and read from any
random machine. That’s cool! Distributed systems!


There might be some complicated reason why it’s hard to make a system
that’s available but I don’t see it – if you don’t care if the data
you’re reading is necessarily totally right, then there’s no problem! Do
whatever you want!

- if you have one machine, you’re consistent, but not that available
(because that machine could explode)
- if you implement Raft, you’re still consistent, but maybe your latency
goes up and your availability doesn’t get to 100% (because there might
be weird network partitions)
- if you sacrifice consistency and add a bunch of machines, you can be
~100% available


## back to my System (why did it stop going down???)


Okay, but why did my System at work stop going down? WELL. We decided
that it didn’t actually need to be consistent! (I won’t go into why, but
it makes sense) We traded off consistency for availability, and now the
system never goes down anymore! Instead sometimes the data in it gets a
little out of date. This is not a big deal.


SO! My system started working because we **dropped consistency as a
requirement**. It wasn’t because we fixed bugs, or because we were
really smart. We changed our mind about what we wanted out of the
system, and that helped us operate it better! COOL. There are LOTS of
systems that don’t need to be consistent, it turns out!


## distributed systems make me grumpy


I think I used to think distributed systems were kind of like.. cool and
awesome and sexy? and that cool smart people worked on them.


I mean, if you work on distributed systems you are probably cool and
smart. But. Now I work with a whole bunch of computers, like hundreds of
them.


These days when i see a distributed systems problem i’m more likely
to think OH NO CAN WE NOT. Like can we just put it on a single computer?
Or can we put it a bunch of computers where none of the computers care
what the other ones are doing? I feel like really good distributed
systems enginering is being like extremely careful about a small number
of consistent systems and then making everything else as dumb as
possible.


Like “the best distributed system is the one you deleted”.


Anyway. Understanding about tradeoffs between consistency and
availability really makes me want to isolate the places where I want
consistency really carefully so I can make sure that they actually work,
and then have everything else rely on those places. I think that’s what
services like [Zookeeper](https://zookeeper.apache.org/) are about?
