---
title: "Has CAPTCHA Been “Broken?”"
date: 2007-11-20
url: https://blog.codinghorror.com/has-captcha-been-broken/
slug: has-captcha-been-broken
word_count: 817
---

A recent Wall Street Journal describes [Ticketmaster’s problems with online scalpers](http://online.wsj.com/public/article/SB119153995723149557.html):


> The Internet era has brought speed and convenience to all sorts of consumer transactions. For concertgoers, however, it has also led to ever-faster sellouts for hot events. Ticketmaster deploys technology that is supposed to stop brokers from gaining access to large numbers of seats via online sales. But it says brokers’ software circumvents the company’s protections.
> That has placed large numbers of seats in the hands of brokers who use eBay Inc.’s StubHub, Craigslist and other online venues to resell the tickets at a big mark up.
> One situation roiling consumers involves the 54-concert “Best of Both Worlds” tour in which singer-actress Miley Cyrus is performing sets as herself and as her fictional alter ego, Hannah Montana. Parents and children have found finding tickets for the shows difficult and expensive. The issue is drawing the attention of government officials. On Thursday – in a rare Internet-age example of authorities enforcing anti-scalping laws – the attorneys general of Missouri and Arkansas filed lawsuits against people accused of illegally reselling Hannah Montana tickets.
> According to StubHub, tickets for “Best of Both Worlds” are currently selling for an average $237, making them pricier than seats for the Police ($209), Justin Timberlake ($182) and Beyoncé ($212). The highest face value for a ticket on the Hannah Montana tour: $63.


They must have *really* pissed off some high ranking political parents to get that kind of attention. Not that they don’t deserve it – scalpers are evil, profiteering bastards, to be sure. They deserve all the pain we can send their way.


The “technology that is supposed to stop brokers” they’re referring to is [CAPTCHA](http://en.wikipedia.org/wiki/Captcha).


> For instance, companies like Ticketmaster require customers searching for tickets online to replicate a set of the squiggly letters and numbers, known as a “Captcha.” Theoretically, only human customers can correctly identify the characters despite the odd fonts, screening out automated purchasing programs. But RMG’s software, according to Mr. Kovach, can also “figure out the randomly generated characters and retype them automatically.” Mr. Kovach said RMG employees also gave him advice on fooling Ticketmaster’s computers into thinking his requests were coming from different Internet addresses. Neither Mr. Kovach nor his lawyer could be reached for comment.


So if online scalpers are somehow beating the system, does that mean CAPTCHA has been broken? I covered this topic a year ago, and my opinion has not changed. **If CAPTCHAs were well and truly broken, Google, Yahoo, and Hotmail would stop using them.** Why would they continue to use something that doesn’t work? I’m not going to rehash all the arguments here, but if you have strong feelings on this topic, I urge you to [read my earlier post](https://blog.codinghorror.com/captcha-effectiveness/) before commenting.


Ticketmaster’s problem is that their CAPTCHA is *not good enough*. Programmers don’t seem to understand what makes a CAPTCHA difficult to “break.” But it’s not difficult to find out. Heck, the hackers themselves will *tell* you how to do CAPTCHA correctly if you just know where to look. For example, this Chinese hacker’s page breaks down [a number of common CAPTCHAs](https://web.archive.org/web/20071127115550/http://www.lafdc.com/captcha/), and the price of software he sells to defeat them at a certain percentage success rate:

kg-card-begin: html


| the9
100%
$500 |  |
| dvbbs
95%
$1,000 |  |
| Shanda
90%
$1,500 |  |
| Baidu
80%
$3,000 |  |
| eBay
70%
$4,000 |  |
| Ticketmaster
50%
$6,000 |  |
| Google
(unbreakable) |  |
| Hotmail
(unbreakable) |  |
| Yahoo
(unbreakable) |  |


kg-card-end: html

It seems an awful lot of programmers subscribe to the “add some crazy patterns and/or colors to the text and pray for the best” school of CAPTCHA design. That’s not only sloppy, it just doesn’t work. The top of this chart is littered with their failed attempts. On some sites, this is OK. They don’t need the same world-class level of protection from bots and scripts that Ticketmaster does – there’s tremendous financial incentive for scalpers to break their system.


This particular hacker estimates a 50% success rate against the Ticketmaster captcha, long before the above article was published. No wonder those parents weren’t able to buy their kids Hannah Montana tickets – **it’s not because of failings in CAPTCHA protection, it’s because the Ticketmaster programmers failed to implement CAPTCHA correctly.**


Instead of hacking together their own partially effective (and often [not even human solvable](https://web.archive.org/web/20080516051449/http://forums.worsethanfailure.com/forums/post/116253.aspx)) CAPTCHA, what Ticketmaster’s programmers *should* have done is studied prior art – in particular, by outright copying the high-volume, extensively researched Yahoo, Google, and Hotmail CAPTCHAs. I’m awfully fond of Google’s CAPTCHA technique; in my professional opinion, it is simultaneously the most readable and the most hellishly difficult to OCR correctly. If you need industrial strength protection from bots and scripts, *that’s* where you want to start.

[e-commerce](https://blog.codinghorror.com/tag/e-commerce/)
[online security](https://blog.codinghorror.com/tag/online-security/)
[ticket scalping](https://blog.codinghorror.com/tag/ticket-scalping/)
[software vulnerabilities](https://blog.codinghorror.com/tag/software-vulnerabilities/)
[online transactions](https://blog.codinghorror.com/tag/online-transactions/)
