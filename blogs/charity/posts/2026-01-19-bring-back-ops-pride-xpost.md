---
title: "Bring Back Ops Pride (xpost)"
date: 2026-01-19
url: https://charity.wtf/2026/01/19/bring-back-ops-pride-xpost/
word_count: 2348
---


*Cross-posted from “[Bring Back Ops Pride](https://charitydotwtf.substack.com/p/bring-back-ops-pride)“*


**“Operations” is not a dirty word, a synonym for toil, or a title for people who can’t write code. May those who shit on ops get the operational outcomes they deserve.**


I was planning to write something else today, but god dammit, I got nerd-sniped.


Last week I published a piece on the Honeycomb blog called “[You Had One Job: Why Twenty Years of DevOps Has Failed to Do It](https://www.honeycomb.io/blog/you-had-one-job-why-twenty-years-of-devops-has-failed-to-do-it).” Allow me to quote myself:


> In retrospect, I think the entire DevOps movement was a mighty, twenty year battle to achieve one thing: a single feedback loop connecting devs with prod.
> On those grounds, it failed.
> Not because software engineers weren’t good at their jobs, or didn’t care enough. It failed because the technology wasn’t good enough. The tools we gave them weren’t designed for this, so using them could easily double, triple, or quadruple the time it took to do their job: writing business logic.
> This isn’t true everywhere. Please keep in mind that **all data tools are effectively fungible** if you can assume an infinite amount of time, money, and engineering skill. You can run production off an Excel spreadsheet if you have to, and some SREs *have done so*. That doesn’t make it a great solution, the right use of resources, or accessible to the median engineering org.


It’s a fun piece, if I do say so myself, and you should go read it. ([Much stick art](https://www.honeycomb.io/blog/you-had-one-job-why-twenty-years-of-devops-has-failed-to-do-it)!)


I posted the link on LinkedIn yesterday morning. Comments, as ever, ensued.


(The internet was a mistake, Virginia.)


## “Devs should own everything”


A number of commenters said things like, “devs should own everything”, “make every team responsible for their own devops work”, and my personal favorite:


> “I still think the main problem is with the ownership model – the fact that devs don’t own the full system, including infra and ops.”


(Courtesy of [Alex Pulver](https://www.linkedin.com/in/alexpulver/), who has graciously allowed me to quote him here by name, adding that “he stands firmly behind this 😂”.)


As it happens, I have been aggressively advocating for the model I believe my friend is describing here, where software developers are empowered (and expected) to own their code in production, for approximately the past decade. No argument!


But “devs should own the full system, including infra and ops”?


We need to talk.


![fire_burn](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21w1R9%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa74323bd-8424-4da9-8724-fbaa9917dfaf_220x220.png?resize=162%2C162&ssl=1)


## I do not think ‘ops’ means what you think it means


In software—and *only* in software—ops has become a dirty word. Nobody wants to claim it. Operations teams got renamed to DevOps teams, SRE, infrastructure, production engineering, or more recently, platform engineering teams. *Anything* but ops.


Ops means Toil! Hashtag #NoOps!


Number one, this is *fucking ridiculous*.


What’s wrong with operations? Ops is not a synonym for toil; it *literally* means “get shit done as efficiently as possible”. Every function has an operational component at scale: business ops, marketing ops, sales ops, product ops, design ops and everything else I could think of to search for, and so far as I can tell, *none *of them are treated with anything like the disrespect, dismissal and outright contempt that software engineering[1](https://charitydotwtf.substack.com/p/bring-back-ops-pride#footnote-1-184825970) has chosen to heap upon its operational function.


Number two…what *happened*?


I can think of a number of contributing factors (APIs and cloud computing, soaring profit margins, etc), but I can also think of one easy, obvious, mustache-twirling villain, which would make a better story for you AND less work for me. (Root cause analysis wins again!! ✊)


## Whose fault is it?


Google. It’s Google’s fault.


I know this, because I asked Google and it told me so.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21FpTy%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7ee21b1e-a5da-4132-99ca-bdf84a72d1f3_685x748.png?resize=660%2C721&ssl=1)


(What? This is a free substack, not science.)


Here’s what I think happened. I think Google came out swinging, saying traditional operations could not scale and needed to become more like software engineering, and it was exactly the right message at exactly the right time, because cloud computing, APIs, SaaSes and so forth were just coming online and making it *possible* to manage systems more programmatically.


So far so good. But a crucial distinction got lost in translation, when we started defining this as developers (people who write code: good) vs *operators* (people who do things by hand: bad), which is what set us on the slippery slope to where we are today, where the entire business-critical function of operations engineering is widely seen as backwards and incompetent.


## Dev vs Ops is a separation of concerns


The difference between “dev” and “ops” is not about whether or not you can write code. Dude, it’s 2026: **everyone writes software**.


The difference between dev and ops is a separation of concerns.


![Dev and ops responsibilities.](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21NbpK%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8cbaee52-99f3-45c1-91f2-b9a563d27a54_605x692.webp?w=241&ssl=1)


If your concern is building new features and products to attract customers and generate new revenue, then congrats: you’re a dev. (But you knew that.)


If your concern is building core services and protecting their ability to serve customers in the face of any and all threats (including, at the top of the list, your own developers): congratulations slash I’m sorry, but you are, in fact, in ops.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21wjo0%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F18ade258-010d-4ec4-bcd4-b2ca52d2f139_525x631.png?w=385&ssl=1)


Both of these functional concerns are vital, as in “you literally can’t survive without them”, and complementary. You need product developers to be focused on building features and products, caring deeply about the experience of each user, and looking for ways to add value to the business. You need operations to provide a resilient, scalable, efficient base for those products to run on.


## The hardest technical problems are found in ops


Ops is not “toil”. It does not mean “dummies who can’t program good”. Operations engineering is not easier or lesser than writing software to build products and features.


What’s darkly ironic is that, if anything, the opposite is true.


Product engineering is typically much simpler than infrastructure engineering—in part, of course, because one of the key functions of operations is to make it **as easy as possible to build and ship products**. Operations absorbs the toughest technical problems and provides a surface layer for product development that is simple, reliable, and easy to navigate.


Not because product engineers are dumb or lesser than (let’s not slip into *that* trap[2](https://charitydotwtf.substack.com/p/bring-back-ops-pride#footnote-2-184825970) again!), but because **cognitive bandwidth is the scarcest resource in any engineering org**, and you want as much of that as possible going towards things that move the business materially forward, instead of wrestling with the messy underbelly.


The hardest technical challenges and the long, stubborn tail of intractable problems have *always* been on the infrastructure side. **That’s why we work *****so hard***** to try not to have them**—to solve them by partnerships, cloud computing, open source, etc. *Anything* is better than trying to build them again, starting over from scratch. We know the cost of new code in our bones.[3](https://charitydotwtf.substack.com/p/bring-back-ops-pride#footnote-3-184825970)


As I have said a thousand times: the closer you get to laying bits down on disk, the more conservative (and afraid) you should be.


The closer you get to user interaction, the more okay it is to get experimental, let AI take a shot, YOLO this puppy.


This is as it should be.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21y7E9%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ad05ab6-c633-4cb0-bbb7-a8ab5e3be82b_300x161.png?resize=300%2C161&ssl=1)

*The cost and pain of developing software is approximately zero compared to the operational cost of maintaining it over time.*


## Domain level differences


The difference between dev and ops isn’t about writing code or not. But there *are* differences. In perspective, priorities, and (often) temperament.


I touched on a number of these in [the article I just wrote on feedback loops](https://www.honeycomb.io/blog/you-had-one-job-why-twenty-years-of-devops-has-failed-to-do-it), so I’m not going to repeat myself here.


The biggest difference I did *not* mention is that they have different relationships with resources and definitions of success.


Infrastructure is a cost center. You aren’t going to make more money if you give ten laptops to everyone in your company, and you aren’t going to make more money by over-spending on infrastructure, either. Great operations engineers and architects never forget that **cost is a first class citizen** of their engineering decisions.


You can, in theory, make more money by spending more on product engineering. This is what we refer to as an “investment”, although sometimes it seems to mean “engineers who forget their time costs money”.


(Sorry, that was rude.)


## What about platform engineering?


“What about platform engineering?” Baby, that’s ops in dressup.


A bit less flippantly: I like my friend [Abby Bangser’s quote](https://www.syntasso.io/post/scaling-platform-building-balancing-what-is-unique-to-your-org-and-common-across-teams): “platforms should encode things that are unique to your business but common to your teams”, and I like [Jack Danger’s stick art](https://jackdanger.com/infrastructure-gravity/), and his observation that “The only thing that naturally draws engineers to look at the middle of their system is pure blinding rage.”


What I love about the platform engineering movement is that it has brought design thinking and product development practices to the operational domain.


Yes, we should absolutely be treating our product developers like customers, and thinking critically about the interfaces we give them. Yes, there is a middle layer between infrastructure and product engineering, with patterns and footguns of its very own.


Also yes: from a functional perspective, platform engineering is still ops. (Or at least, more ops than not.)


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21Dpti%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb05ad97-920a-4b3b-ae27-8456723ea389_300x153.png?resize=300%2C153&ssl=1)

*Yes, you need an ops team. If you have hard operational problems. You should try not to have hard operational problems. (from a talk I gave back in 2015)*


## Does it matter what we call it?


Yeah, I kinda think it does.


All these trendy naming schemes do not change the core value of operations, which is to consolidate and efficiently serve the revenue-generating parts of the function.[4](https://charitydotwtf.substack.com/p/bring-back-ops-pride#footnote-4-184825970) This is as true in technology as it is in sales or marketing. Running away from the term and denying your purpose muddies the water and causes confusion at the exact point where **clarity is most needed**.


An engineering team needs to know if they are oriented towards efficiency or investment. It changes how you hire, how you build, how you think about success and measure progress. It changes not only your appetite for risk, but what counts as a risk in the first place. *You can’t optimize for both at once.*


They also need to know whether they are responsible for the business logic or the platform it runs on.


Why? Because **no one can do everything**. Telling devs to own their code is one thing. (Great.) Asking them to own their code and *the entire technological iceberg beneath it* is wholly another. The more surface area you ask someone to master and attend to, the less focus you can expect from them in any given place. Do you want your revenue-generating teams generating revenue, or not?


If you can’t separate these concerns at the moment, maybe that’s something to work towards. Which is going to be hard to do, if we can’t talk about the function of operations without half the room running away and the remaining half squawking “toil!”


## Naming is a form of respect


Operational rigor and excellence are not, how shall I say this…not yet something you can take for granted in the tech industry. The most striking thing about the 2025 DORA report was that the *majority of companies* report that AI is just adding more chaos to a system already defined by chaos. In other words, most companies are bad at ops.


To some extent, this is because the problems are hard. To a larger extent, I think it’s the cause (and result) of our wholesale abandonment of operations as a term of pride.


It’s another a fucking feedback loop. Ambitious young engineers get the message that being associated with ops is bad, so they run away from those teams. Managers and execs want to recruit great talent and make jobs sound enticing, so they adopt trendy naming schemes to make it clear this work is *not ops*.


If you want to do something well, historically speaking, this is not the way. The way to build excellence is to name it for what it is, build communities of practice, raise the bar, and compensate for a job well done.


Or as [one prognosticator](https://charity.wtf/2016/05/31/wtf-is-operations-serverless/) said, way back in 2016:


> I think **it’s time to bring back “operations” as a term of pride.** As a thing that is valued, and rewarded.
> “Operations” comes with baggage, no doubt. But I just don’t think that distance and denial are an effective approach for making something better, let alone trash talking and devaluing the skill sets that you need to deliver quality services.
> **You don’t make operational outcomes magically better by renaming the team “DevOps” or “SRE” or anything else.** You make it better by naming it and claiming it for what it is, and helping everyone understand how their role relates to your operational objectives.


Wow. Truly, I couldn’t have said it better myself.


### Footnotes

[1](https://charitydotwtf.substack.com/p/bring-back-ops-pride#footnote-anchor-1-184825970)

Not to get all Jungian on you all, but part of me has to wonder if “ops” represents the shadow self to software engineers, the parts of yourself that you hate and despise and are most insecure about (I am weak and bad at coding!! I might be automated out of a job!), and thus need to project onto some externalized other that can be safely loathed from a distance.

[2](https://charitydotwtf.substack.com/p/bring-back-ops-pride#footnote-anchor-2-184825970)

This might surprise you youngsters, but there was a time when systems folks were clearly the cool kids and developers were considered rather dim. Devs had to know data structures and algorithms, but sysadmins had to know *everything*. These things tend to come and go in cycles, so we may as well not shit on each other, eh?

[3](https://charitydotwtf.substack.com/p/bring-back-ops-pride#footnote-anchor-3-184825970)

As my friend Peter van Hardenburg likes to say, “The best code is no code at all. The second best code is code someone else writes and maintains for you. The worst code is the code you have to write and maintain yourself.” If it would fit on my knuckles, I would get this in knuckle tatts.

[4](https://charitydotwtf.substack.com/p/bring-back-ops-pride#footnote-anchor-4-184825970)

Would it be helpful to acknowledge that IT/ops serves an entirely different function than software engineering operations for production systems? Because it absolutely does.
