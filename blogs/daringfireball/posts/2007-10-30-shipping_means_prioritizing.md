---
title: "Shipping Means Prioritizing"
date: 2007-10-30
url: https://daringfireball.net/2007/10/shipping_means_prioritizing
slug: shipping_means_prioritizing
word_count: 685
---


So I’ve gotten a sizable stream of feedback regarding my Linked List quip regarding Java developers who are pissed at Apple about Leopard’s crummy Java support. [I wrote](http://daringfireball.net/linked/2007/october#tue-30-java):


> I fail to see why anyone (other than Java developers themselves) would care.


And, of course, just about every message I’ve gotten telling me that I’m wrong or arrogant (or both) has been from a Java developer.


This is not complicated. Leopard was already late. Apple originally stated it would ship in the “first half” of 2007. It slipped four months and they got a ton of negative publicity when they had to announce the slip. And, from what I can tell, talking to friends at Apple and judging by the developer seeds over the last few months, a lot of engineers at Apple have been working their asses off for a long time to get Leopard into the state it’s in today.


Shipping is hard.


The only way to ship software is to prioritize, and prioritizing means dropping things that are less essential in exchange for things that are more essential. Obviously, for Apple, Java 6 is not a priority. And, judging by reports that even Java 5 support is worse on Leopard than it was on Tiger, Java as a whole is not a priority for Apple. [**Update:** Several readers say that reports of Java 5’s suckage on Leopard are greatly exaggerated — *different*, yes, but the UI changes are an improvement, at least in some Java developers’ eyes.]


But it’s not like Apple is sitting on a top-notch Java-6-for-Mac-OS-X and withholding it out of spite. They simply decided to allocate engineering resources elsewhere. In the case of Java, I don’t think it was even a close call. What should they have done? Delayed Leopard even further? Pulled engineering resources from something that *did* ship with Leopard for Java? Java simply isn’t relevant to the Mac.


Several irritated Java developers suggested that I’d feel differently if it were a developer runtime that I personally cared about — that I’d be irate if, say, Perl or Ruby or Python were dropped or degraded in Leopard. But that’s not a good comparison; Perl, Python, and Ruby pretty much compile out of the box on Mac OS X. Apple doesn’t have to do much at all — at least relative to Java — to include them on Mac OS X. Why? Because that’s how these tools are designed and engineered — they’re made to “just build” on any Unix-like OS. It’s not Apple’s responsibility that Java isn’t like that — it’s Sun’s.


Apple made all sorts of compromises in order to ship Leopard. Look no further than 64-bit Carbon, which was *in* when Leopard was initially announced at WWDC 2006, but was dropped at WWDC 2007. Carbon *is* directly relevant to the Mac; it remains the foundation for many of the most popular apps on the platform. As [John Siracusa wrote in his Leopard review](http://arstechnica.com/reviews/os/mac-os-x-10-5.ars/6):


> In the end, Apple made the hard choice instead of the easy one. I think it will pay off, though the short-term consequences could be pretty grim. After all, just look at how long it’s taking to get an Intel-native version of Microsoft Office for the Mac. Should we expect a 64-bit Cocoa version in, say, 2012? And I have no idea what Adobe’s going to do about 64-bit versions of its products. That’s many millions of lines of Carbon code between those two companies alone. We may be in for a rough patch, so buckle up.


Compared to the decision to abandon work on 64-bit Carbon, Apple’s decision to abandon (or *postpone*, for all we know) work on Java 6 was easy. Some of the most important software for the Mac depends on Carbon. No important software for the Mac depends on Java.1


---

1. Where by “no” I mean “some very small amount, and what small amount there is, I’ll wager still works as well on 10.5 as it did on 10.4”. ↩︎



| **Previous:** | [Blue in the Face](https://daringfireball.net/2007/10/blue_in_the_face) |
| **Next:** | [Happy Halloween, Savvy?](https://daringfireball.net/2007/10/happy_halloween_savvy) |


PreviousNext