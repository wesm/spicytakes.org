---
title: "Data Engineering in 2024. What I'm Seeing."
subtitle: "Joe's Nerdy Rants #29 - Weekend reads and other stuff"
date: 2024-01-13T15:42:03+00:00
url: https://joereis.substack.com/p/data-engineering-in-2024-what-im
slug: data-engineering-in-2024-what-im
word_count: 1712
---


![A digital artwork depicting two contrasting characters, representing bored and excited data engineers. The first character is a bored data engineer, slouched in an office chair, with a dull expression, surrounded by piles of paperwork and multiple computer screens displaying graphs and code. The second character is an excited data engineer, standing energetically with a big smile, holding a laptop displaying colorful data visualizations. They are in a modern office environment with desks, computers, and tech gadgets. The atmosphere for the bored engineer is monochromatic and dull, while the excited engineer's space is vibrant and colorful.](https://substackcdn.com/image/fetch/$s_!YxZd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0eb5b4c9-69ec-4e82-abc8-63ecbd769d77_1024x1024.webp)


People often ask for my thoughts on what’s happening in data engineering. These aren’t predictions, per se. At the beginning of the year, I mentioned I avoid making predictions. While predictions can be entertaining to read, I've found them somewhat frivolous, trivia-laden, and often wrong. Instead, I prefer to share my thoughts and observations based on what I'm seeing, based on a ton of travel, conversations, and work. Feel free to extrapolate however you want.


My primary focus is advising data teams at "most companies." Although I engage in discussions with data teams from Big Tech, their work is so unique that it doesn't necessarily reflect the reality of what data engineers are doing at 99% of non-Big Tech companies. I’ve seen that most data engineers still do fairly vanilla work, like ETL/ELT, data warehousing, batch processing, and serving data for analytics and basic data science use cases. Most of these companies are still struggling to do BI, let alone AI.


Coming into 2024, here are some things I’m seeing with data engineering teams.


Continued Tooling Abstraction


One of the major trends in data engineering is the continued abstraction of tools. Open-source tools likeMageare fully-fledged and hide a lot of the low-level plumbing work data engineers used to do behind a beautiful UI. Streaming is getting simplified with tools likeEstuary,Upsolver, and more. Unless there’s a good reason, why handroll your infrastructure these days? Abstraction streamlines the development process and allows engineers to focus more on solving complex and value-added problems rather than managing low-level infrastructure and code.


FinOps, “Showing Me the Money,” and “Adding Value”


FinOps (financial ops) is getting popular in data, and everyone is asking the data team to “show me the money.” This shouldn’t be surprising, as most businesses are focused on controlling costs. Doing more with less is the name of the game. Adding “business value” is another big theme. Data engineering teams (and data teams in general) are becoming more capable of managing the financial aspects of data operations, optimizing costs, and squeezing efficiency gains from tooling and infrastructure resources. One further thought - FinOps shouldn’t just be about cost control but also leveraging data to increase revenues.


The Resurgence of "Enterprisey" Data Practices


Data modeling, data management, and other traditional “enterprisey” practices were out of favor during the 2010s and early 2020s. The pendulum is swinging back in favor of these practices as organizations recognize their importance in maintaining data quality, consistency, and governance. The rise of AI is forcing some of this renewed attention, and the walk-of-shame many data teams are doing after the giant mess they made on the Modern Data Stack. Data engineering is maturing as a field, and this is a good thing.


CoPilot is the gateway drug to AI


Every company seems to want to do AI, whatever that means. When I dig into actual AI use cases that can move the needle, stuff like Github CoPilot comes to mind as a gateway drug for many companies to get value from AI. It’s like staffing your engineering team with interns and junior-level engineers who are super convincing and often need their code reworked. But for the most part, the code output is passable, or at least eventually useable. There’s a catch - I don’t expect AI-enabled workflows to replace handwritten code anytime soon, as engineers still prefer writing code. Engineers want to engineer. Clanking on a keyboard is a very tactile and cathartic experience for engineers. AI coding assistants just make it easier (most of the time) to get work done.


Upskilling and Leveling Up


I’m seeing a lot of interest in data teams leveling up their competency and skills. Data engineering is a pretty new job title, and there’s yet no standardized training for data engineers. Random and scattered skillsets are the norm for most data engineering teams. At most companies, there’s often no official playbook for how to work asdata engineers, nor a framework for how data engineers should function within their company. As a consequence, most teams spend their time reacting, duct taping systems, and firefighting. For data engineering to become a legitimate field, data engineers will need standardized training and companies need to understand how to properly integrate data engineering into their organization. Thankfully, I’m seeing schools and companies interested in leveling up and investing in data engineering training and education. Like I’ve said before, we have no shortage of great tools and technologies, but we need to level up our knowledge and skills to use these tools to their fullest potential.


Playing Defense and Offense


Sol Rashidiintroduced me to defense and offense playbooks for data. The offense playbook focuses on activities that add value, while the defense playbook is about building robust systems. All too often, data engineering teams focus on defense. This seems to be changing as data engineers work more closely with the business, which is where offense is key. Again, this is part of data engineering maturing as a field and “adding value” to the business.


2024 seems both exciting and boring for data engineers. It's exciting because data engineering is finally recognized as critical to making data initiatives succeed (it wasn’t this way a few years ago). It’s boring because data engineering is moving toward “enterprisey” work. These are great things.


Listen to the audio clip above on this topic, which is also my5-Minute Friday on Spotify.


---


# Cool Weekend Reads


Here are some cool things I read this week. Enjoy!


### Tech, AI, Data


Of stream processing and lateness (part 1/2) (AB Tasty Tech)


Late arriving data happens in event streaming. This is a really good article (using Apache Beam as an example) on how to handle late data.


How to Write Great Tech Specs (Nicola Ballotta)


Tech specs are notoriously tricky to write. This is one of the better and more succinct approaches I’ve seen.


Introducing the GPT Store (OpenAI)


Stoked to check out the apps, and I’m very curious to see how this goes.


The Internet Is Full of AI Dogshit (Aftermath)


Speaking of which ;)


