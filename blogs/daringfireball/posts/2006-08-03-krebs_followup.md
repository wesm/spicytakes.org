---
title: "Regarding Brian Krebs’s Reporting on the Supposed MacBook Wi-Fi Exploit"
date: 2006-08-03
url: https://daringfireball.net/2006/08/krebs_followup
slug: krebs_followup
word_count: 743
---


[Brian Krebs has written a follow-up](http://blog.washingtonpost.com/securityfix/2006/08/followup_to_macbook_post.html) regarding yesterday’s “[Hijacking a Macbook in 60 Seconds or Less](http://blog.washingtonpost.com/securityfix/2006/08/hijacking_a_macbook_in_60_seco.html)” post on his Washington Post “Security Fix” weblog:


> I’d like to respond to the people who commented on
> [yesterday’s post](http://blog.washingtonpost.com/securityfix/2006/08/hijacking_a_macbook_in_60_seco.html) about the video’s depiction of the use
> of a third-party wireless card on the Macbook [*sic*]. I spent
> more than an hour with Dave Maynor watching this exploit in
> action and peppering him with questions about it.
> During the course of our interview, it came out that Apple had
> leaned on Maynor and Ellch pretty hard not to make this an
> issue about the Mac drivers — mainly because Apple had not
> fixed the problem yet.


What does this mean, that Apple “leaned on Maynor and Ellch pretty hard”? Were they threatened? By whom at Apple, exactly? And how? With a lawsuit? With violence?


And, if Apple did in fact “lean on” them, why didn’t Apple ask them not to use a Mac in the demo at all? What was Apple’s request, exactly? “Go ahead and show it on a MacBook, but use a third-party wireless card? And it’s OK for you to confirm to reporters that the built-in AirPort drivers are also exploitable, we just don’t want you to show it in a video.” What sense does that make?


If they’re willing to say that the built-in driver is exploitable, why are they not willing to prove it?


> Maynor acknowledged that he used a third-party
> wireless card in the demo so as not to draw attention to the flaw
> resident in Macbook drivers. But he also admitted that the same
> flaws were resident in the default Macbook wireless device
> drivers, and that those drivers were identically exploitable. And
> that is what I reported.
> I stand by my own reporting, as according to Maynor and Ellch it
> remains a fact that the default Macbook drivers are indeed
> exploitable.


But did Krebs *see* the exploit work against a MacBook’s built-in AirPort card? He says he stands by his reporting, but he did not report that the exploit works against the MacBook’s built-in AirPort driver; he reported that Maynor and Ellch *told him* that it works against the MacBook’s built-in AirPort driver. “I stand by that *they told me* the built-in driver is expoitable” is very different than “I stand by that the built-in driver is exploitable”.


If it’s true that this exploit *does* work against the MacBook’s built-in AirPort driver, it’s one of the most serious security exploits ever discovered against Mac OS X. Basing their demo video on a third-party card makes matters *worse*, not better, because it creates the perception that the majority of MacBook users are safe because they aren’t using third-party cards.


Krebs’s shoddy reporting leaves nearly all the important questions regarding this exploit unanswered. What about other models? Are MacBook Pros exploitable as well? PowerBooks? iBooks? Desktop Macs that use AirPort? Is a Mac vulnerable in its default out-of-the-box configuration? For example, by default, Mac OS X is configured to ask for confirmation before joining an unknown open Wi-Fi network. Does this exploit require that this setting (in the Network panel in System Preferences) be changed to allow joining unknown open networks automatically? Are any other changes to the default networking configuration required to allow this exploit to work? Is there anything Mac users can do to protect themselves other than completely disabling AirPort?


Aren’t these questions completely obvious?


> Again, the whole point of this story was not to pick on Macs, but
> to point to a security issue that affects multiple operating
> systems and one that is long overdue for some serious code review
> by the companies that OEMs rely upon to produce this software.


With a headline like “Hijacking a Macbook in 60 Seconds or Less”, or his quote from exploit co-discoverer David Maynor saying “if you watch those ‘Get a Mac’ commercials enough, it eventually makes you want to stab one of those users in the eye with a lit cigarette or something,” where would anyone get the idea that the point of Krebs’s post was to pick on Macs? Or, more accurately, to generate a sensational amount of attention by playing off the Mac’s sterling reputation for security?



| **Previous:** | [Magic 8-Ball Answers Your Questions Regarding Microsoft’s ‘Zune’](https://daringfireball.net/2006/07/magic_8-ball_zune) |
| **Next:** | [Highly Selective](https://daringfireball.net/2006/08/highly_selective) |


PreviousNext