---
title: "Is there an optimal piracy rate?"
date: 2006-01-14
url: https://blog.codinghorror.com/is-there-an-optimal-piracy-rate/
slug: is-there-an-optimal-piracy-rate
word_count: 752
---

I’ve recently been struggling with a number of [racing sims](https://blog.codinghorror.com/pc-racing-sims/) I bought to use after work hours in our [new racing cockpit](https://web.archive.org/web/20061004221730/http://blogs.vertigosoftware.com/jatwood/archive/2006/01/13/1861.aspx). I’m a big believer in supporting developers. I’m a developer myself. But digging around for CDs or DVDs is impractical for dedicated gaming rigs, so I install no-cd patches when I can.


Unfortunately, finding no-cd patches is getting harder and harder because of a relatively new copy protection known as [StarForce](http://en.wikipedia.org/wiki/StarForce). It’s a kernel-mode device driver that talks directly to the IDE hardware to validate the CD or DVD. Beyond that, the technical details are sketchy, probably to prevent crackers from gaining the upper hand. But the net result is that **no-cd patches for games with the latest StarForce protection are rare**.


For example, [Splinter Cell: Chaos Theory](https://web.archive.org/web/20061017141610/http://www.gamespot.com/pc/action/splintercell3/), which was released early last year, has no known working no-cd patch as of today – almost a year later. That’s *amazing*. There are legions of hackers and crackers out there. Fending them off for this long is completely unprecedented. For as long as there has been software, there have been crackers – and they’ve always won.


My hat is off to the developers of [StarForce](http://www.star-force.com/). However you feel about copy protection, they’ve accomplished what many thought could never be done. Now, before you spam the comments with diatribes about how much StarForce sucks, how it kills small children and formats your hard drive, etcetera, take the time to read their point of view in this [interview with a StarForce rep](https://web.archive.org/web/20060114074128/http://www.firingsquad.com/features/starforce_interview/). It has their side of the story, and many additional details. I’ll also add that I played, completed, and sold Splinter Cell Chaos Theory earlier this year without once knowing that I was playing a StarForce protected game.


Now, this is not to say that StarForce can’t be circumvented. It can. The primary method of circumventing StarForce at the moment is to **stop using parallel ATA optical drives**:

1. physically unplug your optical drives*
2. use a special utility to completely disable parallel ATA on your PC (that’s assuming you're using serial ATA hard drives)
3. switch to external USB optical drives


It’s kind of a scorched earth solution, but it’s the only thing that works. And once you’ve done that, you’re still not done! The very, very latest versions of StarForce monitor hard drive access at the time of disc validation to see if that “DVD” you mounted is really being read from the hard drive. So you have to load an additional device driver that hides the physical drive access from StarForce.


All in all, a giant pain in the ass. **Which is entirely the point of copy protection.**


But is StarForce *too much* copy protection? Chris Anderson maintains that there is an [optimal level of piracy](http://longtail.typepad.com/the_long_tail/2005/08/just_enough_pir.html) for any industry, due to the following effects:

- Remember [dongles](http://en.wikipedia.org/wiki/Dongle)? Any protection technology that is really difficult to crack is probably too cumbersome to be accepted by consumers.
- Piracy can let you raise your prices. Rather than pricing between the absolute economic bottom and the top, you cede the bottom to piracy – no price can compete with free – and set your price between the middle and the top.
- Piracy helps seed technology markets. The ubiquity of pirated Windows and Office have made them de-facto national standards in many countries.


Chris proposes that a certain level of piracy is simply good business:


> *When all these effects are considered, it appears that there actually is an optimal level of piracy. That right level would vary from industry to industry. Today the estimated piracy rates are 33% for CDs and 15% for DVDs. The industries say that’s too high, but most anti-copying technologies they’ve brought in to lower that figure have proven unpopular. Would even tighter lock-downs help? Probably not. Maybe 15%-30% is simply the market saying that this is the optimal rate of piracy for those industries, and any effort to lower that significantly would either choke demand or push even more people to the dark side.*


I tend to agree. I think DVDs are an excellent example of this “good enough” theory in action. They have a basic level of copy protection, but they’re priced so reasonably very few people bother to pirate them. The people that continue to pirate DVDs probably wouldn’t buy them no matter how low they were priced.


*No, disabling them in the BIOS doesn’t work. StarForce talks directly to the ATA hardware at the kernel level.

[security](https://blog.codinghorror.com/tag/security/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
