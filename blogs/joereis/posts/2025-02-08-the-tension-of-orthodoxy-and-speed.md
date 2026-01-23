---
title: "The Tension of Orthodoxy and Speed"
subtitle: "Joe's Nerdy Rants #64 - Weekend reads, podcasts, and other stuff"
date: 2025-02-08T19:13:28+00:00
url: https://joereis.substack.com/p/the-tension-of-orthodoxy-and-speed
slug: the-tension-of-orthodoxy-and-speed
word_count: 1906
---


![](https://substackcdn.com/image/fetch/$s_!5vRB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F218e9b15-3dc4-4727-b764-283e049a79bb_600x428.jpeg)

0:00
-17:44

> “There is never enough time to do it right, but there is always enough time to do it over.”  - John W. Bergman“Stubborn table-centric people are the data equivalent of Flat Earthers.” -  Joe Reis


As I write mybookon data modeling, a common theme keeps recurring - doing things “the right way” versus optimizing for speed. Speed can mean many things. In data modeling, I look at speed in a couple of ways. First, speed can mean faster technical performance. Or, speed can be seen as the ability of teams to operate “fast,” ideally with faster high-quality value delivery.


Doing things “the right way” means being thoughtful and intentional in data modeling. This brings us to orthodox and conventional data modeling approaches. There was once a process that nearly everyone followed -intentionalconceptual and logical modeling, having a shared vocabulary, modeling the business, and translating these models into a physical data model. The relational model has been the mainstay for transactional data used in applications since the 1970s. In analytics, Kimball’s dimensional model is the most popular approach, with Data Vault also prevalent in some areas. All of these approaches have an established way of handling data. There’s a “right way” to relationally or dimensionally model data. Each approach has a framework, a vocabulary, and a goal. Follow the convention, and you’ll have a data model that’s understandable by many people, performant (most of the time), and with minimal defects and higher quality. The latter point is key since higher quality often leads to the ability to move faster, as discussed a few months ago inThe Quality Paradox.


Speed and fast performance sit at the other end of the spectrum. I often observe tension between sticking with a conventional data modeling framework or ignoring convention and doing things to “move faster.” Data modeling is sometimes perceived as being “old school” and too slow, hampering speed and fast delivery. The thinking is it’s better to deliver “something” quickly since that’s what you’re incentivized to do. Add “agile” and “scrum” (I put these in quotes because people say they practice them, but it’s usually more cargo-culting than anything), and intentional data modeling went out the window. There’s very little time to think, and “shipping” looks better on a burndown chart. For many teams these days,thinkingis often replaced by managing a Jira backlog and slogging through 2-week sprints, all in the name of “shipping.”


Speed also means the ability to make things technically more performant. The Big Data era (2000s) came about because of high volumes web and mobile data creation and processing, arriving at high velocity, and in more variety than traditional relational databases could handle. One friend told me that at Yahoo, their RDBMS simply wouldn’t finish a massive cross-join analytical query, but Hadoop finished the result in minutes. During this time, new types of data processing technologies emerged (NoSQL, streaming, etc), with the data model tightly coupled to its physical implementation. Along the way,intentionalconceptual and logical modeling practices were somehow lost. It was too easy to throw data into a “new school” database and forget about it. While these Big Data solutions often made sense for big tech companies, the “set it and forget it” mentality was passed down to the masses (remember theMEAN stack?) I know of quite a few companies still trying to extricate themselves from self-inflicted data messes brought about by “unintentional” data models that have since grown into a serious liability.


This tension of orthodoxy vs speed goes back to the introductory quote. You have a lot of opportunities to do things over. In theory, you also have time to make it right. This is often evident in most software and data teams' “tech debt” backlog. But when do you ever set aside the time to do it right? As far as I can tell, the latter is what people strive to do (very few set out to intentionally do things poorly), but they rarely get around to it.


In an age of fast delivery, does orthodoxy matter anymore? I strongly believe it does. If you understand orthodoxy, you know why you’d want to follow the rules. You also understand what rules to break and why. There are lots of rules that are worth following. Orthodoxy exists for a reason. It’s well established because people have invested time (often decades) and money into it, honing and shaping its imperfections over time, which implies it works for many people. The relational and dimensional models have been implemented in production across countless companies of all sizes and industries. For the 99% of companies out there, these modeling approaches will work. Don’t think you’re smart enough to ignore orthodoxy without understanding the consequences. Not understanding orthodoxy means you will either misapply it or reinvent the wheel. I’ve seen countless software and data teams get into big trouble because of errors of omission and commission.


While I write this in the context of data modeling, you can apply this almost universally. There are always best, better, and poor ways of doing things, and your job is to choose thebestapproach based on your situation. But this assumes you know the approaches to choose from and what works best. This is an investment in education and upskilling as much as understanding what game you’re playing. For example, resume-driven development is where people play the wrong game, adopting a particular hot technology or modeling approach because they read it in a Big Tech blog somewhere and want it on their resume, usually not asking if this is the best fit for their situation. I once saw a startup build their data infrastructure in Protobuf because they came from Google, and that was what they knew. Good enough for Google, good enough for a ten-person startup. Until it started severely creaking. Never mind that Postgres could do what they needed with a fraction of the complexity. That was a “fun” re-architecture gig…


Orthodoxy is great for providing you with a mental framework and conventions. It gives you a shared vocabulary and understanding with other people about what you’re doing. In data modeling, the relational model has proven to be a mainstay for decades in creating bulletproof database models that minimize redundancy and side effect errors. So, while developing a relation model might be slow initially, it helps make work faster over time. If others on your team are familiar with the relational model process, then when you say things like “normalization” or “3rd normal form”, you have a common vocabulary and meaning. There's no ambiguity because standards are established about the various normalization stages.


On the flip side, it’s easy to become overly orthodox and dogmatic. Dogmatism is almost more dangerous than premature optimization. There needs to be a balance. A big theme ofMixed Model Artsis knowing how to model data and choose the approach that works best for your situation. Someone well-versed in the relational model should also know when it’s not as effective and thealternatives to the relational model. And since the worlds of apps, analytics, and AI are converging, thinking only in tables is not enough nowadays. Stubborn table-centric people are the data equivalent of Flat Earthers. There’s text, audio, semi-structured, and otherforms of datathat are worth considering. How do you handle these forms of data? How do you blend AI into BI and apps?


I view most things in pendulums. For decades, the pendulum swung toward conventional approaches. Then, in the 2000s to 2010s, it swung the other way toward fast and informal. Now, I see things balancing out. The world of data is changing extremely fast, and knowing how to apply orthodoxy to move fast is important. But it’s also imperative to move thoughtfully and intentionally to maintain high quality, which allows you to move faster over time. The future data professional is “old school” AND “new school.”


Have a wonderful weekend,


Joe


---


# Cool Weekend Reads & Listens


## Tech, Data, and AI


The real DeepSeek revelation: The market doesn’t understand AI | Semafor


Everyone knows your location: tracking myself down through in-app ads


DeepSeek has ripped away AI’s veil of mystique. That’s the real reason the tech bros fear it


The End of Search, The Beginning of Research


Access Pattern Optimizations for Alt-Relational Data


Writing a good design document


GitHub Copilot: The agent awakens


Which countries have banned DeepSeek and why?


## Biz & Culture


Why Mark Zuckerberg wants to redefine open source so badly | ZDNET


Hydrogen Truck Maker Nikola Explores Bankruptcy


When Your Country Hits The Skids


The Real Reason No One Is Hiring or Getting Hired


## Podcast


Freestyle Fridays - Old School vs New School Data Modeling (Spotify)


Evan Wimpey - On Being a Data Comedian, a Bayesian, and Other Priors (Spotify)


Data Day Texas Recap w/ Tony Baer, Matt Housley, and Juan Sequeda (Spotify)


Freestyle Fridays - Unhinged Rants w/ Carly Taylor (Spotify)


Remco Broekmans - Data Modeling, Data Vault, and More (Spotify)


Freestyle Fridays - Bridge Skills w/ Eevamaija Virtanen (Spotify)


Chip Huyen - AI Engineering, Agents, and More (Spotify)


Jamie Davidson - Modern Data Modeling (Spotify)


Carly Taylor & Ghalib Suleiman - Dealing with Burnout (Spotify)


Sarah Levy - Modern Data Governance for Analytics (Spotify)


Carsten Bange - Trends in Data, Analytics, and AI (Spotify)


Freestyle Fridays - Old School BI vs AI BI (Spotify)


Way more episodes over at the Joe Reis Show, available onSpotify,Apple Podcasts, or wherever you get your podcasts. It will soon be available on YouTube.


# Upcoming Events


The Data T: Data Hot Takes with Joe Reis & Coalesce - Virtual.Register here.


Data Dates - San Francisco. February 20.Register here.


Winter Data Conference - Austria. March 7.Register here. Use code JOEREIS-50 for 50% off tickets!


Deep Dish Data w/ Matillion - April TBA


Snowflake and/or Databricks - June TBA


Iceland - June TBA


Australia, Data Eng Bytes - July TBA


Big Data London - September TBA


Helsinki Data Week - October TBA


More to be announced soon…


# Thanks! If you want to support this newsletter

- The Data Engineering Professional Certificate is one of the most popular courses on Coursera! Learn practical data engineering with lots of challenging hands-on examples. Shoutout to the fantastic people at Deeplearning.ai and AWS, who helped make this a reality over the last year. Enrollhere.
- Practical Data Modeling. Great discussions about data modeling with data practitioners. This is also where early drafts of my new data modeling book will be published.
- Fundamentals of Data Engineering by Matt Housley and I, available atAmazon,O’Reilly, and wherever you get your books.
- The Data Therapy Session calendar is postedhere. It’s an incredible group where you can share your experiences with data - good and bad - in a judgment-free place with other data professionals. If you’re interested in regularly attending, add it to your calendar.
- My other show is The Joe Reis Show (Spotifyand wherever you get your podcasts). I interview guests on it, and it’s unscripted, always fun, and free of shilling.
- Want me to speak at your event? Pleasesubmit a speaking requestif you want me to speak or give a workshop at your event.
- If you’d like to sponsor my newsletter, pleasereach out to me.


Be sure to leave a lovely review if you like the content.


Thanks!


Joe Reis


Thanks for reading Joe’s Nerdy Rants! Subscribe for free to receive new posts and support my work.
