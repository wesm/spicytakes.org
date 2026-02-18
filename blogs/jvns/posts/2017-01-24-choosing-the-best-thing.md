---
title: "Choosing the 'best software'"
date: 2017-01-24
url: https://jvns.ca/blog/2017/01/24/choosing-the-best-thing/
slug: choosing-the-best-thing
word_count: 783
---


When we write software, we make a lot of decisions. Should I use Angular or
React? Apache or nginx? Python or Ruby? Which one is the BEST?


I am going to make an argument that “it literally does not matter what is the
best”. Is it a good argument? I’m not sure!


Now – I took, like, 3 optimization classes in university. Obviously I am into
optimization. So I obviously care somewhat about picking the Best Thing. But I
often find this question of “what is the BEST THING TO USE” kind of…
paralyzing? So it doesn’t seem like that framework is working for me very well.


### another way to think about making decisions


So, let’s talk about another way to think about making decisions than “what is
the Best Thing in this situation”.


I run an event series called “lightning talks and pie”. At the most recent one, Ines Sombra gave a talk about capacity planning. In it, she said that there are 3 reasons you might want to change something about your system:

1. It’s too expensive
2. It’s too difficult to operate (humans spend a ton of time worrying about it)
3. It’s not doing the job it’s supposed to


I find these 3 criteria a lot easier to reason about than the “Choose The Best
Thing” framework. For example! At work, we have load balancers. I had a
conversation today with someone about how their load balancer system is
different from ours.


Our loadbalancers

1. are not expensive to operate
2. don’t take a lot of maintenance (they generally Just Work)
3. load balance requests like we want them to, as far as I know


So, it literally does not matter at all if they are the Best System! It’s
possible that there is a strictly better way to do load balancing. But the
system is actually pretty great, and there are several things that are too
expensive or that require a lot of maintenance or that are not working the
right way that I could be working on improving instead.


It is of course still interesting to learn about other load balancer systems
– in the event that we *do* need to change something later, it is useful to
know what other things people are doing in the world.


### tradeoffs


One thing sometimes people say to me when I am trying to make a decision about
whether to use X or Y is “well, you know, there are tradeoffs, it depends on
your situation”. This is definitely true (there are always tradeoffs)! But I
find this framing does not really help me actually make a decision. Because
often the situation is something like “well, X is slower but easier to use, Y
is faster but harder for humans to use”. And I often feel like.. “okay, so
what do I do now? Saying that there’s a ’tradeoff’ doesn’t help me at all!”


So I feel like this process is easier for me to actually follow:

1. figure out what you actually **need** the system to do
2. figure out which choices will accomplish that, at least mostly
3. pick one at random, or whatever people feel better about that day, who knows
4. Probably pick the one that people like the best. How the people around you feel is important.


Nobody has ever told me “you should make technical decision by just figuring
out what will work and then just pick whatever is the most popular”, but it
seems kind of reasonable to me?


### some limitations


The question of “does the system work” is complicated.


For example, sometimes **I** will think that a system works fine the way it
is, and that there’s no need to change it. But then someone else will have an
AMAZING IDEA about how that thing could be way way better, and they’ll put it
into practice, and then I’ll be like “wow, that is totally way better in ways
that I did not understand at all. Good thing you changed it!”.


So there is definitely room for redefining what “the system works” even means.


### “it doesn’t matter what the best thing is”


I find the idea that “it doesn’t matter what the best thing is” kind of
freeing. After all, building a system that works well enough within the
constraints that you have is already REALLY HARD. So it seems unreasonable to
additionally require that that system also be the Best Possible Thing.


If you have more and better ideas about this you can tell me [on twitter](https://twitter.com/b0rk). We will return to our regularly scheduled
excitement abour programming soon. (I have a networking zine which is almost
ready!!!)
