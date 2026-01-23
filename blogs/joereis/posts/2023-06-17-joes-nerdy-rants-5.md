---
title: "Joe's Nerdy Rants #5"
subtitle: "WTF is a Model?, plus weekend reads and other stuff"
date: 2023-06-17T16:58:25+00:00
url: https://joereis.substack.com/p/joes-nerdy-rants-5
slug: joes-nerdy-rants-5
word_count: 1518
---


# WTF is a Model?

0:00
-5:40

“We are not modeling reality, but the way information about reality is processed, by people.” - William Kent (Data and Reality, 1978)


![](https://substackcdn.com/image/fetch/$s_!eZ1J!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F521ad432-7cda-42f3-9ff6-837cb46fc416_537x464.jpeg)


The world of data is so jumbled that you might be forgiven for not being clear on what a “model” is. When you hear the word “model,” what comes to mind? If you work in data, you might be thinking of the canonical stages of data modeling (conceptual, logical, physical), a relational data model, a dimensional model, a machine learning model, a dbt model file,  a Django or Rails model file, a Python Pickle model artifact, etc. The word “model” is pervasive in our field, and I think it’s causing data people to cross wires when they talk to each other. A data scientist considers her ML model to be a model. A DBA implements a 3rd normal-form relational data model in a database. An analytics engineering team interacts with various dbt models, which might also be modeled dimensionally, just a bunch of tables or one big table. You get the idea. We’re all modeling, but very often in different ways.


When I ask data professionals from across different modes of operation what they consider a “model,” I get answers like the ones above. Meanwhile, I see the formal practice of data modeling as either unknown or willfully ignored by software and data practitioners across the board. Oftentimes, people complain that formal “data modeling” is too rigid and takes too long. Instead, models are often created ad hoc. We model for what’s in front of us at the expense of the bigger picture. The tradeoff is expediency versus knowledge. I strongly believe we do data modeling whether we’re intentional or not. The lack of a data model is still a data model, albeit a potentially crappy one.


Ironically, in a field that advocates for consistent data governance and management, we struggle to use a simple word like "model" consistently or accurately. This has significant consequences. Instead of using modeling to establish a shared understanding of our organization's vocabulary, rules, and processes, we have extreme fragmentation in our models. Most models don't align with each other and only focus on tiny aspects of reality, which leads to a lack of understanding of the bigger picture.


The big picture is what matters. We need to revisit higher-level data modeling, namely conceptual and logical. A shared understanding of data at a high level will help pave the way toward the broad use of consistent and believable models (analytical, ML, application, etc.) across and between organizations.


I’m writing a longer article on this theme, to be published soon. This theme is part of the much broader theme of my ongoing book on resurrecting and revamping data modeling.


Listen to the audio clip above on this topic, which is also my5 Minute Friday onSpotify.


---


# Cool Weekend Reads


### Tech, AI & Data


EU lawmakers pass landmark artificial intelligence regulation (CNBC)


Whatever you think about the EU AI Act, this was a historic week. Enough said.


Unifying Large Language Models and Knowledge Graphs: A Roadmap


Might knowledge graphs be a solution to the notorious hallucination problem with LLM’s? This great whitepaper might end up being “one of those” papers that changes the game in AI.


How the Computer Graphics Industry Got Started at the University of Utah (IEEE Spectrum)


The University of Utah is my alma mater, and the legacy of the computer graphics innovations that happened there is legendary. My oldest son loves to write video games. One of my favorite things to do with him is taking him around the Warnock Engineering building (named after the founder of Adobe), where he can see Ed Catmull’s (Founder of Pixar) report card (he got A’s) and then play Atari games (started by Nolan Bushnell). Sidenote - The U of U was also among the original four nodes of Arpanet, which would become the Internet.


MusicGen: Simple and Controllable Music Generation (Facebook Research)


Text to music is a trend I’m definitely interested in, partly because I make music in my spare time (I swear I’ll post tracks to my Soundcloud soon). I’m very curious how stuff like MusicGen will impact creators of stock music.


Metis: Building Airbnb’s Next Generation Data Management Platform (The Airbnb Tech Blog)


Pretty cool to see Airbnb embracing data management. Really good read on their journey. Curious if this gets open-sourced, or if employees spin out a startup.


92% of programmers are using AI tools, says GitHub developer survey (ZDNET)


“This is more than just people working on external open-source projects or just fooling around. Only 6% of developers said they solely use these tools outside of work. In other words, today, AI programming tools are part and parcel of modern business IT.”


The nature of programming has already changed. That said, reasoning about code won’t go away anytime soon. You still need to know if and why AI-generated code works.


### Business & Startups


Crypto collapse? Get in loser, we’re pivoting to AI


“Half of crypto has been pivoting to AI. Crypto’s pretty quiet — so let’s give it a try ourselves. Turns out it’s the same grift. And frequently the same grifters.”


Yep. Same grift, different day. Seems like everyone is suddenly an “AI” expert.


Elevating Data to a Profession: Why It Matters (Data with Intent)


My friend Benny explains why professional qualifications in data are necessary.


Using AI for loans and mortgages is big risk, warns EU boss (BBC News)


“Discrimination is a more pressing concern from advancing artificial intelligence than human extinction, says the EU's competition chief.”


I agree.


A trip to the internet in 1996 with The Rough Guide 2.0 (Planet Jones)


When I was a teenager, I owned a literal “phone book” for the Internet. This article brings back many fun memories of when the modern Internet was still getting started and had a sense of purity and mystique.


Iran's 'quantum processor' turned out to be a $600 dev board (PC Gamer)


Golf clap for the troll job.


When I lost my job, I learned to code. Now AI doom mongers are trying toscare me all over again (The Guardian)


“The spectre of AI will be used as a threat and a cudgel by those who see creative pursuit as only possessing worth if it can be monetised, but they’re wrong. A machine has no capacity for self-expression, no compulsion to communicate: this is who I was, this is how I felt and this is what I stood for. We do, andin all of our endeavours we need to start refusing attempts to make us forget how valuable our humanity really is.”


---


# New Content, Events, and Upcoming Stuff


### This week


Monday Morning Data Chat - Data Modeling in 2023 w/ Colin Zima (Spotify,YouTube)


The Joe Reis Show


Murielle Popa-Fabre - The AI Regulatory Gold (or Rule?) Rush (Spotify)


Rebecca Taylor -  Navigating Large Companies to Build ML (Spotify)


George Park - Automation, Change Management, and More (Spotify)


5 Minute Friday -  WTF is a Model? (Spotify)


### Upcoming


Monday Morning Data Chat - Joe Perez


The Joe Reis Show - Lots of episodes are dropping soon. Stay tuned. Big names, great names, and always excellent conversations.


Here are some cool upcoming in-person events I’ll be at in June and beyond for 2023


Vancouver BC - Low Key Happy Hour, Thursday 6/22. DAMA, Friday 6/23


Ethan Aaron Low Key Happy Hour - Vegas Edition. Monday 6/26.


Data Engineering Meetup, San Francisco Edition - Tuesday, 6/27 (register here)


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
