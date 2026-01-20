---
title: "We don’t need another SQL chatbot"
subtitle: "We want one, to do the tedious parts of our job. But it might be better suited to take the fun parts."
date: 2023-07-14T18:29:30+00:00
url: https://benn.substack.com/p/we-dont-need-another-sql-chatbot
slug: we-dont-need-another-sql-chatbot
word_count: 2634
---


![](https://substackcdn.com/image/fetch/$s_!M2iy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3cf4c63f-0f38-4822-ba34-ca0b5e3fe745_3488x1958.png)

*Attack of the the Clones, 2002.*


Another week, another text-to-SQL chatbot.


Ask it a question; it’ll write a query. Ask it a question, it’ll send a thin prompt to ChatGPT: “You are a senior data analyst. Here are some notes about a few tables and a sample query.” Ask it a question, and it’ll send your entire schema, your dbt project, and your data dictionary’s API keys to Claude. It uses LangChain to validate SQL syntax;it doesn’t use LangChainbecause it’s too slow; it uses LangChain to ensure industry-leading accuracy; it doesn’t use LangChain because its errors compound intoa Waluigi.


The bots are everywhere. They’re launching on Hacker News; they’re asking for your upvotes on Product Hunt. They’re in your Slack; they’re in your database; they’re in your Twitter DMs; they’re in Section 4, Article C of the update to your terms of surface. They’re tacked on to your favorite data tool; they’re your friend’s startup; they’re your other friend’s startup’s pivot. They’re a YC company; they’re backed by Accel; they raised $500 million from Masayoshi Son.


Never write a SQL query again; chat with your data. Never file another ticket with a data team; ask Dash, or Alan, or Newton,1your friendly neighborhood analyst. It will respond with an answer; it will respond with charts, and a SQL query. It will ask for your feedback on what it told you. It will be there for you on Slack, or Teams, or over email. Its responses will be full of emojis; its responses will include cutesy jokes written by cheugy millennials.2


This is the future of analysis. ChatGPT’s Code Interpreter is the 🚨BIGGEST AI RELEASE YET 🚨, says a Twitter account that bought 200,000 followers. Data analysts are obsolete, says a Medium post. “Are data analysts obsolete?,” asks a user on Reddit who’s learning to become a data analyst.


No they aren’t, says a startup founder. An amateur historian on LinkedIn will say that AI gives them time to solve more important problems. Someone with a blog on a personal website will write a post about the history of technological innovation, citing Paul Graham, Tyler Cowen, and several articles that they found after googling “the history of technological innovation.”


And some contrarian clown will go on Substack to throw a fit about these bots, to question if they work, and to suggest that they may still replace analysts after all—but, of course, not in the way that we all expect.


# Twenty pages of context in a ten-page window


If you build a product with charts, you’re going to build a BI tool.


Nobody believes it at first.We tell ourselves that this time is different. We’re solving a different problem, for a different audience. We can make something complementary to BI, something narrower, lighter, more focused. We tell ourselves we're more principled than the others; we have more discipline;wewon't cave andbuildpiecharts.


Maybe we're right, in theory; maybe it can, eventually, be done. But the market can stay irrationallonger than a startup can stay solvent. And our customers will see our charts and want more of them; they'll want reports, and alerts, and explorable dashboards that can be exported as a PDF. They'll want granular permissions, and to connect to an old version of SQL Server running on aDell Optiplex 3020under Jeff's desk.3They'll want exactly what we’re selling, plus just this one feature, and they'll pay us $100,000 if we can build it.


This is the devil thatfollows all of us. Andtwo of themare hunting for every chatbot and AI-powered SQL writer.


The first monster is BI itself—most query generators are destined to be BI tools in their own right. If it writes a query, people will want it to run a query; then they’ll want to chart the results; and then pin them somewhere, and then drill into them by clicking on them, and then, and then, and then—and then you concede the inevitable andadmit to being BI.


But there’s a second parallel between chatbots and BI: For both, there’s a canyon between what works well enough to get a few customers and what works well enough to win a market.


An engineer can build a simple data visualization tool in a day. There are open-source libraries; there are well-documented APIs; there are best practices. But simple bar charts don’t support a venture-scale startup. Customers will want faceted bar charts, with four series, and two axes, and filters, adjusted so that weeks start on Monday, with the right date format, and branded fonts, and labels for the first day of every quarter, everyfiscalquarter, with a particular way of handling nulls, on six million records, and a trend line, that’s dashed, with the most recent incomplete week excluded from the calculation.


Similarly, getting GPT to write a SQL query on a tidy schema of six tables is relatively easy.4But prompting it to answer a vague question about orders from new accounts on top of 3,500 tables, that are named using abbreviations and legacy terms, and are full of messy and duplicative columns, and four different timestamps, where there are layers of relations to join through, and test accounts to exclude, and “new” is defined in a nuanced way, and any calculation about orders has to account for the way the sales team used to log contracts in Salesforce, for the way that the sales team now logs contracts in Salesforce, and for the way that one sales rogue rep always logged his contracts in Salesforce? That’s a very different beast.


For bots to be successful query writers—and even harder, for them to be proper analysts that can answer questions about a business—LLMs will likely only be a small part of the solution. There will also have to be semantic models, methods for mapping vague requests onto those semantic models, frameworks for governing access control, ways to test if it said thesame answer today as it said yesterday, and more. Building a good text-to-SQL bot requires building systems that include all of this context in the prompt, despite it being far more information than can easily fit in the context window of an LLM.


Put differently, the LLM isn’t an application, or even close to one. It’s a fancy function inside of an application—and building the rest of that application likely requires far more work than anything done with OpenAI’s API.5Which isn’t to say that it’s impossible to build a product that writes good queries from fuzzy questions (and the unavoidable pieces of BI that come with it)—it just takes a tremendous amount of work and ingenuity.6


More bluntly, LLMs and query writing are fundamentally mismatched. The former is probabilistic, creative, andinductive—it’s best used to generate ideas from short prompts. But analysts have to do the opposite when answering questions. They need to be precise, rigorous, anddeductive—they need to know all of the nuanced laws governing how data is used, and apply them to questions that don’t specify those details.


But that doesn’t mean that LLMs aren’t useful for data analysis, or that all of our jobs are safe. It just means that most query bots are focused on the wrong problem.


# We can be good, or we can have fun


In a very rough sense, we can plot all of the tasks we do for our jobs and in our lives along a single axis. At the bottom, there are mechanical tasks that are mostly mindless legwork—digging holes, filing papers in filing cabinets, scheduling a meeting over email,printing out binders full of chartsfor an executive team’s weekly business review. At the top, there are “strategic” and creative projects—designing a building, diagnosing a patient, giving a sales pitch to a prospective customer, making decisions about how to run a company. You could also place the components of an individual task along the spectrum as well: When planning a night out, booking a reservation is lower than choosing the restaurant; when working with data, typing correct SQL syntax is lower than reasoning through a query, which is lower than coming up with an analytical technique for answering a question.


There are lots of ways that people might describe each pole. The bottom is repetitive; low-skill; boring; frustrating; simple. The top is inventive; high-skill; interesting; fun; intellectual. For obvious reasons, given the choice of where we want to spend their time—either in our careers or in a single task—most of us would probably say the top.7


Computers, in a very rough sense, usually help us do that. We don’t have to dig as many holes because machines can do it for us. We don’t have to file papers in filing cabinets, or even have files at all; computers can organize millions of documents in milliseconds. We have software that can help us schedule meetings, and BI tools that will replace our three-ring binders with live dashboards that update entirely on their own.


Moreover, over the last several decades, as computers have gotten "smarter," they’ve typically moved up the spectrum—and let us spend more and more time at the top. They used to only be able to dobasic math; then they could docomplicated math. Then theymade charts, and now they can makeinteractive forecasts that update by the minute. Computers replaced ourdaily planners, then theyhelped usschedule meetings, and now theyshame usfor scheduling meetings.


This pattern—computers automating more and more mechanical work; people doing more and more creative work—has become our default assumption about how technology advances,andfor what we should do with new technology. New inventions push up the boundary that divides what computers can do from what we have to do; with every new tool, we try to figure out how we can hand over our most tedious remaining errands to the machines.


But this doesn’t have to continue forever. Technology could—again, in a very rough sense—go the other way. It could be more creative than reliable. It could subsume our lives from the top down, outperforming us in strategic tasks while struggling with the tactical ones. If this happens, the best things we could build with it might impose a choice: Do we use it to make us better at something, or do we use it to replace something we don’t want to do?


Because so far, one of the most striking things about LLMs is that they’re much better at the creative parts of analysis than they are at the mechanical parts.8Ask ChatGPT to write a SQL query against an artificially simple schema;it’s a junior analyst, at best. But ask it to come up with possible hypotheses to explain why there’s some anomaly in a metric, and it does better than I would.9


For example, we gave ChatGPT a dataset with a bunch of events that are exactly—and suspiciously—one hour apart. When we asked it why that might be the case, it gave more reasons than I could come up with: Coincidence; programmatically scheduled activities; a time zone issue; system maintenance; the product could be one that people use at regular intervals; and access restrictions or throttling could queue user actions to reset every hour. That’s pretty good! And when we asked it how to figure out which one it might be, it had pretty good ideas for that too. It didn’t, however, do a good job of writing the queries that would run that analysis.


In other words,it inverted the workflow between human and computer.It was better at coming up with ideas than I was; I was better at doing the work. I was its assistant, its agent, its copilot. It was assigning instructions, and I was following them. It didn’t allow me to work on higher value work; it did the higher value work, and told me how to do the manual labor.


I’m not sure that I want to say that all the query-writing chatbots should pivot into analytical reasoning bots. That’sthe job I want, to be at the top of the creative food chain with an army of machines doing the mundane tedium below me. But the army we’re building—creative, unpredictable, and equally prone to both novel ideas and lies—is becomingmore man than machine. If we’re looking for chatbots that make us all better at working with data, without having to rebuild an entire BI tool in the process, our best option may be to let them do the jobwewanted to do all along.

[1](https://benn.substack.com/p/we-dont-need-another-sql-chatbot#footnote-anchor-1-134863380)

These names aren’t real, but they’re close to the real ones. My point here isn’t to single anything out, so I leave it to the reader to google “sql writing bot,” or to imagine which one is, in fact, in my Twitter DMs.

[2](https://benn.substack.com/p/we-dont-need-another-sql-chatbot#footnote-anchor-2-134863380)

Somehow, this style has become the standard for these sorts of things. As far as I can tell, Slack started it, with the twee Slackbot aesthetic. Now, every other brand is a clumsy and lovable klutz who enjoys using emojis, attempting humor, and phrases like “D’oh!”

[3](https://benn.substack.com/p/we-dont-need-another-sql-chatbot#footnote-anchor-3-134863380)

Jeff, of course, quit eight years ago.

[4](https://benn.substack.com/p/we-dont-need-another-sql-chatbot#footnote-anchor-4-134863380)

For example,this paperevaluates how well a model performs in various text-to-SQL tasks. Though they stress-test different models by using imprecise language (e.g., asking for puppies when pets are labeled as dogs), the tests appear to be run against very small schemas often with fewer than a dozen tables. And even against that benchmark, the SQL is correct only eighty percent of the time.

[5](https://benn.substack.com/p/we-dont-need-another-sql-chatbot#footnote-anchor-5-134863380)

There’s a longer post to write here about how LLMs fail (you know,forthebrand). The quick version goes something like this: We use LLMs to write SQL queries; they don’t work out of the box, so we start wrapping them with better prompts, and semantic models, and rules to make sure they return consistent results. Eventually, prompt engineering is just engineering, telling the model exactly what to do and how to handle edge cases, to the point that we’re working around the LLM as much as we’re working with it.

[6](https://benn.substack.com/p/we-dont-need-another-sql-chatbot#footnote-anchor-6-134863380)

This is one of the reasons why we took the call—and eventually, theacquisition offer—from ThoughtSpot. They’ve built both the BI tool and alot of the infrastructurethat can make LLMs useful for translating questions into queries. Obviously, other vendors could do that too, but it takes very real work, for which there aren’t yet any shortcuts. (So why bother,buy ThoughtSpot! OrMode! Or, like, skip a step, and just Venmo me, @Benn-Stancil.*)


* I’d rather use the Cash app, because theyouthstell me it’s the cool one, and because my handle (cashtag?) is $benn. However, I signed up for the Cash app ten years ago using a debit card that’s long since expired. I need to know that debit card number to log in to the Cash app, and my bank statement forensics have only yielded 10 of its 16 digits. So my handle—and a fortune of tens of dollars—is locked away forever behinda code I can’t quite remember.

[7](https://benn.substack.com/p/we-dont-need-another-sql-chatbot#footnote-anchor-7-134863380)

This is especially true if you’re three years and two jobs out of college, have spent nine months posting “content” on LinkedIn, and are interviewing to work for a startup. “I don’t care that much about the exact role; I just want to be working on stuff that’s really strategic,to have the kind of impact that I know I can have, you know?” says the 26-year old white guy whose résumé describes him as being low ego.

[8](https://benn.substack.com/p/we-dont-need-another-sql-chatbot#footnote-anchor-8-134863380)

Analysis, by the way, isn’t creatingvarious pivots of a datasetthat plot a bunch of dimensions against a bunch of metrics, or asking a computer to find “interesting” correlations in a spreadsheet. At best, that’s data profiling; at worst, it’s fishing for red herrings. Analysis is asking a hard question, coming with different hypotheses, finding evidence that supports or refutes those hypotheses, and drawing conclusions from it. It isindeed strangethat computers can now do the former, but it’s a very different thing than the latter.

[9](https://benn.substack.com/p/we-dont-need-another-sql-chatbot#footnote-anchor-9-134863380)

Yeah, yeah, low bar, I know.
