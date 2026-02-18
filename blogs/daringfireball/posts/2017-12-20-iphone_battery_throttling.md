---
title: "Apple Addresses Why Some iPhones With Older Batteries Are Benchmarking Slower"
date: 2017-12-20
url: https://daringfireball.net/2017/12/iphone_battery_throttling
slug: iphone_battery_throttling
word_count: 1142
---


[Matthew Panzarino, writing for TechCrunch](https://techcrunch.com/2017/12/20/apple-addresses-why-people-are-saying-their-iphones-with-older-batteries-are-running-slower/):


> Here’s a statement that Apple provided when I inquired about the
> power profile that people were seeing when testing iPhones with
> older batteries:
> “Our goal is to deliver the best experience for customers, which
> includes overall performance and prolonging the life of their
> devices. Lithium-ion batteries become less capable of supplying
> peak current demands when in cold conditions, have a low battery
> charge or as they age over time, which can result in the device
> unexpectedly shutting down to protect its electronic components.
> Last year we released a feature for iPhone 6, iPhone 6s and iPhone
> SE to smooth out the instantaneous peaks only when needed to
> prevent the device from unexpectedly shutting down during these
> conditions. We’ve now extended that feature to iPhone 7 with iOS
> 11.2, and plan to add support for other products in the future.”


Panzarino’s piece is (unsurprisingly) a good, sober look at the story. Basically, Apple is being painted in a *damned if they do, damned if they don’t* corner. Prior to adding this feature to iOS last year, iPhones with older declining batteries were shutting down unexpectedly when taxed at peak performance. That’s obviously not good. So now, iPhones with older declining batteries are throttled, when necessary, to keep them running. But now Apple faces accusations that they’re deliberately slowing these devices down to convince people to buy new iPhones. The thing to keep in mind is that there is nothing Apple can do about the fact that lithium-ion batteries decline over time. One way or another, older much-used iPhones are going to suffer in some way. I think what Apple is doing here is a reasonable balance between trade-offs.


I agree with Panzarino, though, that Apple should do a better job *communicating* about this:


> Apple should examine whether the gap between when the algorithm
> starts smoothing out the peaks of performance and when they’re
> notified that their performance is taking a hit due to battery age
> is too large. If a person is noticing (and it seems they are given
> the discussion threads and social activity on this) that their
> phone is running slower then they need to know *why*.
> The point at which iOS will tell you that your battery has gone to
> hell is currently very, *very* conservative. Perhaps this can be
> set to be more aggressive. Then, of course, users will complain
> that Apple is cash grabbing on battery replacements but humans
> will remain humans.


[James Thomson put it well](https://twitter.com/jamesthomson/status/943590508131209216):


> I get the whole “it’s better to clock your phone slower rather
> than have it randomly crash” aspect to this story. It’s more the
> fact that Apple wasn’t upfront about it, and thus we’ve all been
> telling people “no, your phone isn’t getting any slower”. Turns
> out, it was.


[An official battery replacement from Apple is only $79](https://support.apple.com/iphone/repair/service/pricing), and free under AppleCare. If more users with older iPhones knew that replacing the battery could restore the original performance, they might happily opt for that.


---


I’ve said the following [before](https://daringfireball.net/linked/2016/07/28/ipod-classic-obsolescence), but I’ll say it again: *Apple does not purposefully cripple older devices to encourage users to buy new devices.* Nor would it be in their long-term interest to do so. [As I wrote in 2013](https://daringfireball.net/2013/12/the_year_in_apple_and_technology):


> If older iPhones suffer upon being updated to iOS 7 — getting
> slower, or worse battery life, or [losing Wi-Fi](http://lessig.tumblr.com/post/65338904338/wow-or-from-the-when-apple-became-the-borg-department) — to such a
> degree that the users conclude they now need to buy a new phone,
> would not the most likely and logical result be that it would
> inspire many of them to switch to Android (or Windows Phone, or
> anything) rather than to buy another iPhone?
> If your car breaks down after just a few years, are you not more
> likely to replace it with a different brand? To posit that Apple
> customers are somehow different, that when they feel screwed by
> Apple their response is to go back for more, is “Cult of Mac”
> logic — the supposition that most Apple customers are irrational
> zealots or trend followers who just mindlessly buy anything with
> an Apple logo on it. The truth is the opposite: Apple’s business
> is making customers happy, and keeping them happy. They make
> products for discriminating people who have higher standards and
> less tolerance for design flaws or problems.


Apple products — including iPhones in particular — hold their resale value far better than those of any competitor. Apple products are designed to last *longer* than the industry standard, not less. When they fall short in this regard, it’s the result of a software bug or inadvertent component failure. I know for a fact that the widely-held belief that Apple booby-traps two-year-old iPhones drives Apple employees — ranging from engineers to senior executives — nuts, because the truth is the opposite. They really do knock themselves out trying to build and maintain products with lasting value.


And at the engineering level, I’ve heard from multiple Apple sources over the years that even if such a dictate were issued from on high, it would result in a revolt. If some shortsighted senior executive demanded that an iOS software update render older iPhone hardware artificially slow, the engineers tasked with the job would almost certainly object. Even if some unscrupulous engineer were willing to implement such a booby trap, how would they keep other engineers on the team from noticing it, fixing it, and figuring out who was responsible? Something along the lines of “`if (deviceAgeInYears > 2) { [self _runFuckingSlow]; }`” is going to stick out in code review after being checked into the iOS source code.


Would they resign in protest if their objections were ignored? Yes, actually, they would. Really. It’s not like software engineers with Apple experience on their resumes have a hard time getting job offers at other companies. Apple attracts people who are looking to do great work, period.


This is why the seemingly endless stream of stories about [malfeasance at Uber](https://www.recode.net/2017/12/15/16782534/alphabet-waymo-uber-self-driving-lawsuit-jacobs-letter-surveillance) is so pernicious for the entire industry. Obviously, some tech companies have executives who engage in underhanded, malicious, user-hostile ([if not downright illegal](https://www.theverge.com/2017/12/14/16778064/uber-criminal-investigation-confirm-doj-waymo)) strategies, and they have low-level employees willing to implement the plans. Given that Uber found engineers willing to create [a “god view” monitoring system](https://www.theguardian.com/technology/2016/dec/13/uber-employees-spying-ex-partners-politicians-beyonce) that allowed employees to spy on celebrities, politicians, and ex-boyfriends and girlfriends, it’s not hard to believe Apple could find engineers willing to make apps run slower on two-year-old iPhones. Such cynicism is understandable, but Apple is not Uber.



| **Previous:** | [First Impressions of the New iMac Pro](https://daringfireball.net/2017/12/imac_pro_first_impressions) |
| **Next:** | [Marzipan](https://daringfireball.net/2017/12/marzipan) |


PreviousNext