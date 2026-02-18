---
title: "25 Years Ago: RAM Doubler"
date: 2019-01-28
url: https://daringfireball.net/2019/01/ram_double_engst
slug: ram_double_engst
word_count: 478
---


Adam Engst, [writing for TidBITS from Macworld Expo 25 years ago](https://tidbits.com/1994/01/10/ram-doubler/):


> RAM Doubler is a single small extension that literally doubles
> your RAM. It’s not guessing at a 2:1 compression ratio, like
> Salient’s AutoDoubler and DiskDoubler (now owned by Symantec) —
> you actually see your total memory being twice your built-in
> memory. Since RAM Doubler is an extension, there are no controls,
> no configuration. You just install it and it doubles the amount of
> application RAM you have available.
> A number of people have expressed disbelief that such a feat is
> possible, saying that they’d avoid anything like RAM Doubler
> because it’s obviously doing strange things to memory, which isn’t
> safe. […]  >
> Needless to say, since RAM Doubler has only been out for a few
> days, we haven’t been testing for long, but I can honestly say
> that neither of us have noticed anything out of the ordinary
> during this time.


This is [the start of a series](https://tidbits.com/2019/01/24/25-years-ago-in-tidbits-ram-doubler-debuts/) TidBITS is running, looking back at old articles from their archive.


I couldn’t use RAM Doubler on my Mac LC, because it required a 68030 processor and the LC only had a 68020. But I used it on other Macs, and it really did work as advertised — it doubled your RAM in exchange for a negligible cost in performance. The most amazing thing, in hindsight, isn’t that compression and clever virtual memory techniques could double your memory — it’s that Mac OS was so open that something as low-level as RAM Doubler was even possible. Effectively, a Mac running RAM Doubler was running a fork of the OS — not just a subtle fork but a fork where the entire memory manager was written by a third party.


In hindsight, the lack of protected memory and disk permissions in classic Mac OS are generally only looked back upon as severe deficiencies. And there certainly were deep problems with that architecture — one app or extension crashing often resulted in the entire machine going down. But that *anything goes* openness also resulted in tremendous opportunities for third-party software.


From a low-level computer science operating systems perspective, the classic Mac OS was dangerously primitive. But from a high-level user interface perspective, it remains amazing. To install RAM Doubler — software that radically changed the way the OS worked — all you had to do was copy one file to the Extensions folder in your System folder. To uninstall, you just moved it out of that folder. That’s it. One file in one special folder and then restart the machine.


Third-party extensions could be exasperating, yes, but they could also be amazing and just plain [fun](https://www.youtube.com/watch?v=GE7EWDKVM1Y) in ways that aren’t possible today.



| **Previous:** | [The R-Word](https://daringfireball.net/2019/01/the_r_word) |
| **Next:** | [On Covering Webcams](https://daringfireball.net/2019/02/on_covering_webcams) |


PreviousNext