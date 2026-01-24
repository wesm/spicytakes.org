---
title: "Dictionary Attacks 101"
date: 2009-01-07
url: https://blog.codinghorror.com/dictionary-attacks-101/
slug: dictionary-attacks-101
word_count: 914
---

Several high profile Twitter accounts [were recently hijacked](https://web.archive.org/web/20090108041718/http://blog.wired.com/27bstroke6/2009/01/professed-twitt.html):


> An 18-year-old hacker with a history of celebrity pranks has admitted to Monday’s hijacking of multiple high-profile Twitter accounts, including President-Elect Barack Obama’s, and the official feed for Fox News.
> The hacker, who goes by the handle GMZ, told Threat Level on Tuesday he gained entry to Twitter’s administrative control panel by pointing an automated password-guesser at a popular user’s account. The user turned out to be a member of Twitter’s support staff, who’d chosen the weak password “happiness.”
> Cracking the site was easy, because **Twitter allowed an unlimited number of rapid-fire log-in attempts**.
> “I feel it’s another case of administrators not putting forth effort toward one of the most obvious and overused security flaws,” he wrote in an IM interview. “I’m sure they find it difficult to admit it.”


If you’re a moderator or administrator it is *especially* negligent to have such an easily guessed password. But the real issue here is the way Twitter allowed unlimited, as-fast-as-possible login attempts.


Given the **average user’s password choices** – as documented by Bruce [Schneier’s analysis](https://web.archive.org/web/20090209035850/http://www.schneier.com/blog/archives/2006/12/realworld_passw.html) of 34,000 actual MySpace passwords captured from a [phishing attack](https://blog.codinghorror.com/phishing-the-forever-hack/) in late 2006 – this is a pretty scary scenario.


![](https://blog.codinghorror.com/content/images/2025/04/image-261.png)


![](https://blog.codinghorror.com/content/images/2025/04/image-260.png)


Based on this data, the average MySpace user has an 8 character alphanumeric password. Which isn’t great, but doesn’t sound *too* bad. That is, until you find out that 28 percent of those alphanumerics were all lowercase with a single final digit – and two-thirds of the time that final digit was 1!


Yes, brute force attacks are [still for dummies](https://blog.codinghorror.com/brute-force-key-attacks-are-for-dummies/). Even the typically terrible MySpace password – eight character all lowercase, ending in 1, would require around 8 billion login attempts:

kg-card-begin: html

```

26 x 26 x 26 x 26 x 26 x 26 x 26 x 1  = 8,031,810,176

```

kg-card-end: html

At one attempt per second, that would take more than 250 years. *Per user!*


But a [dictionary attack](http://en.wikipedia.org/wiki/Dictionary_attack), like the one used in the Twitter hack? Well, that’s another story. The entire Oxford English Dictionary contains around 171,000 words. As you might imagine, the average person only uses a tiny fraction of those words, by some estimates somewhere [between 10 and 40 thousand](http://www.worldwidewords.org/articles/howmany.htm). At one attempt per second, we could try **every word in the Oxford English Dictionary in slightly less than two days**.


Clearly, the *last* thing you want to do is give attackers carte blanche to run unlimited login attempts. All it takes is one user with a weak password to provide attackers a toehold in your system. In Twitter’s case, the attackers really hit the jackpot: the user with the weakest password happened to be a member of the Twitter administrative staff.


**Limiting the number of login attempts per user is security 101.** If you don’t do this, you’re practically setting out a welcome mat for anyone to launch a dictionary attack on your site, an attack that gets statistically more effective every day the more users you attract. In some systems, your account can get locked out if you try and fail to log in a certain number of times in a row. This can lead to denial of service attacks, however, and is generally discouraged. It’s more typical for each failed login attempt to take longer and longer, like so:

kg-card-begin: html


| 1st failed login | no delay |
| 2nd failed login | 2 sec delay |
| 3rd failed login | 4 sec delay |
| 4th failed login | 8 sec delay |
| 5th failed login | 16 sec delay |


kg-card-end: html

And so on. Alternately, you could display a [CAPTCHA](http://en.wikipedia.org/wiki/Captcha) after the fourth attempt.


There are endless variations of this technique, but the net effect is the same: attackers can only try a handful of passwords each day. A brute force attack is out of the question, and a broad dictionary attack becomes impractical, at least in any kind of human time.


It’s tempting to blame Twitter here, but honestly, I’m not sure they’re alone. I [forget my passwords a lot](https://blog.codinghorror.com/the-login-explosion/). I’ve made at least five or six attempts to guess my password on multiple websites and I can’t recall ever experiencing any sort of calculated delay or account lockouts. I’m reasonably sure the big commercial sites have this mostly figured out. But since every rinky-dink website on the planet demands that I create [unique credentials especially for them](https://blog.codinghorror.com/openid-does-the-world-really-need-yet-another-username-and-password/), any of them could be vulnerable. **You better hope they’re *all* smart enough to throttle failed logins** – and that you’re careful to use unique credentials on every single website you visit.


Maybe this was less of a problem in the [bad old days of modems](https://blog.codinghorror.com/do-modems-still-matter/), as there were severe physical limits on how fast data could be transmitted to a website, and how quickly that website could respond. But today, we have the one-two punch of naïve websites running on blazing fast hardware, and users with speedy broadband connections. Under these conditions, I could see attackers regularly achieving up to two password attempts per second.


If you thought of dictionary attacks as mostly a desktop phenomenon, perhaps it’s time to revisit that assumption. As Twitter illustrates, the web now offers ripe conditions for dictionary attacks. I urge you to test your website, or any websites you use – and **make sure they all have some form of failed login throttling in place.**

[security](https://blog.codinghorror.com/tag/security/)
[dictionary attacks](https://blog.codinghorror.com/tag/dictionary-attacks/)
[hacking](https://blog.codinghorror.com/tag/hacking/)
[password guessing](https://blog.codinghorror.com/tag/password-guessing/)
[cybersecurity](https://blog.codinghorror.com/tag/cybersecurity/)
