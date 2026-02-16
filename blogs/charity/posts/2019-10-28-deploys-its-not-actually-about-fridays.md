---
title: "Deploys: It’s Not Actually About Fridays"
date: 2019-10-28
url: https://charity.wtf/2019/10/28/deploys-its-not-actually-about-fridays/
word_count: 2839
---


I just read [this piece](https://hackernoon.com/deploy-on-fridays-or-dont-qg2y32jk), which is basically a very long subtweet about my Friday deploy threads.  Go on and read it: I’ll wait.


Here’s the thing.  After getting over some of the personal gibes *(smug optimism?  literally no one has ever accused me of being an optimist, kind sir)*, you may be expecting me to issue a vigorous rebuttal.  But I shan’t.  Because we are actually in violent agreement, almost entirely.


I have repeatedly stressed the following points:

1. I want to make engineers’ lives better, by giving them more uninterrupted weekends and nights of sleep.  This is the goal that underpins everything I do.
2. Anyone who ships code should develop and exercise good engineering judgment about when to deploy, every day of the week
3. Every team has to make their own determination about which policies and norms are right given their circumstances and risk tolerance
4. A policy of “no Friday deploys” may be reasonable for now but should be seen as a smell, a sign that your deploys are risky.  It is also likely to make things WORSE for you, not better, by causing you to adopt other risky practices (e.g. elongating the interval between merge and deploy, batching changes up in a single deploy)


This has been the most frustrating thing about this conversation: that a) I am not in fact the absolutist y’all are arguing against, and b) MY number one priority is engineers and their work/life balance.  Which makes this particularly aggravating:


