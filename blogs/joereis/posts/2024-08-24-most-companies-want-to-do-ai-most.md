---
title: "Most Companies Want To Do AI. Most Are Barely Doing BI."
subtitle: "Joe's Nerdy Rants #50 - Weekend reads and other stuff"
date: 2024-08-24T19:55:04+00:00
url: https://joereis.substack.com/p/most-companies-want-to-do-ai-most
slug: most-companies-want-to-do-ai-most
word_count: 2572
---


Last week I made a very short and simpleLinkedIn postthat caused a bit of a ruckus.


![](https://substackcdn.com/image/fetch/$s_!s1dL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf50afdc-23d9-4b8d-999e-aad6418e804b_499x230.png)


This isn’t the first time I’ve publicly said something along these lines. I think the first time was in the 2010s, during the tail end of the previous ML/AI hype cycle. Back then, it seemed like every company was jumping on themselves to do machine learning. Most found out how hard it was to do in production. Even more could barely get BI dashboards consistently working or get adoption of these dashboards across business users. And here we are again, at what I think is the peak of another ML/AI hype cycle, this time pushed by generative AI.


Why did these two sentences in the post hit home? I have a few ideas. First, people have gotten used to hype cycles in data and tech. We've seen many hype cycles in machine learning (now called “AI” for marketing reasons). There was the “citizen data scientist” in the early 2010s, the rise of deep learning in the mid-2010s, and generative AI in the late 2010s/early 2020s. Each cycle brought new approaches to machine learning, along with inflated expectations. Each cycle also proved worthy, with these techniques adopted at many companies, often flying under the radar and providing a ton of utility. When something adds utility and just does its job, it’s no longer cool. It’s “legacy” and makes money.


Is this time different? In a way, yes. The widespread consumer adoption of generative AI makes this hype cycle different. ChatGPT was one of the fastest-growing consumer applications of all time. I’ll never forget talking to my son’s 6th-grade class about AI last year. The kids fully understood ChatGPT and how they could use it (namely, solving homework problems). If kids intuitively get something, then pay attention. They’re generally more keen than adults. And as a general rule, anytime you see consumer adoption of technology, expect to see it trickle into companies. We saw this with PC’s, the Web, and mobile. Generative AI was the killer introduction to machine learning. Now it’s mainstream, even though it’s been a part of most web and mobile applications for ages (e.g., your phone is a massive ML engine for various use cases).


Back to AI and BI. I’m not here to say there’s no utility in generative AI. I think there’s a lot of utility. And a lot of overly inflated expectations. We’re at the beginning of a very long evolution of generative AI and ML, along with new approaches yet to be invented. The general long-term utility of AI is a separate argument from the short-term hype suggestingeverycompany jump into AI. The underlying reality is that digital transformation is difficult, no matter the fad of the day.


Most companies want to do AI. Most are barely doing BI.


Let’s unpack each sentence in turn.


# Most Companies Want To Do AI


The expectations for generative AI are very strong. Because things are moving fast, it’s hard to get a steady read on the exuberance for AI. Most surveys and articles I’ve seen suggest that most IT leaders (say, 50% to 60% or higher) are prioritizing generative AI for their businesses. At the same time, there’s a disconnect between hope and reality. According to an article fromthe Registerciting a recent IBM survey, “The report highlights a disconnect between CEOs and the IT department, with three quarters of the former believing that their organization's digital infrastructure is ready to scale and "deliver value." However, only 16 percent of tech execs say they're confident their current cloud and data processing capabilities are ready to support generative AI, given the enormous demands it places on infrastructure, particularly during training.” So it's been with digital transformation and process improvement initiatives. It seems easy to those who are far from the technical and implementation details. To those close to the technology, it’s often more pessimistic.


Why do companies want to incorporate generative AI into every nook and cranny of their business? I won’t get into the FOMO arguments because that’s a distracting wormhole. Instead, I’ll look at the practical reason why companies invest in ML/AI.


Here’s the punchline…get ready…AI means you get more work done with fewer humans. Instead of hiring workers to complete a task, I can incorporate ML/AI into a workflow and augment or eliminate the pesky humans. So, it's been with automation for hundreds of years. Automation reduces the need for redundant human labor. So it goes, and so it will go. Humans create things that make their lives simpler and their income streams obsolete. We’re smart and dumb that way.


I’m not sure generative AI is the solution to most business problems. But if you need to summarize, translate, or synthesize things like text, images, audio, or video, generative AI is the best approach we have today.


# Most Companies Are Barely Doing BI


Ah, good old BI. For decades, the rallying cry has been that BI is how we “get insights from data that drive business value.” By most accounts, the historical success rate of BI projects hovers around a depressing 20%. Most companies are barely doing BI.


Based on my anecdotal observations and discussions, the challenges for success with BI are the same as they ever were. I don’t think the issue is BI itself. Data initiatives generally have a dismal success rate, which I’ll discuss in a bit. Unsurprisingly, according to arecent study by Rand, AI initiatives are following suit at a 20% success rate.


# Is BI Necessary For AI?


Is BI necessary for AI? No. I think conflating the two is part of the issue I’m describing. I often hear traditional data practitioners talk about ML and generative AI in the same way as BI. You'll know these are different if you’ve worked with ML or AI.


AI is not BI, and BI is not AI.


The conflation stems from the notion that AI will rely on the same underlying datasets that power BI. If so, then yes, you should get BI right before moving to AI. My experience is the data used in BI is actually pretty useless for ML use cases (classification or regression), because what are you trying to automate or answer beyond what the data already provides? The answer is usually in the data itself, because it was modeled to provide answers. If you’re trying to throw an LLM on top of your BI data, the underlying data model needs to be sound. And you’d be wise to provide semantic and knowledge context of top of it, via a semantic layer or knowledge graph, lest you get wild hallucinations in your text-to-sql queries. Finally, I’d ask if this is even the right approach. If your BI efforts are flailing, I’m guessing adoption of your dashboards and reports are pretty light or nonexistent. Will throwing a chatbot on top of this same data suddenly make people interested in data and analytics, especially if similar dashboards or reports answer most questions they’ll ask? I guessf*ck around and find out.


However, the argument that BI is always a prerequisite to AI makes no sense when dealing with unstructured data like text or images, or use cases that don’t involve BI or analytics. That’s like saying you need to be a great 400m runner to be a Olympic level Australian breakdancer. One of these is not the other. The traditional approaches to data (namely tabular data for BI) will work when dealing with traditional problems. They won’t work when dealing with new approaches or problems. It pains me to see data management people shoehorn in their methodologies where they’re antiquated and make no sense. The data world is multimodal and heterogeneous, and I don’t feel like traditional data management is keeping up. Same old crying in the proverbial beer about how data needs to add value, and same old lousy results. But that’s a rant for another week.


# The Point - Change Is Hard. Data Is Hard.


The above Rand study on the challenges faced by AI initiatives summarizes five root causes.“First, industry stakeholders often misunderstand — or miscommunicate — what problem needs to be solved using AI.


Second, many AI projects fail because the organization lacks the necessary data to adequately train an effective AI model.


Third, in some cases, AI projects fail because the organization focuses more on using the latest and greatest technology than on solving real problems for their intended users.


Fourth, organizations might not have adequate infrastructure to manage their data and deploy completed AI models, which increases the likelihood of project failure.


Finally, in some cases, AI projects fail because the technology is applied to problems that are too difficult for AI to solve.”


Sound familiar? Replace AI with BI, “Big Data,” data science, or whatever other trends captured the imagination of businesses back in the day. It’s all the same thing. Change is hard. Data is hard.


But not all is lost, and we need to keep pressing forward. Apply AI to proper use cases as they make sense, especially in areas tailor made for AI. For instance, a friend at a Fortune 100 told me about using LLMs to automate the summarization and search of millions of manufacturing documents, saving a ton of time and freeing up employees to focus on more value-added work. He kept saying to take the time to make text datasets “generative AI ready.” There might be a podcast about this at some point. His example is a perfect use case for generative AI - summarizing massive amounts of text that would otherwise take humans thousands of years to read.


Another key thing we need is education and training about what AI is and where it’s a good fit in the business. I talk with people who think AI will automate every facet of their business overnight. I’m not sure what science fiction movies or Black Mirror episodes they’re watching, but that’s fantasyland, at least today. That said, there’s a ton of research and focus on agentic AI, and I’m bullish on the long-term utility of agents. But where would agents make sense? That’s where education and training will help people have honest discussions about these fast-evolving technologies. Knowledge of what’s possible and what’s stupid will also help temper overly enthusiastic pie-in-the-sky promises that ultimately fail when it comes time to implement them.


You must keep the context in mind. We’re still super early in the days of generative AI and machine learning in general. The current hype cycle will burst (I think we’re at the top right now), and the people building really useful AI and ML can operate in an environment without as many hucksters and bullshit artists. I’m optimistic about the long term implications of AI on the data industry as a whole. The potential is too large, and there will need to be investment to clean up the underlying datasets that will power AI. If that happens, maybe, just maybe, we can finally start doing BIandAI.


---


On another note, the very popular Data Therapy Session calendar is postedhere. It’s an incredible group where you can share your experiences with data - good and bad - in a judgment-free place with other data professionals. If you’re interested in regularly attending, add it to your calendar.


Hope you have a fun weekend!


Thanks,


Joe


P.S. If you haven’t done so, please sign up forPractical Data Modeling. There are lots of great discussions on data modeling, and I’ll also be releasing early drafts of chapters for my new data modeling book here. Thanks!


---


# Cool Weekend Reads


How Postgres stores data on disk – this one's a page turner (drew's dev blog)


