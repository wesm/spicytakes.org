---
title: "Why is self-serve still a problem?"
subtitle: "We’re not going to solve it until we define it."
date: 2021-04-08T15:15:37+00:00
url: https://benn.substack.com/p/self-serve-still-a-problem
slug: self-serve-still-a-problem
word_count: 1068
---


![Who doesn't look at the Sagrada Família and think, "Yes, that reminds of BI"?](https://substackcdn.com/image/fetch/$s_!OQWB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff367c40a-8c39-4dfe-957c-013dc3e0635f_2400x1350.jpeg)

*done any day now*


In the opening days of 2010, a data scientist—a trendy new titlecoined months earlier—fired up their state-of-the-artiPod with an antenna, loaded forrester.com over5 Mbps internet, and readthis call to armsabout their revolutionary new industry:


> Self-service is all the rage in the world of business intelligence (BI), but it’s no fad. In fact, it’s the only way to make BI more pervasive, delivering insights into every decision—important or mundane—that drives your business.


Last month, the same data scientist, now well-versed in technologies thatcan write short storiesand conjureTom Cruise TikToksout of thin air, opened up their 14th generation iPhone 12, hopped on a fifteen-way live video call over their home internet, and joined adata scientist roundtableto discuss…how to make a self-serve analytics program successful. Despite everything else we’ve created over the last eleven years, we’re still—still!—chasing the decade-long dream of making sure execs can reliably pull revenue numbers for board presentations without asking for help.


While there’s a lot that explains this failure,1one issue stands out to me: Self-serve initiatives try to solve the wrong problem.


If you ask a data team why self-serve BI is important, they tend to say they’re overwhelmed with questions and want people to answer them on their own. In their post, Forrester describes another common motivation. Translating business questions from subject-matter experts to analysts and back again is a slow, imprecise game of telephone. The more we can tighten this loop—the more we can move these two roles closer together—the faster people can answer questions and make decisions. And nothing collapses that space more than making them “one and the same person.”


Both of these answers encourage us to think of self-serve BI as a code-free version of what analysts do. Self-serve’s aim is to, according to Forrester, help anyone “explore rich analytic information sets from all possible angles,” just as an analyst would. “In the self-service scenario, the core development issue becomes one of user creativity.”2


I believe this framing is wrong. Analysts and non-analysts use data in structurally different ways. By conceptualizing self-serve BI as a simplified means for doing an analyst’s job, we’re not only making the self-serve problem too hard—we’re solving the wrong thing altogether.


To see why, consider a thought-experiment. Suppose you ask an analyst and a sales VP to investigate how the sales team is performing this quarter, and to share their findings with you tomorrow. To level the technical playing field, the sales leader can sketch any chart they want to see, and it’ll magically get filled with the correct data. If each person shared their results with you anonymously, could you tell who created each one?


The answer is almost certainly yes. The sales VP would likely survey core metrics like bookings, close rates, and deal velocity by segment, region, and team. They would compare these numbers to prior quarters and to the current targets. Then, weighing this body of evidence, they would make an overall assessment of the quarter.


While the analyst might start with a brief survey of KPIs, they'd likely spend more time explaining the results they see. Why are enterprise bookings down so much compared to last quarter? Why are win rates different by region? Because you can't typically answer questions like these with existing metrics, analysts develop new ways to measure the phenomena they’re trying to understand.


To put it another way, when you ask an analyst a question, their first thought is often, “how might we measure that?” They work like scientists, creating new datasets and aggregating them in novel ways to draw conclusions about specific, nuanced hypotheses. Non-analysts work like journalists, collating existing metrics and drawing conclusions by considering them in their totality. Rather than looking for new ways to assess a question, they start by asking, “how do we currently measure that?”


In this context, it doesn't make sense to design self-serve tools to answer the complex questions that analysts ask. To do so would be like building a tool for journalists to conduct their own scientific experiments—a few might use it, but it's vastly overpowered for most. A better solution recognizes what that majority wants:metric extraction.They want to choose from a list of understood KPIs, apply it to a filtered set of records, and aggregate it by a particular dimension. It's analyticalMad Libs—show meaverage order sizefororders that used gift cardsbymonth.


We have (and have had for years) the tools to do this. The hard part of realizing this vision isn’t developing the technology, but finding the discipline. As a data team, each question we get is a little different, and doesn’t always fit into the clean structure above. In those cases, it’s easy to expand the boundaries of our existing self-serve tooling just a bit, adding a new option here or a new complication there. Eventually, we tell ourselves, with enough additions like these, our self-serve models will be “complete.”


But this path is a catch-22. The more questions people can theoretically self-serve, the fewer they can practically self-serve. As you add more options, self-serve tools stop looking like Mad Libs, and start looking like a blank document that requires people to write their own stories in their entirety. While that’s what analysts want, it’s not what everyone wants.


A better solution borrows from the lessonELTproviders taught us: Opinionated simplicity is better than indifferent optionality. ELT tools like Fivetran and Stitch provide (or, at least in their early versions, provided) a strict subset of the functionality that legacy ETL vendors provided.


Those limits were their magic. When using an ELT tool, rather than trying to fit the tool to our every need, we instead considered those needs more carefully. Could we get what we wanted from this simple architecture? The answer, it turns out, was almost always yes—we just needed to be told to try it.


For those of us providing self-serve data to others, we should embrace the same philosophy. Even if every question doesn’t initially fit neatly into a “metric extraction” framework, we should point people there first. And more often than not, we’ll find—unlike a lot of our other self-serve efforts over the last eleven years—it’ll get the job done.

[1](https://benn.substack.com/p/self-serve-still-a-problem#footnote-anchor-1-34884151)

More on these things later...one rant at a time, folks.

[2](https://benn.substack.com/p/self-serve-still-a-problem#footnote-anchor-2-34884151)

I think this misrepresents what analysts do. More on that later as well.
