---
title: "Mixed Model Arts - The Convergence of Data Modeling Disciplines"
subtitle: "Joe's Nerdy Rants #46 - Weekend reads and other stuff"
date: 2024-06-29T15:30:13+00:00
url: https://joereis.substack.com/p/mixed-model-arts-the-convergence
slug: mixed-model-arts-the-convergence
word_count: 1974
---

0:00
-8:09

![Art 'One Glove' Jimmerson, who fought in very first UFC event, dead at 60 |  Fox News](https://substackcdn.com/image/fetch/$s_!Z5Dt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa76d6266-e713-4533-b064-beb3f0e8328b_1200x675.jpeg)

*UFC 1 - Royce Gracie fought Art Jimmerson, who mysteriously wore ONE boxing glove in a no-holds-barred fight. This fight was the beginning of mainstream MMA.*


It’s no secret I’m very much into mixed martial arts (MMA) and combat sports. If I hadn’t gone into data 20+ years ago, there’s a strong likelihood I’d have ended up doing MMA full-time instead. I suppose fate from the good Lord intervened, and I’m instead writing an article and book that somehow ties MMA to data modeling.


The early days of combat sports were very similar to how data modeling is viewed today and in the past several decades. In combat sports back in the day, you used to get away with being a “kung fu grandmaster,” a boxer, a wrestler, a Brazilian Jiu-Jitsu expert, etc. As a kid, I remember constant speculation about what would happen if Bruce Lee1and Mike Tyson fought. Or Muhammad Ali vs Hulk Hogan. And you’d always hear rumors about some secret fighting style in the mountains of China, where a grandmaster could kill you just by looking at you. But you couldn’t learn more, because it’s a secret. Everyone was OK in their kingdom, believing their fighting style reigned supreme.


Then, the UFC was live on pay-per-view2in November 1993. This was the beginning of modern MMA. I’ll never forget Royce Gracie’s match against Art Jimmerson. It was comical. As you can see in the image above, Royce (Brazilian Jiu Jitsu) looks like a kid in pajamas, and Art (a boxer) wearsoneboxing glove. Royce proceeded to take down Art and choke him out in rapid fashion. You have to remember that barely anybody understood grappling back then, so getting someone on the ground was pretty novel.


Fast forward to today, and MMA fighters are expected to know how to fight standing up, clinched against a cage, and on the ground. I can’t imagine a professional boxer showing up in the UFC today, only knowing boxing. That one-dimensional boxer would get straight-up mauled. Being one-dimensional in MMA is a recipe for disaster. Knowing boxing, Muay Thai/kickboxing, wrestling, and jiu-jitsu is the standard baseline skillset. And you need to bereallygood in every aspect of the fight game. Today’s MMA fighters are, by necessity, multi-disciplinary.


People working with data in a one-dimensional way are similar to combat sports before the UFC. An analytics practitioner might be a Kimball dimensional modeling or Data Vault expert. A software engineer might also be an expert at relational data modeling. Finally, an ML engineer or data scientist would know the ins and outs of feature engineering and deep learning. Everyone sticks to their silo, often unaware of how data is being handled outside of their area of expertise. This causes many problems, as data is “tossed over the wall,” forcing people downstream to handle any data problems independently. So it’s been for decades.


But this is changing, with people in different disciplines starting to learn each other’s craft. I’m starting to see software engineers and analysts learning machine learning/AI. Data scientists are learning to write production-grade code so they can work better with software engineers and integrate ML models into software applications.


The core ofPractical Data Modeling(the working title for my new book) is that the days of being one-dimensional with data modeling are over. It’s not enough to be proficient in a single data modeling approach. Today, the trend is moving toward combining various data modeling approaches. Very soon, you’ll need to know how to work with data across various use cases. Ignore this, and you’re like the boxer in UFC 1 wearing a single boxing glove. You’re not going to win at the game of data. Instead, like an MMA fighter moving between stand-up and ground, you need to know what data modeling technique to use for a given situation.


Two macro trends are forcing data modeling into a multi-disciplinary practice.


First, AI is rapidly ushering in a new era where anyone who works with data will interface with “AI.” This probably sounds like marketing speak (and it very much IS today), but this is the future. I’m seeing AI creep into nearly every workflow, whether helping you with the code you write or how you interface with tools. Also, working with multimodal data (images, audio, video, text, tabular, semistructured, etc) is becoming more common. The world isn’t just about tabular datasets anymore. Anyone who works with data must be proficient in modeling data of various types, shapes, and varieties. Finally, with seemingly every company interested in “doing AI, " many corporate systems' underlying datasets are getting a second look. As if doing BI wasn’t enough of a challenge, now companies want to throw LLMs on top of their data. Data modeling is getting a second wind precisely because the data isoften structured poorly and has quality issues. AI without good-quality data means you’ll do dumb things more quickly. And the underlying data model - combined with semantic structure (think knowledge graphs, semantic layers, etc) - is the key to making this work. Records and queries in transactional databases and data warehouses are saved as embeddings in a vector database. The worlds of ML/AI are merging with transactional, graph, and analytical data modeling. But we also can’t allow or expect AI to simply do everything on its own. More than ever, you must understand what’s happening under the hood.


Second, data-powered products are moving toward a fusion of how data is used across various use cases - software applications, analytics, and ML/AI. For instance, analytics is moving far beyond internal-facing reports and away fromEnterpriseland toward Productland. Nowadays, an application might rely on heavy OLAP processing behind the scenes to provide a better user experience and embedded reports for end-users. And the same application could have an ML model powering another aspect of the customer experience. Data in this example application is modeled differently, depending on the situation.


As data-powered products become normal, anyone who works with data must understand how data is modeled across various situations. You might model data relationally in an RDBMS, create a star schema for your data warehouse, and feature engineer the same dataset to create an ML model. The feedback loop between various use cases forces people to know what’s happening across the multiple ways data is used. Data’s no longer “one and done.” Instead, data continuously flows through the data-powered product. This breaks down the traditional siloes mentioned earlier.


Bigger companies will have the luxury of hiring for specific roles. However, as the lines between applications, analytics, and ML/AI blur, knowledge of various data modeling techniques will become standard. I expect titles will evolve toward something like “data product engineer,” which is much more cross-disciplinary than today’s roles. In general, Productland is the future and Enterpriseland is a dead-end. The world is moving toward data products, which requires a different way of working with data.


Mixed Model Arts is the new trend of becoming cross-disciplinary in data modeling. This is the future. And this is the central theme of my latest book -stop obsessing over specific siloed techniques.Get to know the big ideas in data modelingacrossdisciplines and use cases.I understand this is a tall order. However, much more will be expected from anyone who steps into the cage to work with data. Welcome to the new world of Mixed Model Arts.


Shameless plug - I’ll drop new draft chapters in my data modeling book atPractical Data Modelingover the next few months. Most will be paywalled. But I’ll also release some free content now and then. The book will drop sometime this Fall. Also, over at Practical Data Modeling, we have regular “Data Therapy” sessions if you want to show up and vent about your data problems or learn from other practitioners. It’s a very useful and supportive group.


Hope you have a fun weekend!


Thanks,


Joe


P.S. If you haven’t done so, please sign up forPractical Data Modeling. There are lots of great discussions on data modeling, and I’ll also be releasing early drafts of chapters for my new data modeling book here. Thanks!


---


# Cool Weekend Reads


Economic Termites Are Everywhere (BIG by Matt Stoller)


No One Wants to Sound Clueless About AI. Especially Your Boss (WSJ)


WWDC 2024: Apple Intelligence (Daring Fireball)


My Memories Are Just Meta's Training Data Now (WIRED)


Has Facebook Stopped Trying? (404 Media)


The Coming Great Conflict (TIME)


AI Doesn’t Kill Jobs? Tell That to Freelancers (WSJ)


The Death of the Junior Developer (Sourcegraph)


6 months ago, I left the bullshit industrial complex (Joan Westenberg)


Finding GPT-4’s mistakes with GPT-4 (OpenAI)


The Origin of Toys“R”Us: Brand Film | Toys"R"Us (YouTube)- The first ad made with Sora.


# New Content, Events, and Upcoming Stuff


## The Joe Reis Show


#### This week…


The Finnish Data Mafia - What’s Up With Data in Finland? (Spotify)


5 Minute Friday - Mixed Model Arts (Spotify)


#### In case you missed it…


Nick Freund - Closing a Startup (Spotify)


5 Minute Friday - “Success” (Spotify)


Doug Needham - Architecture Deep Dive, The Hard Work of Generative AI in the Enterprise, and more (Spotify)


5 Minute Friday - WTF is a “Data Team”? (Spotify)


5 Minute Friday - Don’t Be A D*ck (Spotify)


Juha Korpela - Conceptual Data Modeling Deep Dive (Spotify)


Bill Inmon - History Lessons of the Data Industry. This is a real treat and a very rare conversation with the godfather himself (Spotify) - PINNED HERE.


## Monday Morning Data Chat


Note: Matt Housley and I are taking the Summer off from the Monday Morning Data Chat. We will be back in the Fall with an incredible new lineup.


That said, we have a special episode dropping soon with Wes McKinney and Nick Schrock. Stay tuned!


#### In case you missed it…


Zhamak Dehghani + Summer Break Special (Spotify,YouTube)


Chris Tabb - Platform Gravity (YouTube)


Ghalib Suleiman - The Zero-Interest Hangover in Data and AI (Spotify,YouTube)


Bart Vandekerckhove - Data Security Deep Dive (Spotify,YouTube)


Yali Sassoon - Using LLMs to Support the Analytics Workflow (Spotify,YouTube)


David Yaffe & John Kutay - The State of Streaming and Change Data Capture (Spotify,YouTube)


## Events I’m At


(Taking the Summer off, sort of…)


USA and virtual events - TBA


Big Data London - September 18-19.Register here


DataEngBytes (Australia) - Late September/Early October, TBA


Helsinki Data Week - Fall TBA


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

[1](https://joereis.substack.com/p/mixed-model-arts-the-convergence#footnote-anchor-1-146062334)

As a sidenote, Bruce Lee is the OG of MMA, having pioneered a multi-disciplinary approach to fighting called Jeet Kune Do.

[2](https://joereis.substack.com/p/mixed-model-arts-the-convergence#footnote-anchor-2-146062334)

Sure, there was Vale Tudo in Brazil and Sambo in Russia. But these didn’t go mainstream worldwide. It also turns out that the UFC was basically an informercial for Gracie Jiu Jitsu.
