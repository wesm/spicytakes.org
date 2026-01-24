---
title: "The Ultimate Software Gold Plating"
date: 2008-07-15
url: https://blog.codinghorror.com/the-ultimate-software-gold-plating/
slug: the-ultimate-software-gold-plating
word_count: 517
---

Some developers love to [gold plate their software](https://blog.codinghorror.com/gold-plating/). There are various shades of... er, gold, I guess, but it’s usually considered wasteful to fritter away time gold plating old code in the face of new features that need to be implemented, or old bugs that could be squashed.


> Developers are fascinated by new technology and are sometimes anxious to try out new features of their language or environment or to create their own implementation of a slick feature they saw in another product – whether or not it’s required in their product. The effort required to design, implement, test, document, and support features that are not required lengthens the schedule.


But gold plating your code isn’t *all* bad. Perhaps the most remarkable tale of successful developer gold plating I’ve ever read is the one [Blake Patterson outlines](http://www.bytecellar.com/archives/000158.php):

kg-card-begin: html

> Not long ago I purchased a new-in-box [Atari Jaguar](http://en.wikipedia.org/wiki/Atari_Jaguar), complete with [Jeff Minter’s](http://en.wikipedia.org/wiki/Jeff_Minter) psychedelic sequel to Tempest, [Tempest 2000](http://en.wikipedia.org/wiki/Tempest_2000). It’s an amazing game that’s been ported to many other platforms, but the consensus is that none are as solid as the Jaguar original. Having played several of the ports, I’d have to agree.
> An interesting thing about “the world’s first 64-bit console” – its controller was, as the Brits would say, fairly pants. It was large, sported a calculator-button array for game overlays (like the [Intellivision](http://en.wikipedia.org/wiki/Intellivision) controller), had no shoulder buttons, and featured only a D-pad for directional control. (ed: certainly one of the weirdest members of the game console controller family tree, to be sure)
> As the arcade original is controlled with a rotary spinner knob, the D-pad falls rather short of providing ideal game control.
> But, of course, being such a savvy chap, Jeff Minter realized this.
> **Jeff wrote in support for an analog rotary controller... *that did not exist*.** Neither Atari nor third party manufacturers produced such a controller in the Jaguar’s heyday. Jeff, as I understand it, hacked his own together by wiring an [Atari paddle controller](http://www.atariage.com/2600/controllers/con_AtariPaddles.jpg) into a Jaguar controller. In the years since the Jaguar’s passing, a few small operations have offered modified Jaguar controllers with spinners wired into them for purchase.

kg-card-end: html

Jeff Minter’s an interesting historical figure in the computer gaming community, as the author of several 8-bit computer era game classics. I’ve talked about his long-standing interest in [audio visualization](https://blog.codinghorror.com/on-audio-visualization/) here once before. He’s still creating games today; his latest is the Xbox Live downloadable title [Space Giraffe](http://en.wikipedia.org/wiki/Space_Giraffe). Jeff [has a blog](http://stinkygoat.livejournal.com/) that he updates fairly regularly.


Still, I’m amazed that Jeff added code to a commercially shipped console game to support **a completely optional homebrew spinner controller of his own creation**. That’s the very definition of “not required.” This code lied dormant in the game until a handful of enthusiasts, fourteen years later, cobbled together custom controllers to play the game as it was originally intended by the author.


If that isn’t the ultimate case of gold plating your software, I don’t know what is. My hat is off to you, Mr. Minter.

[software development](https://blog.codinghorror.com/tag/software-development/)
[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[software design](https://blog.codinghorror.com/tag/software-design/)
