---
title: "Boring is Back - The Longer Rant"
subtitle: "Joe's Nerdy Rants #17 - Weekend reads and other stuff"
date: 2023-09-15T16:35:49+00:00
url: https://joereis.substack.com/p/boring-is-back-the-longer-rant
slug: boring-is-back-the-longer-rant
word_count: 1671
---


# Boring is Back - The Longer Rant


![Habits of Extremely Boring People](https://substackcdn.com/image/fetch/$s_!6J-1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff702554-5442-468b-b612-8766b00e8886_750x563.jpeg)


InFundamentals of Data Engineering, Matt Housley and I observed that the tools data professionals use will continue to simplify, with complexity constantly abstracted away. These days, in the realm of “classical” data work - data warehousing, ETL/ELT, BI, etc. - it’s hard to find truly terrible tools. The complaints about the traditional complexity people used to have to manage back in the day - running and patching servers, dealing with networking issues, disk failures, and all the pains of dealing with infrastructure - seem very distant. The modern data stack greatly simplified the analytical workflows that we’d been dealing with for the last 30 years. Now, with the swipe of a credit card, you’ve got insane amounts of power and capability available to you. There are very few problems in the “classical” sense that aren’t solved by an open-source tool or a SAAS company.


That said, the modern data stack is not really that modern anymore. If I place a date on the start of the modern data stack, it’s the launch of AWS Redshift in late 2012. In the dog years of tech, that’s ancient. The modern data stack served its purpose, and I don’t think there are too many data professionals who yearn to return to the days of grinding it out on the older technology. It’s time to move beyond the modern data stack to the “boring data stack.”


Boring is back. Because the focus isn’t on managing the underlying technology anymore, we can now turn our attention to the boring stuff we conveniently ignored during the heyday of the modern data stack era - data governance, data management, data modeling, and other “enterprisey” practices. This is the stuff that’s boring as hell to most people, yet critical to making data work in any organization.


Another reason we need to tackle the boring stuff is the rise of AI and ML. To me, this is the biggest opportunity for the data profession to get its house in order. As I wrote before, if we’re not going to get things in order now, when are we going to do it? In a past life, I worked at startups focused on automated ML (give us any dataset, we’ll give you classifications or predictions). I saw first-hand how most corporate datasets were very messy, lacked sufficient quality, and barely worked for BI, let alone AI. The rise of LLM’s poured gasoline on this hot mess. This means we need to operate not just in a world of rows and columns, but a world that blends unstructured and tabular data together. Recently,Juan Sequeda and I chattedabout how this moves us from a data-centric world to a knowledge-centric one. This future is exciting, and boring stuff will be necessary to get there.


Here’s where I think things gets boring, and in a good way.

1. Data governance and management are cool again. In most companies, if you mention these things, you’ll be “heard” and then shunned forever. That’s changing. With the increased focus on “getting value from data”, you’ll see a lot more emphasis on the boring things that achieve value. Data governance and data management are two cornerstones of making data work at its highest potential.
2. Data modeling makes a return, and not in the way you think. Crappy and non-existent data models are a plague for many data teams, especially in the last several years. We’re still arguing about one-big-table vs Kimball, while ignoring the big picture - conceptual and logical data modeling. Right now, I notice a tendency to jump straight into physical data modeling. Meanwhile, the physical data models are often disconnected from the reality of the business it’s trying to serve, and also become victims of side effects such as redundant/duplicate data, update and delete problems, and more. It’s like we forgot decades of formal data modeling practices because it’s easier to just throw compute at the problem. Turns out, the problem doesn’t simply disappear.Conceptual modeling captures the business rules, vocabulary, information flows, and so on. Especially with LLMs working alongside corporate databases, having a solid conceptual model (and a logical model that translates this to the physical model) will be critical. It’s not just about data anymore, it’s about turning data into knowledge that’s believable and useful for humansandmachines.
3. The “data” and ML divide will disappear. There’s a weird sense among people that data and ML are two different universes. AI and ML depend upon great data. This is not negotiable.


I’ll have a lot more to say on this topic in future rants, but I’ve got to pack for my trip to London. If you’re at Big Data London next week, please say hi. I’m boring as hell ;)


Listen to the audio clip above on this topic, which is also my5-Minute Friday on Spotify.


---


# Cool Weekend Reads


I hope you all had a great week. I’ve been touring Australia all week and enjoying it!


Here are some cool things I read this week…


### Tech, AI & Data


Tackling Data's Biggest Culture Problem (Chad Sanderson)


Data contracts are going to change the game. I’m very stoked for Chad and the team atGable.ai!


Serverless is still not designed for data (Bauplanlabs)


