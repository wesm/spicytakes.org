---
title: "Shipping Software Should Not Be Scary"
date: 2018-08-19
url: https://charity.wtf/2018/08/19/shipping-software-should-not-be-scary/
word_count: 1515
---


On twitter this week, @[srhtcn](http://twitter.com/srhtcn) noted that “Many incidents happen during or right after release” and asked for advice on ways to fix this.


And he’s right!  Rolling out new software is the proximate cause for the overwhelming majority of incidents, at companies of all sizes.  Upgrading software is both a necessity and a minor insanity, considering how often it breaks things.


I’m not going to recap the [history of continuous integration and delivery,](https://circleci.com/blog/a-brief-history-of-devops-part-iv-continuous-delivery-and-continuous-deployment/) suffice it to say that we now know that smaller and more frequent changes are much safer than larger and less frequent changes.


But it’s still risky.  And most issues are still caused by humans and our pesky need for “improvements”.  So what can be done?


## It’s not ok for software releases to be scary and hazardous


First of all: **If releasing is risky for you, you need to fix that**.  Make this a priority.  Track your failures, practice post mortems, evaluate your on call practices and culture.  Know if you’re getting better or worse.  This is a project that will take weeks if not months until you can be confident in the results.


You *have* to fix it though, because these things are self-reinforcing.  If shipping changes is scary and fraught, people will do it less and it will get even MORE scary and treacherous.


Likewise, if you turn it into a non-cortisol inducing event and set expectations, engineers will ship their code more often in smaller diffs and therefore break the world less.


Fixing deploys isn’t about eliminating errors, it’s about **making your pipeline resilient** to errors.  It’s fundamentally about detecting common failures and recovering from them, without requiring human intervention.


## Value your tools more


As an short term patch, you should run deploys in the mornings or whenever everyone is around and fresh.  Then take a hard look at your deploy pipeline.


In too many organizations, deploy code is a technical backwater, an accumulation of crufty scripts and glue code, forked gems and interns’ earnest attempts to hack up Capistrano.  It usually gives off a strong whiff of “sloppily evolved from many 2 am patches with no code review”.


This is insane.  **Deploy software is the most important software** you have.  Treat it that way: recruit an owner, allocate real time for development and testing, bake in metrics and track them over time.


If it doesn’t have an owner, it will never improve.  And you will need to invest in frequent improvements even after you’re over this first hump.

- **Signal high organizational value** by putting one of your best engineers on it.
- Recruit help from the design side of the house as well.  The “right” thing to do must be the fastest, easiest thing to do, with friendly prompts and good docs.  No “shortcuts” for people to reach for at the worst possible time.  You need user research and design here.
- Track how often deploys fail and why.  Managers should pay close attention to this metric, just like the one for people getting interrupted or woken up, and allocate time to fixing this early whenever it sags.  ***Before* it gets bad**.
- Allocate real time for development, testing, and training — don’t expect the work to get shoved into people’s “spare time” or post mortem cleanup time.  Make sure other managers understand the impact of this work and are on board.  Make this one of your KPIs.


In other words, **make deploy tools a first class citizen** of your technical toolset.  Make the work prestigious and valued — even aspirational.  If you do performance reviews, recognize the impact there.


(Btw, “how we hardened our deploys” is total Velocity-bait (&& other practitioner conferences) as well as being great for recruiting and general visibility in blog post form.  People love these stories; there definitely aren’t enough of them.)


## Turn software engineers into software owners


The canonical CI/CD advice starts with “ship early, ship often, ship smaller change sets”.  That’s great advice: you should definitely do those things.  But they are covered plenty elsewhere.  What’s software ownership?


**Software ownership is the natural end state of DevOps**.  Software engineers, operations engineers, platform engineers, mobile engineers — everyone who writes code should be own the full lifecycle of their software.


Software owners are people who:

1. Write code****
2. Can deploy and roll back their own code
3. Are able to debug their own issues in prod (via instrumentation, not ssh)


If you’re lacking any one of those three ingredients, **you don’t have ownership**.


Why ownership?  Because **software ownership makes for better engineers, better software, and a better experience for customers. ** It shortens feedback loops and means the person debugging is usually the person with the most context on what has recently changed.


Some engineers might balk at this, but you’ll be doing them a favor.  [We are all distributed systems engineers](https://opensource.com/article/17/7/state-systems-administration) now, and distributed systems require a much higher level of operational literacy.  May as well start today.


## Fail fast, fix fast


This is about shifting your mindset from one of brittleness and a tight grip, to one of flexibility where **failures are no big deal** because they happen all the time, don’t impact users, and give everyone lots of practice at detecting and recovering from them.


Here are a few of the best practices you should adopt with this practice.

- The engineer who writes the code and merges the PR should also **run the deploy**
- Everyone who writes code must be trained in how to deploy, roll back & revert to last known good state (before escalating if necessary).  They should also know the basics of instrumentation, feature flagging and debugging in prod..
- After deploying you MUST go verify: **are your changes behaving as expected**?  Does anything else look .. *unexpected*?  [You have the most context on what to expect](https://www.honeycomb.io/blog/2017/11/how-honeycomb-uses-honeycomb-part-8-a-bees-life/); just two minutes spent verifying that things look reasonable will catch the overwhelming majority of errors before users even notice.
- **[Practice observability-driven development](https://www.honeycomb.io/blog/2018/02/development-at-honeycomb-crossing-the-observability-bridge-to-production/)**.  [Instrument each change so you can verify it is working](https://www.honeycomb.io/blog/2017/10/how-honeycomb-uses-honeycomb-part-7-measure-twice-cut-once-how-we-made-our-queries-50-faster-with-data/).  ([Hell, instrument in advance](https://www.honeycomb.io/blog/2018/06/how-honeycomb-uses-honeycomb-part-9-tracing-the-query-path/) in order to [determine the impact](https://www.honeycomb.io/blog/2017/10/how-honeycomb-uses-honeycomb-part-6-instrumenting-a-production-service/) of [your proposed change](https://www.honeycomb.io/blog/2017/08/how-honeycomb-uses-honeycomb-part-5-the-correlations-are-not-what-they-seem/) and see if it’s even worth doing.)
- (You need solid observability for your instrumentation in order to expect your engineers to do [this kind of side-by-side comparison](https://www.honeycomb.io/blog/2016/08/how-honeycomb-uses-honeycomb-part-2-migrating-api-versions/), something with high cardinality support (like [honeycomb](http://honeycomb.io)) that lets you drill down to the individual event level.  It limits the amount of ownership you can reasonably expect if your [software engineers are flying blind](https://www.honeycomb.io/blog/2016/08/how-honeycomb-uses-honeycomb-part-1-the-long-tail/).)


**Make operability a high-value skill set.**  Never promote someone to “senior engineer” if they can’t deploy and debug their own code.


Software engineers don’t have to [become operational experts](https://www.honeycomb.io/blog/2017/01/how-honeycomb-uses-honeycomb-part-3-end-to-end-failures/).  They do need to know the bare basics of [instrumentation, deploy/revert, and debugging](https://www.honeycomb.io/blog/2017/05/how-honeycomb-uses-honeycomb-part-4-check-before-you-change/).


Everyone who puts software in production needs to understand and feel responsible for the full lifecycle of their code, not just how it works in their IDE.


## Baking: it’s not just for cookies


Shipping something to production is a process of incrementally gaining confidence, not a switch you can flip.


You can’t trust code until it’s been in prod a while, until you’ve seen it perform under a wide range of load and concurrency scenarios, in lots of partial failure modes.  Only over time can you develop confidence in it not being terrible.


**Nothing is production except production**.  Don’t rely on never failing; expect failure, embrace failure.  Practice failure!  Build guard rails around your production systems to help you find and fix problems quickly.


The changes you need to make your pipeline more resilient are roughly the same changes you need to safely [test in production](https://opensource.com/article/17/8/testing-production).  These are a few of your guard rails.

- Use **[feature flags](http://launchdarkly.com)** to switch new code paths on and off
- Build **canaries** for your deploy process, so you can promote releases gracefully and automatically to larger subsets of your traffic as you gain confidence in them
- Create cohorts.  Deploy to internal users first, then any free tier, etc in order of ascending importance.  Don’t jump from 10% to 25% to 50% and then 100% — some changes are related to saturating backend resources, and the 50%-100% jump will kill you.
- Have robots check the health of your software as it rolls out to decide whether to promote the canary.  Over time the robot checks will mature and eventually catch a ton of problems and regressions for you.


The quality of code is not knowable before it hits production.  You may able to spot some problems, but you can never guarantee a lack of then.  **It takes *time* to bake a new release** and gain incremental confidence in new code.


## In summary.

1. Get someone to own the deploy software
2. Value the work
3. Create a culture of software ownership
4. LOOK at what you’ve done after you do it
5. Be suspicious of new versions until they prove themselves


[Two blog posts in one weekend](https://charity.wtf/2018/08/17/on-engineers-and-influence/)!  That’s definitely never happened before.  Thanks to [Baron](http://twitter.com/xaprb) for asking me to draft this up following the weekend’s twitter thread: [https://twitter.com/mipsytipsy/status/1030340072741064704](https://twitter.com/mipsytipsy/status/1030340072741064704).
