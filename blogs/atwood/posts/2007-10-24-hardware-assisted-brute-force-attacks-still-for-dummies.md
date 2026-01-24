---
title: "Hardware Assisted Brute Force Attacks: Still For Dummies"
date: 2007-10-24
url: https://blog.codinghorror.com/hardware-assisted-brute-force-attacks-still-for-dummies/
slug: hardware-assisted-brute-force-attacks-still-for-dummies
word_count: 1046
---

Evidently hardware assisted [brute force password cracking](https://web.archive.org/web/20071025081650/http://technology.newscientist.com/article.ns?id=dn12825) has arrived:


> A technique for cracking computer passwords using inexpensive off-the-shelf computer graphics hardware is causing a stir in the computer security community.
> Elcomsoft, a software company based in Moscow, Russia, has filed a US patent for the technique. It takes advantage of the “massively parallel processing” capabilities of a graphics processing unit (GPU) - the processor normally used to produce realistic graphics for video games.
> Using an $800 graphics card from nVidia called the GeForce 8800 Ultra, Elcomsoft increased the speed of its password cracking by a factor of 25, according to the company’s CEO, Vladimir Katalov. The toughest passwords, including those used to log in to a Windows Vista computer, would normally take months of continuous computer processing time to crack using a computer’s central processing unit (CPU). By harnessing a $150 GPU – less powerful than the nVidia 8800 card – Elcomsoft says they can be cracked in just three to five days. Less complex passwords can be retrieved in minutes, rather than hours or days.


GPUs, with their [massive built-in paralellism](https://blog.codinghorror.com/cpu-vs-gpu/), were built to do [things like this](https://blog.codinghorror.com/folding-the-death-of-the-general-purpose-cpu/). I’m encouraged that we’re finally able to harness all that video silicon to do useful things beyond rendering Doom at 60 frames per second with anti-aliasing and [anisotropic filtering](https://blog.codinghorror.com/anisotropic-filtering/).


There’s a bit more detail on the Elecom approach in their [one-page PDF](https://web.archive.org/web/20071026161431/http://www.elcomsoft.com/EDPR/gpu_en.pdf). They provide actual numbers there.


> Using the “brute force” technique of recovering passwords, it was possible, though time-consuming, to recover passwords from popular applications. For example, the logon password for Windows Vista might be an eight-character string composed of uppercase and lowercase alphabetic characters. There would about 55 trillion (52 to the eighth power) possible passwords. Windows Vista uses NTLM hashing by default, so using a modern dual-core PC you could test up to 10,000,000 passwords per second, and perform a complete analysis in about two months. **With ElcomSoft’s new technology, the process would take only three to five days, depending upon the CPU and GPU**.
> Preliminary tests using Elcomsoft Distributed Password Recovery show that **the [brute force password cracking] speed has increased by a factor of twenty, simply by hooking up with a $150 video card’s onboard GPU**. ElcomSoft expects to find similar results as this new technology is incorporated into their password recovery products for Microsoft Office, PGP, and dozens of other popular applications.


It’s fun, and it makes for a shocking “Password Cracking Supercomputers On Every Desktop Make Passwords Irrelevant” headline, but password cracking supercomputers on every desktop *doesn’t* mean the end of password-protected civilization as we know it. Let’s do the math.


**How many passwords can we attempt per second?**

kg-card-begin: html


| Dual Core CPU | 10,000,000 |
| GPU | 200,000,000 |


kg-card-end: html

**How many password combinations do we have to try?**


528 = 53,459,728,531,456


That’s a lot of potential passwords. Let’s stop playing Quake Wars for a few days and get cracking:

kg-card-begin: html

```

53,459,728,531,456 /  10,000,000 pps / 60 / 60 / 24 = 61.9 days
53,459,728,531,456 / 200,000,000 pps / 60 / 60 / 24 =  3.1 days

```

kg-card-end: html

As promised by Elecom, that works out to a little over **three days at the GPU crack rate**, and two months at the CPU crack rate. Oooh. Scary. Worried yet? If so, you shouldn’t be. Watch what happens when I add four additional characters to the password:

kg-card-begin: html

```

5212 / 200,000,000 pps / 60 / 60 / 24 =  22,620,197 days

```

kg-card-end: html

For those of you keeping score at home, with a 12 character password this hardware assisted brute-force attack would take **61,973 years**. Even if we increased the brute force attack rate by *a factor of a thousand*, it would *still* take 62 years.


Elecom’s idea of an 8 character password is awfully convenient, too. Only lowercase and uppercase letters, a total of 52 possible choices per character. Who has passwords without at least one number? [Even MySpace users are smarter](http://www.schneier.com/blog/archives/2006/12/realworld_passw.html) than that. If you include a number in your 8 character password, or a non-alphanumeric character like “%,” attack times increase substantially. Not enough to mitigate the potential attack completely, mind you, but you’d definitely put a serious dent in any brute forcing effort by switching out a character or two.

kg-card-begin: html

```

628 / 200,000,000 pps / 60 / 60 / 24 =  13 days
728 / 200,000,000 pps / 60 / 60 / 24 =  42 days

```

kg-card-end: html

Personally, I think it’s easier to go with [a pass phrase](https://blog.codinghorror.com/passwords-vs-pass-phrases/) than a bunch of random, difficult to remember gibberish characters as a password. Even if your pass phrase is in all lower-case – a mere 26 possible characters – that exponent is *incredibly* potent.

kg-card-begin: html

```

2610 / 200,000,000 pps / 60 / 60 / 24 =  8 days
2612 / 200,000,000 pps / 60 / 60 / 24 =  15 years
2614 / 200,000,000 pps / 60 / 60 / 24 =  10,228 years

```

kg-card-end: html

By the time you get to a mere 14 characters – even if they’re all lowercase letters – you can pretty much forget about anyone brute forcing your password. Ever.


So what have we learned?


Brute force attacks, even fancy hardware-assisted brute force attacks, are [still for dummies.](https://blog.codinghorror.com/brute-force-key-attacks-are-for-dummies/) If this is the best your attackers can do, they’re too stupid to be dangerous. Brute forcing is almost always a waste of time, when [vastly more effective social vectors](https://blog.codinghorror.com/phishing-the-forever-hack/) and [superior technical approaches](https://blog.codinghorror.com/rainbow-hash-cracking/) are readily available.


**Hardware-assisted brute force attacks will never be a credible threat. But short, simple passwords are still dangerous.** *If* your password is only 8 alphabet characters, and *if* it’s exposed in a way that allows brute force hardware assisted attack, you could be in trouble. All you need to do to sleep soundly at night (well, at least as far as brute force attacks are concerned) is choose a slightly longer password. It’s much safer to think of your security in terms of passphrases instead of passwords. And unlike “secure” 8 character passwords, passphrases are easy to remember, too. Have you considered [helping me evangelize passphrases?](https://blog.codinghorror.com/passphrase-evangelism/)

[security](https://blog.codinghorror.com/tag/security/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
[brute force attack](https://blog.codinghorror.com/tag/brute-force-attack/)
[gpu computing](https://blog.codinghorror.com/tag/gpu-computing/)
[password cracking](https://blog.codinghorror.com/tag/password-cracking/)