National Public Data Published Its Own Passwords (Krebs on Security)


Splicing Duck and Elephant DNA (Motherduck)


"We ran out of columns" - The best, worst codebase (Jimmy Miller)


Generative AI hype is ending – and now the technology might actually become useful (The Conversation)


Be an AI Power User: Success Strategies in the AI Landscape (The New Stack)


The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed: Avoiding the Anti-Patterns of AI (Rand)


The hidden reason AI costs are soaring—and it’s not because Nvidia chips are more expensive (Fortune)


The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery (Sakana)


Palmer Luckey, American Vulcan (Tablet Magazine)


‘Bumble fumble’: online dating apps struggle as people swear off swiping (The Guardian)


The Warehouse Worker Who Became a Philosopher (The Atlantic)


The American Con Man Who Pioneered Offshore Finance (The Atlantic)


# New Show & Upcoming Events


## The Joe Reis Show


Nik Suresh Will F*cking Piledrive You If You Say AI Again (Spotify)


5 Minute Friday - 5 Minute Friday - Most Companies Want to do AI, Most are Barely Doing BI (Spotify)


Rehgan Bleile - AI Governance, Creating Opportunities for Women Speakers at Conferences, and more (Spotify)


5 Minute Friday - 1:1 or 1:Many? (Spotify)


