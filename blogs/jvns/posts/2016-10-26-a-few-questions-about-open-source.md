---
title: "A few questions about open source"
date: 2016-10-26
url: https://jvns.ca/blog/2016/10/26/a-few-questions-about-open-source/
slug: a-few-questions-about-open-source
word_count: 1254
---


I’ve been thinking a bit about where open source software comes from and
how it works and when and how you should use it. I’m thinking about this
in the context of working for a tech company, not a volunteer
contributor. (I do not contribute to open source in my spare time, I
write this blog instead.)


some facts:

- my company (and most tech companies) depend very heavily on open
source software (see [Roads and Bridges: the unseen labor behind our digital infrastructure [pdf]](https://fordfoundcontent.blob.core.windows.net/media/2976/roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure.pdf)) for a great overview
- a lot of open source software (even the important software) is
maintained by a very small number of people
- some companies spend a large amount of money developing open source
software (for instance people are paid to work on kubernetes)
- some open source software is really high quality and some isn’t
- also a lot of open source software is really really valuable (for example:
postgresql, sqlite, openssl, nginx, hadoop just to name a few)


and some questions:


## how can you tell when you should use an open source tool vs writing it yourself?


Sometimes this is really obvious: I should almost certainly not write a
web server. Instead I should almost always use nginx or something!


But sometimes the task I’m trying to do is kind of weird and not that
common, and the open source tools available are.. kind of bad?


some things that might help here:

- how many hours have been spent on the open source tool? is it a
weekend side project? have there been 2 person-years spent developing
it?
- does it have the same architecture as the thing I think I need, or has
it made architecture choices that I think are bad?
- is it actually solving the problem that I have or does it do a bunch
of extra stuff that isn’t my concern?


using nginx instead of writing a web server myself probably saves me
like 2 years of developer time or something. But using open source I
think doesn’t always save you time! Sometimes it takes extra time and
it’s not better.


## why do companies pay to create open source software?


Here are some reasons I know right now! This reads as a bit cynical and
i really do believe in the RAINBOWS PEOPLE WORKING TOGETHER TOWARDS THE IMPROVEMENT OF HUMANKIND version of open source but I am trying to understand some of
the more practical reasons right now.


Paying people to develop open source software is super expensive
(because paying people is expensive) so I want to work out some of the
reasons why it happens. Mostly I want to work this out because a good
chunk of the software I use someone *was* paid to write so I want to
understand why.


(also I would like to understand how it works when nobody is paid to
work on the software, but that is a whole other question)

- because you think investing in community-maintained open source software will be valuable for the business in the long term. there’s an
excellent [post by jessie frazelle](https://blog.jessfraz.com/post/blurred-lines/) that talks about the relationship between individual passion for open source and a business investment
- because you need software (like the Linux kernel) to have new features and a bunch of
companies have enough of the same needs from that software that it’s
worth it for a bunch of people to get paid to build software that
everyone gets to use
- you have to write the software anyway so you might as well open source
it while you’re at it so that other people get to use it
- social pressure: a lot of people won’t use software that *isn’t* open
source so maybe if you’re releasing software for your customers to use
you have to release your software as open source to get anyone to use
it at all.
- developers often like writing open source software so maybe it helps
with keeping people happy
- [@mcpherrinm](https://twitter.com/mcpherrinm): “I will eventually quit
my job and want to keep using tools I wrote for this one. Open Source
lets me do that”


I think I’m missing a bunch of important reasons here.


## when you use open source, who wrote the software? what are their priorities?


Right now I’m using some software called rkt at work. When I use rkt,
it’s incredibly useful to me to know who runs the project (CoreOS), what
their company priorities are right now (getting OCI working), how much
they’re likely to make improvements to the appc standard (not very) and
how willing they are to accept contributions (pretty likely!).


I kinda feel like working on open source is like being
part of a really big company and you have to know what the other people
who are paying to develop the software care about and what kind of
contributions they’re likely to accept / be enthusiastic about.


## how do you decide when to build software as open source?


If you build something and make it open source, does the discipline of
making it general help you build better software? Or does having to
support other use cases get in the way of building something that will
work well for you? Probably it depends! But what does it depend on
exactly?


## is it harmful to open source and promote software that doesn’t actually work well?


Someone told me a story the other day of an open source thing they used
for a while. Eventually they figured out after a few months of pain that
this software actually just doesn’t really work that well and nobody
really uses it. Oops.


On one hand this seems kind of irresponsible on the hand of the project
maintainers. On the other hand I’ve definitely released software where I
have *no idea* if anybody other than me has ever used it successfully,
and I have no real intentions of finding out. Is that bad? I feel like
my current default assumption about software I find in the wild is that
it is unmaintained and possibly nobody has ever used it except the
people who wrote it. Ideally people would write on the tin “we have no
idea if anyone other than us has ever used this software successfully” though.


## how do you even evaluate software?


Evaluating unknown software to decide if you should use it is really
hard! I think the only thing that really makes it worth it is that, if
you genuinely cannot use known software to do the thing you want to do,
you need to either

1. evaluate some unknown software, or
2. write a thing yourself from scratch


So maybe the saving grace of unknown software is that it is maybe
sometimes faster than writing it all yourself? And spending the time to
understand how a new thing works can save you a lot of time. Evaluating
software is hard and I still don’t really know how to do this well.


A lot of the discussions I see on the internet comparing software are
not great.


## open source is very important and pretty confusing


Anyway hopefully some of these questions are interesting. I don’t
actually know a lot about how open source really works and I don’t work
on open source today – i think there are a lot of subtleties and
feelings and human things here around “community” and “passion” and
“making money”.


thanks to Tavish for encouraging me to post this
