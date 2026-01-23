---
title: "The Tortoise and the Hare - Horizontal vs Vertical Integration"
subtitle: "Joe's Nerdy Rants #48 - Weekend reads and other stuff"
date: 2024-07-13T17:30:50+00:00
url: https://joereis.substack.com/p/the-tortoise-and-the-hare-horizontal
slug: the-tortoise-and-the-hare-horizontal
word_count: 1479
---


I really enjoyed the recent podcast with Nick Schrock (Dagster, GraphSQL, etc) and Wes McKinney (Pandas, Arrow, Ibis, Voltron, etc). Around the 58 minute mark, the conversation moved to the heart of a big crossroads the data industry finds itself right now. Do we go the route of a handful of vertically-integrated Mega Platforms (big clouds and similar) or a horizontal interoperable ecosystem of open technologies? This is a tension that’s played out many times in tech, and it seems like we’re here once again.


Nick kicked this off by saying1, “I think one of the biggest things that's gonna happen in the next few years is like this, there's just gonna be this tension between all the big companies are gonna try to vertically integrate and provide tools in every category. Because a lot of their customers just want out of the box solutions. There needs to be a countervailing force of horizontal integration slash composability. And I think it's gonna carry out in multiple planes in the data stack.” He further says, “what world do you want to live in? A vertically integrated one or one where it's horizontally integrated and best of breed? But it's really challenging to deliver cohesive user experiences in the horizontal integration world. So whoever can do that can provide a ton of value for the community and the ecosystem.”


Then Wes added, “I mean, it's like the tortoise and the hare approach. So I think the modular data stack, the horizontal approach, is definitely the tortoise approach. It requires a lot of open source diplomacy, a lot of coordination across projects, getting people to agree to specialize and then work together toward productive ends. It's very laborious. But we've had our heads down. Just doing that. And so I think having, you know, now we've got really great open source orchestration solutions. We've got good modular computing engines, open data lake formats, open source file formats, protocols for building database drivers and building distributed systems that use these kind of open standards and protocols. So all the right pieces are are falling into place. It takes a lot longer than building a vertically integrated system. But I think ultimately we're by kind of doing the reverse tower of Babel approach. We're going to get to some place that's more interesting and ultimately, has a lot better staying power and lends itself also to better long-term maintainability because we don't have tight coupling between components so that we can incrementally say, well, it's time to like rethink our approach to this problem.”


All of this is against the backdrop of

- Big clouds clamoring for dominance
- Snowflake vs Databricks
- Whether open table formats will be “open”
- The death of the modern data stack and question marks on what happens with the bajillion MDS vendors and projects
- Data team budgets under intense scrutiny, assuming there’s a data team remaining at all…
- A red-hot AI hype cycle where seemingly every MDS vendor is now an “AI” company.


The last one is particularly interesting. I’m not sure what horizontal integration looks like in AI. Non-AI horizontal integration is hard enough, but I think it’s doable. As Wes says, it’s a slow game. I think it’s the right one too, in the same way that Linux and other open-source tools eventually won the mindshare of software developers. It took a long time, but peoplegenerallyfigured out how to make various open-source tools work together. Now open-source is the standard in any software development stack (pick your stack/tool combo - they’re mostly going to be open source). Data’s catching up with software, and I think we’ll see a similar ecosystem within the decade.


AI’s another story entirely, mainly because model training is insanely expensive. Right now, it’s much more cost-effective for developers to plug into the APIs of the major AI vendors (OpenAI, Anthropic, Google, etc). I know of people hosting open-source Llama models (among others), and Huggingface is hugely popular. I’d hate to see a world where the AI-Industrial Complex is the gatekeeper to models. It already sucks seeing the big clouds as the tollroads for many companies’ tech and data workloads, although cloud repatriation is thankfully happening where it makes sense.


Even after the current AI bubble pops (the one where LLMs are somehow the same as “AI”), I think we’ll have a world of models we have today, models we can’t even fathom today, AI-powered workflows, and so on. That’s how technology’s always been. The big question is who owns this stack - a handful of big megacorporations or nobody? For innovation and humanity’s sake, I very much hope it’s the latter.


Hope you have a fun weekend!


Thanks,


Joe


P.S. If you haven’t done so, please sign up forPractical Data Modeling. There are lots of great discussions on data modeling, and I’ll also be releasing early drafts of chapters for my new data modeling book here. Thanks!


---