“The internet has been broken in a fundamental way. It is no longer a repository of people communicating with people; increasingly, it is just a series of machines communicating with machines.”


Yep…


### Biz, Culture, Other Randomness


IT Employment Grew by Just 700 Jobs in 2023, Down From 267,000 in 2022 (WSJ)


Only700jobs…


The New York Times’ AI Opportunity (Stratechery)


Easily the best analysis I’ve seen of the NYTimes lawsuit against OpenAI. A long but important read.


Google Cloud cuts egress and promotes cloud exits (DHH)


Egress fees remind me of cell phone minutes (remember those?). Props to GCP for removing egress fees if you want to export your data out of GCP. Now I’m just waiting for a cloud provider to entirely ditch egress fees. That day is coming…


Zero-Sum vs. Positive-Sum Product Theory (Working Theorys)


I talk with a ton of people, and it seems like people feel like most of their life is a zero-sum game. I win, you lose. Unless you’re in a “life or death” situation, you’re actually likely in growth mode. Know the difference and operate accordingly.


# New Content, Events, and Upcoming Stuff


## Monday Morning Data Chat


#### Coming up…


Joe Reis & Matt Housley, Dave Langer, and more!


#### In case you missed it…


Alex Gallego - Alex Gallego - The Streaming Data Renaissance, Open Formats, More (YouTube)


Mike Ferguson - Top Key Trends in Data Management and Analytics (Spotify,YouTube)


Tristan Handy - Data Engineering Ecosystems, Moats, Semantic Layers (Spotify,YouTube)


Sol Rashidi - Getting Business Value From Data, the CXO Playbook (Spotify,YouTube)


## The Joe Reis Show


#### Coming up…


Jordan Morrow, Ari Kaplan, Andrew Meister, and more…


#### This week…


Steve Nouri - Building a Global Data Community (Spotify)


5 Minute Friday - Data Engineering in 2024. What I’m Seeing (Spotify)


#### In case you missed it…


Sol Rashidi - The Rogue Data Executive (Spotify)


5 Minute Friday - Practical Data Modeling (Spotify)


5 Minute Friday - My Thoughts on 2024 Predictions and Resolutions (Spotify)


Will Gaviria Rojas - Using AI to Bring Structure to Unstructured Data (Spotify)


5 Minute Friday - The Internet of Bullsh*t (Spotify)


Bill Inmon - History Lessons of the Data Industry. This is a real treat and a very rare conversation with the godfather himself (Spotify) - PINNED HERE.


## Events


Data Day Texas (Austin), 1/27 -Register here


Chill Data Summit (NYC) - Tuesday 2/6 -Register here


Data Modeling Zone (Arizona), 2/28 -Register here


Skiers in Data (Switzerland), March 1-3 -Register here


Deepfest (Saudi Arabia) - March 4-7, TBA


ODSC (Boston) - April, TBA


GenAI Conference (London) - May, TBA


On the Beach (Malaga, Spain) - May, TBA


Gitex (Morocco) - May, TBA


DAMA Days (Vancouver, BC) - June, TBA


(Taking the Summer off)


Australia - Fall, TBA


Europe - Fall, TBA


Asia - Fall, TBA


Would you like me to speak at your event?Submit a speaking requesthere.


# Thanks! If you want to help out…


Thanks for supporting my content. If you aren’t a subscriber, please consider subscribing to this Substack.


You can also find me here:


Monday Morning Data Chat (YouTube/Spotifyand wherever you get your podcasts). Matt Housely and I interview the top people in the field. Live and unscripted. Zero shilling tolerated.


The Joe Reis Show (Spotifyand wherever you get your podcasts). My other show. I interview guests, and it’s unscripted with no shilling.


Fundamentals of Data Engineering (Amazon,O’Reilly, and wherever you get your books)


Be sure to leave a lovely review if you like the content.


Thanks! - Joe Reis


Thanks for reading Joe’s Nerdy Rants! Subscribe for free to receive new posts and support my work.
