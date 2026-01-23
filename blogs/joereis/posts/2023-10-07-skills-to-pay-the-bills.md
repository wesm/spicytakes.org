---
title: "Skills to Pay the Bills"
subtitle: "Joe's Nerdy Rants #18 - Weekend reads and other stuff"
date: 2023-10-07T02:32:41+00:00
url: https://joereis.substack.com/p/skills-to-pay-the-bills
slug: skills-to-pay-the-bills
word_count: 1816
---


Before I rant, I’d taken some time off the newsletter to get a better idea of my schedule for 2023/24. Needless to say, I’ve got a lot going on. Probably too much. Oh well, call the whambulance. I’ve got content to create for YOU.


Even with a lot going on, the show must go on. After getting feedback from my readers (thanks to all whoreplied) there’s sufficient demand for both this weekly newsletter and longer-form articles. I’ll aim for the regular weekly newsletter, as a lot of you like it and it keeps me accountable to regularly write. Additionally, I’ll write long-form articles on a random basis (for now), where I’ll dive deeper into topics of interest to the data community.


And, stay tuned forPractical Data Modeling, a new Substack I’m launching very soon that’ll contain content on data modeling (duh) - early access chapters to my new book (out Q1 2024), audio/videos, related articles, community, and much more. If you’re into data modeling, this will be the place for you! Let’s bring back data modeling.


Finally, a note to conference and event organizers - I’m going to be heads down the first half of 2024. If you’d like me to speak at your event in the first half of 2024 (virtual or in-person), pleasecontact meby 11/6/2023 to get things going. After that date, I’m going to stop taking inquiries, no matter who you are.


Thank you for your support,


Joe Reis


# Skills to Pay the Bills


