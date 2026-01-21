---
title: "AI IDEs Need Moats"
subtitle: "VS Code eliminated the switching cost for AI IDEs. They need to build moats to survive. Partnering with software vendors and new open source projects could help."
date: 2025-03-12T19:25:02+00:00
url: https://materializedview.io/p/ai-ides-need-moats
slug: ai-ides-need-moats
word_count: 924
---


Martin Kleppmannand I gave a keynote interview for theMonster SCALEconference today. I always enjoyScyllaDB’sconferences and this one was no exception. Check out our interviewhere. While you’re at it, watchAlmog Gavra’sSlateDBtalk, too!


---


I’ve avoided talking about AI on my newsletter thus far. The space is moving so rapidly. It feels futile to try and keep up, and anything written becomes stale very quickly. Still, I have been using AI daily for the past few years, primarily for coding. First withChatGPT, then withWindsurf. I’m going to break my embargo for this post to cover some recent discussions I’ve had about AI IDEs like Windsurf andCursor.


For the non-developers out there, Windsurf is an AI-powered agenticintegrated developer environment(IDE) akin to Cursor. In layman’s terms, these are application that developers use to write code along side an AI. Both Windsurf and Cursor are built onVisual Studio Code, and both are quite effective. I primarily use Windsurf’s AI features when writing unit tests and small scripts, be it Python, Bash, or Github Actions YAML. A few weeks back, I decided to check in and see if I should switch to Cursor.


There was no consensus. My impression from the comments was that Windsurf was slightly better than Cursor. I decided to stay with Windsurf since I was already using it. Fast forward a few weeks, andthis poston Twitter caught my eye:


![](https://substackcdn.com/image/fetch/$s_!BmRr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2267b1c-37fa-4773-b1c4-a8ff42b41a6a_1370x542.png)

*View Post*


Tom’s post validates my impression, but it also raises an interesting question about moats. As Tom says, since both Windsurf and Cursor are forks of VS Code with nearly identical interfaces, the switching cost is nearly zero. When I switched from VS Code to Windsurf, it took all of 30 minutes. I haven’t looked back. Switching from Windsurf to Cursor, I’m confident, would be the same.


![](https://substackcdn.com/image/fetch/$s_!LoxH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ae5141f-b013-4817-95e1-a9d55dbb685d_1370x468.png)

*View Post*


It’s easy to think these IDEs are destined to be commodities. I don’t think so. The fact that Windsurf is unseating Cursor right now is a signal that, even with commodity LLMs, Windsurf is offering a better product than Cursor. It does make the space highly competitive, however. As Steve’s post says, the IDEs have to be more than API calls to OpenAI and Anthropic. What might this look like?


Last week,Josh Willsand I were discussing AI IDEs over coffee (he’s hiringatDatologyAI, by the way!). Josh made an off-hand comment that LLMs really struggle withdataframelibraries that aren’tPandas; they hallucinate and assume you’re using Pandas. This resonated with me. I had the exact same experience when trying to learnZigin 2023. The language was very new, and similar enough toGoandPythonthat ChatGPT would intermingle the three languages together.


This dynamic is interesting: LLMs struggle with new infrastructure and tools. The same is true for proprietary software—both internal company code and closed source vendor software. There isn’t enough public data on the internet to train the LLMs on such software.


A poor LLM experience with new and proprietary software makes for an interesting virtuous cycle. Developers get a better experience working with legacy software that has thousands of stack overflow questions and github repositories. A better experience increases the adoption cost for new software (or decreases the cost of using legacy software). Developers will stick with the existing software, which will give the AI IDEs and LLM models yet more data to train on. This, in turn, will further improve the developer experience for the existing software.


Proprietary vendors and new open source projects need to figure out how to break this cycle. Offering software that is far better than incumbents could justify the increased switching cost. Vendors could also build their own plugins that help withprompt engineeringandretrieval-augmented generation(RAG). Anthropic’sModel Context Protocol(MCP),llms.txt, andagents.jsonstandard might also be adopted. Indeed,Nile﹩ announced anMCP serverfor its product as I write this post.


AI IDEs like Windsurf and Cursor seem well positioned to help with the adoption problem. IDE companies could partner with vendors to integrate tightly into the IDE’s agents. The companies might also help with fine-tuned models, smaller LLMs purpose-built on curated data, custom integrations, VS Code plugins, or even preferred placement in the IDE—all for specific languages, tools, and vendors. A partnership between Windsurf and a company bringing a new software product to market would be symbiotic. Windsurf would build a better (more sticky) IDE while the company it partners with would gain a better developer experience. Windsurf might even be able to charge for such services.


AI IDE companies could extend this work to internal company software as well. This is whereSourcegraph(the company that makesCody) got its start. Internal company codebases are not typically publicly available, so LLMs know less about them. Both Cursor and Windsurf are already selling into the enterprise; they should be able to offer a wide range of tools for this use case.


And then there isGithub. In the Bluesky thread above,Qian Lipointed outthat Github already has access to many proprietary (private) repositories. They also offer Copilot. They, too, seemed well positioned to compete as an AI IDE. I’m less confident in their ability to execute, however. Copilot has lagged behind its competitors despite strong competitive advantages.


So yes, AI IDEs are a very competitive space, but I believe they’ll develop moats around specialized-models, partnerships, proprietary training data, and more.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profileandMaterialized View Capitalfor a complete list.
