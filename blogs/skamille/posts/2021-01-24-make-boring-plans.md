---
title: "Make Boring Plans"
date: 2021-01-24
url: https://www.elidedbranches.com/2021/01/make-boring-plans.html
word_count: 1624
---


You’re probably familiar with the concept of [Choose Boring Technology.](https://mcfunley.com/choose-boring-technology) If you’re not, I’ll wait for you to read the excellent blog post by Dan McKinley that inspired a much-needed correction in tech to balance “innovation” with stability. I’m here to take this to the next level, and talk about how “boring” should apply not just to your technology choices, but to your plans.


I spoke to someone several months ago who was frustrated with their management chain. They were anxious about the fact that the management chain was always pushing on delivery in an unpredictable way. The team felt really high pressure, even though the projects they were working on were all part of long-running infrastructure renovations. Why was this so stressful? Why, they asked, was the plan not already laid out? Why isn’t this boring?


**Why isn’t this boring?**


It might say something about the area that I focus on, Platform Engineering*, that “why isn’t this boring” would ever come up. You see, usually when people are in this situation, they blame everything but the lack of planning for their problems. It is a common belief in engineering that, with a clear enough vision, the rest of the pieces of work will fall into place. With a well-understood goal and smart engineers, the idea is that you can trust that people will work towards that vision faithfully and deliver something great. And this does, in rare cases, seem to work. After all, half of the hiring wisdom of the past has been “hire smart people and get out of their way.” Magic can happen with a small, highly-motivated group of people building a new thing towards a clear goal.


However, this concept of building towards a grand vision falls apart when you are building the underlying software that other engineers rely on. For better and for worse, Platform often has to be the place where we push new things to the rest of the company. A big change in the platform is the definition of an innovation token being spent. You want to move to Kubernetes? You’re gonna spend a lot of time figuring out how to operate it well in your environment, to start. You want to support a massive monorepo for the whole company? Hello innovation tokens everywhere, as you try to make it scale and perform well for all of your engineers and all of the languages they want to use. Speaking of new languages, you want to introduce Rust, or O’Caml, or even just C++17? The platform will have to support it.


Before you go blaming the Platform team for spending all of the innovation tokens for the company, remember that these initiatives are often driven by someone else. If Platform doesn’t support Kubernetes, some team will decide to build shadow infrastructure because they’re convinced that it will solve the problem they have to handle with their tens of microservices, and then it will land in the lap of Platform after a year with none of the work done to make it easy to operate, but all of the operational expectations anyway. Our goal is to build just enough ahead of you so that when you realize you need the capacity, it’s there, or can be with minimal fuss, and it’s reliable to boot.


**Novel Technology Deserves Boring Plans**


Since we often end up in the land of novel technology, we owe it to ourselves and our customers to be boring in other ways. And the most important way that a Platform team can be boring is by writing boring plans.


It’s great to have a vision for the future of the platform. To achieve this vision, a non-trivial amount of our job is not just building new big, scalable, complex software infrastructure, but moving everyone from the last generation of this software infrastructure to the next generation. Upgrade the programming languages, the operating systems, the libraries. Move from OpenStack to Kubernetes, from on-prem to the cloud, from maven to bazel, from svn to git. Migrate from the old storage system that was optimized for a rare legacy usecase, to a new storage system with higher availability and performance.


Making these changes happen, under the covers, has both interesting parts and boring parts. If you’re not a platform engineer, you shouldn’t see the interesting parts. The interesting parts are where we go and tune the kernel to perform well for our workloads. The interesting parts are where we build out automatic failover, so that we can meet the availability needs of the workloads. The interesting parts are the many patches we might contribute back to the inevitably-broken open source projects that hold half the world together but still don’t seem to understand how to work with FQDNs. The interesting parts are where we understand deeply the dependencies of our technology stack, the opportunities and limitations, and build solutions for our customers that fix limitations and unlock new opportunities.


When we don’t attend to the boring parts by making our plans predictable, the interesting parts turn into extra stress on top of the overwhelming anxiety of juggling these moves. When you make plans that start and end with the vision “we will move everyone to the public cloud, and it will be great,” you find yourself in the exhausting situation of running all of your old infrastructure, trying to figure out the new cloud stuff, and dealing with customers who are confused and angry that the thing they want to do doesn’t seem to quite work in either world.


Contrast this to the team that turns that vision into boring plans. They start with a small proof of concept, migrating perhaps a single application and learning in the process. Then they do the work of looking across other applications on the old platform, to see which ones are similar to the one that is now in the cloud. They work with those users to get them migrated and running, all the while gaining comfort with this new environment and uncovering the interesting gotchas. They write down what they’re learning, so that each new step in the migration builds on the last, and others can be pulled in without a huge knowledge transfer. The team focuses on the hard parts of the moment, whether they are figuring out data mirroring, or fixing a bug in a popular open source project, and they are free from the anxious overhead of wondering what is happening tomorrow. The users are also free from the stress of wondering when the work they need will be delivered, because the team has communicated plans that account for this process of iteration, learning, and gradual migration.


**A Strategic Plan Is Obvious and Simple, Even Boring**


Making boring plans is a foundational step in getting good at setting engineering strategy. Strategy is often confused with innovation and vision in tech circles, but they are far from the same thing. Having a future vision and recognizing the potential of innovations is valuable in building great strategy, but strategies that rely on unproven magic bullets are not good strategies. Good strategy identifies a problem with the current situation, proposes a principled approach to overcome it, and then shows you a coherent roadmap to follow. Strategy is not in the business of razzle-dazzle, it’s in the business of getting to the core of the issues so that the solution becomes simple and obvious. Good strategy provides the clarity that enables boring plans.


To become great at technology strategy, start by getting good at making boring plans. Get clear about the problem you are overcoming with your plans. Make the principles of the work at each stage clear:

- How do we know when we’re in exploration mode, and how do we know when we’re ready to commit to a direction?
- Have we talked to our users? Do we understand how they are using our systems, and have we made plans that account for their needs?
- What are the problems we’re focused on solving right now, and which problems are we leaving to worry about another day?
- How do we know if we’re on the wrong track, what are the guardrails, milestones, or metrics that tell us whether the plan needs review?


Your teams need more than a clear idea of the end state and the hope that smart engineers will inevitably get you there. Plans that are formed around hope are failing plans; hope is not a plan. Plans that change constantly are failing plans. When your plans are constantly changing, it is a sign that you either are making plans that express a certainty you don’t have, or you haven’t done your research to get the right certainty in place. Either of these is a waste of time and an unnecessary stress on the team.


So leaders, you owe it your teams, and to your users, to free them from the tyranny and stress of uncertainty. You must do the work to go beyond vision, create concrete actions, and make boring plans.


** I’ve defined Platform Engineering before, but the simple description is “the software infrastructure that all of engineering relies on.” Your operation system, storage systems, distributed compute frameworks, and software development tools may all fall into this bucket. To be clear, however, everything in this post tends to apply to any team that is working outside of pure greenfield product development, particularly when the work they do has a lot of downstream impact on users of their systems.*

more

*Enjoy this post? You might like my book, [The Manager’s Path](http://amzn.to/2nw1QN5), available on Amazon and Safari Online! I also recommend the book [Good Strategy, Bad Strategy](https://amzn.to/366mIze), for those who want to improve their strategic skills. *
