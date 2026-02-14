---
title: "We tried that, didn’t work"
date: 2023-10-13
url: https://world.hey.com/dhh/we-tried-that-didn-t-work-d9c42fe1
slug: we-tried-that-didn-t-work-d9c42fe1
word_count: 593
---

In our quest for making programming simpler, faster, and prettier, no logical fallacy provides as much of an obstacle as “we tried that, didn’t work”. The fallacy that past failed attempts dictates the scope of what's possible.
That just because someone, somewhere, one time attempted something similar and failed, nobody else should try. That lowering our collective ambition to whatever was unachievable by others is somehow good.
There would be no human progress if we all quit trying after any unsuccessful attempt.
This fallacy is bad enough when it talks about what hasn’t yet successfully been achieved, but it’s downright bewildering when it’s trotted out to refute the reality of what’s already been proven possible.
Take the example of building fast, modern web applications with
[#NoBuild JavaScript](https://world.hey.com/dhh/you-can-t-get-faster-than-no-build-7a44131c)
. We've been running
[HEY](https://hey.com/)
without bundling or compiling JavaScript for three years now (you can
[sign up](https://app.hey.com/sign_up)
and
[View Source](https://m.signalvnoise.com/paying-tribute-to-the-web-with-view-source/)
to see exactly how!). We have tens of thousands of happy, paying customers, and we've made millions in profits from this product. Yet
[certain quarters](https://x.com/cramforce/status/1712265070213050390?s=20)
of the dev discourse continue to insist what we've done isn't possible. Wat?
It's like insisting your map is correct even after it failed to record the massive mountain you're literally staring at. Refusing to believe reality because it doesn't comport to your mental model of the world is an intellectual failure state.
Part of that outdated mental map of what's possible on the web includes the notion that #NoBuild JavaScript inevitably leads to slow applications. That you'll drown in the waterfall of requests cascading through your dependencies. Here's a report from Google's web performance tool Lighthouse. HEY literally gets a perfect 100/100 score on performance:

![F8QLrHdXsAAqr9D.jpeg](https://world.hey.com/dhh/d9c42fe1/representations/eyJfcmFpbHMiOnsiZGF0YSI6MTM5NDA5MzQ4NywicHVyIjoiYmxvYl9pZCJ9fQ--20e512bdfbc906564af7b3ccb11cba82b3b0b478c6c8737e5fe50fc282de458a/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGVnIiwicmVzaXplX3RvX2xpbWl0IjpbMzg0MCwyNTYwXSwicXVhbGl0eSI6NjAsImxvYWRlciI6eyJwYWdlIjpudWxsfSwiY29hbGVzY2UiOnRydWV9LCJwdXIiOiJ2YXJpYXRpb24ifX0--86fa621099aa99aa0c7ae156d97d21b387d30fa6ac57aa5c89948af503464a06/F8QLrHdXsAAqr9D.jpeg)

Now yes, that's because HEY is built differently from, say, Khan Academy or Vercel. We don't have hundreds of dependencies or thousands of JavaScript files. We send about ~100 individual JavaScript files over HTTP/2, and only rely on a handful of external libraries, mostly
[Hotwire](https://hotwired.dev)
.
That's how progress usually happens! By someone doing something different than whoever went before them in pursuit of the same goal. But instead of recognizing that, and perhaps becoming just a bit curious at how it was done, the "we tried that, didn't work" fallacy sucks people into the small world of "can't".
Making programming better requires a willingness to test your priors. To question your assumptions. To recognize the half-life of facts. Yes, how we built HEY wasn't feasible prior to 2020,
[before import maps opened the door](https://world.hey.com/dhh/modern-web-apps-without-javascript-bundling-or-transpiling-a20f2755)
. So if your mental model of the web is soaked in the possibilities of 2010-2020, I understand your skepticism, but please don't let it restrict your ability to appreciate the progress happening now.
None of this is an argument that everyone should follow us into this glorious #NoBuild future. I've retired from trying to convince anyone who's happily making stuff with other tools that they must change their ways. I'm sharing how we're building HEY because it not only works, but works exceptionally well for us. Do with that testimony and technology as you please.
But when you're building with small teams, or even alone, you need all the
[conceptual compression](https://www.youtube.com/watch?v=zKyv-IGvgGE&t=1037s)
you can get. Nothing compresses what you need to know like removing an entire step from the equation.
That's always been what excited my about building for the web, from Ruby on Rails through Hotwire through everything. Making programmers more effective by reducing the amount of moving parts they have to learn and wrestle with on the daily.
Don't get stuck in the mud of complexity.
