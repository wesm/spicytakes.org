---
title: "Bring Your Own Cloud, Nuon, and Hosted SaaS Challenges With Jon Morehouse"
subtitle: "Jon Morehouse, the CEO of Nuon, talks with me about bring your own cloud (BYOC). We discuss tradeoffs with hosted SaaS, how Nuon enables BYOC vendor deployments, the future of B2B SaaS, and more..."
date: 2024-07-09T10:51:37+00:00
url: https://materializedview.io/p/bring-your-own-cloud-nuon-and-hosted
slug: bring-your-own-cloud-nuon-and-hosted
word_count: 2267
---


The following is a transcript of my interview withJon Morehouse. Jon is the CEO and founder ofNuon﹩, a tool that enables SaaS vendors to deploy their software inside a customer’s cloud. Jon has been building cloud infrastructure for almost a decade. Prior to starting Nuon, he worked atAmazon Web Services,BuzzFeed, and founded two startups.


---


C.R.: Software infrastructure vendors have always had to deal with two challenges: deployment and management. The first—where software is deployed—has largely (but not completely) shifted from on-premises to the cloud. The latter—who manages the software—is in flux.


Software as a service (SaaS) tried to shift the management burden from the customer to the vendor. In doing so, providers have coupled management with deployment. Most SaaS vendors want to run their software on their own cloud infrastructure. This has created an all-or-nothing dynamic that many customers aren't comfortable with; they want to own their infrastructure but not the management responsibilities.


Bring your own cloud(BYOC) seems to solve this by decoupling software deployment from management. Software can be managed by a vendor while residing in a customer's environment.


Does this summary match your view of the world? How do you see BYOC fitting in?


J.M.: This summary is pretty close, but I think about it even a bit more holistically. Everything we know about today's software ecosystem is rooted in multi-tenant SaaS software. When AWS EC2 launched, we suddenly saw (almost overnight), companies popping up and creating new services. The barrier was lowered to all software creators, and then you start to see all these interesting trends:

- Mobile
- Big-data
- Observability/day-2 operations
- Kubernetes
- and now AI


What I think we've missed is that each of these evolutions (and the standards that they created) were designed around a different set of constraints—building massive business-to-consumer (B2C), multi-tenant consumer applications. Along the way we adopted this set of requirements for business-to-business (B2B) and infrastructure software that are not actually required. Unless you are a vertical cloud, you probably only need to design for your largest customers.


I see an opportunity to design a new way to deploy business software, not just critical infrastructure. As we look at the next 5 years, customer data is only going to increase in value. We'll see shifts where the average seed or series A company does not want to give up their internal data.


From there, I think we'll start to see more demand for a new deployment option that is not just for the enterprise, but for every single company. This creates a flywheel. As more vendors offer new deployment approaches, the market is educated on them, and demands them. This pushes more vendors to offer those deployment models, and so on and so forth.


To this point, I've only really said that today’s software deployment model does not work. I haven't really talked about this idea of BYOC, bring your own cloud. We're pretty bullish on it for a few reasons:

1. This combines the best of SaaS with the best of on-premises/hosted deployments
2. The emerging virtual private cloud (VPC) architecture and how it relates to AI
3. Security/cost constraints


I could probably spend this entire interview on any of these, but I'll leave it with this — with software, new is always a derivative of old, and I think that BYOC is just a mixup of all the previous deployment types we've had. Yes, today it's really hard because of the level of automation/standardization it needs. But it will become easy, and it'll open up entirely new architectures and business models/product capabilities.


C.R.: It sounds like you’re saying that we adopted high-scalability and multi-tenant requirements for SaaS infrastructure and you want to undo that. How does BYOC enable this? What new architectures do you expect to see?


J.M.: Exactly. It feels like each B2B/infrastructure company has invested all this money, time, and energy into building SaaS offerings; yet their customer's do not actually want them. It just feels… broken.


This is the magic of BYOC. You can take the same SaaS user experience, where a customer can just sign up and use your product, and make it so that it still runs in the customer’s cloud account. The customer gets new updates, a managed experience, and the "SaaS" experience, all without surrendering their data, requiring the same level of trust with the vendor, and so forth.


For the vendor, BYOC is even more powerful. All of a sudden, you can service yourentirecustomer base with one deployment option. Instead of building a sophisticated SaaS multi-tenant offering that many customers don’t actually want, you can focus all that energy on just building a great BYOC experience. I'm not saying this is easy (hence, why we exist), but with the right tooling in place, a vendor should be able to build their application, and ignore a bunch of the extra stuff that operating SaaS requires. Early stage companies have finite resources, so the companies who adopt this early on in their lifecycle reap the benefits of not having to do a bunch of things that are not core to their business.


And this leads to the new architectures that we see, which I think are even more interesting:

- Control-plane/data-plane: with the data plane in a customer's account. We see this today, where a worker or database is provisioned in the customer's cloud and a hosted control plane that can talk to it. No customer data has to touch the vendor's servers or be copied/stored.
- Bring your own LLM: With new self-hosted models and things like Azure's OpenAI integration, you see a lot of AI applications getting pulled to run in customer's accounts.
- Bring your own identity provider (IDP): If you can run your application in the customer's VPC, you can often integrate with their IDP, virtual private network (VPN), and other internal tools. I'm not sure how far we are from this one, but I see a world where a lot of vendors start stripping out many of the classic "Saas" tooling around AuthN/AuthZ and just defer that to the customer.


I think we're only scratching the surface of what's possible, because the tooling for BYOC just hasn't existed (yet).


