---
title: "Modular Monoliths Are a Good Idea, Actually"
subtitle: "Microservices aren't the only way to get high cohesion and low coupling."
date: 2024-09-13T19:07:10+00:00
url: https://materializedview.io/p/modular-monoliths-are-a-good-idea
slug: modular-monoliths-are-a-good-idea
word_count: 1163
---


I’ve been doing personal angel investing for several years. I’m excited to announce that I’ve launchedMaterialized View Capital (MVC). MVC is a micro VC fund where I’ll continue investing in early stage infrastructure startups. I’ll also continue tagging any companies that I mention on my newsletter with a ﹩ if I’ve invested in them. Thanks for all your support!


In other news, myPrefect Summit 2024keynote is up. Check out4 infrastructure trends in 20 minutesto learn about primary persistence on object storage, composable databases, PostgreSQL's renaissance, and durable execution.


---


It’s a story as old as time. A tech startup is born. Early engineers work night and day to build a product that customers want. They iterate furiously—adding new features and repurposing old code. No time to refactor; they need revenue. And then, if they’re lucky, miraculously, the startup gets customers. Product market fit is achieved, and it’s time to put the pedal to the metal. More customers, more features, more scale, and more engineers.


Somewhere along the way, the codebase goes from 100,000 lines to 10,000,000. The application that the early engineers built—a monolithic application in a single repository—is now a house of cards. Every change breaks something. It’s taking longer to build, test, and deploy. Even checking the code out is cause for a coffee break.


And then the FAANG engineers arrive. What are you even doing, they ask. You need scale, you need isolation, you need to decouple. You have a fever, and the only prescription is more microservices. And so the “escape the monolith” death march begins.


Scaling a monolith is hard, no doubt. To date, the only real tool we’ve had in our toolbox has been to switch to a service oriented architecture. Services can be built and deployed independently. This isolation keeps build times small, tests passing, and makes deployment easier.


At least that’s the pitch. In practice microservices can be just as tough to wrangle as monoliths. Services get tightly coupled; deploying a change in one can break another. Deploying 1000s of services independently requires an immense amount of tooling. Developers now need to spin up dozens of services to test locally, or manage their own cloud environment. Remote procedure call (RPC) frameworks need tooling to enforce compatible schema changes. Operations has to wrangle service meshes, distributed tracing, Kubernetes, Terraform, and so much more.


I’ve lived this story twice. First as an understudy at LinkedIn, then as an instigator at WePay. Both projects were brutal. At LinkedIn, we had to halt much of engineering for several months while we tore our monolith apart. Kevin Scott, our SVP of engineering wrote a great write-up about this in,When Your Tech Debt Comes Due. At WePay, the monolith migration project never ended. I wrote WePay’s second microservice when I joined in 2015. When I left in 2021, the monolith still housed much of WePay’s core logic. I have microservice fatigue.


Yet, I don’t see a lot of alternative solutions being offered. So I’m pleased to see themodular monolithtrend growing. The idea is to build a monolithic application as aseries of modules, each responsible for a portion of business logic. At first blush, this sounds silly. Isn’t this just good engineering? I was skeptical


![](https://substackcdn.com/image/fetch/$s_!ACGe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b8c13b3-70c4-42de-ae0d-db293a8773b2_689x195.png)


But the more I think about modular monoliths, the more excited I get. Yes, writing modular code is a good idea, and yes it’s obvious. Yet, we’re not doing it. Our monoliths always end up as spaghetti code. Rather than fixing the monolithic code, we’ve jumped straight to microservices. Why? I think the answer is tooling.


What might modular monolith tooling look like? Let’s start with the benefits that microservices confer: they can be built, tested, and deployed independently; they have isolated databases; and they have clear public APIs. To get similar characteristics from a monolith, developers need:

- Incremental build systems
- Incremental testing frameworks
- Branch management tooling
- Code isolation enforcement
- Database isolation enforcement


Incremental build systems speed up monolithic build times. Rather than rebuilding an entire application, only the portions that change are rebuilt. Similarly, incremental testing allows developers and continuous integration (CI) systems to run tests only for the portion of the monolith that’s changed (including upstream and downstream dependencies).Bazelis doing a lot of work in this area.


Since all developers are committing to the same codebase, branch management is also important. There are many options here:GitHub Flow,GitLab Flow,Trunk-Based Development, and so on.


By extension, CI tooling is important. If a developer breaks the monolith, they’ve broken it for everyone. Breaking builds must be quickly detected and fixed. Tools to predict whether a change is risky, to detect which change in a batch of commits broke the build, and to manage reverting or fixing forward are all required. Unlike incremental build and test, I find many teams are rolling their own scripts to manage such activities.


Changes that introduce new cross-module dependencies must be detected. Calls to non-public interfaces must be actively rejected. And code owners must be notified when new modules depend on their own modules. Code ownership files that define owners and approvers for each module must be added, and tooling built around them.Gauge﹩ is doing interesting work here with their open source dependency management tool,Tach.


Finally, monolithic databases need to be broken up. This is often the biggest chunk of work for any monolith migration. All parts of the codebase share a single ORM and assume they’re interacting with a single transactional database. Transaction boundaries must be defined and separated between modules. Tables must be grouped by module and isolated from other modules. Tables must then be migrated to separate schemas either on the same database or a separate one. I am not aware of any tools that help detect such boundaries and enforce isolation right now.


For monoliths just starting out, it would be great if full stack frameworks likeNext.js,Redwood.js,Rails, and others began to adopt modular concepts in their codebase. This would help developers writing new software to do the write thing from the get-go.


Best of all, I don’t see the modular monolith vs. microservices as an either-or choice. I see it as a stepping stone that can extend a monolith’s life. For some, the modular monolith might be all that’s needed. For others, it can provide a more natural transition to a service based architecture. Modular monolith tooling could even facilitate such a migration. And I suspect the result of a migration would be a well maintained monolith with 7 ± 2 services. I find such an architecture far more appealing than 1000s of services. We’ve spent decades building tooling for microservices. It’s time to give monoliths the same respect.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profilefor a complete list.
