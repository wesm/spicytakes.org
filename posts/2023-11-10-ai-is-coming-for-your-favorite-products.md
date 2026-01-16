---
title: "AI is coming for your favorite product's good user experience"
subtitle: "And BI is still coming for everything, except Excel."
date: 2023-11-10T17:00:40+00:00
url: https://benn.substack.com/p/ai-is-coming-for-your-favorite-products
slug: ai-is-coming-for-your-favorite-products
word_count: 2687
---


![](https://substackcdn.com/image/fetch/$s_!fkxG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7600fe2-4eb2-4b1a-9b1a-4b0c29b3411d_1600x834.png)

*Squirrel!*


If you’re the CEO of a public company, Wall Street is probably going toask you questionsabout how you plan to use AI to make your business better. There are a couple ways you can answer those questions:

1. You can say that large language models are still a young and rapidly developing technology. Your team is closely monitoring how they’re evolving, and is experimenting with new ideas that you think will make your products better and your business more efficient. You can’t share too many details yet, however, because you want to make sure that you’re always delivering the best possible experience for your customers. That requires being decisive, but deliberate, especially when deploying a technology that reinvents the state-of-the-art every six months.
2. You can say YOLO, buy a .ai domain, and talk about all the chatbots you’re building.


Most CEOs, it seems,are choosing option 2. For example, in just the last three months, PwC builtChatPwCto help its employees research “common tax questions and regulations.” Walmart launched a tool calledMy Assistantto “change how our associates work and solve problems.” McKinsey rolled outLilli, a “platform that provides a streamlined, impartial search and synthesis of the firm’s vast stores of knowledge to bring our best insights, quickly and efficiently, to clients.” And EY isinvesting $1.4 billionin EY.ai.1


Software companies are building similar things in their products.Zoom AI Companionwill chat with you about the meeting that you’re in, and tell you what you missed if you joined late.Intercom Finwill answer half of your customer support questions on its own. Notion isfull of chatbots—it will take notes for you, write summaries of your notes, and edit them to be friendlier or more professional.Atlassian Intelligencelets you interact with Jira tickets via chat.Generative AI in Slackwill…bring the power of generative AI in Slack to help you work smarter, learn faster, and communicate better?2And inside of data companies, we all now have SQL-writing chatbots—Snowflake Copilot,Databricks Assistant,Atlan AI,Hex Magic,ThoughtSpot Sage,Equals AI Assist.


I have no idea how hard it is to create a botthat canscan McKinsey’s “entire landscape of knowledge, identify between five to seven of most relevant pieces of content, summarize key points, include links, and even identify experts in the appropriate fields,” or onethat canmonitor incoming Jira tickets and “resolve help requests instantly based on its understanding of knowledge base articles,” including asking “follow-up questions to take any necessary actions.” But I do have some sense of how hard it is to build a SQL-writing bot. And the answer is very hard.


There are challenges that everyone already points out: When I ask “How many accounts did we have in Europe last quarter?,” the bot has to determine what I mean by accounts, where exactly Europe is, and if I’m referring to a fiscal quarter or calendar quarter. It has to know what our fiscal quarter is. It has to know that engineers typically use the term account to refer to a team workspace in a SaaS product, and sales reps typically use the term account to refer to a business that they’re selling to. It has to guarantee, despite LLMs being probabilistic, that when it generates a second query based on my follow-up question, “Of those accounts, which ones were new?,” it builds on the exact same logic that it used in the prior question. It has to make a bunch of assumptions about what “new” means. It has to do all of this on messy data, often spread across thousands of constantly-changing tables that are undocumented, poorly named, and full of ambiguous and seemingly duplicative columns. And it has to know when it doesn’t know the answer, and notconfidently grandstand unhinged nonsense.


None of this is impossible, but it takes a lot of time and effort—and a lot of work that goes beyond tuning the AI model itself. You have to build and maintain integrations into metadata repositories; you’ve got to build infrastructure for storing that metadata and evaluating its usefulness; you’ve got to build systems for evaluating the accuracy of results; you have to test hundreds of versions of different prompts;3you have to build feedback loops to help models improve. And you have to let it all run, in the wild, for a long time, to collect and slowly stamp out the thousands of edge cases that no amount of pre-launch testing will ever uncover. It’sall handstands again—months of daily practice, and not a two-week sprint.


Most AI applications are probably like that. There’s some data engineer at McKinsey who thought they were joining a bleeding-edge research group to build Lilli; instead, they are now the permanent maintainer of a pipeline that’s supposed to ingest interview transcripts from a dozen different SharePoint sites. There’s a team inside Atlassian that spent two days working with GPT, and is now on month six of figuring out how to reliably interact with Jira’s APIs.


Unless the company is existentially bound making these features work, it’s easy to imagine the various chatbots and assistants slowly spiraling into decay. A flashy launch goes out the door; the CEO touts their bold vision;the stock shoots up. The initial version—rushed to market to satisfy an impatient Wall Street—is kind of a dud; it works fine on the simple requests, but falls down on the hard stuff that would be really valuable. But nobody is that upset, because nobody really wanted the feature that much in the first place. There was no burning need that it solved, orpressing jobs for it to do. It was mostly marketing, after all. So it stagnates in its half-built form, left in the product as demo candy, and to prove that the company is thinking about the future, until a new thing becomes the future, and we all move on.


It’s a movie we saw just a few years ago with the blockchain—until AI became the future, and we all moved on. In 2015,according to a surveyconducted by the World Economic Forum, more than half of global business leaders thought that ten percent of global GDP would be stored on the blockchain by 2027.4So, naturally, we bought some domains and built some useless products.


In 2017, the Long Island Iced Tea Corp.changed its nameto Long Blockchain Corp., moved to longblockchain.com, and announced their intent to “leverage the benefits of blockchain technology.” In 2018, EY released “blockchain audit technology” calledEY Blockchain Analyzer, saying it was the “first step in [their] ability to develop tools to test various blockchain-based business contracts.” Later that year, IBM and shipping giant Maersk launchedTradeLens, “a blockchain-enabled shipping solution designed to promote more efficient and secure global trade.” In early 2022, JPMorgan Chase announced that theywere committing $12 billionto new tech investments, including projects for staying ahead of the blockchain revolution: “We believe blockchain technology can be a game changer in terms of process optimization, improved client experience, and the creation of new revenue streams.”


It didn’t go great? Long Blockchain Corp’sstock also shot up—but then theystopped filing financial reportswith the SEC, gotforcibly delistedfrom the Nasdaq, never made any meaningful investments in blockchain technology, several people got chargedwith insider trading, and longblockchain.com now redirects to BestCryptoExchangeAustralia.com because, according to the site, Best Crypto Exchange Australia acquired the, uh, “established brand” of  Long Blockchain in 2021.5IBM and Maersk—i.e., real companies—shut down TradeLensin 2022.6EY and JPMorgan both shipped their products, but I suspect it took much longer than most people expected—they launched less than a month ago. On October 11,JPMorgan went live“with its first collateral settlement for clients using blockchain;” on October 17,EY announcedthat Blockchain Analyzer: Reconciler had its first enterprise client.


For companies launching AI products inside of existing, successful businesses,7this is probably the reality of what’s coming next. Some will be hype-hunting frauds, a lot of products like TradeLens will never really take off, and some, from the companies that are really committed to making them work, might end up beingsurprisingly useful. But without that effort, a lot of products will end up full of chatbots that get in our way, and there will be a lot ofglitterthat isn’t gold.


---


# BI is a black hole, part 28


In addition to building an SQL-writing AI assistant, Equals, a web-based spreadsheet that connects to databases, recentlylaunched dashboards.


It was inevitable, I suppose. If you cross the BI event horizon—which I’d say isbuilding chartsthat users can edit—you get pulled by an endless series of customer requests into building a fully-featured business intelligence tool. At leastit looks coolbefore you get pulverized into oblivion by requests for row-based access controls, for skeuomorphic charts that look like a fuel gauge, andPDF exports.


One of Equal’s promises, however, was that you wouldn’t need an export toExcel. When it first launched, Equals was unabashed inits ambitions to replace Excel. They weregoing after the king,straight through the front door. But now, that message seems to have softened, and theenemy is BI.


This new lean from Equals does raise an interesting question though: If Equals is becoming a BI tool, how has Excel—or perhaps more analogously, Google Sheets—resistedit? How have those products managed to remain distinct from BI, while tools like Equals, which was designed to be Excel “if it were built today,” are pulled into the black hole?


My best guess is Excel’s biggest weakness—that it’s disconnected from live data, and that every file is named monthly_results_final_v2_FINAL.xlsx—is actually its moat. What makes Excel (and Google Sheets) unique from BI is that it’s not just a tool for working with data; itisthe data. You can create in it; you can update it without being afraid that you might break something else; you can share it, all in a single file. You can save it, and know, with total confidence, that when you open it tomorrow, next week, or next year, it’ll be the same as it was when you last left it. It’s not a tool for exploring and presenting data—which is what BI is for—but a sharable, self-contained sandbox for writing down numbers and adding them up. That makes replacing Excel a catch-22: If you build a tool that solves its biggest problems—being disconnected and static—you’re suddenly building a BI tool and not Excel.


In Equals’launch post, they said that the “spreadsheet is the best interface for working with data.” BI tools are for working with data. Excel is also forstoringdata.


---


# Privatizing the efficiency gains


A common criticism of the 2008 bank bailouts was that theyprivatized the gains and socialized the losses. When bankers’ trades are good, they make money; when their trades blow up, taxpayers get the bill.


In some rough sense, the deal we sign with an employer when we take a job is that we’ll socialize our gains in exchange for socializing our losses. We get paid a steady salary, and the company takes on the risk that if we do something bad—like leaving an expensive computer running in the cloud for no reason—they’ll bear the cost. But if we do something good—like turn the expensive computer off—they get to keep the gains. They might fire us or promote us, but they lose—or make—the money.


In a recent blog post, an engineer who saved their company a lot of money by tweaking a few settings on their Snowflake database8wants toprivatize the gains:


> I ask management for a 30K raise after saving 500K and my message is still unread. I suspect I will eventually receive either nothing or 5K.


And from afollow-up post:


> There were some [other stories like the one from the first blog post], with a handful genuinely seeming to possibly add up to billions of dollars saved industry-wide, but the largest payout anyone ever received in the emails was $5K. Sampling bias, yadda yadda, listen, I'm pretty sure things are just fucked up.


I set up Mode’s Snowflake database a few years ago, and configured it in the same way that saved this other company $500,000, so, amen, pay me? But also, can you imagine a company that actually did this? Would I still get a $30,000 raise, or does it not count unless we wasted $500,000 first? What if I set up Snowflake to be egregiously inefficient, burning millions of dollars a year? Can I turn that down and collect ten percent of $5 million worth of savings? Can I collect ten percent of $5 million worth of savings because Icould’veset it up to be egregiously inefficient, but didn’t? If that’s too obvious, can I pay someone else to abuse Snowflake, with the promise of splitting my bonus with them when I fix it?


Or do we privatize the losses too? Should the blog post’s author’s company garnish $30,000 of some engineer’s wages for setting up Snowflake in a suboptimal way? If someone discovers a better configuration than what the author set up, do they have to pay that person part of their bonus?


Why stop with cloud computing costs? Ship a bug; get charged for it. Resolve an urgent support ticket for a customer that’s in the middle of a tricky renewal; make five percent commission on the deal. Schedule an unnecessary meeting,get charged $1,500. Cancel that meeting, get paid $1,500—presumably, out of the pocket of the person who scheduled it. Start areply-all stampedethat takes down Outlook and prevents all of Microsoft from scheduling any meetings for two days? Get paid $10 million? Owe 100,000 people $100 each? Get fired? I have no idea.


This is probably why we don’t do this. But I love afun scheme, and would be very excited if someone tried it.

[1](https://benn.substack.com/p/ai-is-coming-for-your-favorite-products#footnote-anchor-1-138759555)

EY.ai redirects to EY.com/ai. How disappointing. If you’re gonna commit to novelty domains, you gotta beall in.

[2](https://benn.substack.com/p/ai-is-coming-for-your-favorite-products#footnote-anchor-2-138759555)

Ironically, the premier enterprise chat application apparently has no clue what to do with chat-based generative AI technology. Like, what on earth is Slack actually announcing here? We’re told to “imagine” three times, what might happen “in the future” twice, and—in what is usually amechanical legal disclaimerbut in this post feels like the only substantive part—that ”any unreleased services or features referenced in this or other press releases or public statements are not currently available and may not be delivered on time or at all.”

[3](https://benn.substack.com/p/ai-is-coming-for-your-favorite-products#footnote-anchor-3-138759555)

Critically, this isn’t just about figuring out if you should tell the LLM it’s a “very helpful senior analyst” or a “expert in SQL,” or hownicely you ask it questions, though it is those things too. It’s also about testing now much schema metadata you provide in the prompt, if you provide sample queries or not, and various other inputs that can require days and weeks of effort to collect, before they can even be tested.

[4](https://benn.substack.com/p/ai-is-coming-for-your-favorite-products#footnote-anchor-4-138759555)

Today, in 2023, cryptocurrencies are worth$1.4 trillion, compared to a global GDP of$100 trillion. NGMI.

[5](https://benn.substack.com/p/ai-is-coming-for-your-favorite-products#footnote-anchor-5-138759555)

We’re already too far down this rabbit hole, but according to theSEC filing, there is a deck somewhere called the “Blockchain Strategy Deck” that was instrumental in convincing the management team of Long Island Iced Tea Corp to “shift its business from soft drink manufacturing to blockchain technology.” Magnificent. It’s like theinfamous WeWork slides, but also full of crimes.

[6](https://benn.substack.com/p/ai-is-coming-for-your-favorite-products#footnote-anchor-6-138759555)

Why, you might ask? Because “the need for full global industry collaboration has not been achieved,” obviously.

[7](https://benn.substack.com/p/ai-is-coming-for-your-favorite-products#footnote-anchor-7-138759555)

This is to say nothing about products that are built for AI. A lot more of these will be frauds, a lot more will be somewhere betweenawkwardand useless, and a lot will probably be useful. But all of them will at least be committed to the bit.

[8](https://benn.substack.com/p/ai-is-coming-for-your-favorite-products#footnote-anchor-8-138759555)

Specifically, Snowflake customers pay for the amount of time the database is running. Snowflake will automatically turn itself off after some period of inactivity, andyou can tell ithow long to wait before it does. It’s similar to a car engine; you don’t want to turn it off every time you take your foot off the gas, but don’t want to idle in a parking lot for ninety minutes either. To extend that analogy, Snowflake defaults to staying on during pauses of a few minutes, like stopping at a stoplight or waiting in line at a drive-thru; for a lot of customers, it’s probably fine to turn the car off in those moments.
