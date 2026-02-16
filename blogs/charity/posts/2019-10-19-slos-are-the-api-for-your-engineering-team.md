---
title: "SLOs Are The API For Your Engineering Team"
date: 2019-10-19
url: https://charity.wtf/2019/10/19/slos-are-the-api-for-your-engineering-team/
word_count: 1742
---


[(Originally posted on InfoQ in October, 2019)](https://www.infoq.com/articles/slos-engineering-team-API/)


If your job involves direct leadership of engineering teams, managing how and what they deliver, you’ve surely come across situations where the pressure to deliver features won out and led to poor service reliability. You’ve probably had your team’s workflow disrupted by interference from senior managers about minor individual issues. Or, you’ve seen or heard execs questioning your team’s planned work to reduce technical debt or improve your delivery processes.


These kinds of clashes are extremely common between engineering teams and management, as well as among different engineering teams. They are all various manifestations of a single issue: the need for a better abstraction layer for people and teams who are trying to interact or collaborate with your team. That abstraction layer is called Service Level Objectives.


You might be furrowing your brow right now, “But I thought SLOs were for users! And isn’t that a technical thing?”


Rather than define SLIs (Service Level Indicators), SLOs (Service Level Objectives), or SLAs (Service Level Agreements) at length here — there’s [plenty of documentation](https://www.youtube.com/watch?v=tEylFyxbDLE) out there about that — here’s a quick summary:

- An SLI is the indicator for goodness.
- The SLO is your objective for how often you can afford for it to fail.
- And an SLA is an agreement with your users about it.


What I want to focus on is why SLOs are necessary for the humans who leverage them, and in particular, how they can benefit the relationships between your team and other individuals and teams.


The common problem across the examples above is that every one of them describes a messy boundary between roles and teams. For example, a VP’s job should not be to nitpick the order you are going to resolve tasks in, or to understand every spike on every dashboard. But this desire often comes from a well-meaning place; they actually care, and this kind of interaction may be the only signal available to them about how things are going or how a user is experiencing your system.


So you need to give them something better to care about.


## Establish your team’s perimeter


You need to establish the perimeter of your team, secure it, build entry points and rules for coming and going, and hold people accountable for using them correctly. And then ignore or bounce every attempt to breach the perimeter and communicate through unauthorized channels, or to get someone to make an exception for them. SLOs can help you make this happen. When you go through the process of identifying what matters to your business by establishing and agreeing upon SLOs and their associated SLIs, you have a framework for managing what is demanded of your team, and how those demands are made.


For these boundaries to hold, all stakeholders must agree on your SLIs and SLO, and you must make sure you are measuring and tracking these appropriately. [This is no small task](https://landing.google.com/sre/workbook/chapters/implementing-slos/), but for the purposes of the focus of this article, assume you have done so and everyone has signed off on a number they believe in. For example, perhaps you have agreed to a SLO stating that for every rolling 90 days, for 99.9% of users of your website, your home page will load “quickly enough” based on the SLI your engineering team has identified for latency in this situation, which might be “ten seconds”.


## Share the ownership of Production Excellence


Beyond their value in ensuring consistent, predictable service delivery, SLOs are a powerful weapon to wield against micromanagers, meddlers, and feature-hungry PMs. That is why it’s so important to get everyone on board and signed off on your SLO. When they sign off on it, they own it too. They agree that your first responsibility is to hold the service to a certain bar of quality. If your service has deteriorated in reliability and availability, they also agree it is your top priority to restore it to good health.


Ensuring adequate service performance requires a set of skills that people and teams need to continuously develop over time, namely: measuring the quality of our users’ experience, understanding production health with observability, sharing expertise, keeping a blameless environment for incident resolution and post-mortems, and addressing structural problems that pose a risk to service performance. They require a focus on production excellence, and a (time) budget for the team to acquire the necessary skills. The good news is that this investment is now justified by the SLOs that management agreed to. The discussion should move away from which pieces of work are being prioritized to which service objectives are we trying to achieve and keep over time.


Let’s look at three possible scenarios of how this could play out in real life.


## Scenario: Boss Freaks Out


The team keeps a dashboard on the wall of errors and latency. This is great most of the time, but when the boss’s boss happens to walk by and notices a spike in errors, he freaks out and starts DMing the engineering lead, or asking the nearest engineer what is wrong.


The team now has to take valuable time out of their day to explain what’s wrong, or explain that nothing is wrong and it just looks bad because it’s unexpected user behavior. It’s time consuming and gets in the way of actually fixing things. Senior management might not understand that fifty thousand things a day are broken, and the team cannot stop and fix or care about every single one of them.


The SLOs help us train managers to care about the important things, and let the unimportant things aside. We can remind them of the page that shows the team’s SLIs and SLOs, so they can see where the team is in their error budget.


## Scenario: CEO Leapfrogs Priorities


The CEO messages the engineering lead a few times a week because one user has messaged the CEO on twitter to complain about an issue affecting their particular app. The CEO wants to know what’s wrong and when she can tell the user it is fixed.


Occasionally this can be helpful, when it helps us catch problems that our monitoring didn’t catch, but far too often it just means that a user’s trivial bug leapfrogs the more important work on our roadmap. Or one of our engineers will spend time shipping a one-off fix for that user, and then we have to fix it twice.


So how can you negotiate with the CEO for less of this type of disruption to planned work?


Check to make sure that this isn’t an example of a real problem lurking or not being captured by your SLOs. Let’s say your mobile app times out and serves an error in 5 seconds. So some segment of mobile traffic is not able to load your page with its 10 second SLI, yet those users are not being identified. If it is being tracked, assure your CEO that it’s within your error budget and will be checked when appropriate. If it is not, bring it up in your SLO periodic review so you can add a new SLI or otherwise account for it in your SLO moving forward.


## Scenario: Feature Frenzy


As an engineering manager you need to keep the on call volume reasonable and protect your team’s ability to sleep through the night. But you might have a hard time pushing back against execs and all the stakeholders who want features shipped and bugs fixed, to carve out enough contiguous development time to address underlying architectural problems, harden your deploy pipeline, and so on. This kind of work is never the most pressing thing at any given time, even though over the long term it may be THE most important thing.


How do you wrestle back enough time to deal with technical debt? And how can you keep stakeholders from micromanaging your roadmap?


As agreed-upon, your first job is to meet your SLO. All other feature work or bug fixing is secondary to this. A SLO is the quality of availability you have committed to provide for your users. That means it is also what you have committed your team to delivering. This has implications for what you choose to build, and when.


Based on this agreement, those asking for your time have already acknowledged that their requests are lower priority until the work your team is doing to stabilize the deployment process has been completed, for example. Perhaps you need your team to work on reducing deployment time so that a bug fix can be deployed to production via a deployment pipeline in less than 10 minutes, otherwise the corresponding SLO for restoring service will blow out.


## The Knob Goes Both Ways


Conversely, some engineering teams will go on tinkering and refactoring forever in a quest for perfection, when you really need them shipping new features. How can you tell whether it’s time to stop polishing and time to get back to shipping new stuff? When you are exceeding your SLO you can stand to add more chaos to the system, so turn the knob back up.


SLOs are the right level of abstraction for agreements between teams within an org for the same reasons they are useful between companies. You don’t care about the implementation details under the hood for your network provider; you just want to know that it will be available 99.95% of the time, and clear communication when it is down and back up. Train your management and other teams to interact with you at the same level of abstraction and trust. Google has a good policy doc for [how to deal with SLO violations](https://cloud.google.com/blog/products/gcp/consequences-of-slo-violations-cre-life-lessons).


In this way, SLOs are even helpful *within *teams.They can help perfectionists tell when it’s okay to relax and let loose a bit, and they can guide the pathological corner cutters toward knowing when it’s time to rein it in and measure twice, cut once.


## A source of comfort … and more capacity to focus


Once you get used to thinking this way, it’s actually a huge relief. Instead of having to deeply understand and evaluate the risk of every single situation in its own unique glory, we have a simple common language for evaluating risk in terms of error budgets. SLOs save everyone involved both time and energy, which you can redirect toward more important things, like keeping your customers happy.
