---
title: "AI Agents and the Pesky Problem of Data"
subtitle: "Joe's Nerdy Rants #60 - Weekend reads, podcasts, and other stuff"
date: 2025-01-04T15:25:39+00:00
url: https://joereis.substack.com/p/ai-agents-and-the-pesky-problem-of
slug: ai-agents-and-the-pesky-problem-of
word_count: 1384
---


![](https://substackcdn.com/image/fetch/$s_!MlSZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F886ddb2f-6d67-4b0f-9e56-b2f06c2c0278_2048x2048.jpeg)

*A pretty bad AI-generated image of secret AI agents*


> NOTE - I sent this newsletter out earlier this morning, but Substack somehow deleted half of the post and put the text in the image caption! No idea what happened. So, I’m re-writing what I can from memory.


Welcome to 2025. Hopefully, you had a great holiday break. I spent most of my time hanging out with family, climbing at theFront(this gym keeps improving!), snow hiking, trail running, and writing a ton.


I’ve also been dabbling with AI agents withCrewAIand similar frameworks for a while and took the break to nerd out on stuff likeClaude Computer Use(beta). Give Computer Use a task, say, “Make me a spreadsheet of all of the top restaurants in Old Town Scottsdale,” and it does the task - open a web browser, type in the request, open a spreadsheet, and fill it in. Use the Docker image. Don’t run it on your machine unless you know the risks! Stuff like Computer Use is eye-opening as a demo and shows a future where computers can do tasks autonomously. Check this out if you want a demo of where things are heading. As someone starting a new business, I’m all for streamlining operations and costs with AI and automation. You’ll find me using AI tools and writing code (sometimes using AI copilots) to automate workflows. This frees up so much time for more meaningful work. Eliminating toil is where I see AI having the most significant impact in any organization.


The zeitgeist over AI agents comes from people like Microsoft CEO Satya Nadella, who claims that AI agents will be the demise of software applications. Salesforce is also all-in on AI agents with Agentforce. The thinking is AI agents will be able to accomplish seemingly any task, and the need for dedicated applications that “do one to a few things” is no longer needed. I suppose this makes sense in theory. But there’s the pesky problem of data. The current state of LLMs relies on some text-to-SQL to query databases. Text-to-SQL is still pretty immature and hallucinates like crazy on complex queries. Improvements like throwing in knowledge graphs help to some extent, but text-to-SQL performs poorly for complicated joins or filtering.


And as you know, most corporate datasets are utter hellscapes, ranging from poorly named columns to janky data models to lord knows what the fuck is happening. Very few people raise their hands when I ask audiences if they’d throw an LLM atop their existing data. If anything, attention to AI forces companies to reckon with their past data sins. I’m seeing more data quality and governance efforts and a renewed interest in data modeling. And I’m starting to see some early production uses of LLMs (I don’t count using ChatGPT or similar). But AI is not yet widespread.


All of this is well and good, but I can’t shake off the question of whether AI agents are being forced onto the business world. I keep seeing claims like “2025 is the year of AI Agents.” I suppose so, but last year was the year of AI. The previous years were all about Web3 and crypto. Every year has a new narrative and hype cycle. Perhaps Big Tech is trying to repay its massive investments in model training and expansion of data centers. Or maybe they need another narrative to keep the stock price high? In the end, fundamentals win. If companies adopt AI and agents with success, the narrative wins. If not, another narrative will arrive on the scene. Time will tell. As I’ve said before, I’m not bullish on short-term bullshit, but I’m long-term bullish on AI.


In other news, as you probably know, Matt Housley and I amicably decided to close down Ternary Data, our longstanding boutique data engineering consultancy. As I mentioned late last year, we’re on to bigger and better things and don’t want to deal with the grind of consulting. We also had a popular live weekly show, The Monday Morning Data Chat. The videos are preserved on YouTube for now. You might be wondering what will happen to Ternary Data’s YouTube channel. I’ll make the channel bigger and better with more video and educational content. The Joe Reis Show will also have a YouTube option. This is part of my new company (TBA), and it will have a lot of rich video content. Short tutorials, courses, thought pieces, podcasts, and much more. While I’ve leaned into writing - and will continue to do so because writing IS me - I also want to expand into new mediums. Video is the next phase since I’ve been doing audio for ages. All I can say is there’s a lot of awesome stuff coming very soon.


Lastly, this newsletter will have a shakeup next week. Expect at least one long-form article to drop during the weekdays, usually with an accompanying podcast/video. Much more depends on my mood and what’s happening in the data/AI space. The weekend edition will be more of a curated list of cool links, podcasts, and videos. The last newsletter I dropped was a LONG article, followed by articles and podcasts I don’t think anyone had a chance to check out. That’s a bummer because there were some gems in there. In this age of AI-generated content, having a human provide some nuggets and hidden treasures is a great offset.


Have a wonderful weekend,


Joe


---


# Cool Weekend Reads


Morris Chang and the Origins of TSMC - by Brian Potter


Over 3.1 million fake "stars" on GitHub projects used to boost rankings


Deepseek: The Quiet Giant Leading China’s AI Race


Databases in 2024: A Year in Review // Blog // Andy Pavlo - Carnegie Mellon University


Silicon Valley stifled the AI doom movement in 2024 | TechCrunch


Why Corporate Managers Are Being Shoved Out The Door


200 Billion Weights of Responsibility


Can LLMs write better code if you keep asking them to “write better code”? | Max Woolf's Blog


# New Show & Upcoming Events


## The Joe Reis Show


Freestyle Fridays - The Year Ahead (Why Data Modeling Matters, AI, Being Human, etc) (Spotify)


Simba Khadder - Feature Stores, Reinforcement Learning, and More (Spotify)


Gordon Wong - What We're Stoked for in 2025 (Spotify)


Matt Housley - End of 2024 Chat, Advice on Consulting, Leaving a Job, AI, and More (Spotify)


Way more over at the Joe Reis Show, available onSpotify,Apple Podcasts, or wherever you get your podcasts. It will soon be available on YouTube.


## Events I’m At


Data Day Texas - Austin, TX. January 25, 2025.Register here


Winter Data Conference - Austria. March 7, 2025.Register here. Use code JOEREIS-50 for 50% off tickets!


London - March TBA


Snowflake and/or Databricks - June TBA


Iceland - June TBA


Australia, Data Eng Bytes - July TBA


Big Data London - September TBA


Helsinki Data Week - October TBA


More to be announced soon…


# Thanks! If you want to help out…

- The Data Engineering Professional Certificate is one of the most popular courses on Coursera! Learn practical data engineering with lots of challenging hands-on examples. Shoutout to the fantastic people at Deeplearning.ai and AWS, who helped make this a reality over the last year. Enrollhere.
- Practical Data Modeling. Great discussions about data modeling with data practitioners. This is also where early drafts of my new data modeling book will be published.
- Fundamentals of Data Engineering by Matt Housley and I, available atAmazon,O’Reilly, and wherever you get your books.
- The Data Therapy Session calendar is postedhere. It’s an incredible group where you can share your experiences with data - good and bad - in a judgment-free place with other data professionals. If you’re interested in regularly attending, add it to your calendar.
- My other show is The Joe Reis Show (Spotifyand wherever you get your podcasts). I interview guests on it, and it’s unscripted, always fun, and free of shilling.
- Want me to speak at your event? Pleasesubmit a speaking requestif you want me to speak or give a workshop at your event.


Be sure to leave a lovely review if you like the content.


Thanks!


Joe Reis


Thanks for reading Joe’s Nerdy Rants! Subscribe for free to receive new posts and support my work.
