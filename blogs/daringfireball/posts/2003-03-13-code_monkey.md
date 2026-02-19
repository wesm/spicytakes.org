---
title: "Code Monkey"
date: 2003-03-13
url: https://daringfireball.net/2003/03/code_monkey
slug: code_monkey
word_count: 698
---


Despite the fact that SmartyPants 1.2.1 was released just two days ago, today I’ve [released version 1.2.2](http://daringfireball.net/projects/smartypants/).  One of the bugs in version 1.2.0 was a bit of regular expression syntax that produced warnings under Perl 5.005.  (Despite the fact that Perl 5.6 has been out for several years and provides numerous vast improvements, it is apparently *de rigueur* when running a second-rate web hosting company to provide your customers with Perl 5.005. Also, for those of you who aren’t Perl nerds, it’s worth noting that with 5.6, Perl’s version numbering scheme changed to resemble something most people would consider normal; Perl 5.005 is what most people would call “Perl 5.5”.)


Anyway, in the course of fixing that bug — which was mostly harmless, and at the very worst resulted in quotes being curled the wrong way in rare situations — version 1.2.1 introduced another change which rendered SmartyPants utterly inoperable under Perl 5.005.  In other words, one of the reasons for version 1.2.1 was to allow SmartyPants to work better under Perl 5.005, but in fact, it didn’t work at all. This has been remedied for 1.2.2, and in fact is the only change. If you’re using version 1.2.1 and haven’t noticed any problems (i.e. you’re using Perl 5.6 or later), feel free to ignore this update.


You’re probably wondering: *How could something like this happen at a well-oiled machine such as Daring Fireball?* The problem is one of delegation.


See, back in 1998 I became the owner of a South American woolly monkey, whom I named Paco, with the intention of training him to assist in my freelance graphic design work. Everyone told me this was a terrible idea, that it would not work, that at the very least I would need a chimpanzee or orangutan, that a mere monkey would never be able to do graphic design.


I was unswayed. Do you know how much food chimpanzees and orangutans eat? And for chrissakes, an orangutan can beat you up — I’ve seen those Clint Eastwood movies, those fuckers can pack a punch. I do not need to be coldcocked by my lower-primate assistant. What I wanted was a monkey, a loyal friend who, when otherwise unoccupied, could sit on my shoulder and pick crumbs out of my hair.


And in the end, I was right. It was no trick at all to train Paco as a graphic designer. Within weeks, he was doing production work in Quark XPress. Within months, he was doing original page layouts, typesetting, and logo design (he did the Daring Fireball logo atop this very page). Paco proved to be an enormous time saver, much more so than AppleScript. And he works for nothing more than food (he is partial to Chex Mix) and a warm box in which to sleep; no taxes, no paperwork, yet perfectly legal.


Paco’s graphic design services freed me to do other things, such as sleeping late, playing golf, and programming. It didn’t take long to begin wondering if I could teach Paco to program, too.


This was not nearly as easy as teaching Paco graphic design. Two years into the effort, and he still refuses to invoke Perl’s “use strict” pragma. (In hindsight, I probably should have tried teaching him Python instead, but I went with Perl thinking that perhaps after he got the hang of it, it would be easier to teach him PHP, which is fairly similar to Perl syntactically.) Yes, he can write functional programs, but his code is nearly unreadable, and he *never* performs tests. Once he gets to the point where he thinks his code looks like it should work, he scampers away.


And so it was in fact Paco who was responsible for this embarrassing mishap in SmartyPants 1.2.1, a bug which would have been glaringly obvious had he simply tried running the damn thing under Perl 5.005 *just once* before we released it. He has been sternly reprimanded, but it is my opinion that he is unrepentant. Thus, henceforth, I will be taking personal responsibility for testing Señor Paco’s code before releasing it unto the world.



| **Previous:** | [SmartyPants 1.2.1](https://daringfireball.net/2003/03/smartypants_121) |
| **Next:** | [Anti-Anti-Aliasing](https://daringfireball.net/2003/03/anti-anti-aliasing) |


PreviousNext