---
title: "“Why are my tests so slow?” A list of likely suspects, anti-patterns, and unresolved personal trauma."
date: 2020-12-31
url: https://charity.wtf/2020/12/31/why-are-my-tests-so-slow-a-list-of-likely-suspects-anti-patterns-and-unresolved-personal-trauma/
word_count: 1387
---


Over the past couple of weeks I’ve been tweeting a LOT about lead time to deploy: the interval encompassing the time from when the code gets written and when it’s been deployed to production. Also described as “how long it takes you to run CI/CD.”


How important is this?


**Fucking central.**


Here is a quickie thread from this week, or just go read “Accelerate” like everybody already should have. 🙃


It’s nigh impossible to have a high-performing team with a long lead time, and becomes drastically easier with a dramatically shorter lead time.


![](https://i0.wp.com/charity.wtf/wp-content/uploads/2020/03/deploy-banner-violet.png?resize=212%2C78&ssl=1)


🌷 **Shorter is always better. 
**


And it should clock in under 15 minutes, all the way from “merging!” to “deployed!”.


Now some people will nod and agree here, and others freak the fuck out. “FIFTEEN MINUTES?” they squall, and begin accusing me of making things up or working for only very small companies. Nope, and nope. There are no magic tricks here, just high standards and good engineering, and the commitment to maintaining your goals quarter by quarter.


If you get CI/CD right, a lot of other critical functions, behaviors, and intuitions are aligned to be comfortably successful and correct with minimal effort. If you get it wrong, you will spend countless cycles chasing pathologies. It’s like choosing to eat your vegetables every day vs choosing a diet of cake and soda for fifty years, then playing whackamole with all the symptoms manifesting on your poor, mouldering body.


![](https://i0.wp.com/charity.wtf/wp-content/uploads/2022/01/04CC9DDB-A632-4CDA-BB5A-E11C66E3474F_1_105_c.jpeg?resize=296%2C168&ssl=1)


Is this ideal achievable for every team, on every stack, product, customer and regulatory environment in the world? No, I’m not being stupid or willfully blind. But I suggest pouring your time and creative energy into figuring out how closely you can approximate the ideal given what you have, instead of compiling all the reasons why you can’t achieve it.


Most of the people who tell me they can’t do this are quite wrong, turns out. And even if you can’t down to 15 minutes, ANY reduction in lead time will pay out massive, compounding, benefits to your team and adjacent teams forever and ever.


So — what was it you said you were working on right now, exactly? that was so important? 🤔


> “Cutting my build time by 90%!” — you


Huzzah. 🤠


So let’s get you started! Here, courtesy of my twitterfriends, is a long compiled list of Likely Suspects and CI/CD Offenders, a long list of anti-patterns, and some unresolved personal pain & suffering to hunt down and question when your build gets slow..


✨15 minutes or bust, baby!✨


> off the top of my head ...
> * building a new AMI
> * using EBS
> * using lots of any AWS calls, really
> * not parallelizing tests
> * tests that take several seconds to init
> * setup/teardown of dbs
> * importing test data
> * selenium and other UX tests
> * rsyncing sequentially
> what else? [https://t.co/Kurr5d42y7](https://t.co/Kurr5d42y7)— Charity Majors (@mipsytipsy) [December 23, 2020](https://twitter.com/mipsytipsy/status/1341871253183860743?ref_src=twsrc%5Etfw)

*Where it all started: what keeps you from getting under 15 minute CI/CD runs?*


### Generally good advice.


![](https://i0.wp.com/charity.wtf/wp-content/uploads/2020/03/friday.png?resize=165%2C290&ssl=1)

- [Instrument your build pipeline with spans and traces](https://www.infoq.com/presentations/honeycomb-build-ssc/) so you can see where all your time is going. ALWAYS. Instrument.
- Order tests by time to execute and likelihood of failure.
- Don’t run all tests, only tests affected by your change
- Similarly, reduce build scope; if you only change front-end code, only build/test/deploy the front end, and for heaven’s sake don’t fuss with all the static asset generation
- Don’t hop regions or zones any more than you absolutely must.
- Prune and expire tests regularly, don’t wait for it to get Really Bad
- Combine functionality of tests where possible — tests need regular massages and refactors too
- Pipeline, pipeline, pipeline tests … with care and intention
- You do not need multiple non-production environment in your CI/CD process. **Push your artifacts to S3 and pull them down from production. **Fight me on this
- Pull is preferable to push. (see below)
- Set a time elapsed target for your team, and give it some maintenance any time it slips by 25%


> this seems to get asked a lot, so i'm going to retweet myself. if you're designing a deploy or distribution process at scale, pull is superior to push in most cases. [https://t.co/7zqQC2Rom6](https://t.co/7zqQC2Rom6)— Charity Majors (@mipsytipsy) [December 23, 2020](https://twitter.com/mipsytipsy/status/1341567369890566145?ref_src=twsrc%5Etfw)


#### The usual suspects

- tests that take several seconds to init
- setup/teardown of databases (HINT try ramdisks)
- importing test data, seeding databases, sometimes multiple times
- rsyncing sequentially
- rsyncing in parallel, all pulling from a single underprovisioned source
- long git pulls (eg cloning whole repo each time)
- CI rot (eg large historical build logs)
- poor teardown (eg prior stuck builds still running, chewing CPU, or artifacts bloating over time
- integration tests that spin up entire services (eg elasticsearch)
- npm install taking 2-3 minutes
- bundle install taking 5 minutes
- resource starvation of CI/CD system
- not using containerized build pipeline
- …(etc)

[https://twitter.com/jetpack/status/1342014251305742336](https://twitter.com/jetpack/status/1342014251305742336)
*Continuous deployment to industrial robots in prod?? Props, man.*


#### Not properly separating the streams of “Our Software” (changes constantly) vs “infrastructure” (changes rarely)

- running cloudformation to setup new load balancers, dbs, etc for an entire acceptance environment
- docker pulls, image builds, docker pushes container spin up for tests


#### “Does this really go here?”

- packaging large build artifacts into different format for distribution
- slow static source code analysis tools
- trying to clone production data back to staging, or reset dbs between runs
- launching temp infra of sibling services for end-to-end tests, running canaries
- selenium and other UX tests, transpiling and bundling assets


> Selenium tests can be speedy, but the main problem I see is people using too many of the things. Ideally, they’re there to check something that nothing else can. *sigh*[@aslak_hellesoy](https://twitter.com/aslak_hellesoy?ref_src=twsrc%5Etfw) did a fun talk about architectures to improve test times [@seleniumconf](https://twitter.com/seleniumconf?ref_src=twsrc%5Etfw) [https://t.co/kSzwfNAmlC](https://t.co/kSzwfNAmlC)— Simon Mavi Stewart (@shs96c) [December 23, 2020](https://twitter.com/shs96c/status/1341883495757606915?ref_src=twsrc%5Etfw)


#### “Have a seat and think about your life choices.”

- excessive number of dependencies
- extreme legacy dependencies (things from the 90s)
- tests with “sleep” in them
- entirely too large frontends that should be broken up into modules


#### “We regret to remind you that most AWS calls operate at the pace of ‘Infrastructure’, not ‘Software'”

- AWS CodeBuild has several minutes of provisioning time before you’re even executing your own code — even a few distinct jobs in a pipeline and you might suffer 15 min of waiting for CodeBuild to do actual work
- building a new AMI
- using EBS
- spinning up EC2 nodes .. sequentially 😱
- cool it with the AWS calls basically


#### Natural Born Opponents: “Just cache it” and “From the top!”

- builds install correct version of toolchain from scratch each time
- rebuilding entire project from source every build
- failure to cache dependencies across runs (eg npm cache not set properly)


#### “Parallelization: the cause of, and solution to, all CI problems”

- shared test state, which prevents parallel testing due to flakiness and non-deterministic test results
- not parallelizing tests


> Cross stack tests which move data among different moving pieces,  hard to mantain and used to be one of the sources of having a slow and unreliable pipeline which adds friction to your deploy strategy.— pfreixes (@pfreixes) [December 25, 2020](https://twitter.com/pfreixes/status/1342414495898079233?ref_src=twsrc%5Etfw)

*I have so many questions….*


Thanks to @wrd83, @sorenvind, @olitomli, @barney_parker, @dastbe, @myajpitz, @gfodor, @mrz, @rwilcox, @tomaslin, @pwyliu, @runewake2, @pdehlkefor, and many more for their contributions!


P.S. what did I say about instrumenting your build pipeline? For more on honeycomb + instrumentation, see this thread. Our free tier is incredibly generous, btw ☺️


> ok i don't think i've ever actually properly pointed people at this fabulous talk, so here is a sample of some favorite ben moments.
> "We read through our build log and we couldn't really tell what we were supposed to care about, so we put it in honeycomb. " [https://t.co/P4Z3yPCVBd](https://t.co/P4Z3yPCVBd)— Charity Majors (@mipsytipsy) [June 10, 2020](https://twitter.com/mipsytipsy/status/1270690062582247424?ref_src=twsrc%5Etfw)


Stay tuned for more long form blog posts on this topic. Coming soon. 🌈


charity


P.S. [this blog post is the best thing i’ve ever read about reducing your build time. EVER.](http://dan.bodar.com/2012/02/28/crazy-fast-build-times-or-when-10-seconds-starts-to-make-you-nervous/)


![](https://i0.wp.com/charity.wtf/wp-content/uploads/2020/05/IMG_1540.png?resize=234%2C312&ssl=1)
