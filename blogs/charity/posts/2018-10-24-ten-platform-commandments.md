---
title: "Ten Platform Commandments"
date: 2018-10-24
url: https://charity.wtf/2018/10/24/ten-platform-commandments/
word_count: 619
---


On Monday I gave a talk at DOES18 called “All the World’s a Platform”, where I talked about a bunch of the lessons learned by using and abusing and running and building platforms at scale.


I promised to do a blog post with the takeaways, so here they are.


**Platform Commandment #1:** Any time you have to think about one particular user, you have failed in some way.  It doesn’t scale.  Just a few one-offs a day will drag you down and drown your forward momentum.


Corollary: you will always have to do this every day.  Solution: turn one-offs into a support problem, not an engineering problem.


**Platform Commandment #2**: keep your critical path as small and independent as possible.  Have explicit tiers of importance.  You cannot care about everything equally, sacrifices must be made.


Example: at Parse the core API was tier 1, push was tier 2, website was somewhere down around tier 10.  We always knew what to bring up and care about first.


**Platform Commandment #3**: It is the job of the platform to protect itself at all costs, including at the expense of your app.


**Platform Commandment #4:** Remember that your platform is a magical black box to your users.  You can’t expect them to behave reasonably without feedback loops and a rich mental model.  Help them out — esp your super-users.  It will save you time if you can help them help themselves.


**Platform Commandment #5**: Always expose a visible request id, shard id, uuid, trace id, any other relevant diagnostic information in user-visible errors.  Up to the point where it reveals too much exploitable information about your service, which is probably much farther than you think.  Poorly obfuscated infrastructure decisions are usually less of a threat to your business than befuddled users are.


**Platform Commandment #6**: Your observability must center your users’ perspective, not your own.  The health of the system doesn’t matter.  The health of every request, and every high-cardinality grouping of requests — those are what matter.


You must be able to care about and inspect the perf and quality from the perspective of every single application and/or user and their users, as richly as though theirs was the *only* application.  In real-time.


Dashboards are practically useless unless you can drill down into them.  Top-10 lists are useless — your biggest customers may not be your most important customers.


Solution**:** Invest in tooling (like Honeycomb) that lets you slice and dice on dimensions of arbitrary cardinality, so you can do things like a) break down by one uuid out of millions, b) break down by endpoint, latency percentile, raw query, data store, etc — to see what the experience actually looks like for that user, not for a high level aggregate like a dashboard.


**Platform Commandment #7**: Use end-to-end checks to traverse all the key code paths and architecture paths.


You will be tempted to disable them because they seem flappy and flaky and need to be fixed.  But this is actually what your users are suffering through every day they use your platform.  Don’t disable them, *fix them.*


**Platform Commandment #8:** Invest early in every kind of throttle, blacklist, velvet rope, in-flight rewrite, custom url/error responder, content inspection, etc … both partial and total, for every slice of events or users.  You will need all these fine-grained controls to keep your platform alive for 99.9% of users while you debug the .1% who are outliers and bad actors.


**Platform Commandment #9:** And use a multi-threaded language ffs.


**Platform Commandment #10**: USE YOUR OWN PLATFORM.  For work, if possible.  Feel the pain that you inflict on others.


**Bonus Commandment**: all cotenancy isolation guarantees are bullshit**


**from a perf standpoint, not security
