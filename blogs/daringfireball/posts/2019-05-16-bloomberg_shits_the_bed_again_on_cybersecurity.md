---
title: "Bloomberg Shits the Bed Again on Cybersecurity"
date: 2019-05-16
url: https://daringfireball.net/2019/05/bloomberg_shits_the_bed_again_on_cybersecurity
slug: bloomberg_shits_the_bed_again_on_cybersecurity
word_count: 1661
---


First things first: earlier this week [WhatsApp announced](https://www.facebook.com/security/advisories/cve-2019-3568) that they had closed a remote code execution vulnerability, affecting all platforms, that attackers could exploit simply by calling a user’s WhatsApp account — *whether the call was answered or not*. (A buffer overflow, no surprise.) They [revealed to The Financial Times](https://www.ft.com/content/4da1117e-756c-11e9-be7d-6d846537acab) that this vulnerability had been exploited, targeting an unknown but presumably small number of users, by software from NSO Group, an Israeli company that sells expensive, exclusive, world-class hacking tools to governments (or at least NSO *claims* only to sell their software to legitimate governments). The FT story is locked behind their paywall (which makes me wonder why WhatsApp went to them with the story), but [TechCrunch has a good summary](https://techcrunch.com/2019/05/13/whatsapp-exploit-let-attackers-install-government-grade-spyware-on-phones/).


Long story short, this was a bad bug that was apparently exploited in the wild. A reasonable point to be taken from this story is that end-to-end encryption is not a panacea. If an attacker manages to install malware on your device, whether via remote exploit or physical access to the device, it’s game over, because they’re now *inside* one of the ends.


It’s like if you have a secure communication line between two rooms, but an attacker gains entry into one of the rooms. The problem is not with the communication line.


“End-to-end encryption is not a panacea” was *not* the lesson taken by Bloomberg columnist Leonid Bershidsky. His take currently runs under the headline “[End-to-End Encryption Isn’t as Safe as You Think](https://www.bloomberg.com/opinion/articles/2019-05-14/whatsapp-hack-shows-end-to-end-encryption-is-pointless)”. When I first saw the story two days ago, though, the headline [was](https://daringfireball.net/misc/2019/05/gimmick.png) “WhatsApp’s End-to-End Encryption Is a Gimmick”.


One of my favorite games to play when trying to see if a headline changed is to [look at the URL slug](https://daringfireball.net/search/url+slug+headline+changed) and the `<title>` tag from the article’s HTML source code. I’ll just repeat myself [from a year ago](https://daringfireball.net/linked/2018/05/02/juiced-headline-of-the-week):


> I point this out from time to time, but the way most websites’
> CMSes work is that an article’s URL slug — like the
> “juiced_headline_of_the_week” segment in this very post’s URL
> — are derived from the article’s original headline. But when a
> headline changes, the URL shouldn’t change unless you have a way
> to redirect traffic going to the old URL to the new one. Most
> websites don’t do that. So when they change a headline, you can
> still tell what the original headline was by looking at the URL
> slug. For some reason, with a lot of news websites, they don’t
> bother updating the headline in the HTML `<title>` element either,
> so you can read the original headline in your browser tab.


The URL slug from Bershidsky’s column: “whatsapp-hack-shows-end-to-end-encryption-is-pointless”.


The `<title>` tag: “WhatsApp Hack Shows End-to-End Encryption Has a Vulnerability”.


These various evolutions on the headline range from bad (“End-to-End Encryption Isn’t as Safe as You Think”) to criminally bad (“WhatsApp Hack Shows End-to-End Encryption Has a Vulnerability / Is Pointless / Is a Gimmick”).


Bloomberg, of all publications, should be on its tip-toes to make sure it gets anything related to cybersecurity *exactly right* — every *i* dotted, every *t* crossed. Their reputation is in tatters in the wake of last year’s [“The Big Hack” debacle](https://daringfireball.net/search/bloomberg+big+hack) — a story which they *still* haven’t retracted (or shown to be true with any actual evidence).1


Instead, they’re publishing this nonsense from Bershidsky:


> The tug of war between tech firms touting end-to-end encryption as
> a way to avoid government snooping and state agencies protesting
> its use is a smokescreen. Government and private hackers are
> working feverishly on new methods to deploy malware with operating
> system-wide privileges.


It’s no smokescreen. Bershidsky’s profound mistake is his apparent belief that security is binary — totally secure or totally insecure. And so in his mind, this week’s WhatsApp exploit means WhatsApp is insecure, and since other such exploitable bugs almost surely exist in other apps and in OSes, no messaging system is secure.


Security is not binary, though — which is obvious if you give it even a moment’s thought. A locked door is more secure than an unlocked one. A door with two locks is more secure than one with a single lock. A locked door with a locked gate in front of it is more secure than one without a gate.


*Security exists on a continuum*. The definition of *continuum* is instructive: “a continuous sequence in which adjacent elements are not perceptibly different from each other, although the extremes are quite distinct”. It’s not secure or insecure; it’s more secure or less secure. Just like faster vs. slower or heavier vs. lighter. There are first grade primers that cover these concepts.


In the same way a door is more secure locked than unlocked, messaging of any sort is more secure encrypted than unencrypted. End-to-end encrypted messaging is more secure than encryption that is not end-to-end — it truly is an essential distinction.2 Just because the government or a criminal *might* be able to exploit software on your device even if the communications were E2E encrypted doesn’t make E2E encryption a “smokescreen”. Especially in the case of law enforcement — it is orders of magnitude easier to issue a subpoena to, say, your email provider than it is to attack your devices with malware to obtain the information they seek.


This week’s WhatsApp exploit was the work of some of the most talented hackers in the world. Calling them geniuses is no hyperbole. Finding vulnerabilities that allow remote code execution is (usually) extremely difficult. Actually *writing* the code to take advantage of them — turning a theoretical vulnerability into a working and deployable exploit — requires some of the best programming talent in the world. And on the other side, the security teams at goliath companies3 like Microsoft, Amazon, Apple, Google, and Facebook employ equally talented programmers trying to close all possible vulnerabilities.4 It’s a cat-and-mouse game at the very highest level of programming and mathematical talent.


Obtaining a subpoena requires nothing of the sort — simply the regular mechanics of law enforcement, judicial oversight, and compliance with the law. Snooping on unencrypted network traffic is similarly trivial. Obtaining email via subpoena requires you to be able to make a free throw; doing what this week’s WhatsApp exploit seemingly accomplished requires you to be Steph Curry and hit 9 three-pointers in a single game against a playoff-caliber NBA defense.


Here’s Bershidsky’s closing:


> The hard truth for activists and journalists in need of secure
> messaging is that the more tech-savvy they are, the safer they can
> make their digital communications. One can, for example, encrypt
> messages on a non-networked device before sending them out through
> one’s phone. But even that wouldn’t guarantee complete security
> since responses could be screen-captured.
> Truly secure communication is really only possible in the analog
> world — and then all the old-school spycraft applies.


In other words, digital communication can never be completely secure, only analog can, except when that’s compromised by “old-school spycraft”. *Complete guaranteed security with well-known exceptions.* It boggles the mind that this was written and edited by sentient humans, and that they’ve spent two days slowly decreasing the asininity of the headline instead of just doing what obviously ought to be done and retracting the whole piece.


---

1. Since “The Big Hack” was published in early October last year, [Robertson’s byline has appeared at Bloomberg zero times](https://www.bloomberg.com/authors/AQrv1y2ieI0/jordan-robertson), and [Riley’s only once](https://www.bloomberg.com/authors/AP2Byct9nRE/michael-riley), which might lead one to believe that despite Bloomberg’s public defense of the piece, internally they suspect something is amiss with the duo’s work. But Bloomberg not only still stands by the story, according to Washington Post media critic Erik Wemple, [Bloomberg had the chutzpah to submit “The Big Hack” to the 2019 National Magazine Awards](https://www.washingtonpost.com/opinions/2019/04/05/bloomberg-submitted-big-hack-story-award/). ↩︎
2. I *think* the whole point of Bershidsky’s tirade is not that encryption of any kind is pointless (but some [clearly took it that way](https://twitter.com/Bershidsky/status/1128445561496010754)), but rather that he thinks companies are emphasizing *end-to-end* encryption in particular as a sort of snake oil, a fool-proof impregnable security solution. It’s hard to make sense from nonsense. Anyway, the distinction between E2E and non-E2E encryption is worth a footnote.
With E2E encryption, a message is encrypted on the sender’s device and is not decrypted until it reaches the recipient’s device. WhatsApp, Signal, and iMessage work this way. With non-E2E encryption, the message is encrypted on the sender’s device, decrypted by a server in the middle, then re-encrypted on the server and sent to the recipient. So with non-E2E encryption, an attacker still can’t get the unencrypted message by simply snooping on the network traffic, but they can get it by attacking — or in the case of law enforcement, simply issuing a subpoena to — the service provider. Email and Twitter DMs work this way — your email provider stores the plain text of all your email, and Twitter stores the plain text of your DMs — even though your devices communicate to your email provider (almost certainly) and Twitter (definitely) over encrypted connections. Removing that middleman as a target of attack or subpoena is what makes E2E encryption important.
But it’s also the reason why you can read email and Twitter DMs on the web, and can’t read your WhatsApp/Signal/iMessage messages on the web. E2E necessitates a trade-off in convenience for additional security. And it’s undeniably convenient to be able to access email and Twitter via the web — essential, even, for millions of users. Trade-offs are always difficult. ↩︎︎
3. Listed here by order of market capitalization today. ↩︎︎
4. No slight intended to upstart Signal, which also has [world-class talent](https://www.wired.com/2016/07/meet-moxie-marlinspike-anarchist-bringing-encryption-us/) ([and serious funding — from the co-founder of WhatsApp](https://signal.org/blog/signal-foundation/)) securing it against exploits. ↩︎︎



| **Previous:** | [All Podcasts Are Shows; Not All Shows Are Podcasts](https://daringfireball.net/2019/04/not_all_shows_are_podcasts) |
| **Next:** | [Some Good Old-Fashioned Speed Bumps for the MacBook Pro Lineup, and a Tweak to the Butterfly Key Mechanism](https://daringfireball.net/2019/05/good_old_fashioned_macbook_pro_speed_bumps) |


PreviousNext