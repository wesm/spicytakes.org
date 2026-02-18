---
title: "Figuring out how to contribute to open source"
date: 2017-08-06
url: https://jvns.ca/blog/2017/08/06/contributing-to-open-source/
slug: contributing-to-open-source
word_count: 1744
---


Lately at work I’ve been working more with large open source projects (like
Kubernetes and Terraform!)


Sometimes there are bugs in those projects, or features I want to add! I
haven’t contributed to open source projects much in the past (beyond like
“here’s a 2-line README fix”. (which is useful but is a lot easier than fixing
a bug)


Historically my approach to bugs / missing features in open source projects has
been to shrug, say “oh well”, and find a workaround or wait for a fix. But
these days I am trying to be more like I AM A PROGRAMMER I CAN MAKE THIS
HAPPEN. Which is true! I can!!


This post isn’t about “how to find small issues in open source projects to get
started with open source” – instead it’s about “I have a specific change I
want to make to a specific project, what will help me get that done”.


### skills I already have


I sometimes feel kind of intimidated by open source. When I feel intimidated I
find it helpful to remind myself that I’m a professional software developer and
most of the things you need to do to contribute to open source projects are
**already things I do every day at work**.


For example!

- make a clear/well-organized pull request
- write tests
- run tests and use a CI system
- navigate a codebase that is tens of thousands of lines of code
- figure out whether something is a bug or expected behavior
- read the code to figure out how the code is *supposed* to work
even if there isn’t a project maintainer I can ask questions
- use git rebase & resolve merge conflicts
- other regular software stuff


### things that are still hard about open source


Okay, so we have basic software engineering skills covered. What makes open
source contributions harder than my regular job, then?


Here are some things that are harder!

- In open source, I need to send code reviews to total
strangers. At work, I generally send code reviews to the same 10 people or
so, most of whom I’ve worked with for a year or more, and who often already
know exactly what I’m working on.
- At work, people mostly share the same goals as me. But if I have a change
to an open source project that’s useful to my company, the open source
maintainers might not agree that that change is broadly useful enough to
include.
- In open source, if I’m contributing to a new repository I need to learn the
standards and conventions from scratch. At work I basically always contribute
to the same 3-4 repositories which I already know inside and out.
- In open source, the code I’m modifying is probably used in ways I don’t know
about. At work I usually already know (or can look up) every way the code I’m
changing is used.
- In open source, I can’t just DM the project maintainers with questions (or
bug them about how they haven’t reviewed my PR) any time I want.


This list is super useful to me! It takes us from “open source is hard and
scary, how do I do it” from “there are a bunch of specific challenges when
contributing to open source projects that I don’t usually have to deal with,
but that’s fine, I just need to deal with them!”


Here are a few tactics that have helped me when working with open source
projects.


### remember that maintaining an open source project is super hard


One thing I always try to remember is – while contributing to an OSS project
is definitely work, **maintaining** a project is often pretty thankless
and is way more work. So through all of this I think it’s important to be
really respectful of open source maintainers’ time!


They spend a ton of time doing code reviews and making sure the project
continues to work for a huge variety of people and thinking about weird edge
cases and a lot of stuff that any individual person contributing to the project
probably doesn’t have to think about anywhere near as much. And often
maintainers are volunteers – I think it’s useful to be aware of whether a
project’s maintainers are paid to maintain the project, or whether they’re
doing it for free on the side.


### start by making a tiny pull request


I read this great short post [Easy Pull Requests](http://vaibhavsagar.com/blog/2017/07/31/easy-pull-requests/index.html)
recently that recommends making a tiny pull request (like fixing a typo or
something) first when getting started with a new open source project to get a
sense for

1. how quickly people respond to pull requests
2. how friendly the maintainers are
3. what the process for getting something merged is like


I haven’t really done this but I think it makes a lot of sense.


### read way more code than usual


Recently I fixed a bug in the Kubernetes scheduler. I did not know how the
Kubernetes scheduler worked and did not have anyone to ask about how it worked.


So instead I just spent a bunch of hours scrolling through the scheduler code
until I [understood how it worked](https://jvns.ca/blog/2017/07/27/how-does-the-kubernetes-scheduler-work/).
This is maybe sort of obvious (“if you don’t have anybody to ask questions, just read
the code until you figure it out”) but code-reading is a muscle that maybe I don’t
always exercise as much as I could and so this was a good reminder of how far
I can get without asking any questions at all.


### don’t be scared to share a work in progress


If I’m making a PR I’m not sure of the details of how it should work, I’ll
often start a `[WIP]` PR like “here’s a sketch, here are the details of what
I’m trying to accomplish, what do you think?”.


I think this is actually a super good idea in open source too (especially if
I’m new to the project) – I’ve found that as long as I explain the idea
clearly maintainers are happy to give early feedback and help me figure out
what the right direction might be.


### write really detailed PR descriptions


At work I often write pretty short PR descriptions because the people reviewing
my code usually already know more or less what I’m working on.


I’ve been spending way more time on writing clear open source PR descriptions
(like.. 5 minutes instead of 10 seconds?). So far it has gone really well! I
will write several paragraphs about what the PR is trying to accomplish, and so
far everyone seems to totally understand and then give me great code reviews.


### smaller pull requests are better


When trying to fix this scheduler bug I started out by writing a PR (+79 lines,
-25) which made a few different improvements related to the bug. It got a lot of
helpful code reviews but after a couple of days was clearly stuck.


I decided “well, this PR is a little complicated and it’s editing a pretty
sensitive piece of code, I will close it and break it up into 2 smaller PRs!”.
This turned out to be a GREAT IDEA – the new smaller PR got a lot more reviews
a lot more quickly and then got merged. Turns out making your code simpler gets
you more reviewers! :)


Also I’ve been really impressed with the Kubernetes project overall, it seems
well organized so far!


### close the PR if nobody replies


A while back I had a PR where originally I got a lot of super helpful reviews,
but after some back and forth eventually I said “ok, I fixed all the issues you
brought up, what do you think about merging this?” and they just didn’t really
reply.


I eventually said “ok, I’m going to close this in a week if nobody replies”.
They didn’t reply and I decided I didn’t want to spend any more time on it so I
just closed it. I think this was an okay outcome! It was helpful to decide “ok,
this one isn’t working out right now for whatever reason, I’ll close this and
maybe revisit it one day later”. No big deal.


### use Slack / mailing lists?


Throughout all of this so far my approach has been “I won’t ask anyone questions if
I’m confused, I’ll just think really hard and eventually figure out the
answer”. So far this has been pretty effective. But a lot of open source
projects have a mailing list / Slack / gitter / IRC channel for discussion.  I
haven’t really figured this out yet because the social norms are kind of
unclear to me (there are often hundreds or thousands of people in the
Kubernetes Slack channels and I don’t know almost any of them), but it seems
like something I should figure out.


### “open source” is a really big world


There are a lot of open source projects with very very different degrees of

- whether they’re actively maintained at all (one person in their free time? 50
people who work on it full time?)
- how big the codebase is (100 lines? 1000 lines? 100,000 lines?)
- how many people use the project (how many people will be affected if something
breaks?)
- how good is the automated testing?
- basically every axis a software project could exist on


So I think it’s hard to give general guidelines – most of what I’m trying to
do really just boils down to

1. be respectful of maintainers’ time and contribute helpful patches
2. communicate clearly what my goals are


### that’s all for now


I used to want to / think I should contribute to open source in my spare time.
I have mostly decided/realized that this is not going to happen. I spent many
hours working on these two PRs to kubernetes and while I think this was a good
use of work time, I probably would not do that strictly for fun. (I write blog
posts in my spare time, I don’t really code)


But I do think “being able to make improvements to open source projects” is a
super good work skill and it’s something I’m excited about getting better at.
And I think it’s important for companies to contribute back to open source
projects they use, and I’m excited to be a very small part of that.
