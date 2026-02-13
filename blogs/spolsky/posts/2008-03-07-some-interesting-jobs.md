---
title: "Some interesting jobs"
date: 2008-03-07
url: https://www.joelonsoftware.com/2008/03/07/some-interesting-jobs/
word_count: 1429
---


The recent release of FogBugz 6.0 has, approximately, doubled our sales, and, while I fully agree that often small teams can accomplish a lot more than large teams, we have a lot of interesting work to be done here and there never seem to be enough people to do it, so we’ve looked for some areas where adding more people would not necessarily slow things down.


We came up with three fairly interesting new positions that might be a perfect fit for you or someone you know. It’s relatively rare for Fog Creek to hire full time engineers; many of the people we’ve hired in the past have been former summer interns, the company is quite small (20 people), and we don’t hire lightly, so this is a rare opportunity to get in the door and take advantage of the fact that Fog Creek was designed from the ground up to be the kind of company where the best software developers want to work ([about Fog Creek](http://www.fogcreek.com/About.html)).


The first position is in system administration. Normally, I’m pretty happy to hire inexperienced but bright people and let them learn on the job. Even for fairly important jobs, like, say, President of the United States.


But system administration is one of those things where experience is really important. You don’t want your new system administrator to learn about how to create secure and robust online services by building something insecure and unrobust and learning from experience. So for our first system administrator, we hired [Michael Gorsuch](http://michaelonsecurity.com/), because he knew how to operate our systems well on day one.


This is a dilemma for smart people who want to learn how to be world class system administrators. If everybody is asking for *x* years of experience, how are you supposed to get that experience? You can take an entry-level job in a big company as, say, junior DNS administrator, typing changes into DNS configuration files, but you won’t learn very much.


Here’s where Fog Creek comes in. Michael and I talked about this and decided that our second hire in that department could be totally inexperienced at system administration, as long as they were smart, got things done, and had the personal characteristics to become a great system administrator (attention to detail, insane curiosity, constant need to be learning new things, strong ability to stay levelheaded and organized even in the most chaotic of situations, doesn’t soil pants in fear when presented with a command prompt, thinks “rtfm” is a great answer, etc.) This is a once-in-a-lifetime chance to learn the field and gain substantial experience on an interesting, mixed environment including Unix and Windows, desktops and servers, internet hosting and internetworking, open source and Microsoft, with all kinds of interesting moving parts. And you’ll be learning from a real master, one on one, in a great environment with zero corporate BS, management that trusts you to order equipment you need without going through some kind of 6 month budget committee process during which a shrill corporate attorney who has been somehow promoted to “head of the capital infrastructure committee” is nervous about using open source hippie software because it seems kind of “communistic,” and she had a terrible experience on a commune in the 60s when this really gross guy who never bathed and wore flip flops even in the winter… well, anyway, I’m getting off the subject. At Fog Creek when you need equipment you order it. That’s really all there is to it.


> Interested? [System administrator at Fog Creek](http://www.fogcreek.com/Jobs/SysAdmin.html)


Our next interesting position is for a Chief Linux Guru. This is a hybrid position for somebody who really loves Linux, wants to do a lot of coding, but also wants a more diverse problem-solving kind of job.


Here’s the theory behind this position. Our main product, FogBugz, is a server product, available for Windows, Linux, and Mac. On Windows servers, everybody has pretty much the same minimal stuff. So our setup program usually works off the shelf.


On Linux, though, there’s a lot more diversity. People have different distros, they have different versions of different important components like MySQL, PHP, and Mono, and they’re not all instantly compatible. A lot of Linux administrators went through their server when they first set it up removing things that they didn’t think they’d need for “security” reasons (“if you’re not going to *use* **/bin/ls**, delete it–it’s just a security hole waiting to be found”, they said), and now, here it is, three years later, and they’re installing FogBugz, and they don’t get why **ls** isn’t working. Bottom line: it takes a little bit of hammering to get FogBugz to work on many Linux systems.


So this position is for a Linux coder who will also be responsible to get FogBugz working on our customers’ systems. My pet theory is that if the person who takes the call when a customer is missing, say, the Pear Mail module, if this person is the same person who maintains the setup code, then they will eventually get sick of sshing into customers’ servers and typing “pear install Mail” for them and they’ll just fix it in the setup code once and for all. And I think a lot of people would find a job that combines problem solving with new software development is going to be pretty interesting, especially if, as I said, you love Linux.


On the development side, you’ve also got to handle all the Linux-specific code. Right now, that’s a mix of PHP, Mono, and various scripting languages. Most of FogBugz is written in our own portable language, Wasabi. You’ll be responsible to maintain the Linux-specific parts of the code, and you’ll be working on keeping Wasabi for Linux at the same level as Wasabi for Windows.


> Interested? [Linux guru at Fog Creek](http://www.fogcreek.com/Jobs/LinuxGuru.html)


Finally, we could use an extreme Windows Internals guru. I don’t mean an “Access/VB” kind of guru. I mean a Win 32, COM, .Net, GDI programming, low level Windows systems stuff in C++ and C# kind of guru. And when I say “.Net” I don’t mean “Ooh look I made an ASP.NET website with a GridView that shows a list of customers.” Uh-uh. Leave that bush league stuff to the boss (me). For *this* job, you’ll be working directly on a native .NET programming language, generating CLR bytecode and integrating with the Visual Studio debugger. You’ll be resolving obscure threading model problems in Other People’s Code. You’ll be hacking GDI to improve the performance of our remote desktop service, [Copilot](https://www.copilot.com). You’ll be figuring out why trivial things that used to work don’t work any more in 64 bit Vista. This is the perfect job for the kind of developer who has been doing API level Windows programming for years, who has been reading MSDN Magazine since it was called MSJ, who actually understands what Don Box is talking about, who can explain how to instantiate a COM object from a DLL without touching the registry, and who can figure out, from crappy Microsoft documentation, how to play the first four bars of *Gaudeamus Igitur *on a computer without a sound card.


> Interested? [Windows internals guru at Fog Creek](http://www.fogcreek.com/Jobs/WinGuru.html)


Don’t small teams get more things done than big teams? Didn’t *The Mythical Man Month* prove conclusively that you should have the smallest team possible? Don’t startups with two kids run circles around the big companies? Isn’t Fog Creek getting big and bureaucratic? Why hire more people?


No, no, no, and no. It’s a little bit more complicated than that. At 20 people we still fit around one lunch table and we’re far from not being able to get things done. And what MMM claimed was only that adding people to a late project makes the project later. The more people you have, the more communication you need, which counterbalances the added productivity of the extra people–that’s the MMM conclusion–and so when we add people we always try to find a way to do it in a way that’s efficient. But the bottom line is that we have a long list of things that we want to do, and our too-small team is forced to do things in serial that we could do in parallel with a couple more people. So in the long run I think we’ll continue hiring carefully and discretely, keeping each of the core teams small (our biggest dev team right now is, um, three people), and I think we’re still a ways of from worrying about Fog Creek being bogged down in bureaucracy.
