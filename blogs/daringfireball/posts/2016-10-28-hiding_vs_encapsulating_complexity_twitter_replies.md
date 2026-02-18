---
title: "On Hiding vs. Encapsulating Complexity, in the Context of Twitter’s Experimental Reply Interface"
date: 2016-10-28
url: https://daringfireball.net/2016/10/hiding_vs_encapsulating_complexity_twitter_replies
slug: hiding_vs_encapsulating_complexity_twitter_replies
word_count: 547
---


Matthew Panzarino hits today’s [DF](http://daringfireball.net/linked/2016/10/28/panzarino-touch-bar) [trifecta](http://daringfireball.net/linked/2016/10/28/panzarino-t1) with [this piece railing against a confusing new reply interface Twitter is testing with some users](https://techcrunch.com/2016/10/28/complaining-about-twitter-on-twitter/):


> The solution for this mess should probably start with removing the
> user names from the character count but leaving the actual user
> names themselves. Much in the way that a link (eventually, still
> not implemented, lol) or photo is added and appears in the tweet
> but does not count towards the character count.
> The argument against this is that ‘normals are confused by ‘@
> names’. I disagree. I think that this may have been an issue early
> on but enormous swaths of people have been familiarized with
> usernames by the huge audience for tweets on mainstream media, TV
> and the web, as well as in pop culture like Jimmy Kimmel’s Mean
> Tweets segments and on and on.


Twitter reply chains *are* confusing to some/many users. Is the problem with Twitter, or with the users?


The fundamental problem with most designers of complex systems intended for mass market use is that they decide to hide complexity. They won’t admit it — they’ll deny it even — but it’s because they’re disdainful of their users. They think their users are stupid, so they need to present them with a design for stupid people. If they weren’t stupid they wouldn’t be confused, right?


That’s fundamentally wrong. If people are confused with a design, the problem is with the design, not with the users. It’s Twitter’s designers who aren’t smart enough, not Twitter’s users, because if Twitter’s designers were smart enough, they’d come up with a design that wasn’t confusing by *encapsulating* rather than merely *hiding* complexity. It’s the difference between actually cleaning up a mess versus just sweeping the mess under a rug. This new Twitter reply interface is a “sweep it under the rug” design.


A good “simple” design will help users to understand what is actually going on, how a thing actually works. A bad “simple” design will leave users just as confused as ever with even less chance of figuring it out, because what they need to see to understand it is hidden.1


---

1. Apple has always been very good at this — designing software and hardware where complexity is encapsulated rather than hidden. The genius of the original Mac wasn’t that it was suitable for dummies but that it was the first system that wasn’t confusing. Smart people flocked to the Mac.
But an example where Apple got this wrong is the way Mac OS X (to use the old name) defaults to hiding file name extensions. [This is a pet topic of mine from the earliest days of Daring Fireball](http://daringfireball.net/2003/04/accommodating). If you’re going to require file name extensions in your system, then show them. If you don’t want to show them (and you shouldn’t, because they’re ugly, inelegant, and easily broken), then design a system where they’re never needed. The classic Mac OS got this right. iOS got this right. Mac OS X got this wrong, and it’s still a bit of a mess on today’s MacOS. ↩︎



| **Previous:** | [On iMessage’s Stickiness](https://daringfireball.net/2016/10/imessage_stickiness) |
| **Next:** | [The New Touch-Bar-Equipped MacBook Pros and the State of the Mac](https://daringfireball.net/2016/11/new_touch_bar_equipped_macbook_pros) |


PreviousNext