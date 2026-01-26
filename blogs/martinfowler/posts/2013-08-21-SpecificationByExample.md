---
title: "Specification By Example"
description: "Given-When-Then is a style of representing tests - or as its   advocates would say - specifying a system's behavior usingSpecificationByExample. It's an   approach developed byDaniel Terhorst-Northand"
date: 2013-08-21T00:00:00
tags: ["testing", "requirements analysis"]
url: https://martinfowler.com/bliki/SpecificationByExample.html
slug: SpecificationByExample
word_count: 872
---


I was attending a workshop at XP/Agile Universe in 2002 when the
phrase 'Specification By Example' struck me as a way to describe one
of roles of testing in [XP](https://martinfowler.com/articles/newMethodology.html#xp).


(These days it's terribly unfashionable to talk about Test Driven
Development (TDD) having anything to do with testing, but like [Jon](http://blogs.codehaus.org/people/tirsen/archives/000582_tdd_is_about_testing.html) I do think that having a comprehensive automated test suite
is more valuable than the term 'side-effect' implies. Rather like if
someone offered me a million dollars to hike up a mountain. I may say
that the main purpose of the hike is the enjoyment of nature, but the
side-effect to my wallet is hardly trivial....)


Specification By Example isn't the way most of us have been
brought up to think of specifications. Specifications are supposed to
be general, to cover all cases. Examples only highlight a few points,
you have to infer the generalizations yourself. This does mean that
Specification By Example can't be the only requirements technique you
use, but it doesn't mean that it can't take a leading role.


So far the dominant idea with rigorous specifications, that is
those that can be clearly judged to be passed or failed, is to use pre
and post conditions. These techniques dominate in formal methods, and
also underpin [Design

by Contract](http://archive.eiffel.com/doc/manuals/technology/contract/). These techniques have their place, but they aren't
ideal. The pre-post conditions can be very easy to write in some
situations, but others can be very tricky. I've tried to use them in a
number enterprise application settings, and I've found that in many
situations it's as hard to write the pre and post conditions as it is
to write the solution. One of the great things about specification by
example is that examples are usually much easier to come up with,
particularly for the non-nerds who we write the software for. ([Timothy Budd](https://www.amazon.com/gp/product/0201824191/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0201824191&linkCode=as2&tag=martinfowlerc-20) pointed out that while you can
show a lot of stack behavior with pre and post conditions, it's very
tricky to write pre and post conditions that show the LIFO
property.)


An important property of TDD tests is that they involve a
double-check. In fact this highlights an amusing little lie of the XP
community. They make a very strong point of saying things Once and
Only Once, but in fact they always say things twice: once in the code
and once in the tests. Kent has pointed out that this double-check
principle is a vital principle, and it's certainly one that humans use
all the time. The value of the double check is very much tied into
using different methods for each side of the double check. Combining
Specification By Example with production code means that you have both
things said quite differently, which increases their ability to find
errors.


The formal specification community have constantly had trouble
verifying that a design satisfies a specification, particularly in
doing this without error prone humans. For Specification By Example,
this is easy. Another case of Specification By Example being less
valuable in theory but more valuable in practice.


One Design by Contract fan pointed out that if you write a
specification in terms of tests, then the supplier could satisfy the
specification by just returning hard-coded responses to the specific
test inputs. My flippant answer to this is that if you are concerned
about this then the issue of tests versus Design by Contract is the
least of your worries. But there is a serious point here. Tests are
always going to be incomplete, so they always have to be backed up
with other mechanisms. Being the twisted mind that I am, I actually
see this as a plus. Since it's clear that Specification By Example
isn't enough, it's clear that you need to do more to ensure that
everything is properly communicated. One of the most dangerous things
about a traditional requirements specification is when people think
that once they've written it they are done communicating.


Specification By Example only works in the context of a working
relationship where both sides are collaborating and not fighting. The
examples trigger abstractions in the design team while keeping the
abstractions grounded. You do need more - things like regular
conversation, techniques like [Domain Driven
Design](https://www.amazon.com/gp/product/0321125215/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0321125215&linkCode=as2&tag=martinfowlerc-20), indeed even doses of Design by Contract. While I've
never had the opportunity to use Design by Contract fully (i.e. with
Eiffel) I regularly think about interfaces in contractual terms.
Specification By Example is a powerful tool, perhaps my most used
tool, but never my only tool.


(For more thinking on Specification By Example, if not by that
name, take a look at [Brian Marick's](http://www.exampler.com/blog/)
writings. Somewhere on his site there probably is one super page that
sums up his view on it. Of course finding it is less valuable than
reading all the stuff there while you're trying)


## Some Later Comments


A couple of years after I first wrote this, there was a [post by Cedric
  Beust](http://beust.com/weblog/archives/000392.html) that was critical of agile methods that
  caused a minor blog spat. There were rebuttals by [Jeff Langr](http://langrsoft.com/2006/06/12/open-note-to-google/) and [Bob
  Martin](http://butunclebob.com/ArticleS.UncleBob.AgilePeopleStillDontGetIt), and I sent this post through the feed again.  Jeff Langr
  later added a [nice
  example](http://langrsoft.com/2006/06/06/are-tests-specs/) using using tests as specification by example for Java's
  Math.pow function.


reposted on 17 Nov 2011