Serverless is a bit of an overloaded term. In the context of trying to adapt serverless software tools for data practices, I agree with this article. There’s still a lot of work to do.


The 11 Types Of Toxic Pull Requests (According To 4.5 Million Code Branches) (Dev Interrupted)


This is a very good look at where pull requests go wrong, and some suggestions for making them better. I suggest every software and data team have a look, just to compare against your own experience.


Inside Elon Musk's Struggle for the Future of AI (Time)


“Tesla and Twitter together could provide the datasets and the processing capability for both approaches: teaching machines to navigate in physical space and to answer questions in natural language.”


Interesting story about the friend/foe dynamics of the big players in AI. Also covers how Twitter/X and Tesla might be Elon’s secret weapon in training AI. Seriously, does anyone want an AGI based on X?!


### Business & Startups


Profound Beliefs (Steve Blank)


“The winning combination isstrong beliefsthat are validated or modified by evidence gathered outside the building.These are “strong opinions loosely held.”


US Copyright Office denies protection for another AI-created image (Reuters)


All I can say is IP will be a very interesting topic in the age of AI-generated content. We’re just getting started.


Seed Market Evolution During A Downturn(Semil Shah)


“Early-stage is perhaps a more attractive stage to deploy smaller dollars these days – a friend remarked everyone wants to gamble, but no one wants to sit at the whale tables just yet.”


Inside Exxon’s Strategy to Downplay Climate Change (WSJ)


“Sprow said he and former Exxon CEO Lee Raymond acknowledged the climate was changing but questioned to what extent human activity was causing it and how serious and rapid the impacts would be. The January study in Science said that Exxon’s climate modelers mostly attributed the changes to humans.”


My opinion on climate change - it’s probably too late to make a dent. I hope not, but the evidence isn’t promising. Humans have been too slow to react, and we’re nowhere near hitting the levels necessary to make a change. That doesn’t mean we can’t reset our individual behaviors to make things better for the planet. We should and must change how we live on this planet. It’s all we’ve got.


---


# New Content, Events, and Upcoming Stuff


## Monday Morning Data Chat


#### Coming up…


Data Career Advice and AMA w/ Matt Housley and Joe Reis (LinkedIn,YouTube)


#### In case you missed it…


The Future of Generative AI in Data Analytics w/ Amit Prakash - (Spotify,YouTube)


Incentivizing Devs to Pursue Open-Source Projects w/ Max Howell  (Spotify,YouTube)


Data Grifters w/ Aaron Hunsaker (Spotify,YouTube)


The Power of 3 (Math Nerds, Professors, and O'Reilly Authors) w/ Hala Nelson (Spotify,YouTube)


## The Joe Reis Show


Ravit Jain - How to Become a Top Data Influencer and Content Creator (Spotify)


Juan Sequeda - The Power of Knowledge Graphs and LLMs on Structured Data in the Enterprise (Spotify)


5-Minute Friday - No 5-Minute Friday this week, as I’m packing and leaving for the UK.


#### In case you missed it…


5 Minute Friday - Boring is Back! (Spotify)


Aaron Neiderhiser & Coco Zuloaga - Fixing Medical Data from First Principles (Spotify)


5 Minute Friday - Start Playing Offense (Spotify)


David Foster - Generative Deep Learning, Writing a Best-Selling Book, and More (Spotify)


Kevin Hu - How the Data Landscape Evolves Alongside LLM’s (Spotify)


## Events


### September


Big Data London- 9/20 -register here


### October


Bangalore, India - 10/12. DEWcon -register here


Dubai -  10/16-10/19. GITEX -register here


Chicago - 10/26 - GOTO Conference Data Engineering Masterclass. This is a VERY rare opportunity to learn data engineering from Matt Housley and me, in person -register here


### November


Canada - DAMA Toronto. Details TBA


Finland - TBA


Las Vegas - ReInvent - got a massive special announcement in store :)


2024 - lots of stuff. Stay tuned :)


### December


TBA


# Thanks! If you want to help out…


Thanks for supporting my content. If you aren’t a subscriber, please consider subscribing to this Substack.


You can also find me here:


Monday Morning Data Chat (YouTube/Spotifyand wherever you get your podcasts). Matt Housely and I interview the top people in the field. Live and unscripted. Zero shilling tolerated.


The Joe Reis Show (Spotifyand wherever you get your podcasts). My other show. I interview guests, and it’s totally unscripted with no shilling.


Fundamentals of Data Engineering (Amazon,O’Reilly, and wherever you get your books)


Be sure to leave a nice review if you like the content.


Thanks! - Joe Reis


Thanks for reading Joe’s Nerdy Rants! Subscribe for free to receive new posts and support my work.
