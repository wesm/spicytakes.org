---
title: "Analytics is a mess"
subtitle: "You can’t stop it, and you shouldn’t try to contain it."
date: 2021-05-17T22:27:29+00:00
url: https://benn.substack.com/p/analytics-is-a-mess
slug: analytics-is-a-mess
word_count: 1417
---


![](https://substackcdn.com/image/fetch/$s_!maCM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F736d7fbf-6599-4159-83e2-e9568e00447c_880x702.jpeg)


Looking back, I’m not sure if I liked math or if I was scared of writing. The prospect of spending most of my time in college writing papers—staring at a blank page, endlessly editing drafts, never knowing if what I was producing was right, much less good—drove me away from most majors. I took refuge in the math and economics departments, where the problems were structured, bounded, and concrete, and the homework was never an essay. Numbers were tidy, I thought, not messy and creative, and I found comfort in that.


When we think about analytics and data science, we often apply the same connotations. Data is factual; math has rules; science is objective. While we can be clever about how we solve problems, there is little space for creativity in what we deliver (I’ve never heard a single executive say, “This dashboard is great, but can you make it more...creative?”). Our jobs, especially those centered around reporting and BI, are to search for the capital-T truth, and represent it as accurately as possible.


The problem is, this is all a lie.


Data isn’t objective, and analysis isn’t structured. It’s just as creative—and just as messy—as the papers I ran away from in college.


Take an example from Mode. We wanted to measure how well Mode performs against our competitors, and if that performance is getting better or worse. We all agreed that we could track this through our win rate. Informally, win rates are easy to understand: Divide the number of people who choose to buy Mode by the number of people who consider it. The better Mode performs in the market, the more likely people would be to choose it.


But we can’t define metrics informally; our instructions have tobe precise. And for metrics like win rates, there are a lot of devils in the details. For example, we have to decide what it means for a customer to consider Mode. Is it any individual who signs up for a Mode account? Is it any company that creates an account for their organization? What about companies who reach out to us for a demo but don’t create an account? What about people who create an account but decline the demo? Do we include people we reach out to, or just those who come to us? Do we only consider companies that enter formal trials managed by our sales team? Does the denominator include only the deals we’ve officially closed, or any deal, open or closed, that didn’t choose to buy Mode after a certain period of time? Do we aggregate our win rate by the date that they decided to evaluate Mode, or the date they made their decision to buy it or not? Do we measure it monthly, quarterly, or over a rolling interval?


Like my freshman year essay about mortality in Emily Dickinson’s poetry,1there are no objectively right answers.2There is no correct win rate waiting to be unearthed; one version isn’t true while another is false. Each version is equally accurate because they are tautological: They measure precisely what they say they measure, no more and no less. Our job as analysts isn’t to do the math right so that we can figure out which answer is in the back of the book; it’s to determine which version, out of a subjective set of options, helps us best run a business.3


This choice isn’t a technical one, but a creative one, built on top of “messy” questions, like “How easy is the metric to understand?,” “Do people already have pre-existing ideas of what this number might mean?,” and “How much do we think we can learn from it?” These are questions we can’t answer without trying stuff out and seeing what happens.


Eventually, this expansive exploratory phase reverses. Some numbers make sense; others don’t. Draft metrics are edited down. After a tuning and refining phase, a clean, standard metric emerges.


## A mess is the process for progress


When we look at companies with mature data practices, we only see the final, stable metrics and dashboards. This, combined with assumptions about the objectivity of math and numbers, leads us to believe that dashboards and BI development should be a fairly linear and direct journey. Standardized reporting, we think, can be built like a house: We create a blueprint and then follow it, building the foundation, the frame, and the finish, one after the other.


But we aren’t building prefab houses. Because no company is the same,4measuring a business, as was the case for us when we were measuring our win rates, is a creative process. Inevitably, even the best laid reporting plans give way to a lot of exploratory messes. Each potential metric produces a bunch of analyses to assess it; each analysis produces more questions and ad hoc offshoots. Multiply this by all the metrics and dashboards on your blueprint, and complicate it by constantly shifting the business underneath it, and the development process looks less like an organized construction site and more like anartist’s studioor awriter’s desk.


This feels wrong—and if you’re like I was in college, it's uncomfortable. But it's not only normal; it's also necessary. We arrive at better answers when we let analysis be generative and spontaneous. Often, the most useful things we find are the things we weren't looking for.


Unfortunately, teams sometimes struggle in these disorganized moments. They see the mess they've created, and assume something has gone terribly wrong. In that discomfort, teams feel the need to reset, to burn the whole thing down, and replace the tools and processes that got them there.


When this happens, it often looks like the right decision. The prior tools and processes were sloppy; the new tools and processes are indeed cleaner and tidier. But this is less about tools and more about timing: The new tools and processes typically get introduced right as the exploratory process is consolidating. If a writer replaces their desk just as they begin editing their book, their new desk will be cleaner, but for reasons completely unrelated to the desk itself.


Obviously, data tools and development processes aren’t desks, and they do have functional differences that go well beyond those of two different desks.5But those differences matter less than the problems the tools are solving. Companies’ first analytics tools, regardless of which ones they choose, will always be disorganized, not because the tool is inherently so, but because the creative process is.


When approaching any analytical problem—from something small like answering a single question to introducing a data practice at a company that’s never had one—we should expect the first steps to be uneven and uncomfortable. Rather than trying to stifle or control this phase, we’re better off having a plan for how to tidy it up later, by working in a sandbox or reserving space for the polished final drafts that we’ll eventually produce. If you force too much structure on a creative exercise, you’ll end up like me when I did the same thing in my English literature class—with a disappointed professor, and the worst grade on your transcript.6

[1](https://benn.substack.com/p/analytics-is-a-mess#footnote-anchor-1-36529090)

Because I could not stop my query—


He kindly stopped for me —

[2](https://benn.substack.com/p/analytics-is-a-mess#footnote-anchor-2-36529090)

But there are, as Professor Franco told me, very much wrong answers.

[3](https://benn.substack.com/p/analytics-is-a-mess#footnote-anchor-3-36529090)

You could argue that this is true of all aggregations of data. Metrics aren’t “real;” they’re abstract constructs that we use to simplify and understand the world. All metrics, from win rates to inflation to quarterback ratings, are full of arbitrary choices about what we include in them and what we don’t. The concepts they represent don’t exist outside of the metric itself. Which is a bit of a trip to think about, and maybe a topic for a future (philosophically indulgent) post.

[4](https://benn.substack.com/p/analytics-is-a-mess#footnote-anchor-4-36529090)

While it’s true that many companies are similar, the small variations make all the difference. Slack and Microsoft Teams, for instance, might look 90 percent the same. They both sell per-seat subscription software to business users. However, the 10 percent difference—Slack sells a standalone product and Microsoft Teams is often sold as part of the Office suite—dramatically changes how each company should measure daily active users, the cost of acquiring customers, and every other standard SaaS metric. This is why I’m skeptical of analytical templates. Even among companies that appear to do the same thing, there’s no one-size-fits-all metric. Maybe a topic for another future post.

[5](https://benn.substack.com/p/analytics-is-a-mess#footnote-anchor-5-36529090)

Maybe.

[6](https://benn.substack.com/p/analytics-is-a-mess#footnote-anchor-6-36529090)

Success is counted sweetest


By those who ne'er succeed.
