---
title: "The Quality Paradox"
subtitle: "Joe's Nerdy Rants #55 - Slow down to move fast, plus weekend reads and other stuff"
date: 2024-11-09T17:30:25+00:00
url: https://joereis.substack.com/p/the-quality-paradox
slug: the-quality-paradox
word_count: 2243
---


![](https://substackcdn.com/image/fetch/$s_!gIaO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffbf9fd7e-78ab-4cf5-ae65-75f0280666b0.heic)

0:00
-11:16

> “Quality is free, but only to those who are willing to pay heavily for it.” - Peopleware


One of my favorite books isPeopleware, written in 1987 by Tom DeMarco and Timothy Lister. The authors wrote a classic on nurturing productive projects and software teams. The great - andverytroubling - thing is the book is as accurate today as it was almost 40 years ago. Since the book was published, these challenges have grown. The practices of managing software teams and project delivery are copied and pasted into analytics and ML/AI, but not in a good way. Same as in 1987, we’re still largely punting on quality to rush things out the door, trying to hit arbitrary deadlines.


When I chat with tech and practitioners, they often lament they don’t have time to do things the right way. Shortcuts are taken. Quality is sacrificed in the name of shipping quickly. I don’t get the impression anyone wants to do shoddy work. Quite the opposite, I believe people want to do the right thing and do their best. But when you’re pumping out crap, do you feel proud of the work you’re doing? Especially when you’ve got a deep feeling that this will cause extra work for you in the future? This is sadly common.


Before I go further, what is quality? Quality means doing something to a standard, ideally reducing or eliminating as many errors and defects as possible. On a personal level, it means delivering something you’re proud of. A nice side effect of high quality is you improve productivity. When you have fewer errors you need to rework, you can instead focus on output. It might take a bit of time to ramp up to higher quality. But once you do, you move much faster than before.


This is the quality paradox. Sometimes, you need to move slower to achieve higher quality. And because you’re not rushing through your work, you ship something - a feature, a report, an ML model, etc - with fewer errors and defects.


This isn’t new thinking. The Total Quality and Lean movements have worked to remove waste from processes for decades. Agile and “XOps” (replace X with dev, data, ml, etc.) are attempts in the tech industry to apply Lean thinking to our discipline. The belief is that continuous improvement leads to higher-quality service to the end customer. So far, so good.


The first principle in the Agile Manifesto is “Our highest priority is to satisfy the customer through early and continuous delivery of valuable software.” The same thinking can extend from software to data and ML/AI. Delivering something of high quality means what it implies. It does not mean shipping junk just to hit an arbitrary deadline.


Another Agile principle is “Deliver working software frequently, from a couple of weeks to a couple of months, with a preference to the shorter timescale.” This often takes the form of sprints. Most tech and data teams practice some form of Agile sprint, but often in a cargo-cult fashion. Often, this takes the form of two week sprints where features, reports, and models are cranked out, often of questionable quality. But hey, you burned down your story points for the sprint. And you’re “iterating.” Well done.


Agile and XOps have both become ceremonial memes. Being “Agile” often means hitting delivery deadlines, even if it introduces error-prone and buggy features. The continuous delivery part from the first Agile principle is there, but the valuable part is missing. This wasn’t the intention of Agile. Still, these days the goal is higher productivity, which is measured by output over a period of time. More output is preferred. Because the time component of Agile (short, incremental work) is a big fixation, we miss the bigger picture of high-quality software delivery.


Nowadays, Agile seems more like a way to deliver “stuff” in regular short bursts, but often at the expense of quality. Quality takes a back burner, with the excuse that the technical debt will be resolved at some later date. That day very rarely comes. Technical debt piles up. More and more new features are delivered. So it goes. At some point, users might notice. But those who notice the most are the devs, analysts, data engineers, and data scientists who know in the back of their heads they’ve built a house of cards. But that’s for other people to worry about, right?


What about XOps? XOps is closely related to Agile and Lean. But it’s hard to continuously deliver something of quality if the notion of quality is ignored. Dev/Data/ML/AI OPs are all opportunities to continuously deliver high-quality features and products, assuming you have a culture of quality.


> “Quality, far beyond that required by the end user, is a means to higher productivity.” - Peopleware


Even if customers or users don’t seem to notice, you should notice and care. Every time you ship something subpar, you put one more chip on the debt pile. At some point, you’ll either pay down those chips or burn the pile to the ground.


I see plenty of software and data teams who are encouraged to ship things, often without tests or validation. There’s little to no investment in quality, either from a training or process standpoint. As the authors wrote in Peopleware, “The organization that is willing to budget only zero dollars and zero cents for quality will always get its money’s worth. A policy of “Quality - If Time Permits” will assure that no quality at all sneaks into the product.” True in 1987 and just as true today.


The problem gets solved when we slow down for a bit, in order to move faster for the long haul. Incentivize your teams to focus on quality1, even if that means lower output for a few sprints. If you’re incentivized to reduce errors while maintaining a decent cadence of delivery, initially you might feel like you’re moving painfully slow. Over time, you’ll end up moving faster and receiving better marks for your efforts.


For software teams, this means writing tests, proper error handling, writing clean code, and other standard software practices. I say standard, but you’ll be surprised at how often these things don’t happen.


Because data modeling is top of mind for me right now, I’ll give some examples. In general, if you’re using a conventional data modeling approach, you’re doing things in a standardized and predictable way. This will lead to few issues because you’re sticking with convention, versus randomly plopping data into tables and fields. Another benefit is your team has a common framework for thinking about and working with data. The model is the central focal point, instead of a bunch of random models floating around git.


If you’re using a relational database for an application, for heaven's sake, use the relational model. It amazes me how often I see relational databases without a relational model, and even more amazed when I hear developers complain about duplicate data and update/delete side effects. The relational model has been popular and taught for several decades because it works!


For analytics, use a mainstream data model like Kimball or Data Vault. Use one big table if you think you’re past the need for the mainstream approaches, but know the tradeoffs. Better analytical data modeling means high data quality for reports and analysis. Your team will have a cohesive data model they all understand and work with instead of an incomprehensible sprawl of tables, notebooks, and scripts. Observe and monitor for data quality issues. Take the time to do the right things and build quality into your data.


Slow down to move faster.


---


If you haven’t checked it out, the Data Engineering Professional Certificate is available on Coursera! Learn practical data engineering with lots of challenging hands-on examples. Shoutout to the fantastic people at Deeplearning.ai and AWS, who helped make this a reality over the last year. Enrollhere.


On another note, the popular Data Therapy Session calendar is postedhere. It’s an incredible group where you can share your experiences with data - good and bad - in a judgment-free place with other data professionals. If you’re interested in regularly attending, add it to your calendar.


Finally, I’m traveling and speaking a lot. My schedule is at the end of this newsletter. I hope to see you somewhere in the world!


Hope you have a fun weekend!


Thanks,


Joe


P.S. If you haven’t done so, please sign up forPractical Data Modeling. There are lots of great discussions on data modeling, and I’ll also be releasing early drafts of chapters for my new data modeling book here. Thanks!


---


# Cool Weekend Reads


Jupiter now scales to 13 Petabits per second | Google Cloud Blog


Get Me Out Of Data Hell — Ludicity


Tom Johnson · Big Data for the Leviathan: Counting without Numbers


Imagine if Jeff Bezos managed your data warehouse | by Martin Chesbrough | EverestEngineering | Nov, 2024 | Medium


https://lethain.com/strategy-systems-modeling/Snowflake’s Fall to Earth 📉 - OnlyCFO's Newsletter


Review of the DataEngBytes conference and how it relates to the Occam Data Framework


Vector Databases Are the Wrong Abstraction


# New Show & Upcoming Events


## The Joe Reis Show


5 Minute Friday - The Quality Paradox (Spotify)


5 Minute Friday - Asking Good Questions at Conferences (Spotify)


Wes McKinney (Spotify)


5 Minute Friday - Is AI a Hail Mary for Tech Debt? (Spotify)


5 Minute Friday - Speaking at Conferences (Spotify)


Vijay Yadav - GenAI-Ready Data (Spotify)


5 Minute Friday -  Playing Not to Lose (Spotify)


Navnit Shukla - Data Wrangling and Architecting Solutions on AWS, Writing Books, and More (Spotify)


5 Minute Friday - Notes from the Field, Early Fall 2024 Edition (Spotify)


Ilya Reznik - How to Lead New and Existing ML Teams and More (Spotify)


Jordan Morrow - How to Write Amazing Books (Spotify)


Venkat Subramaniam - Moving Beyond Agile as a Buzzword, Learning to do Less, and more (Spotify)


Paco Nathan - Hacker Culture, Cyberpunk, AI, and More (Spotify)


Bill Inmon - History Lessons of the Data Industry. This is a real treat and a very rare conversation with the godfather himself (Spotify) - PINNED HERE.


## Monday Morning Data Chat


Note - The Monday Morning Data Chat’ is over. But you can still find the back catalog on your podcast platform of choice, or on YouTube.


The Finale! -YouTube


Paco Nathan - (Spotify,YouTube)


Weimo Liu - (Spotify,YouTube)


Matthew Mullins - (Spotify,YouTube)


Ricky Thomas and Paul Dudley - (Spotify,YouTube)


Andrew Ng - Why Data Engineering is Critical to Data-Centric AI (Spotify,YouTube)


Tevje Olin - What Should Data Engineers Focus On? (Spotify,YouTube)


Rob Harmon - Small Data, Efficiency, and Data Modeling (Spotify,YouTube)


Joe Reis & Matt Housley - The Return of the Show! (Spotify,YouTube)


Nick Schrock & Wes McKinney - Composable Data Stacks and more (Spotify,YouTube)


Zhamak Dehghani + Summer Break Special (Spotify,YouTube)


Chris Tabb - Platform Gravity (YouTube)


Ghalib Suleiman - The Zero-Interest Hangover in Data and AI (Spotify,YouTube)


## Events I’m At


NYC - Data Galaxy Event. November 13.Register here


Forward Data Conference - Paris, France. November 25.Register here


AWS ReInvent - Las Vegas. Early December. Doing the after-conference scene. Let’s meet up.


Seoul, Korea - TBA. Mid-December.


CES - Las Vegas. Early January 2025.


Data Day Texas - Austin, TX. January 25, 2025.Register here


Data Modeling Zone - Arizona. March 4, 2025.Register here


Winter Data Conference - Austria. March 7, 2025.Register here


Netherlands - TBA. April 2025


Much more to be announced soon…


# Thanks! If you want to help out…


Thanks for supporting my content. If you aren’t a subscriber, please consider subscribing to this Substack.


Would you like me to speak at your event?Submit a speaking requesthere.


You can also find me here:

- Monday Morning Data Chat (YouTube/Spotifyand wherever you get your podcasts). The show is gone, but the back catalog is great. Matt Housely and I interview the top people in the field. Live and unscripted.
- My other show is The Joe Reis Show (Spotifyand wherever you get your podcasts). I interview guests on it, and it’s unscripted and free of shilling.
- Practical Data Modeling. Great discussions about data modeling with data practitioners. This is also where early drafts of my new data modeling book will be published.
- Fundamentals of Data Engineering by Matt Housley and I, available atAmazon,O’Reilly, and wherever you get your books.


Be sure to leave a lovely review if you like the content.


Thanks!


Joe Reis


Thanks for reading Joe’s Nerdy Rants! Subscribe for free to receive new posts and support my work.

[1](https://joereis.substack.com/p/the-quality-paradox#footnote-anchor-1-151403465)

When should you ignore or suspend quality? The caveat is if you’re in a POC phase, a startup trying to find an MVP, or you’re doing exploratory data analysis (EDA). In these cases, you’re exploring. These aren’t features or products that will live in production. The big misnomer I see is people equate these with production features and use them as an excuse that “we’re iterating and staying Agile.” Know when you’re exploring and when you’re shipping to production. These are not the same things. An MVP might become a production app, so you should harden the app for production. The toy MVP is not ready for prime time, and don’t be under the illusion that it is. Same with EDA. EDA isn’t the same as shipping an executive report or dashboard or a ML model that serves your end customers on an ongoing, non-testing basis.
