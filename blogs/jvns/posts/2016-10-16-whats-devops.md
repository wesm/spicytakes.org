---
title: "What's devops?"
date: 2016-10-16
url: https://jvns.ca/blog/2016/10/16/whats-devops/
slug: whats-devops
word_count: 1187
---


I started reading “[Effective DevOps](https://www.amazon.com/Effective-DevOps-Building-Collaboration-Affinity/dp/1491926309)” by [Jennifer Davis](https://twitter.com/sigje) and
[Ryn Daniels](https://twitter.com/beerops) yesterday.


I’m still only part of the way through, but I realized while reading it
that I had no idea what “devops” even meant. I had some vague idea that
it meant “running programs, administrating servers, using chef and
puppet, I don’t know”.


I think the term “devops” is kind of contentious and I don’t really care
to get into discussions about what words do or do not mean. BUT. What is
described as “devops” and “the devops movement” in Effective DevOps is
an extremely positive thing that I am excited about! So let’s talk about
what this very positive thing is, and while we talk about it we will
call it devops.


### what isn’t devops?


One of the first things they clear up is what they *don’t* mean by
devops.


**Not a job title, not an organization**


Of course devops **is** a job title that people use – someone emailed
me just today asking if I was interested as a job as a “devops
engineer”. And that does mean something, but it’s not what we’re talking
about right now.


I enjoyed reading [this article about devops at Etsy](http://www.networkworld.com/article/2886672/software/how-etsy-makes-devops-work.html).
One of the really key things about this article is – there is no devops
organization at Etsy. It’s about how developers and operations people
work productively together! Also, it was a slow incremental migration
towards different practices. They did not wake up one day and become
devops. I think this is the [first talk that used the term ‘devops’](https://youtu.be/LdOe18KhtT4)?


It’s also not about “everyone is a software developer” – one of the authors of
this book, Ryn Daniels, is a [senior operations engineer at Etsy](https://beero.ps/2015/09/26/on-becoming-a-senior-engineer/).
I don’t know any of the details of their job, but my impression is that they have a
lot of expertise in operations. It’s not like “make operations so
easy that nobody has to be an expert at it”. Of course you need people who
know a ton about operations! Probably those people write software as
part of their job?


**not just automation**


There have a been a bunch of super positive changes around reducing
automation when administering systems. puppet/chef! soon, terraform! AWS
autoscaling groups! But that is not devops. devops is about how people
work together.


### a definition, sort of


I looked up devops on wikipedia and got this:


> In traditional functionally separated organizations there is rarely
> cross-departmental integration of these functions with IT operations.
> devops promotes a set of processes and methods for thinking about
> communication and collaboration between development, QA, and IT
> operations.


Okay, this is interesting! devops is about “communication and
collaboration”. That is really different from “chef and puppet and
continuous integration and stuff” – Puppet is software, communication
is about how humans work together.


Near the beginning of the book, Davis and Daniels describe some of their
respective experiences being the only person on-call and in charge of
keeping some software running. They then, over the course of the book,
talk through a bunch of case studies of organizations moving towards
more sustainable practice.


This really helped me understand where the book was coming from! I have
never worked at an organization with an “operations team” where
development and operations were separated into different organizations.


So devops is about people who with different strengths effectively
collaborating to build awesome software that runs reliably. That is a
thing I like!


### ideas & practices that are part of devops

- you should integrate development and operations together (or: you
should stop breaking dev and ops apart (thanks tef))
- operations experts should have a hand in leading **systems design and
architecture**, not just be handed finished systems to run
- when things go wrong, run blameless postmortems
- **continuous integration**. I also learned from this book what
continuous integration was! It is when you merge your changes into a
mainline branch very frequently instead of going off and building a
feature for weeks!
- configuration management and automation tools like chef/puppet (“no
snowflake servers”)


There are a lot more things, those are just 5.


Most of these things are about processes and people, not about technology.


Another pretty important thing here seems to be the
[devopsdays](https://www.devopsdays.org/) conferences – it’s really
cool that there’s a series of local conferences that talk about how to
operate reliable software and bring people with different kinds of
expertise to talk. I haven’t been to any of them yet, but bringing
people from different companies together to talk seems to be an
important part of the “devops movement”.


### assumptions are important


One of my favorite things about this book is that it makes a lot of my
assumptions explicit! Etsy influenced a lot of devops ideas, and where I
work now is influenced by Etsy, so a lot of this stuff is implicitly
familiar to me. But I hadn’t thought of them as choices!


When I learned what “continuous integration” was (merging your changes
into master after working on them for 1-2 days instead of waiting weeks)
I was like “uh, wait, what else would you do?”. A lot of the stuff in
this book was like that – I hadn’t realized that this was a choice my
organization was making, I thought that was just how things were!


But of course any organizational choice (like continuous integration,
blameless postmortems, having a separate operations team) **is** a
choice, and it’s useful to understand why you’re making it. Because
maybe there are even more improvements you can make over time!


### what’s the difference between devops and SRE?


This [transcript of a panel discussion on devops vs SRE is good](http://blog.catchpoint.com/2016/09/01/oreilly-media-devops-vs-sre/).


### why devops is exciting (& evolution)


I think I didn’t realize it was exciting because I hadn’t really
internalized that you could totally separate development and
operations. Right now the team I work on has maybe more operational
responsibilities than some other teams, but they’ve never been separate.


But thinking of this as a **choice** where you recognize how important
operational expertise is, train developers to be better at operations,
make sure that operational concerns get seen at early stages of the
development process – that is super exciting to me! And this book
“effective devops” has a lot of ideas that I use already all the time,
but it also has ideas that I haven’t thought of before!


And it makes me want to make my organization even better at it than it
already is, because even if we ostensibly practice “devops” and do
continuous integration and use jenkins and deploy 100 times a day or
whatever, that doesn’t actually mean that we’re the best and awesome and
that we can stop. That is never true! There is always more work to do to
make a more awesome organization.


And devops seems to be less about a “manifesto” (like the extreme
programming manifesto) and more of a large and fuzzy set of practices
that we’re all learning together as an industry over time. That we can
constantly improve! And that is okay.
