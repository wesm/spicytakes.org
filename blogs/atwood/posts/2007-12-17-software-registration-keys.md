---
title: "Software Registration Keys"
date: 2007-12-17
url: https://blog.codinghorror.com/software-registration-keys/
slug: software-registration-keys
word_count: 1218
---

Software is digital through and through, and yet there’s one unavoidable aspect of software installation that remains thoroughly analog: entering the registration key.


![](https://blog.codinghorror.com/content/images/2025/03/image-181.png)


![](https://blog.codinghorror.com/content/images/2025/03/image-180.png)


![](https://blog.codinghorror.com/content/images/2025/03/image-179.png)


![](https://blog.codinghorror.com/content/images/2025/03/image-178.png)


The aggravation is intentional. Unique registration keys exist only to prevent piracy. Like all piracy solutions – short of completely server hosted applications and games, where piracy means you’d have to host your own rogue server – it’s an incomplete client-side solution. How effective is it? One vendor implemented code to **detect false registration keys** and phone home with some basic information such as the IP address when these false keys are entered. [Here’s what they found:](https://web.archive.org/web/20080103070839/http://sharewarejustice.com/software_piracy.htm)

kg-card-begin: html


| Software Connectivity | Ratio of pirated
to legitimate keys |
| no internet connection required | 45 : 1 |
| occasional internet connection necessary | 60 : 1 |
| internet must be “always on” | 110 : 1 |


kg-card-end: html

I have no idea how reliable this data is. The vendor is never named, and given that the title of the URL is sharewarejustice.com/software-piracy.htm, I’d expect it to be biased. But it is data, and without the registration key concept (and pervasive internet connectivity), we’d have no data whatsoever to quantify how much piracy actually exists. The BSA [estimated 35% of all software was pirated](https://web.archive.org/web/20080220060408/http://www.bsa.org/country/News%20and%20Events/News%20Archives/Worldwide%20Software%20Piracy%20Rate%20Holds%20Steady.aspx) in 2006, but it is just that – an estimate. I’ll choose biased data over no data whatsoever, every time.


I don’t have a problem with registration keys. You could, in fact, argue that registration key validation actually works. Microsoft recently stated that the piracy rate of Vista is half that of XP, largely due to improvements in their [Windows Genuine Advantage program](http://en.wikipedia.org/wiki/Windows_Genuine_Advantage) – Microsoft’s global registration key validation service.


As a software developer, I can empathize with Microsoft to a degree. Unless you oppose the very concept of commercial software, there has to be *some* kind of enforcement in place. The digital nature of software makes it both easy and impersonal for people to avoid paying (note that I did not say “steal”), which is an irresistible combination for many. **Unless you provide some disincentives, that’s exactly what people will do – they’ll pay nothing for your software.**


Microsoft’s history with piracy goes way, way back – all the way back to the original microcomputers. Witness Bill Gates’ [Open Letter To Hobbyists](http://www.digibarn.com/collections/newsletters/homebrew/V2_01/gatesletter.html), written in 1976.


> Almost a year ago, Paul Allen and myself, expecting the hobby market to expand, hired Monte Davidoff and developed Altair BASIC. Though the initial work took only two months, the three of us have spent most of the last year documenting, improving and adding features to BASIC. Now we have 4K, 8K, EXTENDED, ROM and DISK BASIC. The value of the computer time we have used exceeds $40,000.
> The feedback we have gotten from the hundreds of people who say they are using BASIC has all been positive. Two surprising things are apparent, however, 1) Most of these “users” never bought BASIC (less than 10% of all Altair owners have bought BASIC), and 2) The amount of royalties we have received from sales to hobbyists makes the time spent on Altair BASIC worth less than $2 an hour.
> Why is this? As the majority of hobbyists must be aware, most of you steal your software. Hardware must be paid for, but software is something to share. Who cares if the people who worked on it get paid?
> Is this fair? One thing you don’t do by stealing software is get back at MITS for some problem you may have had. MITS doesn’t make money selling software. The royalty paid to us, the manual, the tape and the overhead make it a break-even operation. One thing you do do is prevent good software from being written. Who can afford to do professional work for nothing? What hobbyist can put 3-man years into programming, finding all bugs, documenting his product and distribute for free? The fact is, no one besides us has invested a lot of money in hobby software. We have written 6800 BASIC, and are writing 8080 APL and 6800 APL, but there is very little incentive to make this software available to hobbyists. Most directly, the thing you do is theft.


Although computers have changed radically in the last thirty years, human behavior hasn’t. (Alternately, you could argue that the economics of computing and the emergence of an ad-supported software ecosystem have fundamentally changed the rules of the game since 1976. But that’s a topic for another blog post.)


I accept that **software registration keys are a necessary evil for commercial software**, and I resign myself to manually keeping track of them, and keying them in. But why do they have to be so painful? You *do* realize a human being has to type this stuff in, right? Here are some things that I’ve seen vendors get wrong with their registration key process:

1. **Using commonly mistaken characters in the key**
Quick! Is that an ‘O’ or an ‘0’? A ‘6’ or a ‘G’? An ‘I’ or an ‘l’? A ‘B’ or an ‘8’? At least have the courtesy to scour your registration key character set of those characters that are commonly mistaken for other characters. And please print the key in a font that minimizes the chances of confusion.
2. **Excessively long keys**
The most rudimentary grasp of mathematics tells us that a conservative 10 character alphanumeric registration key is good for 197 trillion unique users. Even [factoring in the pigeonhole principle](https://blog.codinghorror.com/hashtables-pigeonholes-and-birthdays/), we can estimate about 14 million random registration key combinations before we have a 50 percent risk of a collision. So why, then, do software developers insist on 20+ character registration keys? It’s ridiculous. Are they planning to sell licenses to every grain of sand on every beach?
3. **Not separating the key into blocks**
Rather than smashing your key into one long string, make it a group of small 4 to 5 characters, separated by a delimiter. It’s the same reason phone numbers are listed as 404-555-1212 and not 4045551212: People have an easier time handling and remembering [small chunks of information](https://blog.codinghorror.com/the-magical-number-seven-plus-or-minus-two/).
4. **Making it difficult to enter the key**
Short of providing every customer a handy USB barcode scanner, at least make the registration key entry form as user friendly as possible:
5. **Where’s the %*@# key?**
The key is important. Without it we can’t install or use the software. So why is it buried in the back of the manual, or on an easy-to-overlook interior edge of the package? Make it easy to find – and difficult to lose. Provide multiple copies of the key in different locations, maybe even as a peelable sticker we can place somewhere useful. And if the software was delivered digitally, please keep track of our key for us. We’re forgetful.


Software registration keys are a disconcerting analog hoop we force users to jump through when using commercial software. Furthermore, **registration keys are often the user’s first experience with our software –** and first impressions matter. If you’re delivering software that relies on registration keys, give that part of the experience some consideration. Any negative feelings generated by an unnecessarily onerous registration key entry process will tend to color users’ perception of your software.

[security](https://blog.codinghorror.com/tag/security/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[piracy](https://blog.codinghorror.com/tag/piracy/)
[registration keys](https://blog.codinghorror.com/tag/registration-keys/)
[anti-piracy](https://blog.codinghorror.com/tag/anti-piracy/)
