---
title: "Joe's Nerdy Rants #6"
subtitle: "Data Modeling is Dead! Long Live Data Modeling, plus weekend reads and other stuff"
date: 2023-06-24T16:14:12+00:00
url: https://joereis.substack.com/p/joes-nerdy-rants-6
slug: joes-nerdy-rants-6
word_count: 1711
---


# Data Modeling is Dead! Long Live Data Modeling.

0:00
-6:59

On Friday (6/23), I gave a new talk at the DAMA Vancouver event called “Data Modeling is Dead! Long Live Data Modeling.” I discussed why the data industry is at a crossroads with data modeling. At best, data modeling is on life support. We either get back to basics and revamp data modeling to work with modern business workflows and technologies, or we might as well forget about it and leave it in the dustbin of history.


There’s an urgency to get back on track with data modeling. The sudden enthusiasm and interest in AI (specifically large language models) mean companies are in a mad rush to turn their companies into “AI companies.” Based on my observations and discussions withmanycompanies and vendors, the underlying data in most companies is, at best, in shambles. Databases and data warehouses are a mess. Yet we’re going to stick LLMs on top of this, hoping to magically transform our capabilities. Most companies are still barely doing BI, and now they want to do AI. This won’t work.


Can’t we throw a semantic layer or data catalog on top of everything? This assumes 1) the underlying data is good and useful 2) the data captures the upstream business concepts, and the upstream data itself is good 3) you know the concepts you’re trying to encapsulate in the semantic layer. And a semantic layer is, at best, a bandaid that doesn’t solve the core problem that a lot of upstream data you depend upon is built on incredibly shaky ground these days. I think semantic layers are a good solution for analytics, but we need to zoom out and solve the root cause.


What’s at stake? For one, the current hype wave for AI might die a tragic death once companies realize their recent AI investments are trash. Furthermore, we just continue bandaging over issues instead of solving the root cause. AI without good data means a lot more bandages.


With respect to data modeling, here are some things I suggest we do or revisit to get back on track as an industry. I’ll dive into these in a future article, as there’s not enough space in my short rant to do each of these topics justice. These are also the basis for my new book on data modeling, hopefully coming out later this year.

- Make data modeling a core practice for any team that works with data - software, applications (these are particularly critical since if you get it wrong at the source, you’re just treating symptoms after the fact), analytics, data engineering, ML, and more.
- Bring back and revamp the practice of conceptual and logical data modeling. Make these simple to do, iterative, and traverse the data lifecycle.
- Model across the data lifecycle. We physically model in silos. Data flows like water, and we need to change our approach.
- Invest in data model patterns, perhaps incorporating these alongside LLMs.
- Stop the stupid and petty religious wars in data modeling. To all the purists out there who’ve been arguing for decades that your way is the one true way of data modeling - your tirades and idiotic behavior are holding the industry back. If your approach had worked by now, we wouldn’t be in this mess. Either be part of the solution or step the f*ck aside.
- Adopt a data product mindset. With data becoming central to external-facing customers, and internal uses of data moving beyond reports, we need to get out of the old ways of working with data. It’s not just reports and dashboards.
- “DataModelOps” - Excuse the ‘ops’ part, as I’m sure the world doesn’t need yet another ops. This is a placeholder for a new approach I’m working on that allows for the continuous automation and deployment of consistent and coherent models across the data lifecycle. Stay tuned.


We are at a critical point in the data industry. I suspect if we can’t get data modeling right, we’re in for a world of hurt. We need to use what worked and modernize and innovate what’s needed. You can be part of the change.


Again, this is a very short space for this content. Expect longer articles, a book, and plenty of discussions about this topic. With respect to data, this is the biggest thing on my mind right now.


Listen to the audio clip above on this topic, which is also my5 Minute Friday.


---


# Cool Weekend Reads


Here are some cool things I read this week…


### Tech, AI & Data


Emerging Architectures for LLM Applications (a16z)


“In this post, we’re sharing a reference architecture for the emerging LLM app stack. It shows the most common systems, tools, and design patterns we’ve seen used by AI startups and sophisticated tech companies. This stack is still very early and may change substantially as the underlying technology advances, but we hope it will be a useful reference for developers working with LLMs now.”


Complete with a new “app stack” diagram :)


Of course, Sequoia also has its ownLLM Stack article…


OpenAI Lobbied the E.U. to Water Down AI Regulation (Time)


It’s a feature of regulations, not a bug. If anyone is surprised that companies craft laws to their advantage, please get with the program. This is regulatory capture 101.


The AI Boom Has Silicon Valley on Another Manic Quest to Change the World (Bloomberg)


AI is the new gold rush. Same as it ever was.


