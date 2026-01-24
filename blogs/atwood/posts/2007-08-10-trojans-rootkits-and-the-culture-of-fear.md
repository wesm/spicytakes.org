---
title: "Trojans, Rootkits, and the Culture of Fear"
date: 2007-08-10
url: https://blog.codinghorror.com/trojans-rootkits-and-the-culture-of-fear/
slug: trojans-rootkits-and-the-culture-of-fear
word_count: 1957
---

Scott Wasson at The Tech Report notes that two of his family members fell victim to [the eCard email exploit](https://web.archive.org/web/20071022032325/http://techreport.com/ja.zz?comments=13029) that has been making the rounds lately:


> I just dropped off a package containing my dad’s laptop at the FedEx depot this afternoon. I spent parts of several days this week recovering his data, wiping the drive, and reinstalling the OS and key apps. My dad’s a tech-savvy guy, but in a moment of weakness, he opened one of those greeting card spam messages recently and his computer became infected with a trojan. The thing had installed a proxy for IE7 and rerouted all DNS queries to a compromised server, and then covered most if its tracks via a rootkit. I wiped the drive and started over because I didn’t think I could be sure otherwise that the trojan was entirely removed from his system.
> I went through the same thing with my wife’s PC not long ago. She also knows better than to open attachments, but the greeting card thing caught her off guard somehow. Took her a while to admit that she’d gone through the steps of opening the email, clicking the link, downloading the payload, and running the executable. I lost a day’s work, at least, to rebuilding that machine from the ground up.
> Were it not for tools like [Rootkit Revealer](http://www.microsoft.com/technet/sysinternals/Utilities/RootkitRevealer.mspx), I might not have even been able to detect the trojans. One of them seemed to be attacking our antivirus software and trying to stop the Revealer process, even.
> I could get mad at my relatives for making a mistake, but it’s hard to see the point. The really frustrating thing is that they both had reason to believe a greeting card might be coming their way at the time and reason to be a little frazzled: my dad had brain surgery recently. These email-based attacks prey on those who might not be operating at 100% for whatever reason. That makes me white-hot mad.
> Which makes me wonder: if it can happen to some fairly tech-savvy folks like these, how widespread is this problem? And what happens when your computer gets infected and you don’t have a close relative who’s a PC expert? The trojan on my wife’s PC wasn’t detected by Windows Defender, [Avast! antivirus](http://www.avast.com/), or the Windows Malicious Software Removal Tool.


I feel his pain. I went through a similar experience on one of my machines recently, which I documented in [How to Clean Up a Windows Spyware Infestation](https://blog.codinghorror.com/how-to-clean-up-a-windows-spyware-infestation/). I’m sure I’d be even angrier if this had happened to someone more vulnerable, like my wife, or my father. But there are a few hard lessons to be learned here:


### 1. Stop Running As Administrator


To answer the question Scott posed at the bottom of his post, the problem is *incredibly* widespread; it’s a [Windows security epidemic](https://blog.codinghorror.com/the-windows-security-epidemic-dont-run-as-an-administrator/). The only real long-term solution for the Windows security epidemic is to stop running as Administrator. Vista’s UAC is a marginally effective half-step at best. Why not emulate the UNIX operating systems, which seem to be immune to most infections to date? When was the last time you heard of a Linux or FreeBSD user running anti-virus software? Or a Mac OS X user? A handful of antivirus programs exist for the Mac, but [they’re largely snake oil](https://web.archive.org/web/20080704160326/http://news.digitaltrends.com/featured_article79.html), as they have little to protect against.


If you take the advice to run as a non-administrator, you may find that the standard user route is painful, too. I received an email from James Boswell that describes the difficulty:


> You and many others have been advocating the use of admin users and standard users on Windows. I’m an experienced Windows developer too, and regularly build machines, but I’ve always had admin access for a single user. This time, I am putting a Vista Home Premium 64 bit machine together for my son and thought I’d take your advice but I have really struggled with multi users.
> When logged in as the standard user, installations of software are hit and miss. For example, 3DMark06, Shockwave 10 and Gamespot Download Manager failed to install correctly as standard user (with admin priv. when prompted for password). All 3 failed installs required me to switch user to the admin and repeat the installs. Plus many installations require me to enter my password several times, not just during the install, but when the program runs for the first time (usually for firewall access or updates).
> All of this is very unhelpful, because my son will no doubt want to install software during his use of the computer, and so will come to me saying “Dad, I want to install {Counter Strike | some web plugin | a screensaver} and Vista is bugging me again” so I will look at what he’s installing and type my password in to approve access, and then I go back to what I was doing. But I will now be waiting for the “DAD!!!... it doesn’t work” follow up because the install failed.
> I will then have to switch user to admin, repeat my son’s actions to access the install program, wait for install to finish, run the app to approve any firewall or other permissions, and then log off. I’m most definitely for the responsible parental control of PCs, but this is a monumental and entirely unnecessary waste of my time.


This is partially the fault of Windows software developers who fail to test as standard user. It’s disappointing, but understandable, since **running as Administrator has long been institutionalized in Windows**. It’s also a particular problem for users who need to install lots of software for whatever reason. In contrast, my wife runs fine as limited user, but she almost never installs software of any kind. I hope more Windows developers are testing their software when running as a standard user, and in time running as a standard user will become as easy(ish) as it is on a Unix based OS.


### 2. Traditional Anti-Virus Doesn’t Work Any More


The blacklist approach used by anti-virus vendors simply doesn’t scale to today’s threat environment. [Blacklists are never particularly effective](https://blog.codinghorror.com/whitelist-blacklist-greylist/). But it’s getting to the point where [the illusion of protection](http://chuvakin.blogspot.com/2007/04/answer-to-my-antivirus-mystery-question.html) afforded by a traditional anti-virus solution is *worse* than no protection at all:


> Let’s suppose somebody who is involved with incident response at a typical US public University collected a few recent malware samples from the compromised machines, and then submitted all the samples to VirusTotal for scanning against all current anti-virus and anti-virus-like products. What do you think the average detection rate is?
> Let me give you the answer: it is 33%. In other words, **the average detection rate of malware from these “solutions” was 33%**, with the maximum at 50% and the minimum at 2%. Keep this number in mind, that shiny anti-virus product you just bought might be protecting you from just 2% of currently active and common malware (not some esoteric and custom uber-haxor stuff)!
> I have to conclude what many security pundits were blabbing about for years: “mainstream” anti-virus is finally DEAD. It’s a weak excuse for defense-in-depth, in about the same sense as wearing an extra shirt provides “another security layer” in a gun fight.


Not only does anti-virus [cripple your machine’s performance](https://blog.codinghorror.com/choosing-anti-anti-virus-software/), it doesn’t even protect you adequately! Even if your anti-virus or anti-malware solution is catching an incredibly optimistic 90% of threats, all it takes is *one new, undetected threat* to get through and your machine is thoroughly 0wned.


And I do mean 0wned. These aren’t your father’s [happy99.exe](http://www.cert.org/incident_notes/IN-99-02.html) trojans. Today’s threats have evolved into very sophisticated beasts. I got a chill when Scott mentioned so casually that **the payload of the eCard trojan is a **[**rootkit**](http://en.wikipedia.org/wiki/Rootkit)** that redirects all DNS queries to a compromised DNS server.** That’s a worst case scenario which is becoming increasingly common. Good luck detecting a threat which subverts the very kernel of the operating system. Traditional programming techniques don’t work; you need to fight fire with fire and hire kernel hackers of your own to pit them against. This leads to a kind of software Armageddon that nobody can really “win”: you’re left with a wake of destroyed operating systems and thoroughly defeated users.


The Mainstreaming of Virtual Machine Sandboxes


### 3. The Mainstreaming of Virtual Machine Sandboxes


Running as non-administrator should be absolutely standard, as it is one of the few security techniques which has a proven track record. But, with sufficient desire and initiative, naïve or malicious users can still subvert the limited user account. If users want to [see the dancing bunnies](https://blog.codinghorror.com/the-dancing-bunnies-problem/) bad enough – or, in Scott’s case, they want to see the eCard someone “sent” them – they’ll type the administrator password in and escalate. Forget about protecting users from malicious threats. Now you have to deal with a far more difficult problem: **how do you protect users from *themselves?*** I think virtualization is the only rational way to [protect users from themselves](https://blog.codinghorror.com/our-virtual-machine-future/) – and that’s why virtualization is the next great frontier for computer security.


Full-machine virtualization as seen in Virtual PC 2007 and [VMWare](http://www.vmware.com/) is one way to achieve this, and it’s a completely natural use for the obscene amount of local processing power we have on our desktops. But there’s also software virtualization, which isolates all disk access from individual applications. Earlier this year, [Google acquired GreenBorder technologies](https://web.archive.org/web/20070827173143/http://blogs.zdnet.com/security/?p=241), which used software virtualization to isolate the browser from the disk and completely prevent any malware attacks. Their product is no longer distributed while they do whatever it is they’re doing as a part of Google, but for context, you can read a [review of their original product](https://web.archive.org/web/20061027230332/http://www.pcmag.com/article2/0,1759,1980980,00.asp), GreenBorder Pro, at PC Magazine. Note the “does not need signature updates” notation in the review. With virtualization, you stop caring about blacklists and signature updates; you’re protected against any possible threat, now or in the future.


Well, except for the rare threats that target the virtualization layer, but that’s a much tougher nut to crack.


Most of all, **I dislike the culture of fear that permeates Windows security software marketing**. I don’t think it’s ethical to scare users into buying your security software product – and it also creates a huge conflict of interest between the security software vendors and the virus, malware, and trojan creators. After all, why would we buy anti-virus software if, like Mac OS X users, we had *almost no risk* of being infected by a virus, malware, or trojan? Windows security software vendors need the threats – and the more credible and fearsome the threats, the better – to make money. They have no economic incentive to support an environment where threats are ineffective. **The status quo of weak Windows security suits them just fine. It sells their products**.


![](https://blog.codinghorror.com/content/images/2025/04/image-711.png)


I believe we can solve the Windows security epidemic without using fear as a marketing tactic. We need to *stop* relying on the illusory, expensive protection of anti-virus blacklists, and *start* implementing better solutions. We already have the ability to run as a limited user account today. It’s too bad the powers that be at Microsoft didn’t have the guts to pull the trigger on limited user accounts as a standard setup in Vista. But that shouldn’t stop us. We should have the guts to [pull the trigger ourselves](https://blog.codinghorror.com/the-windows-security-epidemic-dont-run-as-an-administrator/). And if we add a little virtualization to the mix, I think we can almost completely eliminate most security threats. Windows anti-virus software is considered mandatory today. But I’d love to see a day where, as on OS X and every other Unix operating system variant, anti-virus software is viewed as unnecessary, even superfluous.

[security](https://blog.codinghorror.com/tag/security/)
[malware](https://blog.codinghorror.com/tag/malware/)
[trojan](https://blog.codinghorror.com/tag/trojan/)
[rootkit](https://blog.codinghorror.com/tag/rootkit/)
[cybersecurity](https://blog.codinghorror.com/tag/cybersecurity/)
