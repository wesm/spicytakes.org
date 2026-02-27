---
title: "Martin Fowler told me the second edition should be shorter (it’s twice as long) (xpost)"
date: 2026-02-18
url: https://charity.wtf/2026/02/18/observability-engineering-a-book-so-nice-we-wrote-it-twice-xpost/
word_count: 1255
---


90% new material, a clearer mission, and a rogues gallery of contributors. The second edition of Observability Engineering is almost done.

[Originally posted here.](https://charitydotwtf.substack.com/p/observability-engineering-a-book)

Last week I got to meet [Martin Fowler](https://bsky.app/profile/martinfowler.com) for the first time in person. This was an exciting moment for me. Martin ranks high on my personal pantheon; he is, so far as I can tell, hardly ever wrong.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%218RWJ%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f4894f1-c0b4-4651-981b-54401808e8e8_1024x768.jpeg?resize=600%2C450&ssl=1)

*Martin Fowler, me, and Nathen Harvey, at the happy hout for Gergely’s Pragmatic Summit! Not pictured: my glass of wine, Nathen’s box of fucks to give*


> “The second edition should always be shorter. I *always* made my second editions shorter. **Shorter books are better books**.”


God dammit, Martin..* Now* you tell me. 🙈


In completely unrelated news, our last few chapters for “[Observability Engineering, 2nd edition](https://www.oreilly.com/library/view/observability-engineering-2nd/9781098179915/)” go out to tech reviewers *this week*! This puts us on track for dead tree publication in June, although chapters will be available earlier for O’Reilly subscribers as well as behind an email gate on the Honeycomb site.


## What’s different about the second edition?


Almost everything. The only chapters that carry over some material are the ones on sampling, retriever (columnar store), and a smattering of the SLO stuff—maybe 10% all told? And we’ve added a monstrous amount of new material.


So no, it will *not* be shorter than the first edition. It is almost twice as long.[1] (Sorry!)


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%211Kti%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9c0ca61-478c-4b8d-83e7-438d4b8ef631_1044x443.png?resize=660%2C280&ssl=1)


## The first edition was a spaghetti mess


Books, as I understand, are like children; if you made them, you are not allowed to say you aren’t proud of them.


So fine, I won’t say it. But I think we can all privately agree that the first edition was a bit of a hot mess.


No shade on my wonderful co-authors, [Liz](https://bsky.app/profile/lizthegrey.com) and [George](https://bsky.app/profile/gmiranda23.bsky.social), or our O’Reilly editors, or myself for that matter. We did our best, but now, with the clarity of hindsight, it’s easy to see all the ways the ground was shifting under us as we wrote.


When we started the book in 2018, Honeycomb was the only observability company, and our definition of observability—high cardinality, high dimensionality, explorability—was the only definition. By the time the book came out in 2021, everyone was rebranding their products as observability, Gartner had waded into the fray.. it was a mess.


Perhaps the mature thing to do would be to have gone back and rewritten the book in light of the evolving market definition. But while I won’t speak for my co-authors, after 3.5 years, I was pretty fucking desperate to be done.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21PfU9%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a31b632-1d2b-4034-95b2-beb8f6bfdf23_604x391.png?resize=534%2C362&ssl=1)

*Artist’s rendering of the traditional authorial glow of pride, joy and deep satisfaction upon completing any book manuscript*


I swore I would never go through that again. And when O’Reilly first approached us about writing a second edition, my first reaction was blind panic.


## The second edition has a clearer mission


But once my lizard brain calmed down, I realized two things. Number one, it absolutely needed to be written; number two, I definitely wanted to help write it.


SO MUCH has changed. SO MUCH needs saying. When we met up in June to pull together a new outline, it seemed to just flow out of us.


A few of the many things that were not at all clear in 2018, but are crystal clear today:

- **Who we are writing for** (software engineers)
- **What they are doing** (instrumenting their code and analyzing it in production, with and without AI)
- **What observability means to analysts and the market at large** (literally anything to do with software telemetry)
- The integrations game is over, and **OpenTelemetry has won**
- **Most companies still don’t have real observability**. And they don’t know it. 😕


I am excited and incredibly grateful for the opportunity to take a second whack at this book in the era of AI. Not how I thought I’d feel, but I will *take it*.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%210HJr%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fada78dbc-5817-4e50-ba20-d464a89f6c86_768x816.jpeg?resize=446%2C756&ssl=1)

*The first edition of “Observability Engineering” was translated into Japanese, Korean, and Chinese (I believe it’s Mandarin?).*


We brought [Austin Parker](https://bsky.app/profile/aparker.io) on as a fourth co-author very early, with a special emphasis on topics related to OpenTelemetry and AI.


We also invited a number of people we admire to contribute in a variety of formats… guest chapters, use cases, stories, embedded advice, and more:

- [Jeremy Morrell](https://bsky.app/profile/jeremymorrell.dev) on how to instrument your code effectively
- [Hanson Ho](http://hanson.wtf/) and [Matt Klein](https://bsky.app/profile/mattklein123.dev) on observability for mobile and frontend
- Kesha Mykhailov and [Darragh Curran](https://www.linkedin.com/in/darraghcurran/) from Intercom on fast feedback loops and developing with LLMs
- [Dale McDiarmid ](https://www.linkedin.com/in/dalemcdiarmid/)on how to use Clickhouse for observability workloads
- [Rick Clark](https://www.linkedin.com/in/dendrobates/) on the mechanics of driving organizational transformation in order to build and learn at the speed of AI
- [Frank Chen](https://www.linkedin.com/in/fxchen/), a returning champion from our first edition, wrote about ontologies for your instrumentation chain
- [Phillip Carter](https://bsky.app/profile/phillipcarter.dev) wrote about eval pipelines and instrumenting LLMs
- [Mat Vine](https://www.linkedin.com/in/matvine1/) has a case study about moving ANZ from thresholds to SLIs/SLOs
- [Mike Kelly](https://www.linkedin.com/in/michaelekelly/) on managing telemetry pipelines for fun and profit
- [Hugo Santos](https://www.linkedin.com/in/hugomgsantos/) on how to instrument your CI/CD pipelines
- [Peter Corless](https://www.linkedin.com/in/petercorless/) made our chapter on “Build vs Buy (vs Open Source)” immensely better and more well-rounded


What a fucking list, huh? 🙌


Truly, this book is a veritable rogues gallery of engineers and companies we look up to (including some of our own direct competitors 😉). The one thing all these people have in common (besides being great writers with a unique perspective, and people who are willing to return our emails) is that **we share a similar vision** for observability and the future of software development.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21xJEF%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F56a31a10-5309-4414-895b-f3b741791771_768x645.jpeg?resize=503%2C597&ssl=1)

*Spotted this week: Nathen Harvey, walking around, giving out fucks by the handful.*


In addition to the sections written for software engineers on “**Instrumentation Fundamentals**” and “**Analysis Workflows**”, both with and without AI, we have a section on “**Observability Use Cases**” and another on “**Technical Deep Dives**”, which lets us cover even more ground.


Which brings us to the last section, the one that I personally signed up to write.


## Part 6: “Observability Governance”


When we met in June, I successfully pitched Liz and George on adding one final section: “Observability Governance”. Unlike the rest of the book, these chapters would be written for the observability team, or the platform engineering team, or whoever is wrestling with problems like cost containment and tool migrations.


I sketched out a few ideas and started writing. July passed, August, September…I was cranking out one governance chapter per month, right on track, planning to wrap up well before November.


In September, halfway through my last chapter, I reached out to the internet for advice. “[Are you an experienced software buyer? I could use some help.](https://charity.wtf/2025/09/19/are-you-an-experienced-software-buyer-i-could-use-some-help/)”


The response was ✨tremendous✨; my inbox swelled with interesting stories, bitter rants, lessons learned, and practical tips from engineers and executives alike.


But when I tried to finish the chapter, my engine stalled out. *I could not write*. I kept doggedly blocking off time on my calendar, silencing interruptions, staring at drafts, writing and rewriting, trying every angle. Four weeks passed with no progress made.


Five weeks. Six.


## Cliffhanger!


Tomorrow I’ll publish the second half of this story, in which the due date for my chapters comes and goes, and I end up throwing away everything I had written and starting over from scratch. Good times!


[1] If we ever write a third edition, I swear on the lives of my theoretical children that it will be MUCH shorter than this one.