C.R.: That last comment—the tooling doesn’t yet exist—is whereNuonfits in. So far, we’ve been talking about the benefits of BYOC. There must be tradeoffs to consider and challenges to overcome when implementing BYOC. What challenges do vendors face when implementing a BYOC architecture and how does Nuon help them?


JM: Great call out. It's not easy (or otherwise we wouldn't be doing what we're doing). Nuon aside, there are three big challenges you end up solving to offer BYOC:

1. Installation automation: You need to figure out how to take your application, infrastructure, and anything else about your cloud environment to get a working version of your product in a different account. From there, you end up solving two fairly large burdens: integrating with any customer network (in their VPC), and figuring out how to support bespoke customer requests and configurations.
2. Day 2 tooling: If you think about all the things that go into operating a SaaS — logs, metrics, alerts, operational scripts, user analytics, and so on—you need to have solutions for each of these. Depending on the customer you are selling too, they might not allow you access to anything. Others might be okay exposing metrics and telemetry data. Figuring out how to make sure things are not going wrong is a big burden because you do not have the luxury of logging into your cloud account console and debugging.
3. Updates: As an industry, we've coalesced on deploying early and often and constantly pushing changes to our users. In a BYOC world, you need to first figure out how to automate those updates (asking your customer to do something like this once a day is untenable), while also supporting different update requirements such as quarterly updates for some customers.


So, when we think about Nuon, our goal is to let you build software like you would SaaS—shipping early/often, leveraging cloud resources, changing architectures—all while allowing you to run the application in your customer's cloud. And then, along the way, we make sure you can update your software and make sure things are working. We think this is pretty ambitious. But if we can deliver on that goal, we think there are some massive shifts in the software world that will come about.


C.R.:Jack Vanlightlywrote apretty good critique of BYOClast year. Two of his points—that you lose resource pooling (and price negotiation power) across tenants, and that the boundary of operational responsibility breaks down—really resonate with me. What do you think about these challenges?


J.M.: This is a great post—definitely eye opening. I think there are two sides here: you are either a cloud company or an application/infrastructure company.


If you are a cloud company, price negotiation power is important and I honestly am unsure if it makes sense for those companies to offer BYOC. Companies likeConfluent,Vercel,Snowflakerepresent "vertical clouds"; they might not offer BYOC, rather they willbethe cloud in BYOC.


This leads to another thing we're seeing in the market: BYOC does not just mean you run your application on AWS, Azure, or GCP. Instead, it means running in many clouds. We're seeing vendors run their applications in vertical clouds (Databricks,Snowflake, and so on), and the future is really bifurcated between the cloud/infrastructure/compute providers and everyone else.


With regards to pricing negotiation power, this is an interesting one—it's a flip. Instead of the vendor requiring pricing negotiation power to get better deals on infrastructure, vendors can leverage theircustomer'sbuying power and remove the need to think about this at all. This allows smaller vendors to leverage their customer's buying power vs. having to have their own.


Also, consider serverless applications. If you are building entirely serverless, you can run BYOC applications for pennies in your customer's account; the individual usage will never get big enough to force you to migrateawayfrom serverless. Whereas, building a multi-tenant SaaS on serverless becomes prohibitively expensive at scale, since you are paying per-request to the hyperscalers.


Imagine a world where all SaaS companies are running in their customer's cloud account. SaaS margins would be purely R&D and support. In such a world, we’d see a shift from products that manage and operate large cloud presences to products that focus on the end customers. Maybe we even see the return of support based contracts.


C.R.: Your differentiation between cloud and application infrastructure companies is really fascinating. I hadn’t considered companies like Confluent or Snowflake as cloud providers, but you’re right; they’re all building platforms with marketplaces and compute. This could explain some of the different points of view.


Getting back to the challenges that Nuon is helping to address—installation, day 2 tooling, and updates—these seem like the sort of thing that internal teams at large organizations need to deal with, too.


Do you see a world where companies use tools like Nuon for their own internal software? Such teams usually have continuous integration, deployment, and observability platforms. Still, many organizations grow multiple versions of those stacks. If a development or operations team is already working with Nuon-powered infrastructure, I could imagine the team wanting it for their own code as well.


J.M.: I don't see a world where companies use Nuon to host a SaaS application. Our conviction is that we're moving away from a world of many deployment options, where vendors have to support several different paths. We’re headed toward a world where B2B SaaS vendorsonlyhave to offer BYOC and use that for their entire product stack.


On the other end, forconsumingsoftware, we believe in a world where most software is run in customer accounts. Some type of tooling for that will need to exist. If you think about it, all of today's cloud products are meant forbuilding software, notconsuming software.Think things like integrated network meshes for all your different applications running in your account, different compute products, and more. I think we will see a cloud that is designed for consuming software, not building software. We want to build the primitives for secure SaaS usage in your own cloud account.


So to answer your actual question, I think you'll see a world where consolidation of the internal stack is driven by BYOC. At Nuon we want to tackle this when the time is right. Right now, we're just building for vendors and giving them the tools to offer BYOC. We will expand from there to build more tools for theendcustomer. Maybe at some point we'll tackle the cloud primitives I mentioned earlier.


C.R.: Your point about a platform for SaaS consumers is spot-on. Cloud infrastructure companies leave SaaS consumption as a bolt-on afterthought—usually via “marketplaces”. A platform that offers first-class features for B2B BYOC SaaS is quite compelling.


I could go on, but we’ve covered so much ground. I’m going to call it here. Thanks so much for taking the time to do this interview. Any parting thoughts?


J.M.: I think that's it on my side! A huge thank you for taking the time to hear us out on why we think BYOC is emerging. We'll have to re-do this conversation in a few years, once it's further along.


---


Share


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profilefor a complete list.
