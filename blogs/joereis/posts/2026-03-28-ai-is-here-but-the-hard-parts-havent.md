---
title: "AI Is Here, But The Hard Parts Haven't Changed"
subtitle: "The Weekend Windup #27 - Results from the March 2026 Practical Data Pulse Survey"
date: 2026-03-28T15:07:04+00:00
url: https://joereis.substack.com/p/ai-is-here-but-the-hard-parts-havent
slug: ai-is-here-but-the-hard-parts-havent
word_count: 2176
---


![](https://substackcdn.com/image/fetch/$s_!MS9V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5b5e9960-6c4d-474a-abeb-33f34ab6ef60_1024x768.jpeg)

*San Francisco and it’s terrible views ;)*


I just got back from San Francisco, where I gave a talk atUndercurrent, a small, intimate data engineering event put on by Confluent. I shared the stage with some legends (Maxime Beauchemin, Josh Wills, Holden Karau, Shinji Kim. The attendees were also stacked, with lots of talented and storied engineers and leaders. I talked to one guy who built and modernized the data warehouses at both LinkedIn and Uber. The Bay Area is like that. Legendseverywhere. Conversations like this are the reason I still get on the road.


But the real reason I’m writing today is some new data. I closed theMarch 2026 Practical Data Pulse Surveyon March 21st and used its results as the backbone of my Undercurrent talk. 194 data professionals responded. These are mostly data engineers, some analytics engineers, and some leaders - all people using AI tools in their data engineering work.


The TL;DR? AI has changed everything except the hard parts.


Everyone’s using AI. That’s not an interesting story anymore. Of the 194 respondents, exactly1person said they don’t use AI tools. One. Thank you to that person for responding, by the way.


This tracks with what we found in the larger2026 State of Data Engineering Survey(n=1,101), where 82% of respondents reported using AI tools daily or more frequently. The adoption story is over. If you’re not using AI at this point, there’s probably a specific reason, like maybe you’re in healthcare or another industry with tight restrictions. But broadly, these tools are now part of the daily toolkit.


So let’s move past adoption and into impact.


## 57% say AI makes them write code significantly faster


Here’s what respondents told us about AI’s biggest impact on their work:

- 57%Makes me write code significantly faster
- 23%Learning and exploration
- 12%Helps, but hasn’t changed my workflow
- 7%Has replaced some manual tasks


That 57% is notable. But here’s where I want to push on this a bit:faster at what, exactly?Is this code going into production, or are you just generating more code? That’s a nuance I need to capture in future pulse surveys. Because churning out code faster and delivering production value faster are two very different things.


One of the free-text responses from the survey put it well. A data engineer wrote that the speed of delivery will lead to quality issues because we’re not re-evaluating our fundamental knowledge. Production is about to become a cesspool, as this person put it. I think we’ve seen variations of this. I know I have.


## Claude is the top AI tool. It’s not close.


When asked which AI tool they use most for data engineering work:

- Claude49%
- GitHub Copilot16%
- ChatGPT / OpenAI15%
- Other(Gemini, etc.) 12%
- Cursor7%


Even if you combine Copilot and Cursor (both IDE-integrated), that’s 23% for IDE tools versus 49% for Claude. There’s some nuance here I’d like to dig into further. You could be using VS Code with Claude, for instance. But the signal is pretty clear that Claude is the dominant tool in this community right now.


## What matters most in 2027? Data modeling.


This was the finding that really stood out. When asked what will matter most in 2027:

- Data modeling and semantic layers49%
- AI-native pipelines23%
- Data governance and compliance21%
- Cost optimization7%


Let that sink in. Nearly half of the respondents - people who are deeply involved in AI-assisted workflows every day - said data modeling and semantic layers matter most going forward. The other stuff is pretty boring and unsexy, too. But I’m interpreting this as AI surfacing the need to get the boring stuff right - context, governance, and cost.


This isn’t a surprise to me, but it might be a surprise to the people who keep telling me that data modeling doesn’t matter anymore because AI will just figure it out. I hear this a lot, and I disagree for a fundamental reason: if you’re only thinking about physical data modeling or migrating schemas, you’re missing the entire point. Data modeling isn’t just about making tables and columns.


AI has read most everything on data modeling and is pretty good at understanding itsrules. But understanding themeaningof data within your organization - mapping business concepts back to a coherent data model -  that’s something AI still isn’t doing, and I don’t think it’s going to do it for a while. This is the year of context /s, so perhaps we’ll see traction here. But I think this will be slow-moving, precisely because capturing context and wringing out value from it has been notoriously difficult for decades. Just because you have a semantic layer or ontology doesn’t mean you’ve magically captured all the tacit knowledge within your organization. And especially now that people are scared shitless of losing their jobs to AI, do you really think people have an incentive to play along and divulge their knowledge? If so, I have some crypto meme coins for sale.


## The hard parts haven’t changed


Now let’s layer in what we found in the larger 2026 survey (1,101 respondents), because this is where the picture comes into focus.


The biggest bottlenecks in data organizations:

- Legacy systems / technical debt25%
- Lack of leadership direction21%
- Poor requirements / upstream issues19%


AI is not going to fix your lack of leadership direction. It’s not going to fix your poor requirements. And honestly, legacy systems and technical debt oftenresultfrom a lack of leadership direction. Poor requirements result from poor communication, silos, and misaligned incentives.


On data modeling specifically, nearly 90% of respondents in the main survey reported at least one pain point. The top two:

- Pressure to move fast59%
- Lack of clear ownership51%


Think about that combination. You’re under pressure to move fast,andnobody knows who owns what. What’s going to happen? People take shortcuts. People actively avoid owning things because ownership is a game of hot potato. And the data showed the consequence clearly: organizations using ad-hoc modeling report the highest rates of firefighting (38%), while those with canonical or semantic models report the lowest (19%).


More than one in four teams spend significant time just fighting fires. That’s an enormous amount of lost productivity across the industry.


## The 1 = 10 dilemma


One of the most interesting tensions in the pulse survey came through in the free-text responses. There’s a growing belief that one person with AI can deliver what a team of 4-10 used to deliver. One respondent put it bluntly:if you have a good PRD, data engineering is over, one person can do 10 people’s worth of work.


But here’s the flip side, from someone in a VP/Director role:Leadership expects increased velocity with AI-enabled, smaller teams without compromising quality. The engineers who can actually do this seem pretty rare. Leadership will learn this the hard way.


This echoes what I’ve been seeing. We have a new form of technical debt: code and systems that nobody wrote, created by AI, that nobody fully understands. It looks correct. It might even pass tests. But do you understand it? Be honest. I know I don’t, most of the time. I trust it does what it says it will, but have I read every line? No. And I don’t think you have either.


This is Jack Bergman’s old quote in action:there’s never enough time to do it right, but there’s always enough time to do it again.


## Career optimism is (mostly) high


Despite all this, 71% of respondents to the pulse survey reported varying degrees of optimism about their careers. The main survey showed a similar vibe: 42% of respondents expect their data teams to grow in 2026, versus only 7% expecting shrinkage.


This tells me something important and unexpected among the doom and gloom of AI-related job slashing. Practitioners aren’t naive about the challenges, but they’re also not panicking. They see AI as a tool that makes them more effective, not a replacement. The ones who should worry are the ones who treat AI as a reason to stop learning, but I’ll get to that.


## What to do about all of this


I’m going to be direct here, because a technical SF audience let me get away with it, and I think you can handle it too.


Invest in the fundamentals.The pulse survey and the main survey tell the same story: data modeling, semantics, and architectural patterns. These are what practitioners want to learn and what they think will matter most. Some people say you don’t need to learn anything anymore because AI will do it all. If that’s your take, honestly, find something else to do. That’s not gatekeeping, it’s just reality. If you don’t understand what you’re building, you’re a button pusher, and button pushers are replaceable.


Implement and get visible wins.There’s massive investment in AI right now, and a lot of talk about agents, context, and whatever the buzzword of the month is. I can see all of this fizzling out, not because the models are incapable, but because companies are incapable of getting wins with them. If all leadership sees is POC purgatory, they’re going to lose patience. We’ve seen this play out with every hype cycle before this one.


Acknowledge the legacy reality.74% of legacy modernization projects fail. For every dollar spent on digital innovation in large companies, about$3 needs to go toward modernization. Even if AI can generate new migration code in hours, you still need legal and compliance to approve it for production, and that takes months. The messy organizational reality isn’t going away just because the models got better.


## Fundamentals still matter…a lot


I closed my talk in SF with this, and I’ll close with the same thing here:


You’ve been told you don’t have time for fundamentals. The data says you don’t have time to skip them.


Bill Inmon (the father of the data warehouse) always tells mefundamentals are gravity.The same problems he’s seen in the IT industry for longer than I’ve been alive are the same problems we’re dealing with today. Organizational incentives, politics, tribal knowledge, and misaligned ownership. No amount of technology will fix this as long as there are humans in organizations.


The models are freakishly good. The capabilities are incredible. I spent last night wiring up the latest Claude tools, and it feels like I’ve unlocked new powers. But does that translate to most businesses? Not yet. And the gap between individual tool adoption (near-universal) and organizational AI maturity (still mostly experimental) is where the real work is.


The next pulse survey (probably in late April) will go deeper on data modeling and semantic layers, unpacking why practitioners say it matters so much and where the real gaps are. Stay tuned.


The full March 2026 pulse survey data is publishedhere. The2026 State of Data Engineering Survey Reportis available now.


Special shout out to Confluent for putting on Undercurrent. Great event, great crew!


Have a great weekend,


Joe


---


Here’s this week’s Freestyle Friday podcast. Available on Spotify, Apple, and wherever else you get your podcasts.Please support the show with a review.It means a lot.


---


![Ellie.ai - Enterprise Data Modeling Powered by AI](https://substackcdn.com/image/fetch/$s_!YB3V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F085929fe-223b-4838-94f4-4678db81d663_626x200.svg)


Modern data modelers need to live at the intersection of business and tech.Ellie.aiallows you to collaborate effectively with business while maintaining credibility with the Tech team. Get contextual support from AI, reverse engineer anything building a repository of sources with synthetic AI generated contextual metadata while delivering insights via an MCP Server and integrating anything with full blown API support.


The full stack data modeling future is here today!


Thanks toEllie.aifor partnering on this newsletter.


---


# Awesome Upcoming Events


![](https://substackcdn.com/image/fetch/$s_!jtH1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0127c585-1f6e-42d3-881f-39e7d1e71c55_1920x1280.png)


🇸🇪 Sweden! See you at the Data Innovation Summit in Stockholm.


I’m doing a keynoteandworkshop on Mixed Model Arts: Data Modeling in the Age of AI.

- May 7 - keynote
- May 8 - workshop


Here’s 10% off: SD10OFF (good for the event. Workshop is not included)Register here


---


# Cool Videos and Reads


---


### Here are some things I read this week that you might enjoy.


Future Casting the Modern Data Stack


Workers who fall for ‘corporate bullshit’ may be worse at their jobs, study finds | Business | The Guardian


‘IKEA’ missile market fears grow as Iran-style AI-guided attack drones surface on Alibaba listings


When Machines Build for MachinesInfrastructure is all that’s left


Seeing like a spreadsheet - David Oks


Thoughts on slowing the fuck down


# Find My Other Content Here


📺YouTube- Interviews, tutorials, product reviews, rants, and more.


🎙️Podcasts- Listen on Spotify or wherever you get your podcasts


📝Practical Data Modeling- This is where I’m writing my upcoming book, Mixed Model Arts, mostly in public. Free and paid content.


# The Practical Data Community


The Practical Data Community is a place for candid, vendor-free conversations about all things tech, data, and AI. We host regular events such as book clubs, lunch-and-learns, Data Therapy, and more.


🤖Join on Discord


Thanks for reading! Subscribe for free to receive new posts and support my work.
