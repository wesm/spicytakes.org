---
title: "How to recover from microservices"
date: 2023-05-05
url: https://world.hey.com/dhh/how-to-recover-from-microservices-ce3803cc
slug: how-to-recover-from-microservices-ce3803cc
word_count: 1168
---

I won't deny there may well be cases where a microservices-first architecture makes sense, but I think they're few and far in between. The vast majority of systems are much better served by starting and staying with a majestic monolith. The Prime Video case study that
[blew up the internet](https://www.linkedin.com/feed/update/urn:li:activity:7059822946831192066/)
yesterday is but the latest illustration.
Maybe once you reach the scale of Netflix or Amazon, there are areas where it starts to make sense, but remember that even the
[likes of GitHub](https://github.blog/2023-04-06-building-github-with-ruby-and-rails/)
and
[Shopify](https://twitter.com/RealGeneKim/status/1653400374378901504)
run their main applications as monoliths with millions of lines of code and have thousands of programmers collaborating on them. Do you have many more millions of lines of code or thousands of programmers working on the same code bases? If not, exercise extreme caution before even thinking about microservices.
But that's advice for folks starting new systems today. What do you do if you already, and prematurely, went with a microservices architecture? How do you recover? Here are a few tips:
**1) Stop digging.**
You can't clean up a mess before you stop making more of it. That means not introducing new microservices. It then means picking one of the existing microservices to be the epicenter that will carry new functionality instead. The gravitational pull of this new center should eventually swallow the majority of other microservices too, but the most important thing to get going is not to make matters worse.
**2) Consolidate critical, dependent paths first.**
The worst form of microservice madness is when you splinter a single, coherent flow across multiple systems. Maybe this is signup, maybe this is checkout, maybe this is visiting a single piece of content. That's where microservices cause the most harm by making it cumbersome and error prone to update the entire flow. Making changes means coordinating across multiple systems, dealing with synchronization issues, and worse. So your consolidation of microservices into macroservices on the way back to the monolith should start here.
**3) Leave isolated performance hotspots for last.**
When microservices are done right, they often target a narrow, isolated, and usually performance-critical segment of the system, which can benefit from a rewrite in a clunkier but faster programming language. Maybe your entire web application is written in
[Ruby on Rails](https://rubyonrails.org)
, but there's this one screen that can see wild load spikes, and for some reason can't be cached, so you pull out Rust or Go or whatever to squeeze all the juice out of your CPU. Well done, you've microserviced with honors! (Just make sure you've actually done the benchmarking to prove the productivity regression was worth it.)
**4) Prioritize dropping the most esoteric implementations.**
One of the terrible side effects of microservice madness is the tendency to embrace a million different programming languages, frameworks, and ecosystems. The siren song of microservices sing tall tales of isolation, which conjure CIO dreams of "best-in-breed", and tickle the natural programmer tendency to experiment with new and different as much as possible.
But the end result might well be a system comprised of 3-5-7 different programming languages, even more diverse frameworks, and a bunch of parallel dependency tracks. This is murder for conceptual comprehension, and leads to the common microservices symptom of "nobody understands or can work on the whole system".
Thus, you must start pruning. The vast majority of systems should have no more than two backend languages in play at any one time: A general purpose language tuned for programmer productivity that you can use 99% of the time, and a high-performance language tuned for addressing the last 1% of hotspots, should they ever appear.
**5) Learn to partition large systems with modules rather than networks.**
So much of the motivation for microservices has been driven by the fallacy that if you can't figure out how to properly architect a large system using programming tools like modules and namespaces, then you can solve this problem by partitioning it with network boundaries. No, no, no.
Making a large, resilient, performant system is hard. Trying to design one for a novel problem space on day one is impossible. Heed the timeless advice of John Gall:

> *A complex system that works is invariably found to have evolved from a simple system that works. The inverse proposition also appears to be true: A complex system designed from scratch never works and cannot be made to work.*

Simplicity demands that you do not start by inviting the beast of complexity – distributed systems – to the first dance. It's possible you'll one day end up with a complex, distributed systems that use microservices with justification, but that will only happen in good conscience if you started with a simple, monolithic design.
The key tome to study for how to break down large problem spaces into beautiful domain models is Eric Evan's
[Domain-Driven Design](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215/)
. But you should only graduate to that level of strategic, architectural aspirations after you've mastered the basics of tactical programming through books like Kent Beck's
[Smalltalk Best Practices](https://www.amazon.com/Smalltalk-Best-Practice-Patterns-Kent/dp/013476904X/)
(if you work in object-orientated languages) and Martin Fowler's
[Patterns of Enterprise Application Architecture](https://www.amazon.com/Patterns-Enterprise-Application-Architecture-Martin/dp/0321127420/)
.
Our industry is full of bright, passionate people. Many of them eager to start an Iron Man before they've done a 5K run. As much as I admire the gumption and self-confidence, and don't believe as a general rule in
[learning speed limits](https://sive.rs/kimo)
, I also think we've done the lot of them a disservice by not being clearer about the dangers of microservices earlier.
But that's the great thing about learning: You can always start! And if learning something new makes you reflect differently on the choices you made before, then you can change your approach from this day forth.
Yes, microservices, like any pattern of programming, is a tool. Yes, "it depends" is technically correct. But we offer no guidance to those looking to design better systems by simply saying that; we need to be willing to say WHAT IT DEPENDS ON. Just saying "it depends" helps nobody, anywhere make better decisions.
So let's be clear. Using microservices well usually depends on:
**a) Having a large, complex system that has successfully evolved from a small, simple system.**
**b) The ability to identify a part of this clearly modularized design that has strong boundaries, and no critical-flow dependencies, as a candidate for extraction.**
Then only proceeding IF there are large performance gains to be had by switching implementation approach OR there are organizational benefits from placing the module with an entire team, which can't easily collaborate with the rest of the system makers.
You might well find other justifications within your system or organization, but they should be clearly articulated, rigorously examined, and critically challenged before embarking on microservices.
Or, you know, you can just YOLO, have fun needlessly splintering your system design into dozens of pieces, and then return to this guide when the hangover hurts enough.
[The majestic monolith](https://m.signalvnoise.com/the-majestic-monolith/)
will always be here when you're ready to enjoy its simplicity and wisdom. Choose your own adventure!