The Age of Chat (New Yorker)


Really good long-form read about the potential and downsides of ubiquitous AI chatbots. On a related note, I’ve been thinking a lot about the value of in-person conversations and how they’ll see a resurgence in popularity once we’re all jaded with nonstop chatbot interactions.


How to make difficult technical decisions you and your team won't regret (Jordan Cutler)


It’s often hard for teams to get on the same page about technical decisions. There are costs - direct, indirect, and opportunity. This article provides a good framework for evaluating technical decisions.


### Business & Startups


Pro Take: CEO Leadership Is the Key to Realizing Full Value From Tech (WSJ)


“Despite the disappointing results, CEOs understand that there is no choice but to invest in digital technology, a driver of corporate productivity growth which in turn affects real wage growth across the entire economy.”


I have mixed feelings about this article. Executives are investing in “digital transformation” mostly out of FOMO and expectations but often without a clear plan for success. You can guess what happens next.


That said, the article is correct that digital transformation must be the mandate of the CEO, with the full faith and support of the CEO (no lip service). Anything less will fail.


GPT-4 Beats Humans in Pitch Effectiveness (Clarify Capital)


Might there be an AI-powered startup incubator someday?


Ultra low-cost smartphone attachment measures blood pressure at home (ArsTechnica)


High blood pressure is a huge problem. Imagine being able to check your blood pressure with your smartphone accurately. Hopefully, this saves lives. Also, Peter Attia had a really good podcast about the implications of high blood pressure on health (punchline - massive). Check out Peter Attia’s #258 –AMA #48: Blood pressure—how to measure, manage, and treat high blood pressure.


How hard is it to get VC money during a drought? We spent 6 monthsfollowing startup Yoodlize as they tried to raise their seed round (Fortune)


Super interesting to read about the challenge of raising money these days.


Elon Musk vs. Mark Zuckerberg? Dana White prepared to make 'biggest fight ever in the history of the world' (MMA Junkie)


This is the world we inhabit today - billionaires actively participating in a mix of Celebrity Deathmatch and Idiocracy. Make this happen!


---


# New Content, Events, and Upcoming Stuff


### This week


Monday Morning Data Chat - #131 - The Importance of Actionable Data to Inform Decision-Making w/ Joe Perez (Spotify)


The Joe Reis Show


Karl "Ivo" Sokolov - Innovating in Europe, Moving from Services to Product, Western and Eastern Europe, and More (Spotify)


Paul Blankley and Ryan Janssen - How LLMs will Change Data and Analytics (Spotify)


Veronika Durgin - Learning and Adapting in a Fast Changing World (Spotify)


5 Minute Friday -  Data Modeling is Dead. Long Live Data Modeling! (Spotify)


### Upcoming


Monday Morning Data Chat - Andrew Padilla


The Joe Reis Show - Tristan Handy, Colleen Fotsch, Ravit Jain, Kris Jenkins, and many more!


Here are some cool upcoming in-person events I’ll be at in June and beyond for 2023


Snowflake Summit Low Key Happy Hour - Vegas Edition. Monday 6/26.


Mage Magic Meetup, San Francisco Edition - Tuesday, 6/27 (register here)


Striim Presents - Data + AI Summit Recap and Mixer w/ Matt Housely and me. Plus book signing. - San Francisco, Wednesday, 6/28 (register here)


Joe Reis + dbt roadshow - Seattle, Atlanta, Chicago, and more. Details are coming soon.


Taking July off…🏔️, except for the virtual Portable Conference and a few other things. My calendar is otherwise completely blocked off from July to early August, so let’s chat over email or similar.


Portable Low Key Conference - July 12


DataEngByes. I’ll be on the continental tour in Perth, Brisbane, Melbourne, and Sydney for a couple of weeks. August 2023 (more info and registration)


Big Data London - I’m keynoting. Big up theLondon Massive. September 2023.


Europe - September 2023 TBA


Dubai - October 2023


Vegas - ReInvent 2023


More to come…


# Thanks! If you mind helping out…


Thanks for supporting my content. If you aren’t a subscriber, please consider subscribing to this Substack.


You can also find me here:


Monday Morning Data Chat (YouTube/Spotifyand wherever you get your podcasts). Matt Housely and I interview the top people in the field. Live and unscripted. Zero shilling tolerated.


The Joe Reis Show (Spotifyand wherever you get your podcasts). My other show. I interview guests, and it’s totally unscripted with no shilling.


Fundamentals of Data Engineering (Amazon,O’Reilly, and wherever you get your books)


Be sure to leave a nice review if you like the content.


Thanks! - Joe Reis


Thanks for reading Joe Reis! Subscribe for free to receive new posts and support my work.
