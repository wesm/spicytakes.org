---
title: "Lies, Damned Lies, and MacBook Wi-Fi Hacks"
date: 2006-09-11
url: https://daringfireball.net/2006/09/lies_damned_lies_and_macbook_wifi_hacks
slug: lies_damned_lies_and_macbook_wifi_hacks
word_count: 2279
---


As I expected, my “[MacBook Wi-Fi Hack Challenge](http://daringfireball.net/2006/09/open_challenge)” was not accepted by David Maynor or Jon Ellch. So what have we proven? Nothing about whether or not stock MacBooks are currently vulnerable to a Wi-Fi based exploit, of course — that they didn’t accept the challenge does not mean they haven’t found an exploit that works against the built-in MacBook AirPort card and driver.


Rich Mogull makes several good points in [his criticism of my challenge](http://securosis.com/2006/09/05/mac-wi-fi-gruber-needs-to-let-it-go-and-maynor-and-ellch-should-ignore-the-challenge/), and continues to present the most reasonable and cogent defense of Maynor/Ellch/SecureWorks that I’ve seen — but it mostly seems to boil down to arguing that a stunt like this is not a fair way to conduct a technical argument. *But of course it wasn’t fair — the unfairness was the entire point of the challenge.* I tried the fair and balanced route when I published “[The Curious Case of the Supposed MacBook Wi-Fi Hack](http://daringfireball.net/2006/08/curious_case)”, and in response received no answers.


Sometimes it’s only effective to fight fire with fire, and make no bones about it, Maynor and Ellch’s MacBook exploit demonstration video from the Black Hat conference was a cheap stunt. The cheap counter-stunt of this challenge was clearly far more effective at bringing attention to the problems and unanswered questions raised by their initial presentation and announcement than my exhaustive analysis was.


A few of Mogull’s specific remarks deserve attention or rebuttal. Delineating the reasons why he felt I should have cancelled the challenge, Mogull wrote:


> *I know the demonstration from Black Hat is real.* Why? Aside
> from being at the presentation I had a personal demo (over live
> video) of exactly what they showed in the video. I got to ask
> detailed questions and walk through each step. Maynor and Ellch
> haven’t bullshitted anyone — their demo, as shown in the video
> and discussed in their presentation, is absolutely real. End of
> story.


I’ll admit that I’m still dubious that even their exploit using the third-party wireless card works, in the wild, exactly as shown in the demo video, but my main point all along has been the question of whether they’ve found a similar exploit against a stock MacBook using only the built-in AirPort card and driver. *That’s* my main question, still unanswered over a month later, and was the central premise of my challenge.


> *Using the third-party card for the demo is responsible:* Why?
> Because their goal was to show a class of attack across multiple
> platforms without disclosing an unpatched vulnerability. By
> using an anonymous card no single platform is exposed. Why the
> Mac? Because it demonstrates that a poorly written device driver
> can expose even a secure system to exploit.


I never argued that their using a third-party card for the demo was
irresponsible. It was their use of a MacBook (or as Maynor called
it, “an Apple”) combined with their refusal to state whether they
also found an exploit against the stock AirPort card and driver that
was irresponsible. Before I explain why, I’ll quote Mogull’s next
reason:


> *Responsible disclosure encourages staying silent until a
> patch is released, or an exploit appears.*


If we assume that Maynor and Ellch also discovered an exploit against the built-in MacBook card and driver, then *how was it responsible to perform the demo on a MacBook?* Even though the demo used a third-party card, the hubbub surrounding the initial media coverage of their announcement and presentation centered around the question of whether regular real-world MacBook users were susceptible to a similar attack. Many people drew the conclusion from the initial coverage (and not just Brian “Hijack a MacBook in 60 Seconds or Less” Krebs’s weblog entries) that Maynor and Ellch *had* announced the discovery of an exploit against normal MacBooks, which in turn is why so many people thought — incorrectly — [that Maynor and Ellch had been caught in a lie](http://www.tuaw.com/2006/08/18/secureworks-admits-to-falsifying-macbook-wireless-hack/) when SecureWorks clarified their web site to emphasize that the original demo was against a third-party card and driver.


I.e. if it would be “irresponsible” to announce publicly that they’d found an exploit against the default MacBook card and driver, because such an announcement would clue malfeasants in to the possibility that they could duplicate the exploit before Apple released a software update to fix it, then it was just as irresponsible to publicize their demo using a MacBook in a way that left many (if not most) people with the impression that they *had* found an exploit against built-in MacBook AirPort cards. Even careful, informed observers were left with the conclusion that Maynor and Ellch *might have* found such an exploit. This uncertainty, to me, is far worse than a flat-out statement that they’ve found an exploit against built-in MacBook AirPort cards.


And if they haven’t found a similar exploit against a normal MacBook, then they were even *more* irresponsible, because they left a lot of people — most especially Brian Krebs — with the completely false impression that they did.1


I may or may not yet be proven wrong about what Maynor and Ellch have discovered and reported to Apple, but I see no way that they can come out of this seen as having acted “responsibly”.


> *This challenge doesn’t help anyone. At all.* Is my MacBook
> Pro vulnerable? I don’t know, but even if it is there’s not a
> damn thing I can do about it until Apple issues a patch. It’s
> not like I’m turning off my wireless until I hear there’s some
> well-known exploit floating around. If Maynor and Ellch
> respond to the challenge all they do is satisfy people’s
> curiosity — it does NOTHING to improve security.


Not so. It may be true that Mogull wouldn’t turn off his AirPort card even if he knew it were vulnerable to an exploit like this, but it’s not true that such an announcement wouldn’t help *anyone*. Many MacBook users *would* disable their AirPort cards until Apple had closed such a hole — not just those who are paranoid or overly cautious, but those who have the choice of connecting via Ethernet, but who usually connect via AirPort only because it’s more convenient.


---


Which brings us to William Carrel and the concept of full disclosure. Three years ago, Carrel discovered a [DHCP security vulnerability in Mac OS X 10.2 and 10.3](http://www.carrel.org/dhcp-vuln.html). This was a bad one — an exploit that could give an attacker with access to your network full control of your computer. (I wrote about it, obliquely, in “[Inflammable Means Flammable?](http://daringfireball.net/2003/12/inflammable_means_flammable)”2.)


Carrel initially followed what are generally considered “responsible disclosure” guidelines: he reported the issue to Apple, privately, with all pertinent details.


And then he waited.


After a series of system updates and security updates came and went, none of which addressed this issue, and during which period he warned Apple that he planned to go public if they didn’t soon address it, Carrel released it as a public advisory — an utterly reasonable 48 days after initially reporting the problem to Apple. Twenty-four days later, Apple released a security update with a fix for the issue. This entire timeline is [documented](http://www.carrel.org/dhcp-vuln.html) on Carrel’s web site.


In [this Slashdot thread](http://it.slashdot.org/comments.pl?sid=195733&cid=16040730) regarding Jon Ellch’s public statements last week on the “Dailydave” mailing list, Carrel addressed the speculation that Ellch and Maynor can’t say anything because they’re being bullied by mean, old Apple Legal:


> When I published my OS X remote root (link-local remote root for
> the pedantic), [a poorly chosen use for DHCP](http://www.carrel.org/dhcp-vuln.html), Apple had
> advance notice of when I was going to release it, numerous avenues
> to attempt contact and I didn’t hear one peep from Apple Legal.
> That this guy was suddenly [chilled](http://www.chillingeffects.org/) and can’t produce
> evidence of it other than making vague insinuations just sounds
> [hokey] to me.
> If he doesn’t feel okay about releasing details until they’ve
> patched the driver that’s one thing. But insinuating that the big
> bad lawyers have silenced you is quite another. The only
> circumstance I can think of where they could actually be
> legitimately silenced is: they are/were being paid to do pen
> testing for Apple, they submitted this bug, they blabbed about it
> at a conference when they were under a contractual NDA, they’re
> now claiming they didn’t say enough violate the NDA and are
> remaining mum until the rest of the details go public.
> […]
> This dilemma is more evidence of why [full disclosure](http://en.wikipedia.org/wiki/Full_disclosure_movement)
> is a good idea.


Carrel links “full disclosure” to [Wikipedia’s as-usual bang-up entry](http://en.wikipedia.org/wiki/Full_disclosure_movement) on the subject, where it is defined thusly:


> *Full disclosure* requires that full details of a security
> vulnerability are disclosed to the public, including details of
> the vulnerability and how to detect and exploit it. The theory
> behind *full disclosure* is that releasing vulnerability
> information immediately results in quicker fixes and better
> security. Fixes are produced faster because vendors and authors
> are forced to respond in order to save face. Security is
> improved because the *window of exposure*, the amount of time
> the vulnerability is open to attack, is reduced.


Further in the Slashdot thread, after discussing Ellch and Maynor’s vague and not-so-vague insinuations that their hands have been tied by lawyers, Carrel [concludes](http://it.slashdot.org/comments.pl?sid=195733&cid=16040730):


> And lastly, there is the debatable point on full disclosure.
> Waiting until Apple issues a patch is not exceedingly
> responsible. It is exceedingly *irresponsible*. It leaves
> users hanging in the breeze, potentially vulnerable to a
> remote root for as long as the vendor cares to take to correct
> the issue, which could be several months. For instance, your
> Ford truck may explode, but we’re not going to tell you how or
> why until Ford issues a service bulletin and recall.


The analogy to an exploding truck might only be slightly hyperbolical, depending upon how important the contents of your hard disk are to you. (There are some people who might ask, “How big an explosion are we talking about?” if asked to choose between sitting in an exploding truck and losing the entire contents of their notebook hard drive to a prankster script kiddie in Starbucks.)


There’s a lot of room for argument regarding what constitutes a reasonable and fair “full disclosure” policy. I would say, for example, that full details on how to exploit a newly discovered vulnerability should still be withheld from a public advisory, at least for some fair amount of time. Taken to its extreme, a truly “full” disclosure would constitute a recipe for attack.


But I agree, on the whole, with Carrel (and I think he bent over backwards to be fair to Apple in 2003 with his DHCP discovery). And this isn’t just about Maynor/Ellch/SecureWorks — Apple, too, is still on the hook, because they could easily clear this saga up with a straightforward statement that, yes, they’re currently investigating a threat along these lines — whether it was or was not reported to them by Maynor and Ellch3 — or that no, they are not currently aware of any such vulnerability affecting stock MacBooks.


I’m not going so far as to say that Apple should release a full list of any and all known as-yet-unpatched security problems in Mac OS X (not that I think it would be disastrous, but that’s simply not going to happen — Apple’s management quite obviously wants to remain as secretive as possible with regard to security). But in this case, if the problem is real, their hand has been forced by Maynor and Ellch (and, let’s not forget, Krebs). And if the problem is not real, they still have the problem that a lot of people are under the impression that it is.


In short, that both sides remain mum means that both sides remain, to some degree at least, wrong.


---

1. Mogull also includes this interesting tidbit regarding Krebs’s initial coverage and Maynor’s infamous “makes you want to stab one of those [Mac] users in the eye with a lit cigarette or something” comments:

Maynor already apologized at Defcon, in front of probably a thousand or more attendees, 2 days after Black Hat, that the trash-talking-Mac quote in Krebs’ article was nothing more than joking around off the record, and never meant for publication. Calling these two liars and personally attacking them without validating through anything other than newspaper reports and blog posts isn’t close to fair.

I certainly have significant complaints about Brian Krebs’s coverage of this saga, but my criticism of his coverage has been of a factual nature. I don’t doubt that it was his intention to get this story right — the problem is that he didn’t. What Maynor is alleging here, at least according to Mogull, is far worse, and I don’t believe it. In my experience, newspaper reporters make it very clear when you’re on the record and when you’re being recorded. I find it very hard to believe that Maynor was not aware that these statements were on the record. ↩︎
2. One of my favorite fireball titles ever. ↩︎
3. Apple director of Mac PR [Lynn Fox’s statement](http://www.macworld.com/news/2006/08/17/wirelesshack/index.php?pf=1) last month that SecureWorks had “provided no evidence” of such a flaw involving the built-in MacBook card and driver is not the same thing as saying that Apple was *not aware* of any such flaw. ↩︎



| **Previous:** | [Update on the MacBook Wi-Fi Exploit Challenge](https://daringfireball.net/2006/09/challenge_update) |
| **Next:** | [Buy New iPods From Amazon and Support Daring Fireball](https://daringfireball.net/2006/09/amazon_ipods) |


PreviousNext