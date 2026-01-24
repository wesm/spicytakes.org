---
title: "Can Your Team Pass The Elevator Test?"
date: 2007-09-26
url: https://blog.codinghorror.com/can-your-team-pass-the-elevator-test/
slug: can-your-team-pass-the-elevator-test
word_count: 1067
---

Software developers do [love to code](https://blog.codinghorror.com/the-best-code-is-no-code-at-all/). But very few of them, in my experience, can explain *why* they’re coding. Try this exercise on one of your teammates if you don’t believe me. Ask them what they’re doing. Then ask them why they’re doing it, and *keep* asking until you get to a reason your customers would understand.


> What are you working on?
> *I’m fixing the sort order on this datagrid.*
> Why are you working on that?
> *Because it’s on the bug list.*
> Why is it on the bug list?
> *Because one of the testers reported it as a bug.*
> Why was it reported as a bug?
> *The tester thinks this field should sort in numeric order instead of alphanumeric order.*
> Why does the tester think that?
> *Evidently the users are having trouble finding things when item 2 is sorted under item 19.*


If this conversation seems strange to you, you probably haven’t worked with many software developers. Like the number of licks it takes to get to the [center of a tootsie pop](https://www.youtube.com/watch?v=O6rHeD5x2tI&pp=ygUPdG9vdHNpZSBwb3Agb3ds), it might surprise you just how many times you have to ask “why” until you get to something – *anything* – your customers would actually care about.


It’s a big disconnect.


**Software developers think their job is writing code. But it’s not.*** Their job is to solve the customer’s problem. Sure, our preferred medium for solving problems is software, and that does involve writing code. But let’s keep this squarely in context: writing code is something you *have* to do to deliver a solution. It is not an end in and of itself.


As software developers, we spend so much time mired in endless, fractal levels of detail that it’s all too easy for us to fall into the trap of coding for the sake of coding. Without a clear focus and something to rally around, we lose the context around our code. That’s why it’s so important to have [a clear project vision statement](https://blog.codinghorror.com/vision-quest/) that everyone can use as a touchstone on the project. If you’ve got the vision statement down, **every person on your team should be able to pass the “elevator test” with a stranger – to clearly explain what they’re working on, and why anyone would care, within 60 seconds**.


If your team can’t explain their work to a layperson in a meaningful way, you’re in trouble, whether you realize it or not. But you are in good company. Jim Highsmith is here to help. He explains a quick formula for building [a project vision model](http://www.joelonsoftware.com/articles/JimHighsmithonProductVisi.html):

kg-card-begin: html

> A product vision model helps team members pass **the elevator test** – the ability to explain the project to someone within two minutes. It comes from Geoffrey Moore’s book [Crossing the Chasm](https://bookshop.org/p/books/crossing-the-chasm-3rd-edition-marketing-and-selling-disruptive-products-to-mainstream-customers-geoffrey-a-moore/6433307). It follows the form:
> for `target customer`
> who `statement of need or opportunity`
> the `product name` is a `product category`
> that `key benefit / compelling reason to buy`
> unlike `primary competitive alternative`
> our product `statement of primary differentiation`
> Creating a product vision statement helps teams remain focused on the critical aspects of the product, even when details are changing rapidly. It is very easy to get focused on the short-term issues associated with a 2-4 week development iteration and lose track of the overall product vision.

kg-card-end: html

I’m not a big fan of formulas, because they’re so, well, *formulaic*. But it’s a reasonable starting point. Play [Mad Libs](https://en.wikipedia.org/wiki/Mad_Libs) and see what you come up with. It’s worlds better than no vision statement, or an uninspiring, rambling, ad-hoc mess masquerading as a vision statement. However, I think Jim’s second suggestion for developing a vision statement holds much more promise:


> Even within an IT organization, I think every project should be considered to produce a “product.” Whether the project results involve enhancements to an internal accounting system or a new e-commerce site, product-oriented thinking pays back benefits.
> One practice that I’ve found effective in getting teams to think about a product vision is the Design-the-Box exercise. This exercise is great to open up a session to initiate a project. **The team makes the assumption that the product will be sold in a shrink-wrapped box, and their task is to design the product box front and back.** This involves coming up with a product name, a graphic, three to four key bullet points on the front to “sell” the product, a detailed feature description on the back, and operating requirements.
> Coming up with 15 or 20 product features proves to be easy. It’s figuring out which 3 or 4 would cause someone to buy the product that is difficult. One thing that usually happens is an intense discussion about who the customers really are.


Design-the-Box is a fantastic way to formulate a vision statement. It’s based on a concrete, real world concept that most people can easily wrap their heads around. Forget those pie-in-the-sky vision quests: **what would our (hypothetical) product box look like?**


We’re all consumers; the design goals for a product box are obvious and universal. What is a product box if not the ultimate elevator pitch? It should...

- Explain what our product is in the simplest possible way.
- Make it crystal clear why a potential customer would want to buy this product.
- Be uniquely identifiable amongst all the other boxes on the shelf.
- Consider the box for the [ill-fated](https://www.eweek.com/it-management/bill-gates-legacy-microsofts-top-10-flops/) Microsoft Bob product as an example. How do you explain why customers should want [Microsoft Bob](https://en.wikipedia.org/wiki/Microsoft_Bob)? How would you even explain what the heck Microsoft Bob *is*?


![](https://blog.codinghorror.com/content/images/2025/09/microsoft-bob-box-art-front-back.jpg)


It’s instructive to look at existing product boxes you find effective, and those you find ineffective. We definitely know what our product box [*shouldn’t* look like](https://www.youtube.com/watch?v=G9HfdSp2E2A).


Have a rock solid vision statement for your project from day one. If you don’t, use one of Jim’s excellent suggestions to build one up immediately. **Without a coherent vision statement, it’s appalling how many teams can’t pass the elevator test – they can’t explain what it is they’re working on, or *why it matters.*** Don’t make that same mistake. Get a kick-ass vision statement that your teammates can relate their work to. Make sure *your* team can pass the elevator test.


*Completely stolen from Billy Hollis’ great [15-minute software addicts talk](https://www.youtube.com/watch?v=LiGsw_k8JhY).

[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
[software engineering](https://blog.codinghorror.com/tag/software-engineering/)
[communication](https://blog.codinghorror.com/tag/communication/)
[problem-solving](https://blog.codinghorror.com/tag/problem-solving-2/)