> Lastly there is some strange argument that choosing not to deploy on Friday “Shouldn’t be a source of glee and pride”. That one I haven’t figured out yet, because I have always had a lot of glee and pride in being extremely (overly?) [protective of the work/life balance](https://www.youtube.com/watch?v=lzl4nu0ZHQo#action=share) of the engineers who either work for me, or with me.  I don’t expect that to change.


Hold up.  Did you catch that clever little logic switcheroo?  You defined “not deploying on Friday” as being *a priori* synonymous with “protecting the work/life balance of engineers”.  This is how I know you haven’t actually grasped my point, and are arguing against a straw man.  My entire point is that the behaviors and practices associated with blocking Friday deploys are in fact **hurting your engineers.**


I, too, take a lot of glee and pride in being extremely, massively, yes even OVERLY protective of the work/life balance of the engineers who either work for me, or with me.


**AND THAT IS WHY WE DEPLOY ON FRIDAYS.**


Because it is BETTER for them.  Because it is part of a deploy ecosystem which results in them being woken up less and having fewer weekends interrupted overall than if I had blocked deploys on Fridays.


It’s not *about* Fridays.  It’s about having a healthy ecosystem and feedback loop where you *trust* your deploys, where deploys aren’t a big deal, and they never cause engineers to have to work outside working hours.  And part of how you get there is by not artificially blocking off a big bunch of the week and not deploying during that time, because that breaks up your virtuous feedback loop and causes your deploys to be much more likely to fail in terrible ways.


The other thing that annoys me is when people say, primly, “you can’t guarantee any deploy is safe, but you can guarantee people have plans for the weekend.”


Know what else you can guarantee?  That people would like to sleep through the fucking night, even on weeknights.


When I hear people say this all I hear is that *they don’t care enough to invest the time to actually fix their shit* so it won’t wake people up or interrupt their off time, seven days a week.  Enough with the virtue signaling already.


You cannot have it both ways, where you block off a bunch of undeployable time AND you have robust, resilient, swift deploys.  Somehow I keep not getting this core point across to a substantial number of very intelligent people.  So let me try a different way.


Let’s try telling a story.


## A tale of two startups


Here are two case studies.


#### Company X


Company X is a three-year-old startup.  It is a large, fast-growing multi-tenant platform on a large distributed system with spiky traffic, lots of user-submitted data, and a very green database.  Company X deploys the API about once per day, and does a global deploy of all services every Tuesday.  Deploys often involve some firefighting and a rollback or two, and Tuesdays often involve deploying and reverting all day (sigh).


Pager volume at Company X isn’t *the worst*, but usually involves getting woken up a couple times a week, and there are deploy-related alerts after maybe a third of deploys, which then need to be triaged to figure out whose diff was the cause.


#### Company Z


Company Z is a three-year-old startup.  It is a large, fast-growing multi-tenant platform on a large distributed system with spiky traffic, lots of user-submitted data, and a very green house-built distributed storage engine.  Company Z automatically triggers a deploy within 30 minutes of a merge to master, for all services impacted by that merge.  Developers at company Z practice observability-driven deployment, where they instrument all changes, ask “how will I know if this change doesn’t work?” during code review, and have a muscle memory habit of checking to see if their changes are working as intended or not after they merge to master.


Deploys rarely result in the pager going off at Company Z; most problems are caught visually by the engineer and reverted or fixed before any paging alert can fire.  **Pager volume consists of roughly one alert per week** outside of working hours, and no one is woken up more than a couple times per year.


#### Same damn problem, better damn solutions.


If it wasn’t extremely obvious, these companies are my last two jobs, Parse (company X, from 2012-2016) and Honeycomb (company Z, from 2016-present).


They have a LOT in common.  Both are services for developers, both are platforms, both are running highly elastic microservices written in golang, both get lots of spiky traffic and store lots of user-defined data in a young, homebrewed columnar storage engine.  They were even built by some of the same people (I built infra for both, and they share four more of the same developers).


At Parse, deploys were run by ops engineers because of how common it was for there to be some firefighting involved.  We discouraged people from deploying on Fridays, we locked deploys around holidays and big launches.  At Honeycomb, none of these things are true.  In fact, we literally can’t remember a time when it was hard to debug a deploy-related change.


## What’s the difference between Company X and Company Z?


So: what’s the difference?  Why are the two companies so dramatically different in the riskiness of their deploys, and the amount of human toil it takes to keep them up?


I’ve thought about this a *lot*.  It comes down to three main things.

1. Observability
2. Observability-driven development
3. Single merge per deploy


#### **1. Observability. **


I think that I’ve been reluctant to hammer this home as much as I ought to, because I’m exquisitely sensitive about sounding like an obnoxious vendor trying to sell you things.  😛  (Which has absolutely been detrimental to my argument.)


When I say observability, I mean in the [precise technical definition](https://www.honeycomb.io/blog/so-you-want-to-build-an-observability-tool/) as I laid out in this piece: with high cardinality, arbitrarily wide structured events, etc.   Metrics and other generic telemetry will not give you the ability to do the necessary things, e.g. break down by build id in combination with all your other dimensions to see the world through the lens of your instrumentation.  Here, for example, are all the deploys for a particular service last Friday:


Each shaded area is the duration of an individual deploy: you can see the counters for each build id, as the new versions replace the old ones,


#### **2. Observability-driven development.**


This is cultural as well as technical.  By this I mean instrumenting a couple steps ahead of yourself as you are developing and shipping code.  I mean making a cultural practice of asking each other “how will you know if this is broken?” during code review.  I mean always going and *looking* at your service through the lens of your instrumentation after every diff you ship.  Like muscle memory.


#### **3.  Single merge per deploy.**


The number one thing you can do to make your deploys intelligible, other than observability and instrumentation, is this: **deploy one changeset at a time**, as **swiftly as possible** after it is merged to master.  NEVER glom multiple changesets into a single deploy — that’s how you get into a state where you aren’t sure which change is at fault, or who to escalate to, or if it’s an intersection of multiple changes, or if you should just start bisecting blindly to try and isolate the source of the problem.  THIS is what turns deploys into long, painful marathons.


headlamps, illuminating whatever’s in front of my face: this is the image in my mind when i think about instrumenting my code


And NEVER wait hours or days to deploy after the change is merged.  As a developer, you know full well how this goes.  After you merge to master one of two things will happen.  Either:

- you promptly pull up a window to watch your changes roll out, checking on your instrumentation to see if it’s doing what you intended it to or if anything looks weird, OR
- you close the project and open a new one.


When you switch to a new project, your brain starts rapidly evicting all the rich context about what you had intended to do and and overwriting it with all the new details about the new project.


Whereas if you shipped that changeset right after merging, then you can WATCH it roll out.  **And 80-90% of all problems can be, should be caught right here,** before your users ever notice —  before alerts can fire off and page you.  If you have the ability to break down by build id, zoom in on any errors that happen to arise, see *exactly* which dimensions all the errors have in common and how they differ from the healthy requests, see *exactly* what the context is for any erroring requests.


## Healthy feedback loops == healthy systems.


That tight, short feedback loop of *build/ship/observe* is the beating heart of a healthy, observable distributed system that can be run and maintained by human beings, without it sucking your life force or ruining your sleep schedule or will to live.


Most engineers have never worked on a system like this.  Most engineers have no idea what a yawning chasm exists between a healthy, tractable system and where they are now.  Most engineers have no idea what a difference observability can make.  Most engineers are far more familiar with spending 40-50% of their week fumbling around in the dark, trying to figure out where in the system is the problem they are trying to fix, and what kind of context do they need to reproduce.


Most engineers are dealing with systems where they blindly shipped bugs with no observability, and reports about those bugs started to trickle in over the next hours, days, weeks, months, or years.  Most engineers are dealing with systems that are obfuscated and obscure, systems which are tangled heaps of bugs and poorly understood behavior for years compounding upon years on end.


That’s why it doesn’t seem like such a big deal to you break up that tight, short feedback loop.  That’s why it doesn’t fill you with horror to think of merging on Friday morning and deploying on Monday.  That’s why it doesn’t appall you to clump together all the changes that happen to get merged between Friday and Monday and push them out in a single deploy.


It just doesn’t seem that much worse than what you normally deal with.  You think this raging trash fire is, unfortunately … normal.


## How realistic is this, though, really?


Maybe you’re rolling your eyes at me now.  “Sure, Charity, that’s nice for you, on your brand new shiny system.  Ours has years of technical debt,  It’s unrealistic to hold us to the same standard.”


Yeah, I know.  It is much harder to dig yourself out of a hole than it is to not create a hole in the first place.  No doubt about that.


Harder, yes.  But not impossible.


*I have done it*.


Parse in 2013 was a trash fire.  It woke us up every night, we spent a lot of time stabbing around in the dark after every deploy.  But after we got acquired by Facebook, after we started shipping some data sets into [Scuba](https://www.facebook.com/notes/facebook-engineering/under-the-hood-data-diving-with-scuba/10150599692628920/), after (in retrospect, I can say) we had event-level observability for our systems, we were able to start paying down that debt and fixing our deploy systems.


We started hooking up that virtuous feedback loop, step by step.

1. We reworked our CI/CD system so that it built a new artifact after every single merge.
2. We put developers at the steering wheel so they could push their own changes out.
3. We got better at instrumentation, and we made a habit of going to look at it during or after each deploy.
4. We hooked up the pager so it would alert the person who merged the last diff, if an alert was generated within an hour after that service was deployed.


We started finding bugs quicker, faster, and paying down the tech debt we had amassed from shipping code without observability/visibility for many years.


Developers got in the habit of shipping their own changes, and watching them as they rolled out, and finding/fixing their bugs immediately.


It took some time.  But after a year of this, our formerly flaky, obscure, mysterious, massively multi-tenant service that was going down every day and wreaking havoc on our sleep schedules was tamed.  Deploys were swift and drama-free.  We stopped blocking deploys on Fridays, holidays, or any other days, because we realized **our systems were more stable **when we always** shipped consistently and quickly.  **


Allow me to repeat.  Our systems were *more stable* when we always shipped right after the changes were merged.  Our systems were *less stable* when we carved out times to pause deployments.  This was not common wisdom at the time, so it surprised me; yet I found it to be true over and over and over again.


## This is literally why I started Honeycomb.


When I was leaving Facebook, I suddenly realized that this meant going back to the Dark Ages in terms of tooling.  I had become so accustomed to having the Parse+scuba tooling and being able to iteratively explore and ask any question without having to predict it in advance.  I couldn’t fathom giving it up.


The idea of going back to a world without observability, a world where one deployed and then stared anxiously at dashboards — it was unthinkable.  It was like I was being asked to give up my five senses for production — like I was going to be blind, deaf, dumb, without taste or touch.


Look, I agree with nearly everything in the author’s piece.  I could have written that piece myself five years ago.


But since then, I’ve learned that systems can be better.  They MUST be better.  Our systems are getting so rapidly more complex, they are outstripping our ability to understand and manage them using the past generation of tools.  If we don’t change our ways, it will chew up another generation of engineering lives, sleep schedules, relationships.


Observability isn’t the whole story.  But it’s certainly where it starts.  If you can’t see where you’re going, you can’t go very far.


## Get you some observability.


And then raise your standards for how systems should feel, and how much of your human life they should consume.  *Do better. *


Because I couldn’t agree with that other post more: it really is all about people and their real lives.


Listen, if you can swing a four day work week, more power to you (most of us can’t).  Any day you aren’t merging code to master, you have no need to deploy either.  *It’s not about Fridays; *it’s about the swift, virtuous feedback loop.


And nobody should be shamed for what they need to do to survive, given the state of their systems today.


But things aren’t gonna get better unless you see clearly how you are contributing to your present pain.  And congratulating ourselves for blocking Friday deploys is like congratulating ourselves for swatting ourselves in the face with the flyswatter.  It’s a gross hack.


Maybe you had a good reason.  Sure.  But I’m telling you, if you truly do care about people and their work/life balance: we can do a lot better.


charity.
