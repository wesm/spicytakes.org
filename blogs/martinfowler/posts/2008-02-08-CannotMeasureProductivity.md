---
title: "Cannot Measure Productivity"
description: "One of the commonly accepted beliefs in the software world is 	that talented programmers are more productive. Since weCannotMeasureProductivitythis is a belief that cannot be 	proven, but it seems rea"
date: 2008-02-08T00:00:00
tags: ["productivity", "metrics", "project planning", "estimation"]
url: https://martinfowler.com/bliki/CannotMeasureProductivity.html
slug: CannotMeasureProductivity
word_count: 1180
---


We see so much emotional discussion about software process,
design practices and the like. Many of these arguments are impossible
to resolve because the software industry lacks the ability to measure
some of the basic elements of the effectiveness of software
development. In particular we have no way of reasonably measuring
productivity.


Productivity, of course, is something you determine by looking at
the input of an activity and its output. So to measure software
productivity you have to measure the output of software development -
the reason we can't measure productivity is because we can't measure
output.


This doesn't mean people don't try. One of my biggest irritations
are studies of productivity based on lines of code. For a start
there's all the stuff about differences between languages, different
counting styles, and differences due to formatting conventions. But
even if you use a consistent counting standard on programs in the same
language, all auto-formatted to a single style - lines of code still
doesn't measure output properly.


Any good developer knows that they can code the same stuff with
huge variations in lines of code, furthermore code that's well
designed and factored will be shorter because it eliminates the
duplication. Copy and paste programming leads to high LOC counts and
poor design because it breeds duplication. You can prove this to
yourself if you go at a program with a refactoring tool that supports
[Inline
Method](http://www.refactoring.com/catalog/inlineMethod.html). Just using that on common routines should allow you to
easy double the LOC count.


You would think that lines of code are dead, but it seems that
every month I see productivity studies based on lines of code - even
in such respected journals as IEEE Software that should know
better.


Now this doesn't mean that LOC is a completely useless measure,
it's pretty good at suggesting the size of a system. I can be pretty
confident that a 100 KLOC system is bigger than a 10KLOC system. But
if I've written the 100KLOC system in a year, and Joe writes the same
system in 10KLOC during the same time, that doesn't make me more
productive. Indeed I would conclude that our productivities are about
the same but my system is much more poorly designed.


Another approach that's often talked about for measuring output
is Function Points. I have a little more sympathy for them, but am
still unconvinced. This hasn't been helped by stories I've heard of
that talk about a single system getting counts that varied by a factor
of three from different function point counters using the same
system.


Even if we did find an accurate way for function points to
determine functionality, I still think we are missing the point of
productivity. I might say that measuring functionality is a way to
look at the direct output of software development, but true output is
something else. Assuming an accurate FP counting system, if I spend a
year delivering a 100FP system and Joe spends the same year delivering
a 50FP system can we assume that I'm more productive? I would say not.
It may be that of my 100FP only 30 is actually functionality that's
useful to my customer, but Joe's is all useful. I would thus argue
that while my direct productivity is higher, Joe's true productivity
is higher.


Jeff Grigg pointed out to me that there's internal factors that
		 affect delivering function points. âMy 100 function points
		are remarkably similar functions, and it took me a year to do them
		because I failed to properly leverage reuse. Joe's 50 functions
		are (bad news for him) all remarkably different. Almost no reuse
		is possible. But in spite of having to implement 50 remarkably
		different function points, for which almost no reuse leverage is
		possible, Joe is an amazing guy, so he did it all in only a
		year.â


But all of this ignores the point that even useful functionality
		isn't the true measure. As I get better I produce 30 useful FP of
		functionality, and Joe only does 15. But someone figures out that
		Joe's 15 leads to $10 million extra profit for our customer and my
		work only leads to $5 million. I would again argue that Joe's true
		productivity is higher because he has delivered more business
		value - and I assert that any true measure of software development
		productivity must be based on delivered business value.


This thinking also feeds into success rates. Common statements about
software success are bogus because people don't understand
[WhatIsFailure](https://martinfowler.com/bliki/WhatIsFailure.html). I might argue that a successful project is
one that delivers more business value than the cost of the project. So
if Joe and I run five projects each, and I succeed on four and Joe on
one - do I finally do a better job than Joe? Not necessarily. If my
four successes yield $1 million profit each, but Joe's one success
yields $10 million more than the cost of all his projects combined -
then he's the one who should get the promotion.


Some people say âif you can't measure it, you can't manage itâ.
That's a cop out. Businesses manage things they can't really measure
the value of all the time. How do you measure the productivity of a
company's lawyers, its marketing department, an educational
institution? You can't - but you still need to manage them (see [Robert Austin](https://www.amazon.com/gp/product/0932633366/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0932633366&linkCode=as2&tag=martinfowlerc-20) for more).


If team productivity is hard to figure out, it's even harder to
measure the contribution of individuals on that team. You can get a
rough sense of a team's output by looking at how many features they
deliver per iteration. It's a crude sense, but you can get a sense of
whether a team's speeding up, or a rough sense if one team is more
productive than another. But individual contributions are much harder
to assess. While some people may be responsible for implementing
features, others may play a supporting role - helping others to
implement their features. Their contribution is that they are raising
the whole team's productivity - but it's very hard to get a sense of
their individual output unless you are a developer on that team.


If all this isn't complicated enough the Economist (sep
		13-19, 2003) had an article
on productivity trends. It seems that economists are now seeing
productivity increases in business due to the computer investments in
the nineties. The point is that the improvements lag the investments:
âInvesting in computers does not automatically boost productivity
growth; firms need to reorganize their business practices as wellâ.
The same lag  occurred with the invention of electricity.


So not just is business value hard to measure, there's a time
lag too. So maybe you can't measure the productivity of a team until a
few years after a release of the software they were building.


I can see why measuring productivity is so seductive. If we
	could do it we could assess software much more easily and
	objectively than we can now. But false measures only make things
	worse. This is somewhere I think we have to admit to our ignorance.
