---
title: "Fear makes you a worse programmer"
date: 2014-12-21
url: https://jvns.ca/blog/2014/12/21/fear-makes-you-a-worse-programmer/
slug: fear-makes-you-a-worse-programmer
word_count: 897
---


Yesterday morning, I asked on Twitter:


> Does anyone have good writing about fear + programming (and how being
> afraid to make important changes makes you a worse programmer?)


and


> I feel like there’s this really important line between caution (a++
> excellent) and fear (which holds you back from doing necessary work)


A lot of [super interesting discussion ensued](https://twitter.com/b0rk/status/546376386672611329), and I’d
like to talk about some of it.


Before I start, [Ryan Kennedy](https://twitter.com/rckenned) linked me
to this slide deck of a presentation he gave called
[Fear Driven Development](https://speakerdeck.com/ryankennedy/fear-driven-development)
which I absolutely loved, and I think you should look at it. I think my
favorite sentence from that presentation is **“Fear creates local
maximums.”**


I find that when I’m afraid, I become super conservative. WE CANNOT
POSSIBLY MAKE THIS CHANGE WHAT IF IT BREAKS?! And this means worse
software! It’s actually kind of disastrous. If you’re scared of making
changes, you can’t make something dramatically better, or do that big
code cleanup. Maybe you can’t even deploy the code that you already
wrote and tested, because it feels too scary. You just want to stick
what’s sort-of-working, even if it’s not great.


## Better tools & process => less fear


A lot of people brought up tools and processes. (in particular the
fantastic [Kelsey Gilmore-Innis](https://twitter.com/kelseyinnis), who
has new-to-me things to say about better processes for testing code
every time I talk to her)


Kelsey:


> I know you’re talking more psychologically, but this is one of my main
> reasons I believe investing in tests early is important


> […] obsessive monitoring, CI, canary deploys, chatops, dogfooding,
> selfserve infra


So! Here are a few ways tools and processes can make us less afraid:


**Version control** means that you can make changes to your code without
being scared of losing the old version. This one is so basic to me now
– I can’t even imagine how afraid I would be if I were programming
without version control.


So many people mentioned **testing** as a way to build confidence. My
favorite thing I’ve ever read about testing is this book [Working
Effectively with Legacy
Code](http://www.amazon.ca/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052),
where [every chapter
title](http://www.amazon.ca/gp/product/toc/0131177052/ref=dp_toc?ie=UTF8&n=916520)
is something that’s scary or difficult about working with legacy code.
(He defines “legacy code” as “code without tests”, to give you a
flavor). For instance: “I Don’t Understand the Code Well Enough To
Change It.”, “How Do I Know That I’m Not Breaking Anything?”, “I Don’t
Have Much Time and I Have To Change It.”


This tweet from [Uncle Bob Martin](https://twitter.com/unclebobmartin/status/469536509822259200),
explains this idea pretty well:


> Even with good design, w/o tests you will fear change and so the code
> will rot.  With good tests, there’s no fear, so you’ll clean the code.


But testing and version control are not the only tools we have! We can
also build

- QA environments where breaking things is totally allowed and encouraged
- deploys that go out a little bit at a time
- the ability to roll back a deploy easily
- QA teams, whose job it is to exhaustively test software
- tools that will email you if your program throws exceptions


and lots more.


## Fear of retribution (and blameless postmortems)


But tools and processes are absolutely not the only thing. Even if I
have amazing tools and QA systems and the best deploy tools and
well-testing code, I’m **still going to make mistakes sometimes**. And
what happens when I make a mistake is really critical.


Etsy and Google and Stripe (where I work) all have [blameless postmortems](https://codeascraft.com/2012/05/22/blameless-postmortems/).
This means that if you make a change and that change breaks something,
people talk about what happened by focusing on the change and the facts,
not on blaming you. (“what about that change caused a problem?” instead
of “how did Julia break it?”)


I also realized that this goes much further than programming, and
[Marc](https://twitter.com/marcprecipice) linked me to
[this amazing site about restorative justice](https://web.archive.org/web/20150626002728/http://justcultureinstitute.com/), which you should also go read.


So if you blame people for breaking things, they’ll be more scared to
make changes in the future, and you’ll end up with worse programs. Huh.


## Irrational fears


One last thing that that [Fear Driven Development talk](https://speakerdeck.com/ryankennedy/fear-driven-development) talks
about that really resonated with me was – some fears are irrational,
and that they can *infect other people*. If you do a deploy, something
goes wrong, and you figure out the cause and fix the problem and nobody
yells at you, hopefully future deploys should not be scary!


But because we are only human and not Logical Robots, sometimes they
still are, and maybe you’ll feel nervous about doing deploys for a while
until you see that things are really usually fine.


I think there’s a lot more to be said about irrational fears, and I
would be interested to hear more.


This year was the first year that I worked on large software systems
that affect lots of people, and it’s been scary sometimes! Next year
will be the second year, and my plan is for it to be easier =)


(thanks to [Maggie Zhou](https://twitter.com/zmagg) and [Kelsey Gilmore-Innis](https://twitter.com/kelseyinnis) and [Melissa Santos](https://twitter.com/ansate) and many others for all saying
excellent things and making me have new thoughts!)


A couple of more talks / posts about fear that I enjoyed:

- [Fear of programming](http://www.logiccolony.com/2010/10/16/Fear-of-Programming-Notes.html) (via [@booleancz](https://twitter.com/booleancz))
- [Fear Driven Development](http://www.hanselman.com/blog/FearDrivenDevelopmentFDD.aspx) (totally different, by Scott Hanselman)
