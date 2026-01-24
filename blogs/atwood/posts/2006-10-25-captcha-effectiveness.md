---
title: "CAPTCHA Effectiveness"
date: 2006-10-25
url: https://blog.codinghorror.com/captcha-effectiveness/
slug: captcha-effectiveness
word_count: 1166
---

If you’ve used the internet at all in the last few years, I’m sure you’ve seen your share of [CAPTCHAs](http://en.wikipedia.org/wiki/Captcha):


![](https://blog.codinghorror.com/content/images/2025/05/image-391.png)


Of course, nobody *wants* to use CAPTCHAs. They’re a necessary evil, just like the locks on the doors to your home and your car.


CAPTCHAs are designed to discriminate between computer scripts from spammers and real human beings. There’s a [popular misconception](https://web.archive.org/web/20070109223243/http://weblogs.asp.net/rhoward/archive/2006/07/19/Why-no-CAPTCHA_3F00_.aspx) in technical circles that CAPTCHA has been “broken”:


> CAPTCHA, which stands for (C)ompletely (A)utomated (P)ublic (T)uring test to tell (C)omputers and (H)umans (A)part, works well for small sites but larger ‘community’ sites where there are multiple SPAM targets CAPTCHA only provides a false sense of security – it can be broken fairly easily and serious spammers are getting more sophisticated all the time.


Some people actually believe that spammers can now “fairly easily” write scripts which use advanced [optical character recognition](http://en.wikipedia.org/wiki/Optical_character_recognition) to automatically defeat any online CAPTCHA form.


Although there have been a number of [CAPTCHA-defeating proof of concepts](http://en.wikipedia.org/wiki/Captcha#Computer_character_recognition) published, there is no practical evidence that these exploits are actually working in the real world. And **if CAPTCHA is so thoroughly defeated, why is it still in use on virtually every major website on the internet?** Google, Yahoo, Hotmail, you name it, if the site is even remotely popular, their new account forms are protected by CAPTCHAs.


The comment form of my blog is protected by what I refer to as “naïve CAPTCHA,” where *the CAPTCHA term is the same every single time*. This has to be the most ineffective CAPTCHA of all time, and yet it stops 99.9% of comment spam. I can count on two hands the number of manually entered comment spams I’ve gotten since I implemented it. Granted, Yahoo is more popular than my blog by many orders of magnitude. But it’s still strong evidence that moving the difficulty bar up even one tiny notch can be quite effective in reducing spam. I went from cleaning up comment spam every day to cleaning one per month. Big difference.


I’ve been experimenting with improving the rendering algorithms in my [CAPTCHA server control](https://web.archive.org/web/20071012022659/http://www.codeproject.com/aspnet/CaptchaControl.asp), and it’s interesting how fragile typical computer OCR really is. SimpleOCR has an online form that allows you to upload and [OCR small greyscale TIF images](http://www.simpleocr.com/Demo/). Here are the results of submitting a few standard 180x50 CAPTCHAs from my reworked rendering algorithm. Note that these CAPTCHAs all use the same font, Courier New.

kg-card-begin: html


| **OCR result** |  |
|  | Standard | CQXKN | 5/5 |
|  | Low perturbation | KxT*2 | 3/5 |
|  | Medium perturbation | acNx4 | 2/5 |
|  | High perturbation | Kc | 0/5 |
|  | Extreme perturbation | (blank) | 0/5 |
|  | Standard, low noise | (blank) | 0/5 |


kg-card-end: html

I didn’t expect it to do well, but I was frankly surprised how poorly the SimpleOCR engine actually performed. **Adding a tiny bit of noise or perturbation to the CAPTCHA text was all it took to break the OCR**. I’m sure there are more advanced OCR engines out there that might be able to do somewhat better than the free SimpleOCR engine. Still, it’s unlikely that any OCR engine could beat high perturbation – where the characters are *physically overlapping each other* – plus a little background noise. And that level of CAPTCHA security is absolute overkill unless you happen to run one of the top 100 most popular sites on the internet. Furthermore, none of these are particularly difficult CAPTCHAs. The most extreme perturbation sample shown above is eminently “human solvable,” at least in my opinion.


The default settings for my new and improved CAPTCHA server control, a combination of…

- high contrast for human readability
- medium, per-character perturbation
- random fonts per character
- low background noise


… should be *far* more protection than most websites need.


![](https://blog.codinghorror.com/content/images/2025/05/image-392.png)


Remember, I use “naïve CAPTCHA” with 99.9% effectiveness. The low settings will be even easier to read than the defaults and may be more appropriate for your user base.


Of course, OCR isn’t the only way to attack CAPTCHA. But the other scenarios for spammers “beating” CAPTCHA are even more far-fetched. The [Petmail documentation](http://petmail.lothar.com/design.html#auto34) explains:


### 1. The Turing Farm


> Let’s say spammers set up a sweatshop to employ people to look at computer screens and answer CAPTCHA challenges. They get to send one message for each challenge passed. Assuming 10 seconds per challenge, and paying roughly $5 per hour, that represents $14 per thousand messages. A typical spam run of 1 million messages per day would cost $14,000 per day and require 116 people working 24/7.
> This would break the economic model used by most current spammers. A recent Wired article showed one spammer earning $10 for each successful sale. At that rate, the cost of $14,000 for 1,000,000 spam emails requires a 1 in 1000 success rate just to break even, whereas current spammers are managing a 1 in 100,000 or even 1 in 1,000,000 success rate.


### 2. The Turing Porn Farm


> A [recent slashdot article](http://yro.slashdot.org/yro/04/01/28/1344207.shtml) described a trick in which spammers run a porn site that is gated by CAPTCHA challenges, which are actually ripped directly from Yahoo’s new account creation page. The humans unwittingly solve the challenge on behalf of the spammers, who can therefore automate a process that was meant to be rate-limited to humans. This attack is simply another way of paying the workers of a Turing Farm. The economics may be infeasible because porn hosting costs money too.


If you’re not using CAPTCHAs because you think they’re compromised, then you’re too gullible for your own good. There’s absolutely no concrete data supporting any of these attack scenarios happening outside laboratory (read: infinite money and time) conditions. Just [ask Google](https://web.archive.org/web/20061107205407/http://online.wsj.com/public/article/SB114903737427467003-BFXQeLeq3RdZ5Icuyb8gkda47DA_20070530.html):


> Some captchas have been solved with more than 90% accuracy by scientists specializing in computer vision research at the University of California, Berkeley, and elsewhere. Hobbyists also regularly write code to solve captchas on commercial sites with a high degree of accuracy.
> But several Internet companies say their captchas appeared to be highly effective at thwarting spammers. “Researchers are really good, and the attackers really are not,” says Mr. Jeske of Google, based in Mountain View, Calif. “Having these methods in place we find extremely effective against automated malicious attackers.”


The real secret to CAPTCHA is that it hits spammers where they are most vulnerable: **in the pocketbook**. The minute you put up a computational barrier, the entire economic model of spam comes crashing down.


Now if you’d prefer not to use CAPTCHA because it’s *an inconvenience for the user*, I can respect that. **CAPTCHA isn’t the only way to block spammers. **But give CAPTCHA its due: it was one of the [original spam blocking measures](https://web.archive.org/web/20061206020724/http://www2.parc.com/istl/projects/captcha/history.htm) used way back in 1997 by AltaVista. And, even more impressively, it’s still one of the most effective ways to block spam at its source *today*.

[security](https://blog.codinghorror.com/tag/security/)
[captcha](https://blog.codinghorror.com/tag/captcha/)
[spam](https://blog.codinghorror.com/tag/spam/)
[internet](https://blog.codinghorror.com/tag/internet/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