Christian Steinert - Consulting in Unsexy, Niche Industries (Spotify)


5 Minute Friday - Courses and Books (Spotify)


Chris Bergh - DataOps Deep Dive (Spotify)


Lexi Pasi - The Shapes of ML/AI Problems (Spotify)


Joseph Machado - Balancing Tools and Fundamentals in Data Engineering (Spotify)


Bill Inmon - History Lessons of the Data Industry. This is a real treat and a very rare conversation with the godfather himself (Spotify) - PINNED HERE.


## Monday Morning Data Chat


Rob Harmon - Small Data, Efficiency, and Data Modeling (Spotify,YouTube)


Joe Reis & Matt Housley - The Return of the Show! (Spotify,YouTube)


Nick Schrock & Wes McKinney - Composable Data Stacks and more (Spotify,YouTube)


Zhamak Dehghani + Summer Break Special (Spotify,YouTube)


Chris Tabb - Platform Gravity (YouTube)


Ghalib Suleiman - The Zero-Interest Hangover in Data and AI (Spotify,YouTube)


## Events I’m At


SLC Low Key Happy Hour - Salt Lake City. September 10.Register here


MLOps Community - Data Engineering for AI/ML (Virtual). September 12.Register here


Big Data London - London, UK. September 18-19.Register here


DataEngBytes - Australia/New Zealand. September 24 - October 4.Register here


dbt Coalesce - Las Vegas. October 7-10.Register here


Helsinki Data Week. October 28 - November 1.Register here


Forward Data Conference. Paris, France. November 25.Register here


Data Day Texas - Austin, TX. January 25, 2025.Register here


Data Modeling Zone - Arizona. March 4, 2025.Register here


Winter Data Conference - Austria. March 7, 2025.Register here


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
