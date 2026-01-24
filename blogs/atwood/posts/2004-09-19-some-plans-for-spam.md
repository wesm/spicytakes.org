---
title: "Some Plan(s) for Spam"
date: 2004-09-19
url: https://blog.codinghorror.com/some-plans-for-spam/
slug: some-plans-for-spam
word_count: 1193
---

After struggling with spam e-mail for years the old fashioned way – highlight, DEL – I finally succumbed and installed [POPFile](http://popfile.sourceforge.net) on my server. POPFile uses a [Bayesian Filter](http://www.process.com/precisemail/bayesian_filtering.htm) technique and it is amazingly effective. Within a day I had 95% accuracy; within a week I had 97% accuracy. Two months later, I’m up to nearly 99% accuracy.


It’s interesting that Bayesian filtering is so effective, yet **most people never heard of it until mid 2002.** Spam has been around seemingly forever; why wasn’t this technique adopted sooner? I did some digging and came up with Paul Graham’s, [A Plan For Spam](http://www.paulgraham.com/spam.html). Paul is an interesting guy with a LISP background, and although he probably wasn’t the first person to think of using Bayesian techniques to fight spam, he was definitely the first person to stump for [a workable algorithm](http://www.paulgraham.com/better.html):


> *I don’t know why I avoided trying the statistical approach for so long. I think it was because I got addicted to trying to identify spam features myself, as if I were playing some kind of competitive game with the spammers. (Nonhackers don’t often realize this, but most hackers are very competitive.) When I did try statistical analysis, I found immediately that it was much cleverer than I had been. It discovered, of course, that terms like “virtumundo” and “teens” were good indicators of spam. But it also discovered that “per” and “FL” and “ff0000” are good indicators of spam. In fact, “ff0000” (html for bright red) turns out to be as good an indicator of spam as any pornographic term.
> But the real advantage of the Bayesian approach, of course, is that you know what you’re measuring. Feature-recognizing filters like SpamAssassin assign a spam “score” to email. The Bayesian approach assigns an actual probability. The problem with a “score” is that no one knows what it means. The user doesn’t know what it means, but worse still, neither does the developer of the filter. How many points should an email get for having the word “sex” in it? A probability can of course be mistaken, but there is little ambiguity about what it means, or how evidence should be combined to calculate it. Based on my corpus, “sex” indicates a .97 probability of the containing email being a spam, whereas “sexy” indicates .99 probability. And Bayes’ Rule, equally unambiguous, says that an email containing both words would, in the (unlikely) absence of any other evidence, have a 99.97% chance of being a spam.
> Because it is measuring probabilities, the Bayesian approach considers all the evidence in the email, both good and bad. Words that occur disproportionately rarely in spam (like “though” or “tonight” or “apparently”) contribute as much to decreasing the probability as bad words like “unsubscribe” and “opt-in” do to increasing it. So an otherwise innocent email that happens to include the word “sex” is not going to get tagged as spam.*


I know what you’re thinking now: say I’m a spammer. **How would I beat a Bayesian Filter? **Well, it’s possible, but it’s hard:

kg-card-begin: html

> Assuming they could solve the problem of the headers, the spam of the future will probably look something like this:
> Hey there.  Thought you should check out the following:
> [http://www.27meg.com/foo](https://web.archive.org/web/20061009185149/http://www.27meg.com/index.asp)
> because that is about as much sales pitch as content-based filtering will leave the spammer room to make. (Indeed, it will be hard even to get this past filters, because if everything else in the email is neutral, the spam probability will hinge on the url, and it will take some effort to make that look neutral.)
> Spammers range from businesses running so-called opt-in lists who don’t even try to conceal their identities, to guys who hijack mail servers to send out spams promoting porn sites. If we use filtering to whittle their options down to mails like the one above, that should pretty much put the spammers on the “legitimate” end of the spectrum out of business; they feel obliged by various state laws to include boilerplate about why their spam is not spam, and how to cancel your “subscription,” and that kind of text is easy to recognize.

kg-card-end: html

Digging through today’s email for examples – what about **messages with no text, only HTML images**?

kg-card-begin: html

```
Received: from host-122-195.firstpointsecure.com ([69.42.122.195]) by server.mydomain.com with Microsoft SMTPSVC(6.0.3790.0);
Sun, 19 Sep 2004 14:32:43 -0400
From: "Good News" <[email protected]>
To: me <[email protected]>
Subject: Single?
Date: Sun, 19 Sep 2004 11:32:56 -0800
MIME-Version: 1.0
Content-type: text/html; charset="ISO-8859-1"
Content-transfer-encoding: 7bit
Message-Id: <0771687B7E76766B477E707A6C346C697C7A70756C7A7A356A7674$4df803ge2@moquije.remarkablenews.com>
Return-Path: [email protected]
<html>
</head>
<body>
<p align="center"><a href="http://quugot.deliveredsavings.com/date3/?i=iog0771687b7e76766b4v&vj=jzv77e707a6c346c697c7ig&n=ksia70756c7a7a356a7674k&pq=vtyk&winner&_m01">
<img border="0" src="http://quugot.deliveredsavings.com/date3/at.gif" width="383" height="210"></a><br>
<br>
<br>
<br>
</p>
<p align="center">
<a href="http://quugot.deliveredsavings.com/date3/rd.cgi?i=iog0771687b7e76766b4v&vj=jzv77e707a6c346c697c7ig&n=ksia70756c7a7a356a7674k&pq=vtyk&winner&_m01">
<img border="0" src="http://quugot.deliveredsavings.com/date3/5.gif" width="502" height="59"></a></p>
<p align="center"></p>
<img src="http://quugot.deliveredsavings.com/date3/logogen.img?i=iog0771687b7e76766b4v&vj=jzv77e707a6c346c697c7ig&n=ksia70756c7a7a356a7674k&pq=vtyk" border=0>
</body>
</html>

```

kg-card-end: html

Or **messages with non-spam spoof text**?

kg-card-begin: html

```
<font size="2" face="Verdana">Stop this <a href="http://www.muss4267pinn.com/a.ddd">please</a>!</font><br>
<br>
christy passport nocturnal director cargoes corrigendum sicklewort doria polaroid <br>
<br>
```

kg-card-end: html

Interestingly, POPFile has no problem at all correctly categorizing these messages as spam. That’s the value of parsing the headers and the HTML, something early researchers failed to do. Graham cites this as the primary reason why Bayesian filtering wasn’t used prior to 2002. They didn’t think it was effective enough!


98.6 percent accuracy is good, one of the best available, but it’s not 100 percent. Can we do better with other spam fighting techniques? I agree with Graham’s position that [blacklists are both a bad idea and a losing battle](http://www.paulgraham.com/falsepositives.html), so I won’t even go there. Whitelists, on the other hand, are more interesting. Take a service like [SpamArrest](http://spamarrest.com), for example. This works like so:

1. Joe sends you an email.
2. An auto-generated response is sent to Joe, explaining that you are fighting spam, and that his email won’t be delivered until he visits the provided URL.
3. Joe clicks the URL, enters the [CAPTCHA](http://www.captcha.net) value, and clicks OK.
4. Joe’s email address is now verified human, and his email is delivered to you.
5. All further emails from Joe will arrive without this additional step.


This type of whitelist delivers damn near 100% effective spam blocking, with no training period required. There’s simply no way a machine can pass this test. **This works great if you commit to only accepting email from human beings. **The downside is, you still have to go through your spam folder to manually authorize any automated emails: newsletters, order confirmations, and so forth. Even though you’ve gone from 2% spam to 0% spam, you probably want to check your rejected email folder periodically.


Some people love whitelists. I’m not a fan. Putting the burden of verification on the sender seems kind of onerous to me. Even though it’s a one time thing, it is an additional hurdle for every person that wants to communicate with me. On the other hand, this type of anti-machine whitelist is a reasonable approach to an intractable problem. Bayes will always let *some* spam slip through, so it is arguably the only way to get an ironclad “100 percent” effective spam blocking.

[machine learning](https://blog.codinghorror.com/tag/machine-learning/)
[bayesian filter](https://blog.codinghorror.com/tag/bayesian-filter/)
[spam filtering](https://blog.codinghorror.com/tag/spam-filtering/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
