---
title: "Beating CAPTCHAs with .NET code"
date: 2005-02-15
url: https://blog.codinghorror.com/beating-captchas-with-net-code/
slug: beating-captchas-with-net-code
word_count: 268
---

I stumbled across an interesting article outlining how to [beat the MSDN visual CAPTCHA](https://web.archive.org/web/20050306040202/http://www.mperfect.net/aiCaptcha/) algorithm with some .NET code. Unfortunately, the author (a Microsoft MVP) demonstrated his “crack” by testing it on the blogs of other MVPs:


> *(if you were one of the 94 people i comment spammed) sorry about that, and hope that you are not pissed. if you are new to my site, then you must realize that i like to stir things up every once in a while. if you’ve been here before, then i’m hoping you’ve got a smile on your face, and sort of expect stuff like this from me :) anyways, you were targeted for 2 reasons. 1) because your blog uses CAPTCHA to provide a false sense of security. 2) because we are members of the same group. so i know a handful of you (and know of most of you). could easily have done this against a bunch of strangers ... but did not think that that was a good idea. this is just my way of saying that we’ve got more work to do. i will not be comment spamming you anymore. unless you comment spam me back in retaliation ... and then i’ll have to blast you out of the water ...  just kidding.*


So, yeah, the author is kind of a jerk. And he has some problems with capitalization and punctuation, too. He tries to explain himself in the FAQ. Anyway, it’s interesting code that appears to leverage the continuous, unbroken lines of contrast between the characters and the background.

[security](https://blog.codinghorror.com/tag/security/)
[.net](https://blog.codinghorror.com/tag/net/)
[captcha](https://blog.codinghorror.com/tag/captcha/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
