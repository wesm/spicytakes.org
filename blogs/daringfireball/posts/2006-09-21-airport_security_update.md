---
title: "The AirPort Security Update and the Supposed MacBook Wi-Fi Hack"
date: 2006-09-21
url: https://daringfireball.net/2006/09/airport_security_update
slug: airport_security_update
word_count: 1605
---


Today’s [AirPort security updates](http://docs.info.apple.com/article.html?artnum=304420) from Apple put August’s “MacBook Wi-Fi Hack” saga back in play.


The first issue, CVE-2006-3507, “affects Power Mac, PowerBook, iMac, Mac Pro, Xserve, and PowerPC-based Mac mini computers equipped with wireless. Intel-based Mac mini, MacBook, and MacBook Pro computers are not affected.” I believe this corresponds to the Macs with AirPort cards with Broadcom chipsets.


The second issue, CVE-2006-3508, “affects Intel-based Mac mini, MacBook, and MacBook Pro computers equipped with wireless. Power Mac, PowerBook, iMac, Mac Pro, Xserve, and PowerPC-based Mac mini computers are not affected.” This list of affected computers corresponds to those whose AirPort cards are based on Atheros chipsets.


Under all normal circumstances, Mac users don’t have to worry about these AirPort chipset differences — from a user’s perspective, AirPort is AirPort, and the UI for turning it on and off and configuring it is the same regardless of which chipset constitutes the guts of your machine’s AirPort card. However, because these are entirely different chipsets, they require separate low-level driver software. Hence the two separate patches.


Apple’s description of the first one, CVE-2006-3507:


> Two separate stack buffer overflows exist in the AirPort wireless
> driver’s handling of malformed frames. An attacker in local
> proximity may be able to trigger an overflow by injecting a
> maliciously-crafted frame into a wireless network. When the
> AirPort is on, this could lead to arbitrary code execution with
> system privileges


Apple’s description of the second, CVE-2006-3508:


> A heap buffer overflow exists in the AirPort wireless driver’s
> handling of scan cache updates. An attacker in local proximity may
> be able to trigger the overflow by injecting a maliciously-crafted
> frame into the wireless network. This could lead to a system
> crash, privilege elevation, or arbitrary code execution with
> system privileges.


I am by no means at all a device driver programmer, but my reading of these descriptions is that the two patches are not quite the same — [the stack and the heap are different things](http://www-ee.eng.hawaii.edu/Courses/EE150/Book/chap14/subsection2.1.1.8.html), for one thing — but in broad terms they address similar problems involving “malformed” or “maliciously-crafted” Wi-Fi “frames”.


The third issue, CVE-2006-3509, also deals with “maliciously-crafted” frames, this time leading to an integer overflow error, but rather than being in a specific driver, is in the AirPort API for *third-party* wireless software. It only affects the MacBook, MacBook Pro, and Intel-based Mac Mini.


All three descriptions include the following statements:

- “There is no known exploit for this issue.”
- “This update addresses the issue(s) by performing additional validation of wireless frames.”


Apple further states that there are no known applications affected by the third issue.


“No known exploit” does not just mean that there aren’t any attacks in the wild; it means *no one* has demonstrated to Apple a way to take advantage of these frame validation issues. They fixed them to eliminate *potential* exploits, not to address *actual, known* exploits.


## Regarding David Maynor and Jon Ellch


If last month’s “Hijack a MacBook in 60 Seconds or Less” saga had not occurred, this would not be a particularly noteworthy security update. But that saga *did* occur, and so the update is noteworthy. Apple went on the offensive, issuing statements to the press explicitly stating that these fixes were not addressing any specific vulnerabilities reported by David Maynor, Jon Ellch, or SecureWorks.


[Apple spokesman Anuj Nayar told Macworld’s Jim Dalrymple](http://www.macworld.com/news/2006/09/21/wireless/index.php?pf=1):


> “[SecureWorks] did not supply us with any information to allow
> us to identify a specific problem, so we initiated an internal
> audit. Today’s update preemptively strengthens our drivers
> against potential vulnerabilities, and while it addresses
> issues found internally by Apple, we are open to hearing from
> security researchers on how to improve security on the Mac.”


My translation of “we are open to hearing from security researchers on how to improve the security” is “We’re not in the business of besmirching the reputations of security researchers who report problems in Mac OS X, but we are not going to sit back and take it when someone grossly exaggerates or lies about a threat.”


Nayar [told the Washington Post’s Brian Krebs](http://blog.washingtonpost.com/securityfix/2006/09/apple_issues_patches_for_macbo.html) (Krebs, of course, being responsible for the [original media frenzy](http://blog.washingtonpost.com/securityfix/2006/08/hijacking_a_macbook_in_60_seco.html)):


> “Basically, what happened is SecureWorks approached Apple with a
> potential flaw that they felt would affect the wireless drivers on
> Macs, but they didn’t supply us with any information to allow us
> to identify a specific problem. So we initiated our own internal
> product audit, and in the course of doing so found these flaws.”


If the extent of Maynor and Ellch’s original claim had been something along the lines of “*We have not yet found any actual exploit against Apple’s AirPort drivers, but believe that there might exist such exploits because these drivers aren’t guarding against malformed frames*,” they could certainly take some pride for having instigated Apple’s audit that turned up these flaws.


But that is not what Maynor and Ellch claimed. Their video demonstration against a third-party (i.e. not from Apple) USB Wi-FI card showed an attacker gaining a remote shell on the attacked machine, and their statements indicated [that they had discovered similar vulnerabilities against Apple’s built-in drivers](http://blog.washingtonpost.com/securityfix/2006/08/followup_to_macbook_post.html). Krebs today reiterated his claim that Maynor demonstrated to him, privately, an exploit against a MacBook using the built-in AirPort card:


> I first wrote about this issue at the Black Hat hacker
> conference in Las Vegas roughly two months ago, where I
> witnessed security researcher David Maynor compromising a
> Macbook from a Windows machine remotely using what he said
> were flaws in the built-in wireless drivers.
> The videotaped demo produced by Maynor and colleague John Ellch
> shown to Black Hat attendees deliberately used a third-party USB
> wireless card plugged into a Macbook. To demonstrate the exploit
> with the Apple wireless drivers before giving the company time to
> inspect and fix them, they argued, would be irresponsible.


According to Apple, Maynor and Ellch never showed them any such exploit, and Apple remains unaware of any such exploits. Maynor and Ellch were, it appears, correct that there were flaws in the AirPort drivers’ handling of malformed frames, but one of the following must be true:

- Maynor and Ellch did *not* find an actual exploit against Apple’s
built-in AirPort drivers, but bamboozled and lied to Brian Krebs
(and let’s not forget [George Ou](http://blogs.zdnet.com/Ou/?p=300)) that they had.
- Maynor and Ellch *did* find such an exploit, but never showed
or proved it to Apple.
- Maynor and Ellch both found such an exploit *and* showed it to
Apple, and Apple continues to lie about what Maynor and Ellch
showed them.


---


Here’s a loose analogy. Imagine Apple’s AirPort code as an office building, where, previously, it was assumed that intruders (malicious Wi-Fi frames) could not get past the front doors, and that everyone who was inside the building was a legitimate employee (a legitimate Wi-Fi frame) and was free to do what they wanted. So, now (i.e. after the security update), after anyone enters the building, their identification is validated (“additional validation of wireless frames”).


By this analogy, Maynor and Ellch’s demonstration video was the equivalent of an intruder entering the building, walking into the executive suite, and taking a dump on the CEO’s desk. But according to Apple, Maynor and Ellch never demonstrated that they could get through the front door — they merely offered the suggestion that Apple should validate Wi-Fi frames as a precaution.


So Krebs is wrong when he [wrote today](http://blog.washingtonpost.com/securityfix/2006/09/apple_issues_patches_for_macbo.html):


> But one thing now appears quite clear: The built-in wireless
> device drivers are indeed vulnerable to exploitation in a manner
> very similar to what Ellch and Maynor detailed in their
> presentation.


Because that’s not clear at all — Apple’s AirPort code is now performing additional validation to guard against such an attack, but there remains no proof that such an attack exists (or existed, before the security update was released). What’s clear is that Apple found ways that they *might* have been vulnerable.


As I concluded in “[The Curious Case of the Supposed MacBook Wi-Fi Hack](http://daringfireball.net/2006/08/curious_case)”:


> It is a simple yes or no question: Have Maynor and Ellch found a
> vulnerability that affects MacBooks using Apple’s built-in cards
> and drivers? That Maynor and Ellch haven’t answered it speaks
> volumes.


Apple, today, offered their answer: Yes, there were AirPort flaws to be fixed, but no, they were neither discovered nor exploited by Maynor and Ellch.


The only way Maynor and Ellch have any credibility remaining is if Apple is flat-out lying. And if that’s the case Maynor and Ellch can simply step forward and prove it. At the conclusion of his coverage of today’s security update, [Glenn Fleishman writes](http://wifinetnews.com/archives/006983.html):


> The next step here, if Maynor and Ellch are still maintaining that
> they had discovered a vulnerability as related by Brian Krebs’s
> reporting on it, is for the two researchers or SecureWorks to
> release everything they have on this to show that Apple is being
> disingenuous. Because SecureWorks is now off the hook, right? I
> don’t think there’s a chance that we’ll see that happen.
> Were Apple to be lying about any of this isn’t credible; that’s a
> huge risk for a multi-billion-dollar public company to take. I
> believe this might be the last we hear about this.


Let’s hope.



| **Previous:** | [Regarding the Features and Capabilities of the Various Fifth Generation iPods](https://daringfireball.net/2006/09/fifth_generation_ipod_features) |
| **Next:** | [Jackass of the Week: Kieren McCarthy](https://daringfireball.net/2006/09/jackass_kieren_mccarthy) |


PreviousNext