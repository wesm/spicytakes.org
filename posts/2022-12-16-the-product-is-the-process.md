---
title: "The product is the process"
subtitle: "Why Slack ruins companies, and why only products can save data teams."
date: 2022-12-16T17:27:13+00:00
url: https://benn.substack.com/p/the-product-is-the-process
slug: the-product-is-the-process
word_count: 2103
---


![Philosophy & Society — The Medium is the Message by Marshall McLuhan | by  Valentin Ducros | Medium](https://substackcdn.com/image/fetch/$s_!0Qf6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9c5e2a87-85a1-48aa-b276-7a6559e6075d_647x389.jpeg)


It’s an almost incomprehensible paradox, if you think about it. Technology and the internet—the world wide web, the information superhighway,not a big truck but a series of tubes—have changed every corner of our lives, and given billions of us access to nearly unimaginable luxuries and conveniences. To name but a single example, we can not only listen to any song ever created—say,Cake by the Oceanby DNCE—but we can also, on a moment’s notice, have a cakedelivered to our house,1summon a car to take us to the beach, and actually eat cake, by the ocean, all while broadcasting the entire thing, live, to the entire world.2More practically, we can now automate next to anything—math,ordering laundry detergent, and, almost,thinking.


Yet, as Robert Solow first observed 35 years ago,none of these advances show up in productivity statistics. Over the last six decades,total factor productivity—the economic indicator that roughly measures the effect technology has on how much stuff we can make—has grown at astubbornly steady ratein the United States. From 1960 to 1979, it grew by 14.5 percent. From 1980 to 1999, as computers graduated from nerdy novelties to everyday staples, it grew by...14.5 percent. And after two decades ofsoftware eating the world, from 2000 to 2019 (the last year data is available), it grew by 11.9 percent.


It makes no sense.How, with all that we can do now that we couldn’t do in 1960, are we only 45 percent more productive? Countless undergraduate students and doctoral candidates—and at least oneNobel Prize-winning economist—have already tried to answer that question, so a part-time data analyst with a shoddily-researched Substack probably isn’t going to crack this nut in one blog post shot from the hip. But, since nobody else has proposed it, I do have a theory to throw out from the cheap seats:3The problem is Slack.


Slack, the regrettably ubiquitous chat app that was unleashed on an unwitting world in 2013, is, on the surface, an impressive technological leap over email. It connects us to all our coworkers in an instant, through a single artery of conversation and integrated applications that helps us, as Slack eagerly puts it, “get work done.” It’s fast. It’s searchable. It’s cheerful and quirky and ergonomically agreeable. It’s like plugging into a corporate Matrix, if the Matrix were designed with the confectionary aesthetic ofThe Good Place.


And it makes us worse at our jobs.


For years, we’ve heard about how Slack’s many inboxes and constant pings are distractions thatmake us less productive. But the problem is deeper than an overeager notification trigger; it’s inherent in Slack’s DNA as a chat-first application. Because posting directly into a channel is the primary call to action, that’s where we post. This, and some people’s understandable tendency to talk in many short messages rather than a few long ones—as decades of internet chatting has taught us to do—encourage us to check Slack often and respond to messages quickly, lest something important get washed away in a firehose of other conversations and posts from bots.


Two feature gaps make this sense of paranoid urgency worse. First, because Slack organizes channels chronologically by the first post of each thread—as is necessary in an application designed around chat rooms rather than message board forums—threaded conversations get pushed up the feed and disappear, even if those threads are very active. To see these conversations, which are presumably important given the engagement with them, you have to catch them on your own, when the thread first starts.4Second, unlike email, Slack doesn’t have any mechanisms for triaging work. In email, people can manage their own workflows by marking some emails as unread, some as read, deleting some from their inbox, and putting others in folders. With Slack, the only two options are read and unread—and unread is horrifically clumsy, since it doesn’t apply to individual messages, but entire channels.5In other words, Slack is a kanban board with two stages: Gone forever, and do it now.


All of this compels us to collaborate in a frenzy of off-the-cuff crosstalk. It’s hard to follow, and makes our writing imprecise and incomplete—which meansourthinking is imprecise and incomplete.6Yes, it’s faster, more centralized, and more integrated than email. But if we score Slack against communication tools’ more meaningful measures—does it help us make good decisions, and keep everyone informed of and aligned around those decisions?—Slack is a spectacular step backwards.


Slack’s advocates—andthe company itself—will say the problem isn’t the tool; it’s how it’s used.7Tweak your notifications, establish best practices, and all is better. This defense, however, rests on what I believe is a fundamentally flawed theory of human nature. Collectively, we’re lazy and unthinking lemmings. If an environment makes a particular behavior convenient, that’s what we’ll do. We follow the paths of least resistance; we take the easiest way down; we spin the wheels that come with the most grease. And unfortunately for us, Slack greases a lot of problematic ones.


That’s why, even after millions of us have been using Slack for a decade, “how to fix Slack” is stillSEObait. Using employee handbooks and behavioral guidelines to push against the grain of a product is like jumping against gravity. No matter how hard we train, orhow far we can fly for a fleeting moment, we can never escape it.


# Tools eat process for breakfast


This doesn’t mean we can’t improve or change behaviors for the better; it means that tools are essentially the only lasting way of doing it. Slack itself proved this, just in the wrong direction.


I think there’s a lesson in this for the data ecosystem: Tools—and as tiresome as it may feel, conversations about tools8— are the only way to meaningfully move the industry forward. No matter how much we blog about best practices, or how many talks we give about better ways to work, people will eventually find their way back into the behavioral grooves cut by the products they use.


We see this time and time again. Aviral blog postgot us excited about engineers not writing ETL—but it took dbt to standardize the practice. The value of code reviews was understood for decades—but “the cumbersome, time-consuming, and synchronous nature of this approachhindered its universal adoption” until products like Githubmade it more accessible. We generally agree that we should protect production systems from malformed data, and that every free-range Excel file is a time bomb waiting to go off—but we won’t create data contracts until there’s a tool that makes it easy, andwe won’t get rid of Exceluntil another product makes it obsolete. If our goal is to improve something, like how data teams work with their stakeholders or find meaningful problems to solve, abstract ideas and new operational processes won’t carry us nearly as far as the current of our tools.


Of course, there’s still value in individual teams and companies trying to institute better operating principles and frameworks. Internally,bikeshedding about technologycan serve as a convenient excuse foravoiding the sticky, uncomfortable confrontationsthat are often required to get anything done.9But if we’re going to solve thefoundational questionsaboutour own usefulnessas an industry, agreeing on process and patterns of organizational design is neither necessary nor sufficient. The tools we have, whether they have deep philosophical roots or are accidental successes, will overwhelm whatever thought leadership we chum the ecosystem with.


For proof, consider how data teams manage inbound requests. This topic has been discussed since time immemorial—and, remarkably, we haven’t taken a single meaningful step forward. We’ve written blog posts. We’ve tweeted passages from those blog posts with enthusiastic stamps of millennial approval (“💯💯💯”). We’ve saved pictures of countless slides at countless conferences. And we’re stuck on the same treadmill we’ve been on for years. More conversations about processes won’t change that. Our only hope is that someone finally builds something that makes it better.10


# The greenfield next door


That, in my view, is where there’s still a considerable amount of whitespace in the data market: For tools that solve non-data problems for data team. As Erik Bernhardssonsaid about Modal,11which provides hosted compute infrastructure for data teams, “data is its own discipline,” with its own technical and productivity needs. Rather than shoehorning analytics organizations into products built for other purposes, what if data teams had tools that understood the nuances of their work?


Managing work requests, which often vary wildly and come to data teams through multiple channels and DMs, is just one example where existing ticketing systems like Asana and Jira don’t quite work. Alerting is another. We often need to fix broken pipelines and stalled ELT jobs, though it doesn’t always make sense to treat these outages in the same way that PagerDuty would treat a product outage.


There are more creative possibilities too. Are there better ways to present results in meetings other than copying and pasting charts in slide decks? Would we benefit from dedicated tools that help us curate and cull the hundreds of stale reports, Slack updates, and Excel files that we know we leave in our wake? Could data teams have their own systems of record for answering questions that enable us to live by the same mantra—”if it didn’t happen in Salesforce, it didn’t happen”—that governs how sales teams log their activities? While these may not be billion dollar businesses, they’re the products that could finally establish new norms for how data teams work within companies they operate.


To butcher every self-styled internet intellectual’sfavorite quote, “the product is the process.” No matter how much we bang on process, we won’t solve our own productivity paradox until we get the products right.

[1](https://benn.substack.com/p/the-product-is-the-process#footnote-anchor-1-91044568)

Today I learned that Doordash has dedicated landing pages, likehttps://www.doordash.com/dish/cakes-near-me, for different items and cuisines. It’s the edible equivalent toNetflix genres, and now I must see an entire list of the foods worthy of their own page.

[2](https://benn.substack.com/p/the-product-is-the-process#footnote-anchor-2-91044568)

You cannot, however, broadcast other people doing this, because Twitter no longer allows the sharing of assassination coordinates.

[3](https://benn.substack.com/p/the-product-is-the-process#footnote-anchor-3-91044568)

Sometimes the people in thenosebleeds are right, Dave.

[4](https://benn.substack.com/p/the-product-is-the-process#footnote-anchor-4-91044568)

I’ve heard people say that using Slack is like running your company on Twitter. I think it’s actually worse than that. Retweets and Twitter’s algorithmic timeline provide a means for showing people popular tweets that they may not have seen when they were first posted. On Slack, there are no such mechanics. If you miss a thread, Slack won’t do anything to make sure you see it.

[5](https://benn.substack.com/p/the-product-is-the-process#footnote-anchor-5-91044568)

You can, to some extent,save messagesas a way to triage them. But this only works if you use the feature entirely as a triage tool and not as means for, you know, saving things you might want to regularly return to.

[6](https://benn.substack.com/p/the-product-is-the-process#footnote-anchor-6-91044568)

Slack is thebulleted listof communication tools (sorryStephenandSandy).

[7](https://benn.substack.com/p/the-product-is-the-process#footnote-anchor-7-91044568)

Slack doesn’t make people dysfunctional; people make people dysfunctional.(Or, maybe more appropriately,Slack doesn’t make people dysfunctional; it’s just thatcertain noiseit makes.)

[8](https://benn.substack.com/p/the-product-is-the-process#footnote-anchor-8-91044568)

You’re welcome, Sandy.

[9](https://benn.substack.com/p/the-product-is-the-process#footnote-anchor-9-91044568)

In fairness to data teams, this is a virus that infects the entire tech industry: “If only we created the right system of rules, all of these messy disagreements would go away.” Everything from data contracts to Twitter’s moderation policies over-index on this fallacy. We’re better offaccepting the messand building systems that work with it rather than trying to govern it away.

[10](https://benn.substack.com/p/the-product-is-the-process#footnote-anchor-10-91044568)

Wait, what abouttalking about tools, you ask? If the point of the community is to advance the industry for future generations, I do think talking about organizational problems through the lens of a product helps do that. When we propose new processes, it’s easy to lazily extrapolate them into good results: “When we better manage our OKRs, we’ll all be more aligned and move faster, and the business will improve!” However, if we frame this proposal around a product, like an hypothetical OKR administration tool, we have to be more explicit about exactly what behaviors that tool should change, and how it should change them. In short, products are ways to ground theory.


All that said, and despite likely saying stuff like this before, I’d generally reject the idea that the communityshouldtalk about anything (I’ll leave that job to theGeneral Secretary). For example, people spill a lot of ink about sports and politics, without any realistic expectation of “moving things forward.” Instead, it’s just people gossiping about their hobbies. Similarly, I view much of the navel gazing that happens in data community as entertainment for its participants. To me, that’s the sign of a healthy ecosystem and something to encourage, not a thing to be stamped out in favor of a “more helpful and practical” dialogue.

[11](https://benn.substack.com/p/the-product-is-the-process#footnote-anchor-11-91044568)

I’m apersonal investorin Modal.
