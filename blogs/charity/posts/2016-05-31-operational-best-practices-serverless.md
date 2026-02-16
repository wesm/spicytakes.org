---
title: "Operational Best Practices #serverless"
date: 2016-05-31
url: https://charity.wtf/2016/05/31/operational-best-practices-serverless/
word_count: 1645
---


This post is part two of my recap of last week’s terrific [Serverless](http://serverlessconf.io) conference.  If you feel like getting bitchy with me about what serverless means or #NoOps or whatever, [please refer back to the prequel post, where I talked about operations engineering in the modern world.](http://charity.wtf/2016/05/31/wtf-is-operations-serverless/)


*Then* you can get bitchy with me.  (xoxoxxooxo)


The title of my talk was:


> the tooth fairy is a useful abstraction for the pain of life and rewards of having people who care about you ^_^
> — Charity Majors (@mipsytipsy) [May 23, 2016](https://twitter.com/mipsytipsy/status/734826592401166338?ref_src=twsrc%5Etfw)


The theme of my talk was basically: what should software engineers know and care about when it comes to operations in a world where we are outsourcing more and more core functionality?


If you care about running a quality service or product, or providing your customers with a reasonable level of service, [you have to care about operational concerns](https://charity.wtf/2016/05/31/wtf-is-operations-serverless/) like design, resiliency, instrumentation and debuggability.  No matter how many abstractions there are between you and the bare metal.


If you chose a provider, you do not get to just point your finger at them in the post mortem and say it’s their fault.  **You chose them, it’s on you**.  It’s tacky to blame the software or the service, and besides your customers don’t give a shit whose “fault” it is.


So given an infinite number of things to care about, where do you start?


### What is your mission, and what are your differentiators?


The first question must always be: **what is your mission**?  Your mission is not writing software.  Your mission is delivering whatever it is your customers are paying you for, and you use software to get there.  (Code is kind of a liability so you should write as little of it as necessary.  hey!! sounds like a good argument for #serverless!)


Second: **what are your core differentiators**?  What are the things that you are doing that are unique, and difficult to replicate, or the things where you have to actually be world class experts in those things?


Those are the things that you will have the hardest time outsourcing, or that you should think about *very carefully* before outsourcing.


### Facts


You can outsource labor, but you can’t outsource caring.  And nobody but you is in the position to think about your core differentiators and your product in a holistic way.


If you’re a typical early startup, you’re probably using somewhere between 5 and 20 SaaS products to get rid of some of the crap work and offload it to dedicated teams who can do it better than you can, much more cheaply, so you are freed up to work on your core value proposition.


**GOOD**.


But you still have to think about things like reliability, your security model, your persistent storage models, your query performance, how all these lovely services talk to each other, how you’re going to debug them, how you’re going to repro when things go wrong, etc.  You still **own** these things, even if you don’t **run** them.


For example, take AWS Lambda.  It’s a pretty great service on many dimensions.  It’s an early version of the future.  It is also INCREDIBLY irritating and challenging to debug in a practically infinite number of insanity-inducing ways.


*** Important side note — I’m talking about actual production systems.  Parse, Heroku, Lambda, etc are GREAT for prototyping and can take you a long, long way.  Early stage startups SHOULD optimize for agility and rapid developer iteration, not reliability.  Thx to @joeemison for reminding me that i left that out of the recap.*


### Focus on the critical path


Your users don’t care if your internal jenkins builds are broken.  They don’t care about a whole lot of things that you have to care about … eventually.  They do care a lot if your product isn’t actually functional.  Which means you have to think through the behavioral and failure characteristics of the providers you’re relying on in any user visible fashion.


Ask lots of questions if you can.  (AWS often won’t tell you much, but smaller providers will.)  Find out as much as you can about their cotenancy model (shared hardware or isolation?), their typical performance variance (run your own tests, don’t trust their claims), and the underlying storage systems.


**Think about how you can bake in resiliency from the user’s perspective**, that doesn’t rely on provider guarantees.  If you’re on mobile, can you provide a reasonable offline experience?  Like Parse did a lot of magic here in the APIs, where it would back off and retry saves if there were any errors.


Can you fail over to another provider if one is down?  Is it even worth it at your company’s stage of maturity and engineering resources to invest in this?


How willing are you to be locked into a vendor or provider, and what is the story if you find yourself forced to switch?  Or if that service goes away, as so many, many, many of them have done and will do.  (RIP, [parse.com](http://parse.com).)


### Tradeoffs


Listen, outsourcing is awesome.  I do it as much as I can.  I’m literally helping build a service that provides outsourced metrics, **I believe in this version of the future!**  It’s basically the latest iteration of capitalism in a nutshell: increased complexity –> increased specialization –> you pay other people to do the job better than you –> everybody wins.


But there are tradeoffs, so let’s be real.


The service, if it is smart, will put strong constraints on how you are able to use it, so they are more likely to deliver on their reliability goals.  **When users have flexibility and options it creates chaos and unreliability.**  If the platform has to choose between your happiness vs thousands of other customers’ happiness, they will choose the many over the one every time — as they should.


Limits may mysteriously change or be invented as they are discovered, esp with fledgling services.  You may be desperate for a particular feature, but you can’t build it.  (This is why I went for Kafka over Kinesis.)


You need to think way more carefully and more deeply about visibility and introspection up front than you would if you were running your own services, because you have no ability to log in and use strace or gdb or tail a logfile or run any system profiling commands when things go dark.


In the best case, you’re giving up some control and quality in exchange for experts doing the work better than you could for cheaper (e.g. i’m never running a fucking physical data center again, jesus.  **EC24lyfe**).  In a common worse case, it’s less reliable than what you would build AND it’s also opaque AND you can’t tell if it’s down for you or for everyone because frankly it’s just *massively harder* to build a service that works for thousands/millions of use cases than for any one of them individually.


### Stateful services


Ohhhh and let’s just briefly talk about state.


The serverless utopia mostly ignores the problems of stateful services.  If pressed they will usually say DynamoDB, or Firebase, or RDS or Aurora or something.


> Real question how does state get persisted with [#serverless](https://twitter.com/hashtag/serverless?src=hash&ref_src=twsrc%5Etfw)? 
> I understand scale out of stateless servers, but who stores the state?
> — Caitie McCaffrey (@caitie) [May 26, 2016](https://twitter.com/caitie/status/735917950041886720?ref_src=twsrc%5Etfw)


This is a big, huge, deep, wide lake of crap to wade in to so all I’m going to say is that there is no such thing as having the luxury of not having to understand how your storage systems work.  Queries will get slow, and you’ll need to be able to figure out why and fix them.  You’ll hit scaling cliffs where suddenly a perfectly-usable app just starts timing everything out because of that extra second of latency coming from …


¯\_(ツ)_/¯


The hardware underlying your instance will degrade (**there’s a server somewhere under all those abstractions, don’t forget**).  The provider will have mysterious failures.  They will be better than you, probably, but less inclined to give you satisfactory progress updates because there are hundreds or thousands or millions of you all clamoring.


The more you understand about your storage system (and the more you stay in the lane of how it was intended to be used), the happier you’ll be.


### In conclusion


These trends are both inevitable and, for the most part, very good news for everyone.


Operations engineering is becoming a more fascinating and specialized skill set.  **The best engineers are flocking to solve category problems** — instead of building the same system at company after company, they are building SaaS solutions to solve it for the internet at large.  Just look at the massive explosion in operational software offerings over the past 5-6 years.


This means that the era of the in-house dedicated ops team, which serves as an absorbent buffer for all the pain of software development, is mostly on its way out the door.  (And good riddance.)


People are waking up to the fact that **software quality improves when feedback loops are tighter** for software engineers, which means being on call and owning services end to end.  The center of gravity is shifting towards engineering teams owning the services they built.


This is awesome!  You get to rent engineers from Google, AWS, Pagerduty, Pingdom, Heroku, etc for much cheaper than if you hired them in-house — if you could even get them, which you probably can’t because talent is scarce.


But the flip side of this is that application engineers need to get better at thinking in traditionally operations-oriented ways about reliability, architecture, instrumentation, visibility, security, and storage. ** Figure out what your core differentiators are, and own the shit out of those.**


Nobody but you can care about your mission as much as you can.  Own it, do it.  Have fun.
