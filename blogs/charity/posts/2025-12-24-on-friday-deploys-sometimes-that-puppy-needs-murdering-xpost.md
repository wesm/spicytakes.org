---
title: "On Friday Deploys: Sometimes that Puppy Needs Murdering (xpost)"
date: 2025-12-24
url: https://charity.wtf/2025/12/24/on-friday-deploys-sometimes-that-puppy-needs-murdering-xpost/
word_count: 1117
---


([Cross posted from its original source](https://charitydotwtf.substack.com/p/on-friday-deploys-sometimes-that))


‘Tis the season that one of my favorite blog posts gets pulled out and put in rotation, much like “White Christmas” on the radio station. I’m speaking, of course, of “[Friday Deploy Freezes are Exactly Like Murdering Puppies](https://substack.com/home/post/p-181561576)” ([old link on WP](https://charity.wtf/2019/05/01/friday-deploy-freezes-are-exactly-like-murdering-puppies/)).


This feels like as good a time as any to note that I am not as much of an extremist as people seem to think I am when it comes to Friday deploys, or deploy freezes in general.


(Sometimes I wonder why people think I’m such an extremist, and then I remember that I did write a post about murdering puppies. Ok, ok. Point taken.)


Take [this recent thread from LinkedIn](https://www.linkedin.com/posts/michael-davis-7033548_friday-deploy-freezes-are-exactly-like-murdering-activity-7408181339444707328-8GjS?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAEP-B4Bn1IFS4Br7okfkI7z81XqQEOEKro), where [Michael Davis](https://www.linkedin.com/in/michael-davis-7033548?) posted an endorsement of my Puppies article along with his own thoughts on holiday code freezes, followed by a number of smart, thoughtful comments on why this isn’t actually attainable for everyone. [Payam Azadi](https://www.linkedin.com/in/payamazadi-nyc?) talks about an “icing” and “defrosting” period where you ease into and out of deploy freezes (never heard of this, I like it!), and a few other highly knowledgeable folks chime in with their own war stories and cautionary tales.


It’s a great thread, with lots of great points. I recommend reading it. I agree with all of them!!


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%2141Lq%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F097e02dc-5952-42ba-b532-d2efada0d4dc_768x1024.jpeg?resize=234%2C312&ssl=1)


For the record, I do not believe that everyone should get rid of deploy freezes, on Fridays or otherwise.


If you do not have the ability to move swiftly *with confidence*, which in practice means “you can generally find problems in your new code before your customers do”, which generally comes down to the quality and usability of your observability tooling, and your ability to explore high cardinality dimensions in real time (which most teams *do not have*), then deploy freezes before a holiday or a big event, or hell, even weekends, are probably the sensible thing to do.


If you can’t do the “right” thing, you find a workaround. This is what we do, as engineers and operators.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21TfFn%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4718da54-36dd-423c-a6e3-ed1fb960a789_978x360.jpeg?w=428&ssl=1)


## Deploy freezes are a hack, not a virtue


Look, you know your systems better than I do. If you say you need to freeze deploys, I believe you.


Honestly, I feel like I’ve *always* been fairly pragmatic about this. The one thing that does get my knickers in a twist is when people adopt a holier-than-thou posture towards their Friday deploy freezes. Like they’re doing it because they Care About People and it’s the Right Thing To Do and some sort of grand moral gesture. Dude, it’s a fucking hack. Just admit it.


It’s the best you can do with the hand you’ve been dealt, and there’s no shame in that! That is ALL I’m saying. Don’t pat yourself on the back, act a little sheepish, and I am so with you.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21xmpo%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d44e948-84a0-4457-a8e7-e6407c8005f7_1458x440.jpeg?w=412&ssl=1)


## I think we can have nice things


I think there’s a lot of wisdom in saying “hey, it’s the holidays, this is not the time to be rushing new shit out the door absent some specific forcing function, alright?”


My favorite time of year to be at work (back when I worked in an office) was always the holidays. It was so quiet and peaceful, the place was empty, my calendar was clear, and I could switch gears and work on completely different things, out of the critical line of fire. I feel like I often peaked creatively during those last few weeks of the year.


I believe we can have the best of both worlds: a yearly period of peace and stability, with relatively low change rate, *and* we can evade the high stakes peril of locks and freezes and terrifying January recoveries.


How? Two things.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21U-tY%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27be66be-5f80-4664-a5fc-a47e3f4b6e1b_1452x540.jpeg?w=412&ssl=1)


## Don’t freeze deploys. Freeze merges.


To a developer, ideally, the act of merging their changes back to main and those changes being deployed to production should feel like one singular atomic action, the faster the better, the less variance the better. You merge, it goes right out. You don’t want it to go out, you better not merge.


The worst of both worlds is when you let devs keep merging diffs, checking items off their todo lists, closing out tasks, for days or weeks. All these changes build up like a snowdrift over a pile of grenades. You aren’t going to find the grenades til you plow into the snowdrift on January 5th, and then you’ll find them with your face. Congrats!


**If you want to freeze deploys, freeze merges**. Let people work on other things. I assure you, there is plenty of other valuable work to be done.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21aR1f%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F673546bf-45ed-41e4-b615-72da93f44c24_2332x337.jpeg?w=558&ssl=1)


## Don’t freeze deploys unless *your goal* is to test deploy freezes


The second thing is a corollary. Don’t *actually* freeze deploys, unless your SREs and on call folks are bored and sitting around together, going “wouldn’t this be a great opportunity to test for memory leaks and other systemic issues that we don’t know about due to the frequency and regularity of our deploys?”


If that’s you, godspeed! Park that deploy engine and sit on the hood, let’s see what happens!


People always remember the outages and instability that we trigger with our actions. We tend to forget about the outages and instability we trigger with our *inaction*. But if you’re used to deploying every day, or many times a day: first, good for you. Second, I bet you a bottle of whiskey that something’s gonna break if you go for two weeks without deploying.


I bet you the good shit. Top shelf. 🥃


This one is *so easy* to mitigate, too. Just run the deploy process every day or two, but **don’t ship new code out**.


Alright. Time for me to go fly to my sister’s house. Happy holidays everyone! May your pagers be silent and your bellies be full, and may no one in your family or friend group mention politics this year!


💜💙💚💛🧡❤️💖

charity


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21cOpy%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e52da0e-c92d-4735-8124-7ea5efdc7b5f_2048x1536.jpeg?w=439&ssl=1)

*Me and Bubba and Miss Pinky Persnickety*


P.S. The title is hyperbole! I was frustrated! I felt like people were intentionally misrepresenting my point and my beliefs, so I leaned into it. Please remember that I grew up on a farm and we ended up eating most of our animals. Possibly I am still adjusting to civilized life. Also, I have two cats and I love them very much and have not eaten either of them yet.


A few other things I’ve written on the topic:

- [Shipping Software Should Not Be Scary](https://substack.com/home/post/p-181561589)
- [Deploys: It’s Not Actually About Fridays](https://substack.com/home/post/p-181561541)
- [How Much Is Your Fear of Continuous Deployment Costing You?](https://substack.com/home/post/p-181561517)
- [Why Are My Tests So Slow? A List of Likely Suspects, Anti-Patterns, and Unresolved Personal Trauma](https://substack.com/home/post/p-181561522)
