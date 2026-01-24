---
title: "Phishing: The Forever Hack"
date: 2007-05-04
url: https://blog.codinghorror.com/phishing-the-forever-hack/
slug: phishing-the-forever-hack
word_count: 1226
---

Most of the hacking techniques described in the 1994 book [Secrets of a Super-Hacker](http://www.amazon.com/exec/obidos/ASIN/1559501065) are now laughably out of date. But not all of them. A few are not only still effective, but *far more* effective in the current era of ubiquitous internet access. As the author notes early in the book, some attacks are timeless:


> Hacking may seem harder than before, but it really isn’t. The *culture* may have become more aware of security, but the individual user still lives in a world of benign indifference, vanity, user-friendliness, and friendly-userness. Users who are in-the-know will always want to help the less fortunate ones who are not. Those who aren’t will seek the advice of the gurus. And so social engineering and reverse social engineering live on, as you shall discover in these pages.
> Ease of use will always rule. The “dumb” password will be a good guess for a long time to come. People just don’t choose “6Fk%810(@vbM-34trwX51” for their passwords.
> Add to this milieu the immense number of computer systems operating today, and the staggering multitudes of inept users who run them. In the past, computers were used by the techno-literate few. Now they are bought, installed, used, managed, and even programmed by folks who have a hard time getting their bread to toast light brown. I’m not denigrating them – I applaud their willingness to step into unfamiliar waters. I just wish (sort of) that they would *realize* what danger they put themselves in every time they act without security in mind.


I don’t think there’s any better illustration of the timelessness of social engineering hacks – and the vulnerability of unsophisticated mainstream users – than [phishing](http://en.wikipedia.org/wiki/Phishing). The results of a 2006 phishing study, [Why Phishing Works](https://web.archive.org/web/20070320001037/http://www.freakonomics.com/pdf/Why%20Phishing%20Works-1.pdf) (pdf), are truly sobering:

- Good phishing websites fooled 90% of participants.
- 23% of participants in the study did not look at the address bar, status bar, or the security indicators.
- On average, the participants incorrectly judged whether a website was real or a spoof 40% of the time.
- 15 out of 22 participants proceeded without hesitation when presented with popup warnings about fraudulent certificates.
- Neither education, age, sex, previous experience, nor hours of computer use showed a statistically significant correlation with vulnerability to phishing. Everyone was vulnerable.


Phishing is remarkably effective. Bear in mind that the users in this study were told in advance to **expect a mixture of real and fake websites**, so these results may actually be *better* than real world performance, as hard as that is to believe. Here’s a detailed breakdown of the test sites used in the study, along with the percent of users who were unable to correctly identify whether the site was real or a spoof:

kg-card-begin: html


|  |  |  | **% Wrong** |
| Bank of the West | Spoof | URL (bankofthevvest.com), padlock in content, Verisign logo and certificate validation seal, consumer alert warning | **91** |
| PayPal | Spoof | Uses Mozilla XML User Interface Language (XUL) to simulate browser chrome w/ fake address bar, status bar and SSL indicators | **81** |
| Etrade | Real | 3rd party URL (etrade.everypath.com), SSL, simple design, no graphics for mobile users | **77** |
| PayPal | Spoof | URL (paypal-signin03.com), padlock in content | **59** |
| PayPal | Spoof | URL (IP address), padlock in content | **59** |
| Capital One | Real | 3rd party URL (cib.ibanking-services.com), SSL, dedicated login page, simple design | **50** |
| PayPal | Spoof | Screenshot of legitimate SSL protected Paypal page within a rogue web page | **50** |
| Ameritrade | Spoof | URL (ameritrading.net) | **50** |
| Bank of America | Spoof | Rogue popup window on top of legitimate BOFA homepage, padlock in content | **36** |
| Bank of the West | Spoof | URL (IP address), urgent anti-fraud warnings (requests large amount of personal data) | **32** |
| USBank | Spoof | URL (IP address), padlock in content, security warnings, identity verification (requests large amount of personal data) | **32** |
| Ebay | Spoof | URL (IP address), account verification (requests large amount of personal data) | **32** |
| Yahoo | Spoof | URL (center.yahoo-security.net), account verification (requests large amount of personal data) | **23** |
| NCUA | Spoof | URL (IP address), padlock in content, account verification (requests large amount of personal data) | **18** |
| Ebay | Real | SSL protected login page, TRUSTe logo | **14** |
| Bank Of America | Real | Login page on non-SSL homepage, padlock in content | **14** |
| Tele-Bears (Student Accounts) | Real | SSL protected login page | **9** |
| PayPal | Real | Login page on non-SSL homepage, padlock in content | **9** |
| Bank One | Real | Login page on non-SSL homepage, padlock in content | **0** |


kg-card-end: html

There’s only one conclusion you can draw from the study’s results: **when presented with a spoofed web page, a large percentage of users will *always* fall for it.** Forever.


Once that spoofed page is up, even if we use the extraordinarily optimistic estimate that only 15 percent of users will fall for it, that’s still a tremendous number of users at risk. Given the poor statistics, the only mitigation strategy that makes sense is to somehow **prevent showing the spoofed page to the user**. The good news is that the latest versions of [Firefox](http://www.mozilla.com/en-US/firefox/phishing-protection/) and Internet Explorer have anti-phishing capabilities which do exactly that: they use real-time, distributed blacklists to prevent showing known spoof sites to users. I visited the [PhishTank](http://www.phishtank.com/index.php) site to gather a set of known phishing URLs to see how well these browsers perform.


Firefox may be using PhishTank as a source; every URL I visited showed the most severe warning, blocking the phishing site from the user behind a sort of smoked glass effect. Unfortunately, it’s all too easy to click the little red X and use the page. I don’t think it’s a good idea for this dialog to be so easily dismissable, like any other run of the mill dialog box.


![](https://blog.codinghorror.com/content/images/2025/03/image-244.png)


IE7 opened some of the recent phishing sites with no warnings at all. But a few triggered the heuristic check for “suspicious,” with a dropdown warning obscuring part of the site:


![](https://blog.codinghorror.com/content/images/2025/03/image-245.png)


Others made the IE7 blacklist and were blocked completely behind a gateway page. I prefer this to the Firefox approach; once the URL is reported as a phishing site, there’s absolutely no reason to show *any* of its content to the user.


![](https://blog.codinghorror.com/content/images/2025/03/image-246.png)


I’m [no fan of distributed blacklists](https://blog.codinghorror.com/whitelist-blacklist-greylist/), but I think they’re a necessary evil in this case. Throughout the last ten years of incremental browser security improvements, users have *always* been susceptible to spoof attacks. It doesn’t matter how many security warnings we present, or how much security browser chrome we wrap websites in. **Phishing is the forever hack.** If the phishing page is displayed at all, it invariably reels a large percentage of users in hook, line, and sinker. The *only* security technique that can protect users from phishing scams, it seems, is the one that prevents them from ever seeing the phishing page in the first place.

[phishing](https://blog.codinghorror.com/tag/phishing/)
[social engineering](https://blog.codinghorror.com/tag/social-engineering/)
[hacking](https://blog.codinghorror.com/tag/hacking/)
[cybersecurity](https://blog.codinghorror.com/tag/cybersecurity/)
[user awareness](https://blog.codinghorror.com/tag/user-awareness/)
