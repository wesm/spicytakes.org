---
title: "Pick a License, Any License"
date: 2007-04-03
url: https://blog.codinghorror.com/pick-a-license-any-license/
slug: pick-a-license-any-license
word_count: 820
---

I hate software licenses. When I read a software license, what I see is a bunch of officious, mind-numbing lawyerly doublespeak. Blah, blah, blah... *kill me now.*


![](https://blog.codinghorror.com/content/images/2025/03/image-248.png)


If I had my way, everything would be released under the [WTFPL](http://sam.zoy.org/wtfpl/). Over time, I’ve begrudgingly come to the conclusion that, like lawyers, death, and taxes, choosing a software license is inevitable. Of course, it doesn’t matter if yours are the only human eyes that will ever see the code. But **a proper software license is a necessary evil for any code you plan to release to the public**.


I definitely regret not choosing a software license for my CodeProject articles. I’ll occasionally get friendly emails from people asking permission to use the code from my articles in various projects, commercial and otherwise. It’s thoughtful of people to ask first. I do appreciate it, and permission is always granted with the single caveat that my name and URL remain in the comments.

kg-card-begin: html

Because I did not explicitly indicate a license, I declared an implicit copyright without explaining how others could use my code. Since the code is unlicensed, I could theoretically assert copyright at any time and demand that people stop using my code. Experienced developers won’t touch unlicensed code because *they have no legal right to use it*. That’s ironic, considering the whole reason I posted the code in the first place was so other developers could benefit from that code.  I could have easily avoided this unfortunate situation if I had done the right thing and **included a software license with my code**.

kg-card-end: html

Unfortunately, we love software licenses like we love standards – that’s why there are [so many of them](http://www.opensource.org/licenses/alphabetical). And what, exactly, are the differences between all these licenses? How do you select the correct license for your software? I’ve attempted to succinctly capture the key differences between the most well-known software licenses in the following handy chart.

kg-card-begin: html


|  | Source | Type (Clauses) |  |
| **None** | Open | None (0) | Without a license, the code is copyrighted by default. People can read the code, but they have no legal right to use it. To use the code, you must contact the author directly and ask permission. |
| [**Public domain**](http://en.wikipedia.org/wiki/Public_domain) | Open | Permissive (0) | If your code is in the public domain, anyone may use your code for any purpose whatsoever. Nothing is in the public domain by default; you have to explicitly put your work in the public domain if you want it there. Otherwise, you must be dead a long time before your work reverts to the public domain. |
| [GPL](http://en.wikipedia.org/wiki/GNU_General_Public_License) | Open | Copyleft (12) | The archetypal bearded, sandal-clad free software license. Your code can never be used in any proprietary program, ever! Take that, capitalism! |
| [LGPL](http://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) | Open | Mostly Copyleft (16) | GPL with a cleverly-constructed pressure valve release. Your free software can be binary linked to proprietary programs under certain very specific circumstances. |
| [MIT/X11](http://en.wikipedia.org/wiki/MIT_License) | Open | Permissive (2) | Short and sweet. Includes generic legal disclaimer of liability. |
| [BSD](http://en.wikipedia.org/wiki/BSD_license) | Open | Permissive (2) | Short and sweet. Includes legal disclaimer of liability with explicitly named organization. |
| [Apache](http://en.wikipedia.org/wiki/Apache_License) | Open | Permissive (9) | Requires derivative works to provide notification of any licensed or proprietary code in a common location. |
| [Eclipse](http://en.wikipedia.org/wiki/Eclipse_Public_License) | Open | Permissive (7) | Business friendly. Allows derivative works to choose their own license for their contributions. |
| [Mozilla](http://en.wikipedia.org/wiki/Mozilla_Public_License) | Open | Weak Copyleft (13) | Allows liberal mixing with proprietary software. |
| [MS Permissive](https://web.archive.org/web/20051029091532/http://www.microsoft.com/resources/sharedsource/licensingbasics/permissivelicense.mspx) | Open | Permissive (3) | Resembles the MIT and BSD licenses. Not formally accepted by OSI, and also offered in a "Windows-only" LPL variant. |
| [MS Community](https://web.archive.org/web/20070514210144/http://www.microsoft.com/resources/sharedsource/licensingbasics/communitylicense.mspx) | Open | Copyleft (3) | Resembles the GPL license. Requires all contributed code to be returned to the community. Not formally accepted by OSI, and also offered in a "Windows-only" LCL version. |
| [MS Reference](https://web.archive.org/web/20070509141855/http://www.microsoft.com/resources/sharedsource/licensingbasics/referencelicense.mspx) | Proprietary | Read Only (3) | You can review the code, or make copies of it, but you can't use it or change it in any way. Allows a window (no pun intended) on formerly completely proprietary, secret code. |


kg-card-end: html

After compiling this table, I’ve learned two things:

1. My head hurts.
2. I still prefer the WTFPL.


I’m not even going to get into the many [religious issues](https://blog.codinghorror.com/are-you-there-god-its-me-microsoft/) of software licensing, such as...

- [open-source software](http://en.wikipedia.org/wiki/Open_source) vs. [proprietary software](http://en.wikipedia.org/wiki/Proprietary_software)
- [copyleft licensing](http://en.wikipedia.org/wiki/Copyleft) vs. [permissive licensing](http://en.wikipedia.org/wiki/Permissive_license)
- [Tivoization](http://en.wikipedia.org/wiki/Tivoisation) in hardware
- the pernicious issue of [software patents](http://en.wikipedia.org/wiki/Software_patent).


It’s a minefield, people. All I’m saying is this: **the next time you release code into the wild, do your fellow developers a favor and pick a license – any license**.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[licensing](https://blog.codinghorror.com/tag/licensing/)
[software licenses](https://blog.codinghorror.com/tag/software-licenses/)
[open source](https://blog.codinghorror.com/tag/open-source/)
[code reuse](https://blog.codinghorror.com/tag/code-reuse/)
