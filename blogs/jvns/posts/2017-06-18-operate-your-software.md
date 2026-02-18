---
title: "What can developers learn from being on call?"
date: 2017-06-18
url: https://jvns.ca/blog/2017/06/18/operate-your-software/
slug: operate-your-software
word_count: 1563
---


We often talk about being on call as being a bad thing. For example, the night
before I wrote this my phone woke me up in the middle of the night because
something went wrong on a computer. That’s no fun! I was grumpy.


In this post, though, we’re going to talk about what you can learn from being
on call and how it can make you a better software engineer!. And to learn from
being on call you don’t necessarily need to get woken up in the middle of the
night. By “being on call”, here, I mean “being responsible for your code when
it breaks”. It could mean waking up to issues that happened overnight and
needing to fix them during your workday!


Everything in here is synthesized from an amazing Twitter thread by Charity Majors where she asked “How has being on call made you a better engineer?”: [https://twitter.com/mipsytipsy/status/847508734188191745](https://twitter.com/mipsytipsy/status/847508734188191745)


### Learn what kinds of production problems are common and uncommon


When you’re designing a system, you need to design for its error cases! When I
was just starting out as an engineer, I found coming up with error cases really
hard. ANYTHING could go wrong! But it’s important to have a better model of
system failure than “anything could go wrong, protect against everything!”
because often you have to prioritize where to spend your time, and you should
spend your time worrying about edge cases that are actually likely to happen.


Being on call can teach you very fast what kinds of edge cases your system runs
into frequently!


For example, after seeing some software fail, I know that DNS queries can fail.
It’s useful to have error handling for DNS queries (and network requests in
general), even if you think the servers you’re talking to are mostly reliable!


I also know that in principle RAM can be faulty (when you set a value in memory, it can get set to something else!) but it’s not something that’s ever happened to me in practice (yet!) so I worry about it less. (this might be because servers use ECC memory?) This post [Exploiting the DRAM rowhammer bug to gain kernel privileges](https://googleprojectzero.blogspot.ca/2015/03/exploiting-dram-rowhammer-bug-to-gain.html) is a good example about how you can use RAM being faulty to make an exploit.


### Learn to build in monitoring and diagnostics early


There’s nothing quite like a system breaking, being in charge of fixing it, and
having no way of seeing what’s wrong to convince you of the value of building
monitoring and logging into your application.


Being on call will teach you quickly what *kinds* of diagnostics you need to
debug your application. If you get paged because your application is taking an
abnormally long time to make database queries, you can start monitoring how
long your database queries take! Then next time it’ll be much easier for the
person on call to see if that’s the problem.


The great thing about this is that these lessons last even beyond your current
on-call rotations – you can notice “hey, every time I write a program I end up
logging how long its database queries take, I’ll just put that in at the
beginning this time!”


### Understand the parts of the system that aren’t yours


It’s easy to think of the parts of the system you don’t own as a black box. “I
just make database queries and they work, it’s fine, the database team is in
charge of the database”.


But it’s actually incredibly useful to have a basic understanding of the
limitations of the systems you work with! If you’re working on the backend for
a web application, you want to know how many queries it’s okay to make to your
database, approximately how much network bandwidth you have to work with, how
much it’s okay to write to disk, and more.


If you get paged because your application is making too many database queries,
this is an awesome opportunity to learn more about the limitations of the
database you use! And then (can you see a pattern here?) the next time you work
on something that makes a lot of database queries, you can check up front to
make sure that it’s okay.


### Gain confidence in your judgement


A couple great quotes from this thread:


> It helped me gain confidence in my own judgment. You have to make big calls, take scary actions, live through terrible decisions.


> I stop second guessing myself. If I’m getting paged, shits down and broken hard - no time to second guess yourself.


### Learn what needs urgent attention


Some problems need to be fixed RIGHT NOW, and other problems… really don’t.
It used to be really mysterious to me how some engineers could just tell you
“yeah, that’s not a big deal” and be.. right about it?


This intuition is really important to build (otherwise you’ll panic every time
there’s an error and you’ll never get anything done!). When you’re on call for
a system, you see the urgent problems when they happen and you understand what
causes them. So you slowly gain intuition for “oh, okay, when X happens it
often causes a serious issue, but when Y happens it’s not a big deal”.


This also lets you prevent upcoming problems proactively – if you see
something worrisome happening, you can fix it before anyone on your team has to
be woken up in the middle of the night.


### Learn to design reliable systems


There’s been a common thread through all of this. A huge part of our jobs as
software engineers is to design systems that continues working for your
customers even when things don’t happen quite as your expected. A great way to
learn how to design for failure is to be on call for your software.


Kamal pointed out to me that it’s easy to have a system where the code is fine
(not too many bugs, etc), but because of some fundamental design choice it
doesn’t run well in production. For example, you could design a system which
needs to make many database queries every time a user makes a request. So
having a good understanding of the production implications of different design
choices will help you design better systems!


### Learn how to make minimum effective change


When there’s an
[incident](https://increment.com/on-call/when-the-pager-goes-off/), you want to
stabilize the system before fixing the root cause (ok, this server is on FIRE,
can we just divert traffic away from it before figuring out why?)! This is a
useful skill when you’re being paged, but also when you have a system that
needs help but don’t necessarily have the time/resources to completely fix it
right now.


### Learn about distributed systems & consistency & race conditions


> Being on call has taught me about race conditions


Recently I got an alert that a job I’d written was failing. I looked at it for
a while, and then I realized “oh, this is happening because S3 list operations
are eventually consistent” – my code was listing a prefix in S3, and the
result it was getting wasn’t up to date. (and “eventually consistent” here
really means “eventually” – apparently sometimes you’ll add / delete an object
from an S3 bucket and it won’t show up in list operations for minutes)


This is how S3 is *supposed* to work, but I hadn’t really thought about that
when I wrote the code.  Arguably I should have read the docs more carefully,
but seeing issues like this in practice helps me understand what “eventually
consistent” systems look like when they fail and remember to write my code with
that in mind next time.


### Other quotes I liked


> I’ve had teams that took on-call very seriously: each issue that paged
> us was reviewed in a weekly meeting, and tasks were assigned to solve


> The lesson for me is that processes are important, and working towards
> continuous improvement is worth it.


and


> Being on call means I can’t pick and choose favorite/comfortable subjects
> avoiding hard/unhappy ones. I’m forced to stretch and learn.


and


> Being able to put aside one’s pride and say “I need help with this
> even though I’m waking someone up to help me.”


and


> It made me much better at figuring out how to break up a complex
> failure condition into smaller pieces that are easier to debug…


### Being responsible for my programs’ operations makes me a better developer


I’ve never really worked in a world where I wrote software and threw it over
the wall to be operated by another team. But I do feel like writing software
and then seeing how it fails in practice has been a good experience! I feel
like it’s a great privilege to be able to write software and see how it
holds up in practice over the course of months/years.


That said – I’ve never been on a particularly arduous on-call rotation
personally, the most I’ve probably ever been paged is like.. 2-3 times per
week, once every 4 weeks. But I feel like I learned a lot from that still!


I’ve probably left out many important things here but I wrote this 2 months ago
and so it’s already being published far later than my usual “write this and
publish it within 4 hours”.
