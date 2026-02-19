---
title: "Accommodating"
date: 2003-04-24
url: https://daringfireball.net/2003/04/accommodating
slug: accommodating
word_count: 1395
---


Something rubbed me the wrong way about Dan Gillmor’s recent article in the San Jose Mercury News, “[NeXT still stands out in its Mac incarnation](https://web.archive.org/web/20030618065842/http://www.siliconvalley.com/mld/siliconvalley/5676137.htm)”, but it took me a few days to put my finger on it. If you haven’t done so already, read his article before continuing with this.


Gillmor is a good writer, and, for a guy whose beat is the entire computer industry, he does a great job covering Apple fairly. And the subject of this article is both true and interesting: there is some great software for Mac OS X coming from old NeXT developers.


What’s wrong with his article is that despite the fact that neither the words “Cocoa” nor “Carbon” appear in the article, there are several inferences that the parts of Mac OS X that come from NeXT are good, and the parts from the old Mac OS are bad.


Let’s start with this bit:


> In bringing the NeXT technology into the heart of the modern Mac environment, Apple has maintained the guts of the old NeXT architecture while simultaneously extending and enhancing it. Some in the former NeXT community worried that Apple, trying to accommodate its legacy customers, would create a Frankenstein, but that hasn’t happened.


Now that’s rich, the idea that the NeXT community was worried about Mac OS technologies polluting *their* water. I forget: which group brought DOS-style filename extensions to the party? And which group brought in a 30-year-old Unix file permissions model that resulted in thousands of Mac OS X users being disallowed from emptying their Trash?


And note the use of the term “legacy customers”, implying the old Mac OS was some sort of antediluvian backwater. When Microsoft released Windows 95, DOS became a legacy system. Users switching from DOS to Windows 95 would have to adopt totally new application software (or else run DOS apps in Windows terminal windows). Users switching from Mac OS 9 to Mac OS X don’t need to switch to new applications — they just need to upgrade to the latest versions of their applications (or use the old versions in Classic). The leading office suite on Mac OS X is still MS Office, the leading graphics program is still Photoshop, and the leading text editor is still BBEdit. These are not legacy apps; they’re just Mac apps.


It’s absurd to claim that Apple could have screwed things up by “accommodating” its existing Mac OS customers. Without those customers, who did they have? The massive NeXT market?


Next comes this quote from long-time NeXT developer [Andrew Stone](http://www.stone.com/):


> “The Mac is now the NeXT with a lot of cool new technology,” says Andrew Stone of Stone Design ([www.stone.com](http://www.stone.com/)) in Albuquerque, an early NeXT and OS X developer.


This just isn’t true. It might be what some NeXT developers (including some now at Apple) *wanted* Mac OS X to be, and it’s also what many long-time Mac users (including me) *worried* that Mac OS X would be. But that’s not what Mac OS X is. Mac OS X is, amazingly and successfully, something much more. It is NeXTStep *and* it is the Mac OS. It’s wrong to claim that it’s simply the NeXT system with a Mac OS compatibility layer on top.


Now, some sort of “minor update to NeXTStep with a new paint job and legacy Mac compatibility layer” *might* have been exactly what the folks from NeXT had in mind when they first joined Apple and began the Rhapsody project, which would certainly explain the overly-optimistic schedule they first came up with. Since the Jobs/Tevanian regime began, Apple has done a remarkable job shipping software on schedule. Mac OS 8.5, 8.6 and 9 all came out more or less right on schedule. Mac OS X 10.0 was years late, but punctuality has been restored with subsequent major updates to OS X. I think the biggest reason Mac OS X 10.0 was so late is that it ended up being so much more than just a new version of NeXTStep with a Mac legacy layer.


There’s no dispute that large and important parts of Mac OS X are based on NeXTStep. But there should also be no dispute that large and important parts are based on classic Mac OS technologies, like QuickTime and Apple events. This is to the benefit of everyone, NeXT and Mac users (and developers) alike.


Then this:


> Stone sees the modern Mac architecture and programming toolkits enabling a “samurai” model of software development. That is, the tools and platform make it possible for a significant number of individual programmers or small teams, not just corporate behemoths, to create seriously innovative applications.


This implies that small developer teams could not create “seriously innovative applications” for the classic Mac OS. Which is ludicrously false. Yes, Microsoft, Adobe, and Macromedia surely qualify as “corporate behemoths”.
But what about companies like [Bare Bones](http://www.barebones.com/), [Casady and Greene](http://www.casadyg.com), [Nisus](http://www.nisus.com/), and [Real Software](http://www.realsoftware.com/)? Or even *smaller* shops, like Peter N. Lewis’s [Interarchy](http://interarchy.com/) (nee Stairways Software) or James Thomson’s [TLA Systems](http://www.tla-systems.co.uk/) (makers of the amazing DragThing)?


It’s silly even to continue the list. Yes, the very biggest fish in the Mac pond are applications from large corporations. But most Mac software has always been produced by small developers. This isn’t new to Mac OS X.


I don’t mean to pick on Andrew Stone, because I know how easy it is for a quote to be taken out of context, and Gillmor’s article contains very few actual quoted words from Stone. But this sentiment — that former NeXT developers have a tremendous advantage over long-time Mac developers — is misguided, and is actually somewhat harmful, as it’s largely responsible for commonly-held belief amongst the masses that “Cocoa is better than Carbon”, which is nonsense. Cocoa and Carbon are *developer* technologies. Mac users should be no more concerned whether an app is Cocoa or Carbon than they would have been 10 years ago whether an app was written in C or Pascal. You really don’t want to know how your sausage is made; you just want it to taste good.


Ever since the Apple/NeXT merger, there’s been a decided amount of “us against them” coming from NeXT developers moving over. I’ve never understood why this is. All Mac OS X developers, regardless from which side of the family, share much in common. For one thing, a devotion to making quality software. For another, a commitment to the Mac market — NeXT developers especially, since Cocoa applications are more tied to Mac OS X than are Carbon applications written in C++.


## You Better You Better You Bet


Grab a few random Mac users and ask them which would be faster for any given task — a Carbon app or a Cocoa one — and the answer will likely be, “Cocoa.” Ask them why, and they’ll probably respond, “That’s what everyone says.”


Let’s take the Finder. The battle cry regarding the glacially slow Finder in OS X 10.0 was “Rewrite it in Cocoa!”, as though that alone would have solve all its performance problems. The fact is, good programs are fast, and poor programs are slow, regardless if they’re Cocoa or Carbon. As [Unsanity’s Slava Karpenko pointed out last week](http://www.unsanity.org/archives/000171.php), out of Apple’s entire iLife suite, the only app that doesn’t slow down dramatically with large amounts of data is iTunes — which is Carbon, not Cocoa.
(See also: Karpenko’s take on [Cocoa vs. Carbon](http://www.unsanity.org/archives/000024.php) from October, 2002.)
iTunes’s “secret” is that it’s engineered by a group of crackerjack Mac programmers, including the illustrious Jeffrey Robbin, a long-time Mac programmer whose previous smash hit was [Casady and Greene’s Conflict Catcher](http://www.casadyg.com/products/conflictcatcher/default.html). (Recall that iTunes began life as Casady and Greene’s SoundJam.)


Note that I’m not making the opposite argument — that Carbon is “fast” and Cocoa is “slow”. What I’m saying is that any such broad generalization is going to be wrong. Even with the best application framework in the world, good apps are only going to come from good programmers.


But yet Mac users have been seeded with this idea that Cocoa is a magic bullet, and Carbon is a rusty bucket. This myth needs to be dispelled, not promulgated. And it’s a shame to see a writer as smart and prominent as Gillmor on the wrong side.



| **Previous:** | [Command Line Fun](https://daringfireball.net/2003/04/command_line_fun) |
| **Next:** | [Stoned](https://daringfireball.net/2003/04/stoned) |


PreviousNext