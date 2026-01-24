---
title: "Rate Limiting and Velocity Checking"
date: 2009-02-23
url: https://blog.codinghorror.com/rate-limiting-and-velocity-checking/
slug: rate-limiting-and-velocity-checking
word_count: 1260
---

Lately, I’ve been seeing these **odd little signs** pop up in storefronts around town.


![](https://blog.codinghorror.com/content/images/2025/04/image-302.png)


All the signs have various forms of this printed on them:


> Only 3 students at a time in the store please


We took that picture at a 7-11 convenience store which happens to be near a high school, so maybe the problem is particularly acute there. But even farther into town, the same signs appear with disturbing regularity. I’m guessing the store owners must consider these rules necessary because:

- teenage students are more likely to shoplift than most customers
- with many teenage students in the store, it’s difficult for the owners to keep an eye on everyone, which further increases the likelihood of shoplifting.


I’m just guessing; I don’t own a store. But like the “no elephants” sign, it must be there to [address a real problem](http://www.joelonsoftware.com/uibook/chapters/fog0000000059.html).


> When you go into a restaurant and see a sign that says “No Dogs Allowed,” you might think that sign is purely proscriptive: Mr. Restaurant doesn’t like dogs around, so when he built the restaurant he put up that sign. If that was all that was going on, there would also be a “No Snakes” sign; after all, nobody likes snakes. And a “No Elephants” sign, because they break the chairs when they sit down. The real reason that sign is there is historical: it is a historical marker that indicates that people used to try to bring their dogs into the restaurant


All these signs are enough to make me **question the ethics of high school students in groups of 3 or more**. Although, to be fair, I’ve seen some really shifty looking graduate students in my day.


In truth, these kinds of limits are *everywhere*; they’re just not as obvious because there’s often no signage trail to follow.

- Most ATMs only allow you to withdraw $300 cash maximum in one day.
- Free email accounts typically limit how many emails can be sent per day.
- Internet providers limit individual download and upload speeds to ensure they aren’t overselling their bandwidth.
- There’s a maximum on how many Xbox Live Points you can add to your account per day. ([All 500+ Rock Band songs](http://en.wikipedia.org/wiki/Downloadable_content_in_Rock_Band) aren’t going to download themselves, after all.)


I’m sure you can think of lots of other real world examples. They’re all around you.


There are people who act like groups of rampaging teenage students online, too, and we deal with them in the same way: by **imposing rate limits!** Consider how Google limits any IP address that’s [submitting “too many” search requests](http://googleonlinesecurity.blogspot.com/2007/07/reason-behind-were-sorry-message.html):

kg-card-begin: html

> Several things can trigger the sorry message.
>       Often it’s due to infected computers or DSL routers that proxy search traffic through your network – this may be at home or even at a workplace where one or more computers might be infected.
>       Overly aggressive SEO ranking tools may trigger this message, too. In other cases, we have seen self-propagating worms that use Google search to identify vulnerable web servers on the Internet and then exploit them.
>       The exploited systems in turn then search Google for more vulnerable web servers and so on. This can lead to a noticeable increase in search queries and *sorry* is one of our mechanisms to deal with this.

kg-card-end: html

I did [a bit of Google scraping](https://blog.codinghorror.com/stop-me-if-you-think-youve-seen-this-word-before/) once for a small research project, but I never ran into the CAPTCHA limiter. I think that entry predates its appearance. But it does make you wonder what typical search volumes are, and how they’re calculated. **Determining how much is “too much” – that’s the art of rate limiting**. It’s a tricky thing, even for the store owner:

- Couldn’t three morally bankrupt students shoplift just as effectively as four?
- How do you tell who is a student? Is it based purely on perception of age?
- Do we expect this rule to be self-enforcing? Will the fourth student walk into the store, identify three other students, and then decide to leave?


Rate limiting isn’t always a precise science. But it’s *necessary*, even with the false positives – consider how dangerous a login entry with [no limits on failed attempts](https://blog.codinghorror.com/dictionary-attacks-101/) could be. This is especially true once your code is connected to the internet. Human students can be a problem, but there’s a practical limit to how many students can fit in a store, and how fast they can physically shoplift your inventory. But **what if those “students” were an infinite number of computer programs, capable of stealing items from your web store at a rate only limited by network bandwidth?** Your store would be picked clean in a matter of minutes. Maybe even seconds!


Not having any sort of rate limiting in your web application is an open invitation to abuse. Even the most innocuous of user actions, if done rapidly enough and by enough users, could have potentially disastrous effects.


Even after you’ve instituted a rate limit, you can still get in trouble. On Stack Overflow, we [designed for evil](https://blog.codinghorror.com/designing-for-evil/). We have a Google-style rate limiting CAPTCHA in place, along with a variety of other bot defeating techniques. They’d been working well so far. But what we failed to consider was that a determined (and apparently ultra-bored) *human* user could sit there and [solve CAPTCHAs as fast](http://blog.stackoverflow.com/2009/02/new-question-answer-rate-limits/) as possible to spam the site.


And thus was born a new user based limit. I suppose we could create a little sign and hang it outside our virtual storefront:


> Only 1 question per new user every 10 minutes, please.


There are a few classes of rate limiting or velocity checking you can do:

1. **Per user or API key**. Ensure that any given user account or API account key holder can only perform (n) actions per minute. This is usually fairly safe, though it won’t protect you from a user who automates the creation of 100 puppet accounts to do their bidding. It all depends how strictly you tie identity to the API key or user; you can easily ban, or in the worst case, track down the culprits and ask them to desist.
2. **Per IP address**. Ensure that any given IP address can only perform (n) actions per minute. This works well in the typical case, but can cause problems for multiple users who happen to be behind a proxy that makes them appear to you as the “same” IP address. This is the only method possible on mostly anonymous sites like Craigslist, and it definitely works, because I’ve been on [the receiving end of it](http://www.codinghorror.com/craigslist/). Example implementations are mod_evasive for Apache, or the [IIS7 Dynamic IP Restriction module](https://web.archive.org/web/20090306160147/http://learn.iis.net/page.aspx/548/using-dynamic-ip-restrictions/).
3. **Per global action**. Ensure that a particular action can only happen (n) times per minute. Kind of the nuclear option, so obviously must be used with care. Can make sense for the “big red launch button” administrator functions which should be extraordinarily rare – until a malicious user happens to gain administrator rights and starts pushing that big red button over and over.


I was shocked how little comprehensive information was out there on rate limiting and velocity checking for software developers, because **they are your first and most important line of defense against a broad spectrum of possible attacks**. It’s amazing how many attacks you can mitigate or even *defeat* by instituting basic rate limiting.


Take a long, hard look your own website – how would it deal with a roving band of bored, morally ambiguous schoolkids?

[security](https://blog.codinghorror.com/tag/security/)
[rate limiting](https://blog.codinghorror.com/tag/rate-limiting/)
[velocity checking](https://blog.codinghorror.com/tag/velocity-checking/)
