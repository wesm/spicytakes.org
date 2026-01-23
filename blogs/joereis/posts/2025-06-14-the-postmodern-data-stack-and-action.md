---
title: "The Postmodern Data Stack & Action-Oriented Architecture"
subtitle: "Joe's Nerdy Rants #81 - Weekend reads, podcasts, and other stuff"
date: 2025-06-14T16:46:10+00:00
url: https://joereis.substack.com/p/the-postmodern-data-stack-and-action
slug: the-postmodern-data-stack-and-action
word_count: 1975
---


![](https://substackcdn.com/image/fetch/$s_!d8D5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F18cc9fc0-bb12-4fb0-b5a3-34393f1110bc_1024x1024.png)

*Very Serious Corporate Joe (tm) vibe-coding a new Postmodern Data Stack*

0:00
-16:29

Every vendor at Snowflake and Databricks conferences had an AI story. Unlike other years, the stories finally started making sense to me.


In the past, AI demos felt superficial, usually just a chatbot with some ✨ sparkly emojis slapped on to some janky ChatGPT wrapper. Now, AI is moving under the hood. It’s becoming part of the system architecture, not just a UI layer or a wrapper.


I’ve been thinking a lot about the evolution of our data architectures and why the commonly used term “Postmodern Data Stack1” actually makes sense now.


The Modern Data Stack was defined by cloud-native tooling, the separation of storage and compute, and a slew of vendors and tools that you could bolt together. Of course, interoperability between tools often leaves much to be desired. Many MDS companies during the ZIRP era were more akin to features. Useful features, but probably not sustainable for growing companies. And as interest rates rose in 2022, the VC funding environment dried up for data startups, and the Great Data Stack Consolidation began. As Iwrote last week, consolidation is underway, along with platform encroachment into its partner ecosystem.


Like its philosophical namesake, the Postmodern Data Stack embraces contradiction, fragmentation, and a deliberate ambiguity embodied in data architecture. If Modernism is about order and rationality, Postmodernism responds with irony, vibes, and a questioning of grand narratives.


We’re seeing something similar play out in data right now.


In the past, architectures were mostly deterministic and idempotent. I saymostlybecause ML is inherently probabilistic and has been a mainstay in many systems for a long time. The latest incarnation of AI, especially vibe coding, is ushering in something of a Postmodern reaction to the way we’ve done things.


It wasn’t long ago that data scientists prized clean code. Now I hear some say the days of caring deeply about quality or robustness are behind us. No longer is idempotency guaranteed, nor is it a major concern for some people. Classical ML is now considered crusty and old-fashioned. Just “vibe.” And with vibes, you probably don’t know what’s being created under the hood, security vulnerabilities and all. This is a reality we’re going to have to get used to, no matter how dumb or reckless it seems. Much like Post Modernism was a reaction to rationality, we’re now in something resembling a post-truth age for architecture.


It’s not all bad, and some things excite me about this future.


Especially popular right now are agents and Model Context Protocol (MCP) implementations across various data vendors and open source tools. Despitelegitimate complaintsabout the robustness of MCP, MCP is here to stay (until its replacement comes along next week, as things happen now) as the protocol for LLMs interacting with databases and APIs, or at least until something else takes its place. Everybody’s got an agent, and everyone’s got an MCP.


While demoing a new MCP server from a popular BI vendor last week, I noticed how familiar it all felt: connect to a data source, ask natural language questions like “what were sales last month?” or “how many users signed up?” These are descriptive questions - what, when, and who. We’ve seen this movie before. The use of MCP wasn’t very imaginative, and felt like it was tacked on so the vendor could have an MCP demo.


To me, the real value of AI isn’t in answering “what” or “when.” It’s unlocking “how” and “why.” During the demo, I took the wheel and asked the LLM strategic questions:

- “What should I do to increase revenue?”
- “Where should I focus my attention in this scenario?”
- “Give me a game plan for pricing.”


Now, if this system has agents or API integrations that can take actions on these interactions, that would be the next natural step. That’s the future I want to see.


For years, I’ve been writing about the shift toward action-oriented interfaces. In Fundamentals of Data Engineering, we called it the Live Data Stack. As I wrote in the book and elsewhere, I criticized real-time analytics with the simple scenario of staring at a real-time report for outliers. Why not simply take action when the outlier occurs, and inform me of the outcome once those actions are completed?


Today’s analytics tools are still stuck solving problems of the past: visualize what happened, slice and dice dimensions, let a human interpret, make a decision, and (maybe) act. That’s still important, but we can start thinking about how to take this a step further, with teams of hundreds, thousands, or even millions of autonomous agents.


These are automations you can dowithoutagents, and have existed for decades.

- “Inventory looked off, so I reordered the top five SKUs.”
- “Ad campaign CTR dropped by X, and budget reallocated to higher-performing channels.”


With agents, I’m guessing we’ll see workflows where actions are optimized up and down the stack. In the inventory example, in addition to reordering the top five SKUs, it also received bids from suppliers, negotiated the best shipping rates, and scheduled shipments to arrive and be stocked at the optimal warehouses. All of this took place in minutes, and the agents continually optimized the entire supply chain from the time the inventory was ordered to when it arrived in the warehouse.


We’re moving from dashboards to decision engines. From analysts to autonomous agents. From “let me know” to “just do it or fix it.”


It’s early days, and I’m not ready to hand over full control of my company or personal life to agents just yet. But I can tell they’re getting better. Perhaps soon, running AI-generated code will feel as normal as running automated CI/CD pipelines. I still have mixed feelings about this, as a ton of controls and guardrails are needed to prevent problems. I half-joke that the apocalypse will happen because rogue AI agents perform DROP TABLE and remove all backups in every corporation and government system around the world.


Bringing it back. If I had to describe the Postmodern Data Stack, for now in mid-2025, it would be this:

- Strategic AI partners
- Automated actions
- Agentic workflows
- Shift left for developers, shift right for decision-makers.
- “Vibe coding” where it makes sense, with guardrails, security, and proper governance. Otherwise,Fuck Around and Find Out.
- Self-healing systems
- Action-oriented. (My friend Bruno Aziza is alsotalking about this.)


It’s not unlike the shift from punch cards and mainframes to terminals and GUIs. The interface layer is changing again. This time, it’s less about screens and more about conversations, intent, and autonomous execution. That’s the shift. Not from data to charts, but from data to decisions, and eventually, from decisions to autonomous outcomes. All done at a scale far beyond what humans can do today without AI.


The old data stack was built for hindsight. This one is built for foresight, action, and even autonomy. Welcome to the Postmodern Data Stack.


Please listen to the audio above or onSpotify(or your podcast platform of choice).


Have a wonderful weekend,


Joe


---


### Is your data stack too complex and expensive?


Stop juggling 10+ tools for extraction, transformation, and storage.Keboolais the all-in-one data operations platform that replaces your entire brittle stack. Connect to 700+ sources, transform with SQL or Python, and load to Snowflake or BigQuery in one place.


Now with the newKeboola MCP Server, their AI assistant can understand your data and build real infrastructure, not just code snippets. It's AI that knows your business, on a platform built for production.Check out Keboola's MCP Server


Thanks toKeboolafor sponsoring this newsletter.


---


# Cool Weekend Reads


Here are some cool articles I read this week. Enjoy!


This city is exploring an unconventional solution to water scarcity: sewage


Inside The Exclusive, Obsessive, Surprisingly Litigious World Of Luxury Fitness


The Gentle Singularity - Sam Altman


“Localhost tracking” explained. It could cost Meta 32 billion.


A Month(ish) of Vibes with Cursor


Model Once, Represent Everywhere: UDA (Unified Data Architecture) at Netflix


Coordinated Progress – Part 1 – Seeing the System: The Graph


CEO Says AI Will Replace So Many Jobs That It’ll Cause a Major Recession(No shit…)


---


### Everyone’s talking about data products, but what does that actually mean?


Are they dashboards? APIs? Embedded analytics? GoodData’s Ryan Dolley chatted with Santona Tuli, Ph.D. to discuss what is (and isn’t) a data product and the key principles in designing and scaling successful data products.


Whether you're an analytics engineer enabling self-service, a product developer embedding insights, or a product owner looking to monetize data, this session will give you a clear framework to build, scale, and succeed with data products. 🚀


📺 Watch the full session here.


Thanks toGoodDatafor sponsoring this newsletter.


---


# Upcoming Events


---


Utah Data Engineering Meetup, June 18.Register here


Iceland - Global Data Summit, June 23-24.Register here


Australia (Sydney, Melbourne) - Data Eng Bytes, July 24-30.Register here


US Tour - September TBA


UK - Big Data London, September 24-25.Register here


Montenegro - October TBA


Vienna - October TBA


Helsinki Data Week - October TBA


Paris - Various spots in November TBA


More to be announced soon…


---


# Podcasts


Freestyle Fridays - Next-Generation Data Architectures. Ramblings and Musings (Spotify)


Zhamak Dehghani - Autonomous Data Products, Decentralized Data and AI, and More (Spotify,YouTube)


Matthew Scullion - The Agentic Data Engineering Team  (Spotify,YouTube)


Freestyle Fridays - Platform or Predator? (Spotify)


Svetlana Tarnagurskaja - Building a Boutique Data Consultancy (Spotify,YouTube)


DuckLake w/ Hannes Mühleisen - Practical Data Lunch and Learn. June 4, 2025 (Spotify,YouTube)


Ash Smith - Data Products, Interoperability, Data Teams, and More (Spotify,YouTube)


Freestyle Fridays - So You Want to Work in Data? w/ Gordon Wong (Spotify)


Hamilton Ulmer - Instant SQL with DuckDB/MotherDuck - Practical Data Lunch and Learn (Spotify)


Gaëlle Seret - Change Management in Large Organizations (Spotify)


Freestyle Fridays - AI Denialism is Holding Back the Data Industry (Spotify)


Ryan Russon - Practical ML Engineering (Spotify)


Freestyle Fridays - What Does AI Do to The Craft of Dev and Engineering? (Spotify)


Laura McDonald - Navigating the Complex World of Enterprise Sales (Spotify)


Freestyle Friday - Navigating Data Strategy in the Age of AI w/ Dia Adams & Gordon Wong (Spotify)


Michael Drogalis - Building a Company in Public (Spotify)


John Giles - The Data Elephant in the Board Room, Data Modeling, and More (Spotify)


There are way more episodes over at the Joe Reis Show, available onSpotify,Apple Podcasts, or wherever you get your podcasts. Also available onYouTube.


---


# Thanks! If you want to support this newsletter

- The Data Engineering Professional Certificate is one of the most popular courses on Coursera! Learn practical data engineering with lots of challenging hands-on examples. Shoutout to the fantastic people at Deeplearning.ai and AWS, who helped make this a reality over the last year. Enrollhere.
- Practical Data Modeling. Great discussions about data modeling with data practitioners. This is also where early drafts of my new data modeling book will be published.
- Fundamentals of Data Engineering by Matt Housley and I, available atAmazon,O’Reilly, and wherever you get your books.
- The Data Therapy Session calendar is postedhere. It’s an incredible group where you can share your experiences with data - good and bad - in a judgment-free place with other data professionals. If you’re interested in regularly attending, add it to your calendar.
- My other show is The Joe Reis Show (Spotifyand wherever you get your podcasts). I interview guests on it, and it’s unscripted, always fun, and free of shilling.


Thanks!


Joe Reis


Thanks for reading Joe’s Nerdy Rants! Subscribe for free to receive new posts and support my work.

[1](https://joereis.substack.com/p/the-postmodern-data-stack-and-action#footnote-anchor-1-165747103)

I’m definitely not the first person to use this term. And I hated it for a long time, but it’s actually very appropriate in the age of vibe coding.
