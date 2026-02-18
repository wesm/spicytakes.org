---
title: "On the Timing of iOS’s SSL Vulnerability and Apple’s ‘Addition’ to the NSA’s PRISM Program"
date: 2014-02-22
url: https://daringfireball.net/2014/02/apple_prism
slug: apple_prism
word_count: 401
---


[Jeffrey Grossman, on Twitter](https://twitter.com/Jeffrey903/status/437273379855667201):


> I have confirmed that the SSL vulnerability was introduced in iOS
> 6.0. It is not present in 5.1.1 and is in 6.0.


[iOS 6.0 shipped on 24 September 2012](http://en.wikipedia.org/wiki/IOS_6#6.0_2).


According to slide 6 in [the leaked PowerPoint deck on NSA’s PRISM program](http://www.theguardian.com/world/interactive/2013/nov/01/prism-slides-nsa-document), Apple was “added” in October 2012.


These three facts prove nothing; it’s purely circumstantial. But the shoe fits.


Sure would be interesting to know who added that spurious line of code to the file. Conspiratorially, one could suppose the NSA planted the bug, through an employee mole, perhaps. Innocuously, the Occam’s Razor explanation would be that this was an inadvertent error on the part of an Apple engineer. [It looks like](https://www.imperialviolet.org/2014/02/22/applebug.html) the sort of bug that could result from a merge gone bad, duplicating the `goto fail;` line.


Once the bug was in place, the NSA wouldn’t even have needed to find it by manually reading the source code. All they would need are automated tests using spoofed certificates that they run against each new release of every OS. Apple releases iOS, the NSA’s automated spoofed certificate testing finds the vulnerability, and boom, Apple gets “added” to PRISM. (Wasn’t even necessarily a fast turnaround — the NSA could have discovered the vulnerability over the summer, while iOS 6 was in developer program beta testing.)


Or, maybe nothing, and this is all a coincidence.


I see five levels of paranoia:

1. Nothing. The NSA was not aware of this vulnerability.
2. The NSA knew about it, but never exploited it.
3. The NSA knew about it, and exploited it.
4. NSA itself planted it surreptitiously.
5. Apple, complicit with the NSA, added it.


Me, I’ll go as far as #3.1 In fact, I think that’s actually the optimistic scenario — because we know from the PRISM slides that the NSA claims some ability to do what this vulnerability would allow. So if this bug, now closed,2 is not what the NSA was exploiting, it means there might exist some other vulnerability that remains open.


---

1. “Never ascribe to malice that which is adequately explained by incompetence.” —[Hanlon’s Razor](http://en.wikipedia.org/wiki/Hanlon's_razor) ↩︎
2. Closed on iOS, that is. As of this writing, it remains open on Mac OS X 10.9.1. I expect it to be closed there soon, though. ↩︎



| **Previous:** | [Microsoft, Past and Future](https://daringfireball.net/2014/02/microsoft_past_and_future) |
| **Next:** | [Just Do Something](https://daringfireball.net/2014/02/action_jackson) |


PreviousNext