# Cool Weekend Reads


AI industry needs to earn $600 billion per year to pay for massive hardware spend — fears of an AI bubble intensify in wake of Sequoia report (Tom's Hardware)andAI’s $600B Question (Sequoia Capital)


Cyber Safety Board Never Probed Causes of SolarWinds Breach (ProPublica)


DevRel's Death as Zero Interest Rate Phenomenon (DevTools Magazine)


AI’s Cognitive Mirror: The Illusion of Consciousness in the Digital Age (Empereur Pirate)


A Brief History of Modern Data Stack (Data Engineering Weekly)


Pop Culture (Where's Your Ed At)


The Right Kind of Stubborn (Paul Graham)


White-Collar Work Is Just Meetings Now - The Atlantic


The AI summer (Benedict Evans)


GraphRAG Analysis, Part 1: How Indexing Elevates Knowledge Graph Performance in RAG (AI Encoder)


OpenAI, Google, Adobe and More Have Embraced the Sparkle Emoji for AI (Bloomberg)


Rise of the Restaurant Robots: Chipotle, Sweetgreen and Others Bet on Automation (WSJ)


# New Content, Events, and Upcoming Stuff


## The Joe Reis Show


#### This week…


5 Minute Friday w/ Matthew Mullins - Two Gumpy Old Men Screaming at the Sky (Spotify)


#### In case you missed it…


Steve Macleod - The Importance of Operational Data Modeling (Spotify)


5 Minute Friday - F*ck Around and Find Out, AI Edition (Spotify)


The Finnish Data Mafia - What’s Up With Data in Finland? (Spotify)


5 Minute Friday - Mixed Model Arts (Spotify)


Nick Freund - Closing a Startup (Spotify)


5 Minute Friday - “Success” (Spotify)


Doug Needham - Architecture Deep Dive, The Hard Work of Generative AI in the Enterprise, and more (Spotify)


Bill Inmon - History Lessons of the Data Industry. This is a real treat and a very rare conversation with the godfather himself (Spotify) - PINNED HERE.


## Monday Morning Data Chat


Note: Matt Housley and I are taking the Summer off from the Monday Morning Data Chat. We will be back in the Fall with an incredible new lineup.


#### In case you missed it…


Nick Schrock & Wes McKinney - Composable Data Stacks and more (Spotify,YouTube)


Zhamak Dehghani + Summer Break Special (Spotify,YouTube)


Chris Tabb - Platform Gravity (YouTube)


Ghalib Suleiman - The Zero-Interest Hangover in Data and AI (Spotify,YouTube)


Bart Vandekerckhove - Data Security Deep Dive (Spotify,YouTube)


Yali Sassoon - Using LLMs to Support the Analytics Workflow (Spotify,YouTube)


David Yaffe & John Kutay - The State of Streaming and Change Data Capture (Spotify,YouTube)


## Events I’m At


Big Data London - London, UK. September 18-19.Register here


DataEngBytes - Australia/New Zealand. September 24 - October 4.Register here


Coalesce - Las Vegas -Register here


GenAI Summit, Atlanta - October TBA


Helsinki Data Week - October 28 - November 1.Register here


Paris - November TBA


Data Day Texas - January 25, 2025. Austin, TX.Register here


Much more to be announced soon…


# Thanks! If you want to help out…


Thanks for supporting my content. If you aren’t a subscriber, please consider subscribing to this Substack.


Would you like me to speak at your event?Submit a speaking requesthere.


You can also find me here:

- Monday Morning Data Chat (YouTube/Spotifyand wherever you get your podcasts). Matt Housely and I interview the top people in the field. Live and unscripted.
- My other show is The Joe Reis Show (Spotifyand wherever you get your podcasts). I interview guests on it, and it’s unscripted and free of shilling.
- Practical Data Modeling. Great discussions about data modeling with data practitioners. This is also where early drafts of my new data modeling book will be published.
- Fundamentals of Data Engineering by Matt Housley and I, available atAmazon,O’Reilly, and wherever you get your books.


Be sure to leave a lovely review if you like the content.


Thanks!


Joe Reis


Thanks for reading Joe’s Nerdy Rants! Subscribe for free to receive new posts and support my work.

[1](https://joereis.substack.com/p/the-tortoise-and-the-hare-horizontal#footnote-anchor-1-146471113)

I cleaned up a few words such as “like” and so on from the transcript to make the quotes easier to read.
