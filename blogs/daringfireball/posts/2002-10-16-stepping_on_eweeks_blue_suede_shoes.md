---
title: "Stepping on eWeek’s Blue Suede Shoes"
date: 2002-10-16
url: https://daringfireball.net/2002/10/stepping_on_eweeks_blue_suede_shoes
slug: stepping_on_eweeks_blue_suede_shoes
word_count: 1421
---


It’s bullshit detection week here at Daring Fireball.


Next on our list is [eWeek’s “scoop”](http://www.eweek.com/article2/0,3959,634711,00.asp) claiming that within the next three weeks, Apple is going to release a 10.2.2 update to Jaguar, which will include, as an option, a journaling file system code-named “Elvis”.


Allow me to dissent from the rah-rah coverage this story is getting elsewhere. Because I don’t believe it.


Disclaimer: I don’t have any sources within Apple. Nor do I have a beta copy of 10.2.2. I’ve got nothing but my own speculation. But if I’m wrong, and 10.2.2 appears in a few weeks with a journaling file system, I’ll eat some crow right here.


From the article:


> The journaled file system, which will run atop the Mac’s traditional HFS file scheme, will be switched off by default; users will be able to switch it on via the command line, sources said. They reported that while Elvis runs in the background, enabling the journaled file system will slow current system performance by 10 percent to 15 percent.


This makes no sense. None.


HFS+ and UFS are two file systems, both supported by Mac OS X. Neither is a journaling file system. (Neither is a “file scheme”, either, whatever that is.) You can’t just turn HFS+ into a journaling file system with a magic layer of pixie dust. To change a disk from one file system to another, you need to reformat it. What eWeek is claiming simply isn’t possible.


A journaling file system doesn’t simply write a single “journal” file containing all the journaling information. The whole point of a journaling file system is that the journaling data is a fundamental part of the format itself.


The article continues:


> Indeed, Apple apparently enlisted the creator of the Be technology for its Elvis project: Be’s BFS journaled file system was written by Dominic Giampaolo, who in March joined Apple as a file system engineer, The Register UK reported.


It’s definitely true that [Apple hired Dominic Giampaolo](http://wmf.editthispage.com/2002/04/07). And it’s also true that Giampaolo was largely responsible for the BeOS’s journaling file system. And it makes a lot of sense that he might be working on a journaling file system for Apple. But if and when such a journaling file system appears, it will, by definition, be a *new* file system.


Nor is it plausible that Apple would debut a brand-new file system in a minor OS update. Since 1984, there have been a grand total of three new Macintosh disk formats: the original Macintosh File System (MFS) in 1984, the Hierarchical File System (HFS) that debuted with System 3.0 in 1986, and HFS Extended (HFS+), which debuted in Mac OS 8.1. And don’t let the “.1” fool you, Mac OS 8.1 was a major update. (Thanks to [MacKiDo](http://www.mackido.com/History/EarlyMacOS.html) for the historical data.)


## Track Records


Co-author Matthew Rothenberg has a terrible track record with his rumor-mongering, and the other byline on the article belongs to Nick de Plume, the pseudonymous author behind the seldom-accurate [Think Secret](http://www.thinksecret.com/).


The October 5 issue of [MWJ](http://macjournals.com) addressed Rothenberg’s recent crowing over Apple confirming his previous “scoop” about future Macs no longer booting into Mac OS 9. As MWJ points out, he scooped no such thing.


What happened is that eWeek published a story titled “[Apple to Slam Lid on Mac OS 9](http://www.eweek.com/article2/0,3959,431382,00.asp)” by Rothenberg on August 2. In that story, he wrote:


> A tweak to new models in its Macintosh line of desktop and portable computers will prevent booting into Mac OS 9, sources said, leaving the Unix-based Mac OS X as the sole operating system. 
> Sources said the Mac OS X-only policy will probably be enforced via a software feature in Pinot, the next major Mac OS X update after Jaguar (Mac OS X 10.2), which Apple said will ship Aug. 24. Apple will most likely make the move by January’s Macworld Expo/San Francisco.


Note that the article alleges that these new Macs *could* boot into OS 9, but that Apple will use a “tweak” to prevent them from doing so.


I’ll let MWJ take it from here:


> Of course, Apple did announce it would make new machines that
>   don’t boot into Mac OS 9, but eWEEK’s details appear
>   substantially wrong. The story describes machines that could
>   boot into Mac OS 9 but are prevented from doing so via a “tweak”
>   or software update, and there’s no available evidence to support
>   that. As MWJ pointed out at the time, a far more plausible
>   explanation is that Apple will finally advance the motherboard
>   to include new technologies that Apple doesn’t want to support
>   in native Mac OS 9, such as faster FireWire, USB, AGP, or even
>   HyperTransport (MWJ 2002.09.18). Turner and Rothenberg’s own
>   article goes to show why disabling Mac OS 9 booting for
>   non-technical reasons is ridiculous: large customers are already
>   saying they won’t purchase those machines. Apple is not in a
>   position to turn away eager Power Macintosh customers in a slow
>   technology economy.
>   However, since the article, eWEEK has published at least three
>   more crowing about how Apple’s announcement “confirmed a recent
>   eWEEK report.” The original article was modified to link to a
>   [new story](http://www.eweek.com/article2/0,3959,525179,00.asp) “in which Apple confirms its plans,” and that
>   story spends its first two paragraphs talking about how Apple
>   was just confirming what eWEEK had already reported — even
>   though Apple did no such thing. A 2002.09.16 Rothenberg column
>   boldly crows about the “scoop”, saying, “I hate to say it, but
>   we told you so,” and “I’m delighted to note that Daniel Drew
>   Turner and I were on the money back at the beginning of August,
>   when we first flagged Apple’s next major step to close the book
>   on Mac OS 9.”
> […]
> Rothenberg, who formerly wrote MacWEEK.com’s “Mac the Knife”
>   column, tends to get onto these rumors and hold them for years,
>   including the “Apple’s about to dump the PowerPC” and
>   “handwriting recognition is the wave of the future” memes.
>   To an extent, this is harmless braggadocio, but eWEEK is
>   starting to change that. The site, and more specifically,
>   Rothenberg, are linking to the “confirmed” report about booting
>   into Mac OS 9 at every opportunity to lend credibility to other
>   rumors that even the Knife likely wouldn’t have gotten into
>   print.


[I had never before seen Rothenberg named as MacWeek.com’s Mac the Knife. Now *that’s* what I call a scoop. If you’re a Mac nerd and don’t subscribe to MWJ, you [ought to](http://www.macjournals.com/pages/mwj/).]


## I Saw Elvis at a K-Mart in Minneapolis


Near the bottom of the journaling file system article, they state:


> Apple reportedly seeded a pre-release build to developers earlier this month, minus the Elvis enhancements.


What sense does this make? Yes, the new Apple is secretive about future products. But what good would it do to seed a version of OS X designed to run under a new file system without the actual file system? If it were true that 10.2.2 is going to offer a journaling file system, wouldn’t that be the feature *most* in need of widespread testing?


It wouldn’t be surprising if Apple were to send out beta seeds missing secret new components that they want to keep under wraps. Like, say, a new iApp. Applications can be tested separately from the operating system itself, and don’t generally have a system-wide effect. But a new file system would constitute a major change to the core of the operating system itself, and would effect the integrity of every single file on the computer.


My guess as to what will really happen:

1. Mac OS X 10.2.2 will indeed be released within a month or two.
2. It will not contain a journaling file system.
3. Rothenberg will claim he was right, but that Apple executives pulled the new feature at the last minute, (a) to wait for Macworld Expo in January, or (b) to wait for the next paid update to Mac OS X.
4. People who believed eWeek will be sorely disappointed, and some will misdirect their disappointment toward *Apple*, a company which, to my knowledge, has yet to say a single word about a journaling file system.


And my advice is not to believe rumors that don’t come with attributed quotes or credible screenshots.



| **Previous:** | [Microsoft Make-Up](https://daringfireball.net/2002/10/microsoft_make-up) |
| **Next:** | [Listen](https://daringfireball.net/2002/10/listen) |


PreviousNext