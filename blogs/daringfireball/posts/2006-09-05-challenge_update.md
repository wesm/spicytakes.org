---
title: "Update on the MacBook Wi-Fi Exploit Challenge"
date: 2006-09-05
url: https://daringfireball.net/2006/09/challenge_update
slug: challenge_update
word_count: 1590
---


My “[hijack this brand-new MacBook via wi-fi and it’s yours to keep](http://daringfireball.net/2006/09/open_challenge)” challenge to David Maynor and Jon Ellch has not yet been accepted, but I do have a few additional points to address.


## Doubling the Offer


[Jim Thompson](http://www.smallworks.com/), whose own coverage of this issue I’ve linked to several times, has offered to contribute a second matching MacBook, should Maynor and Ellch succeed in my challenge. Not only does this double the size of the bounty, but it should also make it easier for Maynor and Ellch to split their winnings — it admittedly wouldn’t be much fun to split a single MacBook.


## Putting Your Money Where My Mouth Is


Dozens of DF readers have emailed offering to contribute money to pay for the MacBook if I lose this challenge. This is both generous and encouraging, and my sincere thanks go out to everyone who’s offered. But, for now, please hold on to your money. If I lose — a big “if” in my opinion — I’ll set up a [DropCash](http://dropcash.com/) campaign for people to contribute to. But I issued this challenge fully willing to foot the entire bill, should I lose.


But I’m pretty certain it won’t come to that. In fact, I’m pretty certain I could up the ante to a gold-plated MacBook at this point.1


## Why I Think This Challenge Is Fair


A few critics have emailed claiming that this challenge is unfair to Maynor and Ellch, on the grounds that they’ve never claimed that a stock MacBook is vulnerable to this attack.


That’s not so. The Washington Post’s Brian Krebs, who broke the [original story](http://blog.washingtonpost.com/securityfix/2006/08/hijacking_a_macbook_in_60_seco.html), wrote the following [in a next-day follow-up](http://blog.washingtonpost.com/securityfix/2006/08/followup_to_macbook_post.html):


> During the course of our interview, it came out that Apple had
> leaned on Maynor and Ellch pretty hard not to make this an issue
> about the Mac drivers — mainly because Apple had not fixed the
> problem yet. Maynor acknowledged that he used a third-party
> wireless card in the demo so as not to draw attention to the flaw
> resident in Macbook drivers. But he also admitted that the same
> flaws were resident in the default Macbook wireless device
> drivers, and that those drivers were identically exploitable. And
> that is what I reported.
> I stand by my own reporting, as according to Maynor and Ellch it
> remains a fact that the default Macbook drivers are indeed
> exploitable.


This could certainly be an error on Krebs’s part, but, if that’s the case, and it had been *my* findings that Krebs had so grossly mis-reported, I’d issue a correction. SecureWorks, Maynor, and Ellch have not apparently contacted Krebs with any additional statements. In his most recent update on the subject, Krebs wrote:


> I have several times now asked SecureWorks to share with me more
> specific information to back up their claims, but so far I have
> received no further details. If I hear back from SecureWorks with
> any more material information, I will update the blog.


And in [their own slides](http://blog.washingtonpost.com/securityfix/response.ppt) for a second presentation last month (linked to by Krebs), Maynor and Ellch published the following Q&A:


> [Q:] I saw some people quote you as saying the bug is in the
> built-in in card and other people quote you as saying as its [*sic*]
> not, who is right?
> [A:] They both are. The exploit shown in the video was targeting a
> specific third party driver and that same vulnerability does not
> affect the built in [*sic*] card. We are, however, doing ongoing
> research on the built-in card as well and have shared our findings
> with Apple.


Clearly, this is not a straightforward answer, but “They both are” certainly implies that “the bug” (i.e. the bug exploited in their video to take control of a MacBook via Wi-Fi) exists in “the built-in card”. The next sentence says it doesn’t exist in the built-in card, and then they blather about their ongoing research.


When repeatedly asked different formations of the obvious question as to why they chose to demonstrate their exploit against a third-party wireless card and driver, they have never responded by saying “Because we have not found a way to perform this exploit against the built-in MacBook card and driver.” Instead, they’ve said, more or less, that they don’t want to demonstrate this exploit against the built-in card.


Refusing to even answer the yes/no “Have you found such an exploit against the built-in MacBook card and driver?” is just silly. If the answer is no, they haven’t, that’s contrary to what has been reported, and contrary to what many people believe. If the answer is yes, confirming that they’ve found such a flaw would not reveal any technical details about how it works.


It makes no sense to me that they won’t even confirm the *existence* of a similar exploit against the stock MacBook driver and card. Why not? So that some malfeasant wouldn’t get the idea to investigate and discover the details for himself? Surely that is no less likely to happen given what has actually transpired.


Why refuse to say “yes” or “no” but instead hint that there *might* be one? Their ambiguity makes it every bit as likely that a malfeasant would investigate on his own than if they had came right out and said, “We have identified a vulnerability in the default MacBook Wi-Fi driver and card, but we are not releasing any details of this vulnerability until Apple has time to issue a patch.” “We have found an exploit” is not much different than “we may or may not have found an exploit” in this regard.


Simply saying “yes”, if it’s true, would also allow MacBook owners to be warned.


## Legal Threats


There’s also rampant speculation that Maynor and Ellch can’t say anything about this issue now because they’ve been threatened by Apple Legal. For example, there’s the initial “Apple had leaned on Maynor and Ellch pretty hard not to make this an issue about the Mac drivers” accusation reported by Krebs.


However, as pointed out by [MDJ](http://macjournals.com/mdj/) last week (as part of their excellent feature article on the saga), when Krebs subsequently posted [the “word-for-word” transcript of his interview with Maynor](http://blog.washingtonpost.com/securityfix/2006/08/the_macbook_wireless_exploit_i.html), it contained no mention of such a threat. From MDJ 2006.08.30:


> For example, at one point in the transcript, Maynor says that to
> do the raw packet injection that the exploit requires, “we had
> to build our own custom kernel.” Krebs, distressingly, does not
> ask if that means the MacBook is running a modified kernel, one
> that might be more vulnerable than the one everyone else is
> running. Also missing from the transcript: the part of the
> interview where Maynor says that Apple, or in fact any vendor,
> pressured him not to demonstrate the exploit. In the “verbatim”
> transcript that Krebs posted, Maynor mentions Apple only twice:
> once to say that it’s “cool” they can demonstrate the problem on
> an Apple computer, and once to say that he and Ellch “talked to
> Apple today.” Even that’s not clear, as we’ll see shortly.


Over the weekend, on the “Dailydave” mailing list, Jon Ellch broke his silence on the saga [and wrote](http://lists.immunitysec.com/pipermail/dailydave/2006-September/003459.html):


> As everyone has noticed by now, we haven’t said anything in public
> about this attack yet. There are two reasons.
> 1) Secureworks absolutely insists on being exceedingly responsible
> and doesn’t want to release any details about anything until Apple
> issues a patch. Whether or not this position was taken after a
> special ops team of lawyers parachuted in out of a black
> helicopter is up for speculation.


It certainly isn’t outlandish to suspect that at some point in this saga Maynor/Ellch/SecureWorks were contacted by Apple Legal. However, if they were, why the elliptical allusions to the threat? If they know about an exploit and can’t say anything about it because they’ve been threatened by Apple Legal, they should at least be able to say “We can’t say anything because Apple has filed an injunction against us.” An injunction prohibiting them from commenting on the exploit wouldn’t disallow them from acknowledging that they’d received such an injunction. Apple Legal can’t simply impose a “You won’t talk about this exploit, nor will you even say that you’re not allowed to talk about this exploit” gag order upon them. Gag orders can only be issued by a court, and they are fairly hard to come by. And when they *are* issued, they apply to both sides, not just one, which, given Apple spokeswoman [Lynn Fox’s statements two weeks ago](http://www.macworld.com/news/2006/08/17/wirelesshack/index.php?pf=1), makes it seem exceedingly unlikely that one has been issued here.


And shouldn’t a security research firm such as SecureWorks be prepared for bullying tactics from vendors?


If it’s true that Maynor/Ellch/SecureWorks are being unfairly bullied by Apple, that’s a shame, and when it comes to light I’ll be as irate as anyone. It certainly wouldn’t be first time I’ve been [critical of Apple’s reaction to security issues](http://daringfireball.net/2004/05/security_cannot_be_spun). As yet, however, we’ve seen no evidence that this is the case.


In the meantime, the questions continue to come faster than the answers. I think we’ll catch up soon, though.


---

1. Even more expensive than the black ones. ↩︎



| **Previous:** | [An Open Challenge to David Maynor and Jon Ellch](https://daringfireball.net/2006/09/open_challenge) |
| **Next:** | [Lies, Damned Lies, and MacBook Wi-Fi Hacks](https://daringfireball.net/2006/09/lies_damned_lies_and_macbook_wifi_hacks) |


PreviousNext