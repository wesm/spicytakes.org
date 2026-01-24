---
title: "Full Trust can’t be trusted"
date: 2004-10-31
url: https://blog.codinghorror.com/full-trust-cant-be-trusted/
slug: full-trust-cant-be-trusted
word_count: 691
---

Microsoft gets blamed for a lot of security problems, and for the most part, they deserve it. There’s no excuse for the irresponsible “on by default” policy that resulted in so many vulnerable Windows 2000 IIS installations. That’s why [Nimda was so devastating](https://web.archive.org/web/20050305214735/http://news.com.com/%22Nimda%22+worm+strikes+Net,+e-mail/2100-1001_3-273128.html). Windows 2003 has a great security record, mostly because of Microsoft’s new “off by default” policy. I expect Windows XP SP2 to be similarly successful.


Here’s what disturbs me, though. **Even if we eliminate all the system vulnerabilities, what about the biggest vulnerability of all – the user?** The fastest growing virus vector is complicit users:


> *In the past year, spyware problems have become especially pernicious, leaving companies scrambling to respond to customers who don’t necessarily realize they have spyware. Companies are concerned about the cost of dealing with such calls. But perhaps more worrisome, they fear customers will wrongly blame them.
> Spyware generally refers to programs that land on computers without their owners’ knowledge. They can deliver hordes of pop-up ads, redirect people to unfamiliar search engines or, in rare cases, steal personal information. Users most often get them by downloading free games or file-sharing software – and consenting to language buried deep within a licensing agreement. And because they consented, “in some ways it ties our hands because we can’t legally interfere,” said Mike George, head of Dell’s U.S. consumer business.*


It’s a thorny problem. **How do you protect users from themselves?** Unix users will quickly respond with “users should not run as root.” And [they’re right](http://www.theregister.co.uk/2003/10/06/linux_vs_windows_viruses/):


> *Unfortunately, running as root (or Administrator) is common in the Windows world. In fact, Microsoft is still engaging in this risky behavior. Windows XP, supposed Microsoft’s most secure desktop operating system, automatically makes the first named user of the system an Administrator, with the power to do anything he wants to the computer. The reasons for this decision boggle the mind. With all the lost money and productivity over the last decade caused by countless Microsoft-borne viruses and worms, you’d think the company could have changed its procedures in this area, but no.*


Windows, unlike Unix, started life as a single user system. So running as Administrator is deeply ingrained into Windows users. While you *can* run as a regular user under XP, the User Accounts section of control panel **practically begs you not to:**


> *Users with limited accounts cannot always install programs. Depending on the program, a user might need administrator privileges to install it. Also programs designed prior to Windows XP or Windows 2000 might not work properly with limited accounts. For best results, choose programs bearing the Designed for Windows XP logo, or, to run older programs, choose the “computer administrator” account type.*


If that doesn’t scare the crap out of the average user, nothing will. The correct, Unix-y idea that users should not run as Administrator will be adopted by the Windows world, albeit excruciatingly slowly. Microsoft has 10 years of history to overcome, and some non-trivial usability hurdles to address. Security is complexity, and users don’t like complexity: they just want to do their thing. To some degree, security and convenience are mutually exclusive.


Although running as a regular user would be a definite improvement in security – at the cost of convenience – it’s still something of an illusion. **If users want software bad enough they will jump through any arbitrary hoop to get it, including switching to an Administrator account.** Never underestimate the power of a free copy of the latest Linkin Park album. Malware vendors will be more than happy to document the “installation” process for their free p2p file sharing software – File, Run As, Administrator. And once that door is open, it’s open for everyone.


So we’re back where we started: how do you protect users from themselves in an increasingly exploitative world, where malware and [phishing](http://www.antiphishing.org/) grow by double digits every year? Maybe the only answer is something like is [Dan Appleman’s education effort](https://web.archive.org/web/20041128172028/http://alwaysuseprotection.com/). While we clearly need to continue attacking the technology part of this problem, it’s unrealistic to think we can ‘solve’ security through technology alone.

[security](https://blog.codinghorror.com/tag/security/)
[microsoft](https://blog.codinghorror.com/tag/microsoft/)
[vulnerabilities](https://blog.codinghorror.com/tag/vulnerabilities/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[spyware](https://blog.codinghorror.com/tag/spyware/)
