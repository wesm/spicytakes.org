---
title: "The Curious Case of the Supposed MacBook Wi-Fi Hack"
date: 2006-08-21
url: https://daringfireball.net/2006/08/curious_case
slug: curious_case
word_count: 6490
---


So remember a few weeks ago when Brian Krebs posted a report titled “[Hijacking a MacBook in 60 Seconds or Less](http://blog.washingtonpost.com/securityfix/2006/08/hijacking_a_macbook_in_60_seco.html)” on his Washington Post computer security weblog? He reported on a supposed Wi-Fi security exploit demonstrated at the Black Hat security conference, wherein “security researchers” Jon Ellch and David Maynor hacked into a MacBook via Wi-Fi.


Krebs’s shoddy reporting left several essential questions unanswered, [which I raised on August 3](http://daringfireball.net/2006/08/krebs_followup). Namely:

- Maynor and Ellch’s demonstration video showed the MacBook —
the target of their “attack” — using a USB-dongle Wi-Fi card.
Given that every MacBook comes with a built-in AirPort Wi-Fi
card, the central question of this entire saga is whether that
built-in AirPort card is similarly vulnerable.
- Krebs reported that they used a third-party card and driver in
their demonstration because “Apple had leaned on Maynor and
Ellch pretty hard not to make this an issue about the Mac
drivers”. Who at Apple “leaned on” them? And what does “leaned
on” them actually mean?


Before proceeding, it’s worth clarifying a few terms here: *card*, *driver*, and *third-party*.


A *card* is the wireless networking hardware; e.g. the AirPort card built into every Apple notebook, or the external USB dongle Maynor plugged into the MacBook in his demo.


A *driver* is software that allows an operating system to communicate with a piece of hardware. Modern operating systems — Mac OS X, Windows, and Linux distributions — all ship with standard drivers for all sorts of hardware. For any hardware that your operating system does not already have a driver for, however, you need to install a driver before the hardware will work. For example, Mac OS X ships with a USB mouse driver that “just works” with any standard USB mouse that you plug in, but Apple updated this driver when they shipped the Mighty Mouse to add support for its specific features. AirPort “just works” because Mac OS X ships with drivers for all of the various AirPort cards that Apple has ever shipped. When Mac users connect to a Wi-Fi network, they normally do so using the built-in AirPort card and the built-in AirPort driver, where by “normally” I mean “almost always”.


*Third-party* refers to a component — hardware or software — that is not produced or officially supported by your computer manufacturer or operating system supplier. In the case of the MacBook, a third-party card would be any Wi-Fi card other than the one pre-installed inside the machine by Apple. A third-party driver would be any software used to control a Wi-Fi card other than the drivers installed as part of Mac OS X. You might think this is a silly thing to clarify, but Krebs himself is creating confusion with his use of the term, on the grounds that some of the code in the drivers that Apple ships with Mac OS X are written by programmers at the companies that make the Wi-Fi chipsets used in Apple’s AirPort-brand cards. Do not be confused: if the driver is supplied by Apple and supported by Apple, it is not “third-party software”.


The central point here is that for this particular exploit to be of any concern whatsoever to MacBook users, it would have to work against the MacBook’s built-in card using Mac OS X’s built-in driver. Using a third-party card — as Maynor clearly and admittedly did in their video demonstration — makes the issue moot to any Mac user using the built-in card. But the same goes for the *driver* — if Maynor and Ellch can demonstrate an attack that works against the MacBook’s built-in card, but which requires a third-party software driver, that’s equally moot.


## What We Know


SecureWorks (slogan: “The Information Security Experts”) is the security group where Maynor is employed as a researcher. As of Thursday, their [web page devoted to this vulnerability](http://secureworks.com/newsandevents/blackhatcoverage.html) contained the following disclaimer (emphasis added):


> This video presentation at Black Hat demonstrates vulnerabilities
> found in wireless device drivers. Although an Apple MacBook was
> used as the demo platform, **it was exploited through a third-party
> wireless device driver** — not the original wireless device driver
> that ships with the MacBook. As part of a responsible disclosure
> policy, we are not disclosing the name of the third-party wireless
> device driver until a patch is available.


What’s notable about this disclosure is that it is about the *driver*. We already know, just from watching the demonstration video, that it was also based on a third-party *card*. This means that either (a) the exploit they discovered uses neither the MacBook’s built-in card *nor* Mac OS X’s built-in driver; (b) the exploit they discovered works against both the third-party driver demonstrated in the video *and* against Apple’s standard driver, and they have inexplicably decided to post this disclaimer to explicitly describe only what is being demonstrated *in the video*; or (c) that the “experts” at SecureWorks do not understand the difference between a driver and a card. My money is on (a).


The reason this is notable is that if (a) is true (that the vulnerability they discovered does not apply to the standard AirPort driver software from Apple) it entirely contradicts Brian Krebs’s original and much-publicized story. [Krebs wrote](http://blog.washingtonpost.com/securityfix/2006/08/hijacking_a_macbook_in_60_seco.html) (emphasis added):


> The video shows Ellch and Maynor targeting a specific security
> flaw in the Macbook’s [*sic*] wireless “device driver,” the
> software that allows the internal wireless card to communicate
> with the underlying OS X operating system. **While those
> device driver flaws are particular to the MacBook** — and
> presently not publicly disclosed — Maynor said the two have
> found at least two similar flaws in device drivers for
> wireless cards either designed for or embedded in machines
> running the Windows OS. Still, the presenters said they
> ultimately decided to run the demo against a Mac due to what
> Maynor called the “Mac user base aura of smugness on security.”


In response to SecureWorks’s admission that their demonstration did not exploit the built-in driver, Apple on Friday released a statement regarding the supposed vulnerability. Lynn Fox, Apple’s director of Mac PR, [told Macworld](http://www.macworld.com/news/2006/08/17/wirelesshack/index.php?pf=1):


> “Despite SecureWorks being quoted saying the Mac is threatened
> by the exploit demonstrated at Black Hat, they have provided
> no evidence that in fact it is. To the contrary, the
> SecureWorks demonstration used a third party USB 802.11
> device — not the 802.11 hardware in the Mac — a device which
> uses a different chip and different software drivers than
> those on the Mac. Further, SecureWorks has not shared or
> demonstrated any code in relation to the Black
> Hat-demonstrated exploit that is relevant to the hardware and
> software that we ship.”


Fox’s statement on behalf of Apple is unequivocal: Maynor and Ellch’s exploit involves neither the MacBook’s standard Wi-Fi hardware card or software driver. That, of course, does not mean that Apple’s standard driver isn’t somehow similarly vulnerable, but if it is, Maynor and Ellch *have not demonstrated such a vulnerability to Apple*, according to Fox.


Further, Bill McFarland, the chief technical office of Atheros Communications, the company that produces the built-in AirPort chipsets Apple includes in every MacBook, sent [the following message to Brian Krebs via email](http://blog.washingtonpost.com/securityfix/2006/08/update_on_the_apple_macbook_cl.html):


> Atheros has not been contacted by SecureWorks and Atheros has
> not received any code or other proof demonstrating a security
> vulnerability in our chips or wireless drivers used in any
> laptop computers. We believe SecureWorks’ modified statement
> and the flaws revealed in its presentation and methodology
> demonstrates only a security vulnerability in the wireless USB
> adapter they used in the demo, not in the laptop’s internal
> Wi-Fi card.


Again, this statement is unequivocal. The chief technical officer of the company that makes the MacBook AirPort cards — and, I believe, that writes at least some of the source code for the drivers that Apple uses — says that Maynor and Ellch haven’t even contacted them, let alone disclosed any actual flaws in their card or driver.


But back on August 3, in a follow-up to his original “Hijacking a MacBook in 60 Seconds or Less”, [Krebs wrote](http://blog.washingtonpost.com/securityfix/2006/08/followup_to_macbook_post.html):


> During the course of our interview, it came out that Apple had
> leaned on Maynor and Ellch pretty hard not to make this an
> issue about the Mac drivers — mainly because Apple had not
> fixed the problem yet. Maynor acknowledged that he used a
> third-party wireless card in the demo so as not to draw
> attention to the flaw resident in Macbook drivers. But he also
> admitted that the same flaws were resident in the default
> Macbook wireless device drivers, and that those drivers were
> identically exploitable. And that is what I reported.
> I stand by my own reporting, as according to Maynor and Ellch
> it remains a fact that the default Macbook drivers are indeed
> exploitable.


So at the beginning of August, Maynor and Ellch told Krebs that the default MacBook drivers were exploitable, but would not, even on video, demonstrate an exploit against them publicly. As of last Thursday, however, their SecureWorks web site explicitly states that their video demonstration does *not* involve Apple’s default drivers, and both Apple and Atheros issued unequivocal statements that Maynor and Ellch have not provided Apple with any evidence showing a flaw in Apple’s drivers.


## The Central, as Yet Unanswered Question


This entire saga boils down to one simple question: Have Maynor and Ellch discovered a vulnerability against MacBooks using Apple’s built-in AirPort cards and drivers?


Given all the facts laid out in the previous section, you might at first think this question *has* been answered, and that the answer is “no”, but unless I’m missing something, this is, inexplicably, still an open question.


Maynor and Ellch’s recent statement on the SecureWorks web site declares that their *video demonstration* does not involve Apple’s driver; that is not the same thing as declaring that they have not *also* identified an exploit against Apple’s driver which is not demonstrated in the video. They have been conspicuously silent on this specific point, other than Maynor’s statement to Krebs earlier this month that Apple’s drivers are “identically exploitable” (which are Krebs’s words, not a direct quote from Maynor).


We do have enough facts, however, to know with certainty that some of our protagonists will not emerge with their reputations intact. Someone, clearly, is either lying or incompetent (or both).


For example, from Apple’s statement on Friday, we know that if Maynor and Ellch *have* identified an exploit against a stock MacBook, that they have not yet contacted Apple (or Atheros) with details about the vulnerability — which is both enormously irresponsible for ostensibly professional security researchers, and which contradicts statements they previously made to Brian Krebs that they *had* been in contact with Apple regarding their discoveries. Or, if they *have* contacted Apple, the statement issued by Apple’s Lynn Fox is flat-out false and Apple has committed an enormous, almost incomprehensibly foolish mistake, because such a mendacious lie will prove far worse for Apple than divulging a Wi-Fi exploit that, *if it actually exists*, is surely going to come to light soon anyway. I.e. why would Apple lie about this if Maynor could call them on it?


On the other hand, if Maynor and Ellch have *not* identified an exploit that works against Apple’s standard MacBook card and driver, then the only possible explanation for what Brian Krebs has reported — that Maynor told him that the default MacBook drivers are “identically exploitable” to those used in their video — is that either (a) Maynor and Ellch are liars and frauds; (b) Brian Krebs is an incompetent hack who grossly and utterly misquoted and misstated what Maynor had told him; or (c) Krebs was in over his head and did not understand the issues he was reporting on.


(A) seems the most likely explanation here; if (b) or (c) were the case — i.e. that Maynor had *not* told Krebs that the MacBook’s default driver was identically or even similarly vulnerable, surely Maynor would have spoken out to set the record straight and call Krebs out on his error — a simple “Hey, I didn’t say what Brian Krebs has reported that I said” would have sufficed. That hasn’t happened.


I thus see no way out of this where Maynor and Ellch escape with their reputations intact, other than if they have in fact discovered a vulnerability against the stock MacBook card and driver, that they have disclosed their findings privately to Apple, and that the statement issued Friday by Apple’s Lynn Fox is in fact scurrilously false. But even in this scenario — which as I see it is the best case for Maynor and Ellch — if they know for certain that MacBooks, as shipped by Apple, are vulnerable, *why have they not plainly said so*? I’m not saying they should have publicly described the nature of the vulnerability in any detail, but they certainly should have stated clearly that owners of whatever specific Macintoshes they have identified flaws against should be careful when turning on AirPort in any public or non-trusted environment.


In short, either Maynor and Ellch have discovered an exploit against a stock MacBook and Apple has decided, incomprehensibly, to scurrilously besmirch their reputations with flat-out lies that will soon be disproved and will bring disgrace to Apple Computer, or, Maynor and Ellch have not discovered such an exploit and they are, at best, gross exaggerators, or, at worst (and more likely in my opinion), outright frauds.


## Brian Krebs Has ‘Dugg’ Himself a Mighty Deep Hole


The Washington Post’s Brian Krebs seems to have painted himself into a particularly uncomfortable corner. It was Krebs who broke the original story, and it was Krebs who gave it the made-for-Digg headline “Hijacking a MacBook in 60 Seconds or Less”. It was Krebs who then wrote, [in a follow-up](http://blog.washingtonpost.com/securityfix/2006/08/followup_to_macbook_post.html):


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


It is becoming more and more clear that the reporting Krebs “stands
by” is false. Maynor and Ellch, I believe, have discovered no such exploit against a stock MacBook. And if I’m right, not only has Krebs blown the story with regard to the security of the MacBook, he has also impugned the integrity of Apple by publishing the claim that the company “leaned on” Maynor and Ellch — an accusation Krebs published without evidence, without details regarding what exactly constituted “leaning on”, and without comment from Apple.


Last week, on Tuesday August 15, Krebs published a third weblog entry on the topic, in which he began:


> I’ve received an overwhelming amount of hate mail from Mac
> enthusiasts over two previous posts on a wireless-device-driver
> presentation at the Black Hat hacker conference, with people
> accusing me of all kinds of nasty things.


Where by “hate mail” Krebs apparently means “criticism”, and where by “nasty things” he apparently means “shitty reporting”. This is one of the oldest tricks in the hack tech writer book: Because, yes, some small number of devoted Mac users are in fact kooks, when you begin receiving criticism after publishing some sort of false or inaccurate analysis regarding the Mac or Apple, you just dismiss it all on the grounds that *all* Mac users are irrational cultists who simply can’t stand to see their beloved company or OS criticized.


Krebs continues:


> I’ve been asked this many times, so let me make this crystal
> clear: I had the opportunity to see a live version of the demo
> Maynor gave to a public audience the next day. In the video shown
> at Black Hat, he plugged a third-party USB wireless card into the
> Macbook — but in the demo Maynor showed me personally, he
> exploited the Macbook without any third-party wireless card
> plugged in.


And then he follows this undeniably bold claim with a transcript of a taped interview he conducted with Maynor, while Maynor performed this demonstration using the built-in AirPort card.


Krebs did not ask several very obvious questions regarding this demonstration. For example: Had Maynor diddled at all with the wireless drivers on the MacBook to make this work? Had he diddled with the default network settings? Could Maynor demonstrate this exploit on a MacBook supplied by Krebs?


Not asking these questions indicates that Krebs is incompetent to write about computer security issues. It’s like watching a magician perform a trick using his own deck of cards, and then not only not asking to see the trick performed with a deck of cards as-yet untouched by the magician, but not even asking whether the cards had been tampered with.


The most interesting part of the transcript is this exchange (emphasis mine):


> Krebs: Explain to me exactly what you’re exploiting in here. Is it
> a flaw in the Macbook itself?
> Maynor: Yes, it’s a device driver. **The thing is, there’s a flaw in
> the OS**, but I don’t want to specifically point to it, so in the
> video you’ll see I used a third-party USB device. What I’m trying
> to do is highlight the problems in device drivers themselves, not
> any one particular flaw. [Maynor misspoke here, and I later
> clarified this point with him. The wireless device driver that
> powers the internal wireless card on the Macbook contains flaws
> that — when exploited — give the attacker the ability to create
> or delete files, or modify system settings. The flaw is in fact in
> the Macbook’s wireless device driver, which is made by a third
> party. So again, to be clear, the flaw is not, as he suggests in
> the transcript of this interview, in the Mac OS X operating system
> itself.]


The bracketed section is an editorial aside from Krebs, who seems deeply confused as to what constitutes “third-party” drivers. Even if portions or the entirety of the MacBook’s AirPort driver are written by engineers at a company other than Apple (like, say, Atheros, the producers of the chipset), if it’s the software that drives the built-in card, and it is installed as a standard component in Mac OS X, and Apple is the company that offers support for the driver — then it is not third-party software. The built-in AirPort drivers are part of Mac OS X.1


Curiously, at the end of this transcript, Krebs provides a link to a [PowerPoint file created by Maynor and Ellch](http://blog.washingtonpost.com/securityfix/response.ppt), containing “slides responding to some of the questions they’d heard from Mac users,” which they apparently presented at DefCon, their second appearance to give this talk.


There are only six slides in the file, the last of which reads:


> [Q:] I saw some people quote you as saying the bug is in the
> built-in in card and other people quote you as saying as its
> [*sic*] not, who is right?
> [A:] They both are. The exploit shown in the video was
> targeting a specific third party driver and that same
> vulnerability does not affect the built in [*sic*] card. We
> are, however, doing ongoing research on the built-in card as
> well and have shared our findings with Apple.


So “both” are right, but they haven’t found an exploit against the
Apple card and driver — just “ongoing research”? Tell me that doesn’t sound like, “We’re trying to find an exploit that works against the MacBook’s built-in driver and card, but haven’t found one yet.”


Krebs goes further off the rails in the comment thread attached to this article. After Macworld published Lynn Fox’s statement on behalf of Apple, a reader named James Bailey called it out in the comments, asking Krebs to justify the discrepancy between what he had reported — that Maynor and Ellch had discovered a vulnerability in Apple’s products and reported it to Apple (and had in turn been “leaned on” to keep quiet about it) — and Apple’s unequivocal statement they hadn’t seen or heard squat from Maynor and Ellch regarding an exploit against the MacBook.


[Krebs responded](http://blog.washingtonpost.com/securityfix/2006/08/the_macbook_wireless_exploit_i.html) (Krebs’s weblog does not offer per-comment permalinks, alas):


> James — and you think that Macworld articles adds anything to
> this because why? You should spend a little bit of time looking at
> what Apple is actually claiming, and what they’re not talking
> about here. Apple’s PR people are basically pointing out exactly
> what I’ve said for the past two posts on this issue — that Maynor
> et. al indeed used a third-party USB card in the video.


What Krebs is doing here is accusing Apple spokesperson Lynn Fox of speaking in precise “it depends what the meaning of the word ‘is’ is”-style legalese. But Fox’s statement did not end with her reiteration of the fact that their video demonstration involved a third-party card (which is a fact that is not disputed by anyone who has watched the video — Maynor makes it explicitly clear in the demonstration video that he’s using a USB wireless card). Fox continued by adding: “Further, SecureWorks has not shared or demonstrated any code in relation to the Black Hat-demonstrated exploit that is relevant to the hardware and software that we ship.” *That’s* the part of Apple’s statement that contradicts Krebs’s reporting.


Krebs continues:


> SecureWorks is claiming that despite Apple’s claims to the
> contrary, that the company is shipping Mac products with
> vulnerable wireless device drivers. What Apple has not addressed
> in any kind of detail is whether or not the embedded drivers in
> the Macbook are vulnerable. All of their response so far is aimed
> at the demo showed in the video publicly.


*Not true.* The second part of Fox’s statement is that Maynor and Ellch “have not shared or demonstrated any code” with Apple related to this supposed exploit.


As for why Apple has not addressed “whether or not the embedded drivers in
the Macbook are vulnerable” — it’s because *they don’t know*, because, and I’ll repeat this again, one last time, Apple says *Maynor and Ellch haven’t shared a demonstration or code with them*. If there is a vulnerability, Apple can’t confirm it because Maynor and Ellch haven’t shared it with them. If there is *not* a vulnerability, Apple can’t know for certain that this is the case — for all Apple knows, Maynor and Ellch *have* identified an exploit against the MacBook’s built-in driver and card, but have, for whatever reason, not yet come forward with it. And since they don’t know, they can’t say, “There is no vulnerability in our product”. What they do know is what they *did* say: that they haven’t seen code or a demo from Maynor and Ellch.


That this sort of basic middle-school-level logic should need to be painstakingly spelled out for the computer security columnist for the Washington Post is astounding.


Finally, on Friday, 16 days after his original post, the cracks began to show in Krebs’s “I stand by my own reporting” facade. He published this fourth post on the topic, headlined “[Follow-Up to the Macbook [*sic*] Post](http://blog.washingtonpost.com/securityfix/2006/08/update_on_the_apple_macbook_cl.html)”.2


After publishing the statement from Lynn Fox which he had callously dismissed as little more than devilish PR corporate ass-covering double-speak the day before, Krebs wrote:


> I have several times now asked SecureWorks to share with me more
> specific information to back up their claims, but so far I have
> received no further details. If I hear back from SecureWorks
> with any more material information, I will update the blog.


Translation: “I no longer stand by my own reporting.”


Alternative translation: “Oh boy am I fucked.”


Krebs then added this intriguing bit, which I’ll return to later:


> Apple’s Fox said that prior to the Black Hat demo, SecureWorks did
> contact Apple about a wireless flaw in FreeBSD, the open-source
> code upon which Apple’s OS X operating system is based. In
> January, FreeBSD released a patch to fix the problem, which
> according to [the accompanying advisory](ftp://ftp.freebsd.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-06:05.80211.asc), related to a flaw in the
> way FreeBSD systems scanned for wireless networks that could be
> exploited to allow attackers to take complete control over the
> targeted machine.
> […] Fox also said Apple staff were already aware of the
> flaw when SecureWorks contacted them about it prior to their Black
> Hat presentation, and that Apple had already determined that the
> wireless flaw addressed in the FreeBSD patch was not exploitable
> on any of the Mac products.
> “SecureWorks has not be able to exploit this for us,” Fox said.
> “No one has been able to show us a way to exploit our internal
> [wireless] device drivers with that flaw.”


So Krebs, albeit belatedly, finally now seems suspicious of the claims Maynor and Ellch had made to him previously, which claims he reported without verification.


But so is it just me, or does the headline Krebs chose for this mea culpa — “Follow-up to the Macbook Post” — seem slightly less provocative than the headline he chose for his original post in the series — “Hijacking a Macbook in 60 Seconds or Less”? A more reciprocally sensational (and therefore reciprocally [*diggable*](http://digg.com/security/Hijacking_a_Macbook_in_60_Seconds_or_Less)) but yet completely accurate headline might have been, say, “Losing My Journalistic Integrity in 60 Seconds or Less”, or “I’m a Gullible Rube and Got So Excited I Nearly Stained My Pants at the Thought of Breaking a Story on a Major Mac Security Exploit”.)


## George Ou: Going Down With the Ship


Joining Krebs in line to flush his credibility and reputation down the journalistic toilet is ZDNet’s George Ou. Ou, who attended the Black Hat conference where Maynor and Ellch first presented their talk, almost had it right when he first wrote about the story [on his weblog](http://blogs.zdnet.com/Ou/?p=283):


> The truth of the matter is that this was a hack on a MacBook
> but it pertains to third party hardware and third party
> drivers.  While this isn’t a flaw on the part of Apple
> [UPDATE: The same flaw [also seems to affect Apple’s
> drivers](http://blog.washingtonpost.com/securityfix/2006/08/followup_to_macbook_post.html)], it is an attack on a MacBook and it shouldn’t
> be entirely dismissed either by the Mac community


But then he added the “update” which pointed to Krebs’s now-seemingly-discredited reporting that Maynor and Ellch had discovered a flaw in Apple’s own driver.


Ou continues:


> This particular Wireless [*sic*] hack shouldn’t be pinned on
> Apple’s products or Apple’s programming, but remember that
> just this week there were 26 flaws patched by Apple and many
> of the flaws were critical.  In fact, there were months when
> Apple patched more than 30 vulnerabilities a month so it’s
> clear that security vulnerabilities on the Mac are abundant.
> David Maynor stated that he loves his Mac but it is a fact
> that the Mac has many security flaws.  The point is that no
> one should not [*sic*] be dismissing security issues on Mac
> and claiming that they are invincible.


This is a straw-man argument; no one sane or knowledgeable has
argued that Mac OS X is “invincible”, or that Mac security issues
should be dismissed or ignored. What many Mac users pointed out
regarding Maynor and Ellch’s demonstration, however, is that if it
doesn’t work as an exploit against the MacBook’s built-in card, then
Mac users *could* dismiss this particular issue.


I detect an undertone of “Some day you Mac users are going to get yours and I’m going to rub it in your faces when it happens,” but all told, this was not a particularly noteworthy weblog entry.


His follow-up published Sunday, however, is a doozy, starting right from the headline: “[Vicious Orchestrated Assault on MacBook Wireless Researchers](http://blogs.zdnet.com/Ou/?p=300)”. Ou begins:


> There has been a vicious orchestrated assault on researcher
> David Maynor and the company SecureWorks claiming that the
> Maynor and SecureWorks falsified their research presented at
> Black Hat 2006.


Ou’s conspicuous use of the passive voice (“There has been…”) thinly veils the implication that the perpetrator of this “vicious orchestrated assault” is Apple Computer. E.g. that Apple’s Lynn Fox is maligning the reputations of Maynor and Ellch in the press. Ou, thankfully, is here to stand up for and defend their honor.


> MacWorld’s [*sic*]3 Jim
> Dalrymple was the [first to regurgitate](http://www.macworld.com/news/2006/08/17/wirelesshack/index.php) this bogus story on
> Thursday and followed up with “[MacBook Wi-Fi hack exposed](http://www.techworld.com/security/news/index.cfm?newsID=6667&pagtype=all)” by
> calling the original research a “misrepresentation”.  David
> Chartier of “The Unofficial Apple Weblog” went as far as
> saying “[SecureWorks admits to falsifying MacBook wireless
> hack](http://www.tuaw.com/2006/08/18/secureworks-admits-to-falsifying-macbook-wireless-hack/)”.  Plenty of other media outlets were fed the same story
> but most of them knew better and refused to run this bogus
> story.  But once Digg and Slashdot ran with this story on
> Friday, all hell broke loose and the story has infected the
> blogsphere [*sic*].


The “regurgitated”, “bogus” story that “most” media outlets knew better than to run that Ou refers to were stories simply publishing Lynn Fox’s statement on behalf of Apple. That’s it.


Ou continues:


> I was absolutely shocked when I ran across these stories on Digg.


Indeed, who wouldn’t be shocked to find [over-hyped sensational bullshit on Digg](http://digg.com/security/Hijacking_a_Macbook_in_60_Seconds_or_Less)? What paragon of journalistic integrity is next? The New York Times? The Wall Street Journal?


> I had personally video interviewed Maynor and his partner Jon
> “Johnny Cache” Ellch and these two gentlemen were very honest
> and straightforward.  But as soon as I read the stories, the
> stench began to rise.


I was tempted to make a joke here about what Ou might have eaten for lunch, but decided against it.


> **Maynor and SecureWorks had been telling the truth the entire
> time and they had falsified nothing.**  The only falsification
> going on was the stories themselves!


(Boldface emphasis is Ou’s.) Even Brian Krebs isn’t sticking with
this line. Ou, on the other hand, seems determined to go down with
the SecureWorks ship.


> So what exactly are Maynor and SecureWorks accused of falsifying?
> They are accused of “admitting” that the wireless hack was an
> exploit of a third party device and a third party driver.  The
> only problem with this accusation is that it isn’t exactly news
> since this is precisely what Maynor and company have been saying
> all along.  This was not only evident in my video interview, but
> it was even in Maynor’s original video demonstration along with
> every other news report earlier this month during Black Hat.


Yet another straw-man argument. No one who has actually watched their video is disputing that the exploit demonstrated by Maynor and Ellch *in the video* of a MacBook equipped with a third-party USB wireless card. The dispute is whether Maynor and Ellch had ever indicated, explicitly or implicitly, that they had also discovered similar or identical vulnerabilities in the MacBook’s built-in card and driver, and if they had, whether they had presented evidence of such to Apple.


Ou continues:


> So Maynor and SecureWorks have been telling the truth about
> this being a third party driver and hardware from the very
> beginning and they never misrepresented anything.  If
> anything, Maynor went out of his way to avoid implicating any
> issues on the part of Apple because Brian Krebs of The
> Washington Post reported that [Apple had leaned on Maynor and
> SecureWorks](http://blog.washingtonpost.com/securityfix/2006/08/followup_to_macbook_post.html) not to disclose the fact that the [default Mac
> wireless hardware and default drivers were in fact vulnerable
> as well](http://blog.washingtonpost.com/securityfix/2006/08/update_on_the_apple_macbook_cl.html).


Be careful here, because if you think about the contradictions in this single paragraph too hard, your head will hurt. Ou claims in the first sentence that it was only ever about third-party cards and drivers, but then in the next sentence trumpets Maynor’s claim to Krebs that the default MacBook card and drivers were “vulnerable as well”. Uh, George, *that’s* the part that’s in dispute, not the external USB dongle demo in their video. And then there’s the lovely idea of Maynor going “out of his way to avoid implicating any issues on the part of Apple” followed immediately by Maynor’s unsubstantiated claim to Krebs that Apple had “leaned on” him to keep his mouth shut.


> When I asked Maynor about this at Black Hat, Maynor would not
> confirm or deny whether Apple had leaned on him or not saying
> that he didn’t want to discuss it at the moment.


He doesn’t seem to have wanted to discuss this leaning-on incident since the conference, either.


> The transcript clearly reveals that **Maynor had demonstrated the
> same exploit on a Mac without any third party wireless hardware!** 
> It also turns out Maynor chose an external third party hardware
> wireless adapter to avoid focusing attention on possible
> Apple hardware and software issues which may endanger Mac users.


If a transcript from Brian Krebs says it happened, it must be true.


> When I contacted David Maynor by email and later phoned him late
> Saturday night, Maynor was very disturbed by the whole incident.


I’ll bet.


> He had already been receiving hate mail and even death threats at
> the Black Hat convention but the threats had escalated with this
> latest fabricated story about him falsifying his research.  In one
> such threat, the person stated “I’m going to f***ing kill you and
> your dog” to which Maynor replied “I don’t have a dog.”


Death threats are funny when they come from those wacky Mac kooks.


> Maynor was even more disgusted with the despicable way this
> story was set up and then planted in the press though […]


This “despicable” story-planting method apparently being Apple spokesperson Lynn Fox’s technique of calling reporters on the phone, going on the record, and issuing an unequivocal statement on the matter.


> I’ve been asked not to reveal any more details on this time [*sic*].
> What I can tell you is that Maynor and SecureWorks will not be
> taking this laying down and the fireworks will start in the
> next couple of days.


Consider the fuses lit.


## Conclusion


The principle of [Occam’s Razor](http://en.wikipedia.org/wiki/Occam's_Razor) holds that the simplest explanation is the most likely to be true. By that guideline and the evidence at hand, it is my guess that Maynor and Ellch are disingenuous publicity hounds who studied a previously-identified vulnerability in a FreeBSD Wi-Fi driver and concluded that they could perhaps use this published vulnerability against Mac OS X. I think they tried — and failed — to find an exploit that works against the standard AirPort cards and drivers used by nearly all Mac users, and that they then realized they could, in a demo, exploit buggy drivers *other than Apple’s* on a doctored MacBook and draw much more attention to themselves and their firm than if their demo had been performed on any other computer, using Windows or an open source operating system. I believe they “informed” Apple about a FreeBSD wireless driver issue that Apple already knew about, so that they (i.e. Maynor and Ellch) could honestly claim to have approached Apple “about a wireless security vulnerability”, even though it wasn’t actually a flaw that they themselves had discovered, or that had actually affected shipping Apple code. I.e. that despite the fact that the exploit they had discovered is completely and utterly irrelevant to anyone using a MacBook with Apple’s default AirPort driver and card, which is to say all MacBooks other than the one that Maynor and Ellch modified specifically for their contrived demo, they chose to perform their demo using the MacBook.


When their supposed exploit was publicized by The Washington Post’s Brian Krebs, who reported that they had found Apple’s own drivers to be “identically exploitable”, they said nothing to dispute Krebs’s report. I believe Maynor and Ellch cultivated the misconception that they had identified a vulnerability in the MacBook’s built-in AirPort card and driver but had performed their demonstration using an external USB card for their video at the request of Apple. This made little sense, [as I wrote at the time](http://daringfireball.net/2006/08/krebs_followup), but the misconception took root, and Maynor and Ellch said nothing to dispute it while their consulting firm [racked up the media attention](http://secureworks.com/newsandevents/blackhatcoverage.html).


Now that the “fireworks” are starting, my guess is that Maynor and Ellch, if they choose to defend themselves rather than quietly walking away from the table, will do so by claiming that they never stated nor implied that they had found any vulnerabilities in the MacBook’s built-in card and driver. But their prevarications were far too clumsy for them to get away with this.


(And that’s the *best case* scenario for how I see this working out. Jim Thompson, after obtaining and studying a high-resolution copy of their exploit demonstration video from which he can read the characters in the terminal windows on-screen, [suggests that even their exploit of the *third-party USB card* was a fraud](http://www.smallworks.com/archives/00000461.htm), based on discrepencies in the MAC addresses and networking interfaces.)


It is a simple yes or no question: Have Maynor and Ellch found a vulnerability that affects MacBooks using Apple’s built-in cards and drivers? That Maynor and Ellch haven’t answered it speaks volumes. Bring on the fireworks.


---

1. They’re not part of the “operating system” in the academic computer science sense of the term, but they’re certainly part of Mac OS X as a “product”, in the same way that bundled applications such as the Finder and Safari are part of the system.  ↩︎
2. Will someone please tell Krebs that the “B” in “MacBook” is capitalized? Thanks. ↩︎
3. It’s *Macworld*, not *MacWorld*. What’s with these guys and their inability to get intercapping right?  ↩︎



| **Previous:** | [Jackass of the Week: Paul Thurrott](https://daringfireball.net/2006/08/jackass_paul_thurrott) |
| **Next:** | [A Bit More Regarding the MacBook Wireless Security Saga](https://daringfireball.net/2006/08/macbook_wireless_saga) |


PreviousNext