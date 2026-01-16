---
title: "We need a new…database?"
subtitle: "I'm, like, tired of all these numbers, man."
date: 2025-05-16T18:08:26+00:00
url: https://benn.substack.com/p/we-need-a-new-database
slug: we-need-a-new-database
word_count: 2961
---


!["Why should we use all these newfangled analytics when when can just see if the deal looks like it's going well?"](https://substackcdn.com/image/fetch/$s_!bn5u!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbec155d8-57b3-4426-bc3b-4608c9271f85_1024x517.png)

*Granola, left, and Notion, right, staring at Databricks,not pictured.*


On one hand, maybecalling Databricks a $36 billion mistakewas a bit hyperbolic. Since I said that three years ago, the Nasdaq has crashed twice, and Snowflake, Databricks’ chief competitor, has gone from being a $70 billion company to a$60 billion company. Meanwhile, Databricks raised another funding round in January that valued the business at$62 billion. Uh, lol, whoops.1


On the other hand, maybe it wasn't hyperbolic enough, and maybe theentire cloud database marketwas a mistake?


Like, if this blog is anything, it’s a stylized history of the last few years of data (andotherconcerns)—and here are some parts of that history:


---


Concern 1: Databases are really good now.


Companies collect tons of information about how their businesses work. They keep a ledger of customers’ purchases; they track clicks on their websites; they record your call for quality and training purposes. In thestrange new world of the internet, we all emit billions of bits of structured digital exhaust—a likeon a TikTok, an ad impression, acredit card swipe—and companies log it all.


Historically, this stuff was scattered across dozens of disparate systems. Today, it’s more centralized. Data is collected from a variety of sources, tidied up and cleaned, and carefully placed into a library of tables. If you were an analyst working for, say, theCharlotte Hornets,2you could log into a single database and type, “Show me all the people we sent a marketing email to, and tell me if they bought a ticket to a game, and if they did, did we win the game, and did they buy any concessions?”3Despite all of that data coming from different places, the magic of the entire modern data apparatus was that you could pretend that they didn’t.


Sure, this all a dramatic oversimplification, and nothing ever quite works this way in practice.4Tables are rarely that well organized, there are often thousands of them, and they often overlap in confusing and contradictory ways. They’re frequently broken and out of date. And the questions people ask usually return messy answers: “Eh, wait, are these actually the people we sent marketing emails to? This doesn’t look right. Are we sure we’re logging this correctly? Oh, I think we used different campaigns for people who hadn’t been to a game before. No, that’s not it. Oh, no, thatisit, we just did it wrong, and some people got both emails. But why does it say that this person who didn’t get an email clicked on one? Why does it say that this person who didn’t get an email clicked on4,000? What is happening? Ah well, at least I don’t have to worry aboutwhether or not we won the game.”


Nevertheless. That was the idea—a single pane of glass, for viewing all of your data—and over the last ten years, databases got a lot better at supporting it. They can hold, for all intents and purposes, unlimited amounts of information. They can run calculations over that data atnearly unfathomable speeds. They can be queried withmany different languages. People canbuildcustomappson top of them. Or as I said a few years ago,comparing 2022 data stuff to 2012 data stuff:


> The tools we have today—built and supported by thousands of people across dozens of companies—represent a profound leap forward from what we had then. And their effect extends beyond easing the daily frustrations of existing data scientists; they also made the work we did in 2012 accessible to a far greater range of companies and aspiring analysts and analytics engineers. Nearly every part of the industry is breathtakingly easier, faster, more powerful, and more reliable than it was a few short years ago.


---


Concern 2: It hasn’t been that useful?


That post continued:


> There’s one nagging inconvenience in the comparison between today’s data teams and the one I was on in 2012: [That] data team was as impactful as any that I’ve ever worked with [since]. It was a key part of the product development process; its members were honorary members of the marketing and customer success leadership groups; it was respected, in-demand, and had a voice in the strategic direction of the company. And all this was done on top of technology that was, relative to what’s available today, fragile, narrow, expensive, and powered bynow-archaic computing capacity.


I’m sure some people will disagree with this, and there are no doubt lots of companies that reinvented themselves on top of theSnowflake AI Data Cloud, or whatever. But compared to what was promised, “analytics” was, at best, a very uneven revolution, and at worst, afad:


> Fifteen or so years ago, a handful of companies, sports teams, and now-celebrities like Nate Silver became very rich and successful by doing more careful analysis. This worked better, in part because they were clever, in part because they were applying these techniques to problems for which datawas particularly useful, and partly because their competition—other companies, other teams,pundits hand-counting yard signs—was immature.We all saw this, and got very excited. Data became important; “being data-driven”became urgent. We started trying to quantify and optimize: A/B test everything;analyze this;analyze that. A cottage industry of content and a booming industry of business applications got built on the idea that everything in the future will become more scientific and more automated.Data literacywill become as important as actual literacy;everycompanywillbecomeadatacompany.And itkinda didn’t work? Or, at best, the resultshave been mixed. There are success stories—Wall Street isdominated by quant funds, for example—but there have also been lots of busts. Increasingly, “we are data-driven” feels less like a competitive advantage, and more like anempty sales pitch.


In other words, most databases are very good, and mostdata teams are still a disappointment.


---


Concern 3: Data is a bank shot.


Why, though? Why are analytical initiatives so valuable for a handful of companies, and failures for so many others? We have thousands of fancy tools; we have anindustrialized training programfor analysts; we havecommunities,conferences, and an endless circular supply ofself-referential soapboxing. What’s still missing?


One explanation remains—the problem isthe data itself:


> Even if we have the tools that companies likeNetflix,Google,Airbnb, and others have, and even if we copy their cultures and hire their employees, we’re still missing the third leg of their gold-plated analytical stool: Their data. And without that—and without similar business problems to apply it to—I’m not sure how much all of the data industry’s recent sound and fury is really worth. …The data of a mid-sized B2B SaaS product simply doesn’t have the potential energy of Google’s search histories, or of Amazon’s browsing logs. If the latter examples are the new oil, the former is a new peat bog. No matter how good the tools are that clean and analyze it, how skilled the engineers are who are working on it, or how mature the culture is around it, it’ll never burn ashot or as bright.…we assume that there are diamonds buried in our rough data, if only we clean it properly, analyze it effectively, or stuff it through the right YC startup's new tool.But what if there aren’t? Or what if they’re buried so deep that they’re impractical to extract? What if some data, no matter how clean and complete it is, just isn’t valuable to the business that owns it?


To be clear, as a resource for mechanical reporting, data is perfectly fine. But it’s hard to go beyond that, because using data is typically an indirect and imprecise wayto figure out what you really want to know:


> CEOs want to know what their customers are thinking. Behavioral data isn’t “truth;” it’s an observable proxy, the input to a kind of analytical alchemy that attempts to turn individual outcomes into generalizations about intentions. … Though most business decisions are driven by numbers, those numbers matter because they define people’s loose mental models for how the world works, not because people need to know about the often-meaningless tedium of things likestatistical significance.


For example, if someone wants to answer questions like “how can our team move faster?” or “what sales deals are in trouble?,” they have navigate through some roundabout prerequisites:

1. What quantitative measures would indicate that a sales deal is in trouble?
2. Using the data that they have, how can we compute those quantitative measures?
3. How do we interpret our results, especially when most of them are aninconclusively wiggly line?


In some cases, the first thing is very hard: Even if you had all the data you could possibly want, how do you figure out how to move faster? In other cases, the second thing is the problem: For companies that are working dozens of sales deals and not thousands, it’s hard to find many meaningful predictors of a deal being in trouble. And in all cases, something is lost in each step: The quantitative measures are imperfect representations of the problem, and people have to compromise on those measures to match them with the data they have.


No matter how big and fast databases get, they can’t solve that.


---


Or maybe they can?


---


Concern 4: “Data” has competition.


Earlier this week, Granola, an automatic note-taking app for meetings,launched Granola 2.0:


> The most up-to-date, relevant data on what’s happening in a company doesn’t lie in a Google Doc, internal wiki, or Slack channel[;] it’s in the conversations employees are having day in, day out. With Granola, it’s now possible to make sense of that sea of information, and harness it in countless ways.With every call in one place, sales leaders can ask “Why are we losing deals this quarter?”, product managers can probe “Which UX issues come up most often?”, and recruiters can diagnose “Where do our interviews keep stalling?” — all answered instantly with source-linked citations.5


Ah ha. We’ve talked about this a lot, so much so that I’ve already saidwe’ve talked about this a lot:


> We’vetalkedaboutthisalot: When we think about the difference between structured spreadsheets of numbers and loose PDFs of sales call transcripts, we often act as though the former has inherently more validity than the latter. It is math; it is science; it is “statistically significant.” Interviews and conversations and product specs are anecdotes, corrupted by emotions and biases. …But if we could query and aggregate words and images the way we can aggregate numbers—if we could put a calculator on top of a bucket of text files—we might find that unstructured data is both more valuable and easier to analyze than our venerated spreadsheets.


And fromanother post, comparing the value of 750 customer interviews with a database full of usage data:


> Though the [Dropbox folder of customer interviews] is probably more valuable than the [database of event logs], we can’t easily mine or manipulate it; we can only sample it. That’s why we instinctively dismiss this sort of information as untrustworthy or biased: Not because it’s wrong, but because there’s no way to look at all of it at once.


But now, with Granola 2.0, you can, quite literally, do exactly that: Record interviews, Granola transcribes them, and gives you a chatbot to query them. It’s not a text-to-SQL-to-proxy-metric-to-an-inscrutable-wiggling-line; it’s just text-to-answer.


---


Concern 5: Isthisuseful?


I have no idea. I have no idea if Granola can actually give useful answers tothe questions is says it can, like “what deals need my help?,” and “how can my team move faster?” I also have my doubts about how much a company can learn from their meeting transcripts alone. But stuff enough information into an LLM and they can do a remarkably good job of summarizing it; with more data to draw from—like emails, customer conversations, and whatever other unstructured sources we might start to collect now that we have something potentially useful to do with it—it’s hard to imagine that a bot like Granola’s couldn’t be at least as proficient in answering these sorts of questions as analysts who are trying to bank shot their way through a database.


Well. This week, Notion released a bot like Granola’s,with more data to draw from:


> Work is splintered across a dizzying number of tools. Conversations happen in Slack and Gmail, files are stored in Google Drive, pull requests are tracked in GitHub. Finding what you need means hunting in a forest of apps or waiting hours for a teammate to respond to questions.With Enterprise Search, there’s no more digging for information. Everything is accessible through a new, fast search experience.Simply ask for whatever you’re looking for, including open-ended questions: “What’s the latest on our upcoming brand campaign?” Notion AI will search your Notion workspace and connected apps to find the answer you’re looking for. Connectors are released for tools like Slack, Microsoft, Jira, Google Workspace, and GitHub, with Linear, Gmail, Zendesk, Box, and Salesforce coming soon.6


Notion isn’t just a chatbot for Notion; it’s a chatbot for everything.


---


Concern 6: Wait, is that a database?


I mean: Companies collect tons of documents about how their business works. They keep meeting notes; they exchange emails; they record your call for quality and training purposes. In thestrange new world of remote work, our entire jobs happen online—in docs, in video calls, on Slack—and companies log it all.


Historically, this stuff was scattered across dozens of disparate systems. Today, it’s…getting centralized by Notion?


Is that really the idea? I get it—everyone wants to be the single pane of glass, for viewing all of your data—but shouldn’t a database be what supports that? Rather than relying on Notion to build integrations with various data sources—orBox, orGlean, or, eventually I’m sure, Granola—shouldn’t it be managed by something that’s more infrastructure than application? In a repository that can hold, for all intents and purposes, unlimited amounts of information? One that invests a lot in how fast people can run calculations over that data? And supports different ways to query it? And lets you build custom apps on top of it?


The easy answer is yes, not only should it exist; it already does. It’s called Databricks.


Eighteen months ago, Iwould’ve agreed. Now, I’m not so sure. Because it seems like what’s needed in a platform like this isn’t an actual database, but something that rhymes with one.


Imagine, for example, how you might answer the question, “What sales deals need my help?” I don’t know; here’s something I came up with in about two minutes:

1. Go get all of the customer emails and internal meeting notes about deals that are currently in progress.
2. Go get all the same information for last quarter’s deals, and group them by if they were won or lost.
3. For each deal in progress, compare that account’s emails to the emails from won and lost accounts. Ask the LLM: Which set is it more similar to? If you had to guess, from reading these emails, if this deal was going to be won or lost, what would you guess?
4. Do the same thing for internal meeting notes.
5. Find the accounts where there’s a mismatch—where the customer emails suggest that you’re going to lose the deal, but the internal conversations say you won’t. Those seem bad? Go help those!


You can’t do this with Notion’s or Granola’s chatbot, nor does it really make sense to do with a database, because the primitives are different. Data sources aren’t tables connected by joins, but documents that are associated by measures of semantic similarity.7Operations aren’t SQL queries, but chains of prompts—take the result from this question, and feed it into this subsequent prompt. Data might not be ingested in the “database” directly, but retrieved on the fly via MCP.8


Surely, people have a gazillion ideas like this sales “query” right now. There are questions people would ask if they could stuff a bunch of documents into ChatGPT without having to manually paste them in. There are analyses people would experiment with, if that analysis was cheap to try out. There are internal tools that people would build if they could take data from one place, mash it through an LLM, find new data based on that result, and mash all it through another prompt. None of these things are conceptually hard to do—and much easier, probably, than coming up with what to do with quantitative data—they’re just a pain to build.


When people talk about how AI could change data (and other concerns), they tend to talk aboutSQL-writing copilotsandagentic analytics platforms. The future is agents, finding the insights in our database that we could not.


I’d bet on the inverse. The potential energy in analytics is in a better data source, not in better analysis. And it’s not the analyst that needs to be different, but the database. (And you can trust me on that—I’m never wrong about this database stuff.)

[1](https://benn.substack.com/p/we-need-a-new-database#footnote-anchor-1-163720943)

The best way forbenn.ventures’ investments to return the fund is for benn.ventures toraise three funds.

[2](https://benn.substack.com/p/we-need-a-new-database#footnote-anchor-2-163720943)

See,people on Redditsay that we don’t talk enough about how historically terrible the Hornets are. But maybe that’s because Eric Collins is constantly losing his mind overmediocre dunks in the second quarter of a 15-point blowout, and ittricks us into thinkingthe Hornets are in fact exciting.

[3](https://benn.substack.com/p/we-need-a-new-database#footnote-anchor-3-163720943)

Yes, they bought alotofCoronas, and a…vodka and blue raspberry tonic?

[4](https://benn.substack.com/p/we-need-a-new-database#footnote-anchor-4-163720943)

And certainly not how it works for the Charlotte Hornets.

[5](https://benn.substack.com/p/we-need-a-new-database#footnote-anchor-5-163720943)

Everything becomes BI, even your note-taking app.

[6](https://benn.substack.com/p/we-need-a-new-database#footnote-anchor-6-163720943)

Everything becomes BI, even your other note-taking app.

[7](https://benn.substack.com/p/we-need-a-new-database#footnote-anchor-7-163720943)

E.g., “Take these engineering tickets, and figure out which features they’re talking about. Then, find all the support tickets in which people complained about those features.” That’skindaa join?

[8](https://benn.substack.com/p/we-need-a-new-database#footnote-anchor-8-163720943)

Was the real data mesh MCP? Does making this joke make me question my life choices?
