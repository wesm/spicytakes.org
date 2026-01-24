---
title: "The Gamification"
date: 2011-10-12
url: https://blog.codinghorror.com/the-gamification/
slug: the-gamification
word_count: 1383
---

When Joel Spolsky and I set out to design the [Stack Exchange](http://stackexchange.com/) Q&A engine in 2008 – then known as Stack Overflow – we borrowed liberally and unapologetically from any online system that we felt worked. Some of our notable influences included:

- Reddit and Digg voting
- Xbox 360 achievements
- Wikipedia editing
- eBay karma
- Blogs and blog comments
- Classic web bulletin boards


All these elements were folded up into the Stack Exchange Q&A engine, so that we might help people create useful artifacts on the internet while learning with and among their peers. You know the old adage that *good artists copy, great artists steal?* That quote is [impossible to source](https://web.archive.org/web/20111015181756/http://www.businessofdesignonline.com/picasso-good-artists-copy/), but it means we were *repurposing* these elements we liked.


> So, what do Picasso and T.S. Eliot mean? They say, in the briefest of terms: **take old work to a new place**. Steal the Google site, strip down what works (fast load, nonexistent graphics, small quirky changes that delight) and use the parts on your own site. Look at the curve of a Coke Bottle and create a beautiful landscape painting with it. Take the hairline pinstriping on the side of somebody’s car, reimagine it on your print job. Find inspiration in the world you live in, where nothing is truly new so that everything has the potential to be innovative.


Unfortunately, the elements we liked were often buried in mounds of stuff that we... sort of hated. So extracting just the good parts and removing the rest was part of the mission. If you’re lucky enough to have a convenient [villain to position yourself against](https://blog.codinghorror.com/whos-your-arch-enemy/), that might be all you need.


Traditional web bulletin board systems have a design that was apparently permanently frozen in place circa 2001 along with Windows XP. Consider this typical forum thread.


![](https://blog.codinghorror.com/content/images/2025/04/image-551.png)


Here is the *actual information* from that forum thread.


![](https://blog.codinghorror.com/content/images/2025/04/image-550.png)


Based on the original size of those screenshots, only **18 percent** of that forum thread page is content. The other 82 percent is lost to signatures, avatars, UI doohickeys, and other web forum frippery that has somehow become accepted as “the way things are done.” I regularly participate in several expert niche bulletin boards of various types today, and they’re all built the same way. Nobody complains.


*But they should.*


This is the status quo that we’re up against. Yes, we fixed it for programmers with Stack Overflow, but why stop there? We want to liberate all the brilliant experts **stuck in these horrible Soviet-era concrete block housing forums** all over the web. We’d like to introduce them to the focused, no-nonsense [Stack Exchange Way](https://stackexchange.com/sites), a beautiful silo of pure Q&A signal without all the associated web forum gunk.


There’s only one teeny-tiny obstacle in our way. As a great programmer I worked with once said:


> It’s the damn users. They’ve ruined every program I’ve ever created.


Every web forum is the way it is *because users wanted it that way*. Yes, the design of the forum software certainly influences behavior, but the classic 2001-era web forum paradigm assumed that what users wanted made sense for the rest of the larger internet. As it turns out, groups are [their own worst enemy](https://blog.codinghorror.com/a-group-is-its-own-worst-enemy/). What groups want, and what the rest of the world needs, are often two very different things. Random discussion is fine for entertainment, but it’s not particularly useful, nor does it tend to generate the kind of artifacts that will be relevant a few years from now like Wikipedia does. So then the problem becomes **how do you encourage groups to do what’s best for the *world*** rather than their own specific, selfish needs?


When I looked at this problem, I felt I knew the answer. But there wasn’t a word for it in 2008. Now there is: [Gamification](https://en.wikipedia.org/wiki/Gamification).


> **Gamification is the use of game design techniques and mechanics to solve problems and engage audiences.** [. . .] Gamification works by… taking advantage of humans’ psychological predisposition to engage in gaming. The technique can encourage people to perform chores that they ordinarily consider boring, such as completing surveys, shopping, or reading web sites.


I had no idea this Wikipedia article even existed until a few months ago, but we are featured prominently in it. It is true that all our stolen ideas about reputation systems, achievements, identity, and vote scoring are in place specifically to encourage the adoption of the brave new no-nonsense, all-signal Stack Exchange Q&A model. Without those incentive systems, when left to their own devices, what you get is… well, every forum ever created. Broken by design.


Yes, [we have ulterior motives](https://blog.codinghorror.com/how-to-write-without-writing/), but let me explain why I think gaming elements are not tacked on to the Stack Exchange Q&A engine, but a natural and essential element of the design from day one.


## Learning is (supposed to be) fun


I’ve had this concept in my head way before the web emerged, long before anyone coined the term “Gamification” in 2010. In fact, I’d trace my inspiration for this all the way back to [1983](https://blog.codinghorror.com/our-programs-are-fun-to-use/).


![](https://blog.codinghorror.com/content/images/2025/09/beagle-bros-statement-of-software-quality.png)


For programmers, everything we know is pretty much guaranteed to be obsolete in 10 years if we’re lucky, and 5 years if we aren’t. It’s changing all the time. The field of programming is almost by definition [one of constant learning](https://blog.codinghorror.com/the-years-of-experience-myth/). Programming [is supposed to be fun](https://blog.codinghorror.com/remember-this-stuff-is-supposed-to-be-fun/) – and it is, if you’re doing it right. Nobody taught me that better than the Beagle Bros on my Apple II. Why can’t learning in every *other* subject matter be just as enjoyable?


## Games are learning aids


There’s a long, rich history of [programmers as gamers](https://blog.codinghorror.com/game-player-game-programmer/). Oftentimes, the whole reason we became programmers in the first place is because we wanted to move beyond being a mere player and *change* the game, control it, modify its parameters, maybe even create our own games.


![](https://blog.codinghorror.com/content/images/2025/04/image-548.png)


We used games to learn how to program. To a programmer, a game is a perfectly natural [introduction to real programming problems](http://www.amazon.com/Computer-gamesmanship-complete-structuring-intelligent/dp/0671495321). I’d posit that *any* field can use games as an introduction to the subject matter – and as a reinforcement to learning.


## Games help people work toward a goal


It’s something of a revelation to me that solid game design can defeat the [Greater Internet F**kwad Theory](http://www.penny-arcade.com/comic/2004/3/19/). Two great examples of this are Counter-Strike and Team Fortress. Both games are more than ten years old, but they’re still actively being played right now, by tens of thousands of people, all anonymous… and playing as cohesive teams!


The game’s objectives and rules are all cleverly constructed to make working *together* the most effective way to win. None of these players know each other; the design of the game forces players to work together, whether they want to or not. It is quite literally impossible to win as a single lone wolf.


![](https://blog.codinghorror.com/content/images/2025/04/image-547.png)


I haven’t ever quite come out and said it this way, but … I played a lot of Counter-Strike from 1998 to 2001, and **Stack Overflow is in many ways my personal Counter-Strike**. It is a programmer in Brazil learning alongside a programmer in New Jersey. Not because they’re friends – but because they both love programming. The *design* of Stack Overflow makes helping your fellow programmers the most effective way to “win” and advance the craft of software development together.


And I say we all win when that happens, no matter which profession we’re talking about.


I feel a little responsible for “Gamification,” since we’re often cited as an example (even, much to my chagrin, on Wikipedia). I wanted to clear up exactly why we made those choices, and specifically that **all the gaming elements are there in service of a higher purpose**. I play the Stack Exchange game happily alongside everyone else, collecting reputation and badges and rank and upvotes, and I am proud to do so, because I believe it ultimately helps me become more knowledgeable and a better communicator while also improving the very fabric of the web for everyone. I hope you feel the same way.


(If you’d like to learn more about the current state of Gamification, I highly recommend [Sebastian Deterding’s page](https://codingconduct.cc/), and specifically his [Meaningful Play: Getting Gamification Right](https://www.slideshare.net/slideshow/meaningful-play-getting-gamification-right/6763616) presentation.)

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