![9. You Pay All Your Own Bills. GIF - Dollar Bill Y All GIFs](https://substackcdn.com/image/fetch/$s_!zuF1!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e732272-c757-49eb-b9f3-35d088e56d8e_500x282.gif)

0:00
-6:49

Yesterday, I chatted with Ryan and Eric Dolley on theirSuper Data Bros Show, making my typical curmudgeonly rant about why the most significant gap in our industry isn’t tooling (I think we’re blessed with many great tools and tech). Still, we need to level up our skills and knowledge to leverage the incredible power at our fingertips properly. It’s not a new argument, as I ranted about this a few months ago in my post,Lots of Fancy Tools, and No Idea How to Use Them. But again, the skill and knowledge gap is massive, and it will take a while for everyone to get up to upskill.


How do you level up your skills and knowledge? I bucket this into two areas - the foundations and the applied. You should spend most of your time studying the fundamentals. Why? First, the fundamentals are often vast, and there’s just a lot of ground to cover (depending on your use case, this could stretch thousands of years of material). Second, mastering the fundamentals means you’ve got the power to evaluate and zoom in on the tens of thousands of technologies and tools that come and go in our industry. Tools and tech come and go at light speed. Mastering the fundamentals is like understanding physics, chemistry, and other strong disciplines. How do foundations differ from applied ones? Let’s have a look.


Thefoundationsare the underlying principles and practices that underpin your field. Reading books is a great place to pick up this knowledge. Don’t skip it because it’s daunting. There’s no shortcut, and you have to put in the work if you want to be great at what you do. For instance, a data analyst should have deep knowledge of data analysis, statistics, experiments, and visualization. For instance, I hope you’ve read classics like Edward Tufte’s “The Visual Display of Quantitative Information.” If you’re a data engineer, I hope you’ve read Fundamentals of Data Engineering 😉, Designing Data-Intensive Applications, The Data Warehouse Toolkit, and understand architecture, infrastructure, data modeling, and everything in between.


The foundational knowledge and skillsets won’t change as quickly and provide a solid foundation for applying this knowledge to your job. For example, I spend around 60% to 70% of my time reading the classic books and papers on technology. Since this spans many decades, I’m not about to run out of reading material. I also find it enjoyable to read articles and books from the 1960s and 1970s, as they provide so much context to where we are today as an industry. What’s interesting is that the problems people faced generations ago are the same ones we now face. Foundational knowledge and skills are necessary to solve problems. Same as it’s always been. So, study the greats and the classics. To paraphrase Charlie Munger, without foundational understanding, “you are like a one-legged man in an ass-kicking contest.”


Theappliedpart of your skills and knowledge involves translating your foundational understanding of your field to the tools and technologies you use to solve problems in your career. If you’re a data engineer, and your team decided to go all in on Spark, Kafka, and AWS, guess what you get to master? All of those. And there’s nuance. AWS is a vast ecosystem whose offerings I often compare to the Cheesecake Factory Menu. AWS is fantastic and can overwhelm you if you don’t understand its ecosystem from first principles.


If you don’t understand the fundamentals of your job, how will you know what to use in AWS, let alone know how Spark and Kafka operate at an atomic level? Spark + Kafka + AWS ecosystem = a buttload of stuff to understand. And it’s your job to understand all of this at a granular level because it’s often the little stuff that’ll sink you. If you know the big ideas, it’s a lot easier to understand how these technologies and platforms fit together. Kafka is a streaming platform. Spark can process data (so can Kafka), and you’re operating within AWS, which has primitives such as EC2, VPCs, S3, regions/AZs, and on and on and on. Know how to tie these various applied details together, and you have a system that works! Skip the step of understanding how servers, networking, storage, and distributed computing work, and you’re dead in the water. At a minimum, you’ll duct tape over problems, incurring all forms of debt at high interest rates that’ll need to be paid back (and you’ll have to pay this back, trust me). At its worst, you’ll cause a catastrophic failure when it didn’t need to happen. This is when you get fired for incompetence, and ruin your reputation as a result. A lack of foundational and applied knowledge has severe consequences.F*ck around, find out.


As the old cliche goes, knowledge is power. Right now, I feel like the most data teams I’ve seen are just scratching the surface of their true potential. It’s not tooling that holds us back. The big challenge is the mastery, knowledge, and understanding of how to use these tools from first principles. Get the skills, pay the bills.


Listen to the audio clip above on this topic, which is also my5-Minute Friday on Spotify.


---


# Cool Weekend Reads


I hope you all had a great week. I’ve been touring Australia all week and enjoying it!


Here are some cool things I read this week…


### Tech, AI & Data


CIOs Feel Heat From CEOs on Generative AI (WSJ)


As I said on LinkedIn about this article, this feels very much like FOMO-driven AI. I don’t imagine the latest AI/ML hype cycle will end well.


Relational is More than SQL (Fauna)


Bob Muglia is an OG in the database field, contributing significantly to Sybase, MS Office, and SQL Server, and worked as the former CEO of Snowflake. He’s right - SQL is due for an upgrade. I’m excited to see where projects like Fauna go.


Also…Stay tuned for my interview with Bob Muglia, dropping next week!


What’s New In Python 3.12 (Python.org)


Lots to love here - Better f strings, type parameter syntax, a per-interpreter GIL (in C only, coming in 3.13), and much more.


An Interactive Intro to CRDTs (Jake Lazaroff)


CDRTs (Conflict-free Replicated Data Type) are everywhere (no pun intended), and you might not know what they are. Now you’ll know.


### Business & Startups


So We Shipped an AI Product. Did it Work? (Honeycomb)


If you’re building an LLM at your company, this is a solid read.


Lost your luggage? That's nothing – we just lost your whole flight! (The Register)


A great and entertaining read, and hopefully this never happens to you.


Nextdata is building data meshes for the enterprise (TechCrunch)


Nextdata is making Data Mesh a reality, and they just announced their funding. Zhamak is a close friend of mine, and I’m stoked for her and her team. Let’s go!


Note - if you’re a heavy hitter, they’rehiring…


---


# New Content, Events, and Upcoming Stuff


## Monday Morning Data Chat


#### Coming up…


Data Warehouses and Semantics Deep Dive, SDF, and more w/ Lukas Schulte -  (LinkedIn,YouTube)


#### In case you missed it…


Improving Your Health and Wellness - Techie Edition w/ Colleen Fotsch (Spotify,YouTube)


Data Engineering AMA w/ Matt Housley & Joe Reis (Spotify, Youtube)


Data Career Advice and AMA w/ Chris Tabb, Matt Housley and Joe Reis (Spotify,YouTube)


The Future of Generative AI in Data Analytics w/ Amit Prakash - (Spotify,YouTube)


## The Joe Reis Show


5 Minute Friday - Skills to Pay the Bills (Spotify)


Egor Gryaznov - The "Non-Modern Data Stack", and Getting Out of Our Data Bubble (Spotify)


Jason Taylor - The Divides in the Data Space, Fighting Dumpster Fires, and More (Spotify)


Michel Tricot - The Impact of AI on the Modern Data Stack (Spotify)


5 Minute Friday - My Thoughts on Vendors at Conferences (Spotify)


#### In case you missed it…


Ravit Jain - How to Become a Top Data Influencer and Content Creator (Spotify)


Juan Sequeda - The Power of Knowledge Graphs and LLMs on Structured Data in the Enterprise (Spotify)


## Events


### October


Bangalore, India - 10/12. DEWcon -register here


Dubai -  10/16-10/19. GITEX -register here


### November


Canada - DAMA Toronto -register here


Finland - Agile Data Engine Summit -register here


San Jose, CA - TBA


Las Vegas - ReInvent


### 2024


Data Day Texas (Austin) -register here


Data Modeling Zone (Arizona) -register here


Skiers in Data (Switzerland)


Again - get your inquiries to me by 11/6/2023. I won’t be accepting talk or event inquiries after this date. Thanks.


# Thanks! If you want to help out…


Thanks for supporting my content. If you aren’t a subscriber, please consider subscribing to this Substack.


You can also find me here:


Monday Morning Data Chat (YouTube/Spotifyand wherever you get your podcasts). Matt Housely and I interview the top people in the field. Live and unscripted. Zero shilling tolerated.


The Joe Reis Show (Spotifyand wherever you get your podcasts). My other show. I interview guests, and it’s totally unscripted with no shilling.


Fundamentals of Data Engineering (Amazon,O’Reilly, and wherever you get your books)


Be sure to leave a nice review if you like the content.


Thanks! - Joe Reis


Thanks for reading Joe’s Nerdy Rants! Subscribe for free to receive new posts and support my work.
