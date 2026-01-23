---
title: "One of the Biggest Challenges in the Data Industry - The Knowledge and Skills Gap"
subtitle: "Joe's Nerdy Rants #57 - Why the knowledge and skills gap is sliding us backward, plus weekend reads and other stuff"
date: 2024-11-30T03:22:31+00:00
url: https://joereis.substack.com/p/one-of-the-biggest-challenges-in
slug: one-of-the-biggest-challenges-in
word_count: 1969
---


![8 Facts About the Grand Canyon You Never… | National Park Foundation](https://substackcdn.com/image/fetch/$s_!Ak1a!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6a4cf8b-7352-4667-bf5f-58be9d31c3ad_1600x900.jpeg)


The data industry is full of challenges. Despite our amazing technology, the solution we reach for is more technology. Although technology makes things easier for practitioners, I sense the data industry is sliding backward precisely when we should be gaining momentum. One of the greatest challenges in the industry is that we have plenty of fantastic tools and little idea of how to use them to their fullest potential.


For example, data modeling should be central to a data practitioner’s skill set. The number of practitioners I meet who truly understand data modeling from first principles is shockingly low. If you mention data modeling to the latest crop of practitioners, they might assume you’re talking about dbt models instead of the practice and craft of data modeling. People might also have a passing familiarity with dimensional modeling. The number of times I see the same questions being asked (online or in person) about facts and dimensions is depressing. If people would take the time to read Ralph Kimball’s Data Warehouse Toolkit, this would most certainly cut down on 99% of the questions and frustration I see. Instead, pursuing knowledge and skill is akin to a gossip mill. It’s almost impossible to master your craft if you’re not studying the giants of our industry.


Another data modeling problem is jumping straight to denormalized One Big Table without considering other options for analytical data modeling. Should you put your data into one table? If so, why? And why not? The default assumption I see is “joins are bad,” so throw all your data into a table (WTF - wide, tall, and full) and forget about it. Never mind that you’re setting yourself up for a host of errors - duplicates, redundancies, update anomalies, etc. You avoided joins, so that’s great. But now you have an indecipherable mess on your hands that would have been solved by learning the basics of the various analytical data modeling techniques that have been practiced for decades.


Then there’s denormalization when you probably don’t understand normalization. This is entirely backward yet super common. How many data practitioners understand how the relational model works and how it impacts normalization? If you don’t understand the difference between first normal form and the Boyce-Codd normal form, how do you know you’ve normalized or denormalized your data in a way that makes sense? You won’t.


The same goes for data warehousing. The topic is not new. Yet people still construct data warehouses (and lakehouses) as if there’s no prior knowledge. Bill Inmon popularized the data warehouse several decades ago, and there’s no shortage of books and literature on the topic. People confuse the data warehouse with technology. It’s not. According to Bill Inmon, a data warehouse is “a subject-oriented, integrated, time-variant and non-volatile collection of data in support of management's decision-making process.” The data warehouse isn’t focused on technology. Yet too many people conclude that a data warehouse is a tool that’s as simple as spinning up a column-oriented OLAP. In the end, data needs to support decision-making and so on. Same as it ever was.


I sometimes hear that the data industry moves too fast to keep up. Perhaps it does if you’re focused on the noise. But the signal is as clear as ever, and there are foundational and time-worn practices. I estimate most technologies have a two-year shelf life. But the foundations and fundamentals last a lot longer. That’s how theLindy Effectworks. Ultimately, the tools and practices in data are meant to serve the end user and customer, not to build fancier shit. Thankfully, nothing has fundamentally changed regarding the expectations of data. Data needs to be believable and add value to the business. You can extend this to AI, which must also be believable and add value. Same as it ever was.


So what’s the cause, and what’s the solution? On a superficial level, laziness might be to blame. In the past, you would ask questions on StackOverflow. Now, you ask AI, which can give you any answer you want, no matter how dubious it might realistically be. This increases the chances of doing dumb things more quickly since you might assume the AI is right no matter what. And even if all available information is implanted in your brain via Neuralink, people generally want to do the right thing but are often constrained for many reasons.


The problem is time and money are significant factors, especially today. We’re all starved for time (thanks for reading this article). In the workplace, time is a component of productivity—inputs and outputs over some time. More productivity means we crank out more outputs given the inputs. And we’re expected to do more with fewer inputs and less time. That means less time to hone one’s craft. Better tools mean you can ship crappier things faster. What’s the point of doing something correctly and with high quality if you’re forced to ship something out as quickly as possible?


The solution is twofold. First, companies must invest in their data team’s knowledge and skills. If companies genuinely value their employees, they’ll invest in their growth. Sadly, right now, companies want it both ways. Get things done faster and “figure it out on your own.” I’ll tell you what to do, and you’ll figure out how. Instead of forcing employees to grind themselves into the ground, invest in training, courses, book clubs, lunch and learns, and conferences.


Second, practitioners need to take charge of their growth and education. Despite my plea for companies to invest in their employees, your employer will unlikely help (kudos if they do). And don’t rely on your company’s internal knowledge, as most of this is akin to a gossip mill. Rumors and “best practices” are passed down from one employee to the next, often without consulting the sources of these ideas. Read the foundational books in the field and invest your time in learning the fundamentals of data. Learn tools as you need, but this shouldn’t be your primary focus until you’ve mastered the fundamentals. For tools, learn what you need to know for the job you need to do. This is necessary, especially when your job depends on understanding how to use a tool. But put yourself in the shoes of a physician. Do you want to know the brand of scalpel you’ll use for open heart surgery or how the heart works? Hopefully, you paid far more attention to the latter, as knowledge of the heart's operation is essential no matter what scalpel brand you use to operate on it.


The data industry is at an inflection point. New tools and technologies will emerge, but the underlying need for believable and valuable data will remain the same. Despite technological advances, the industry will continue to slide backward until our skills and knowledge can rise to the occasion. It’s up to us in the data industry to grow our foundational knowledge and skills to make this happen.


Also, listen to myaudio rantfor full color.


---


# Cool Weekend Reads


Good software development habits (Zarar's blog)


How AI Could Break the Career Ladder (Bloomberg)


It's Time to Merge Analytics and Data Engineering (Again) (Materialized View)


What’s Coming: The Changing Domestic and World Orders Under the Trump Administration (Ray Dalio Blog)


Write and Write Nots (Paul Graham)


Don't Do This (Postgres)


He Bought a Sub Shop as a Teen. Now He’s Selling Jersey Mike’s for $8 Billion (WSJ)


I do not think it means what you think it means (Raw Signal Group)


The Beginning of the End of Big Tech (WIRED)


AI is making Philippine call center work more efficient, for better and worse (Rest of the World)


# New Show & Upcoming Events


## The Joe Reis Show


Freestyle Fridays - The Skills Gap in Data (Spotify)


Albert Bellamy - Getting Your Job in Data (Spotify)


Tanya Bragin - Clickhouse, Open Source vs Commercial, and More (Spotify)


Freestyle Fridays - Obscurity is Your Enemy (Spotify)


Chris Riccomini - Building (and Writing About) Data Intensive Applications (Spotify)


Beers and Data with Friends in Helsinki, Finland (Spotify)


5 Minute Friday - The Quality Paradox (Spotify)


5 Minute Friday - Asking Good Questions at Conferences (Spotify)


Wes McKinney (Spotify)


5 Minute Friday - Is AI a Hail Mary for Tech Debt? (Spotify)


5 Minute Friday - Speaking at Conferences (Spotify)


Vijay Yadav - GenAI-Ready Data (Spotify)


5 Minute Friday -  Playing Not to Lose (Spotify)


Bill Inmon - History Lessons of the Data Industry. This is a real treat and a very rare conversation with the godfather himself (Spotify) - PINNED HERE.


## Monday Morning Data Chat


Note—The Monday Morning Data Chat is over. However, you can still find the back catalog on your podcast platform of choice or YouTube.


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


Data Day Texas - Austin, TX. January 25, 2025.Register here


Winter Data Conference - Austria. March 7, 2025.Register here


More to be announced soon…


Please note: I've traveled a lot for the last few years—probably too much for a person to stay sane or healthy. I tried to figure out how many times I’d traveled the globe. I have no idea. It’s a lot. And…In 2025, I’m reducing my travel. For one, I'm hyper-focused on a new company I’m starting (stay tuned for details). I also want to spend more time with my family and get outside in the Mountain West. I live in one of the most incredible places on the planet and never see it. Nature calls.I only accept workshops and speaking engagements that meet my fee requirements, except for rare exceptions. That said, you get what you pay for and then some. You'll get a ton of enthusiastic attendees and a very entertaining and informative talk/session. Your event will be on the global map. My track record speaks for itself. Please submit a speaking request if you want me to speak or give a workshop at your event.


# Thanks! If you want to help out…

- The Data Engineering Professional Certificate is one of the most popular courses on Coursera! Learn practical data engineering with lots of challenging hands-on examples. Shoutout to the fantastic people at Deeplearning.ai and AWS, who helped make this a reality over the last year. Enrollhere.
- Practical Data Modeling. Great discussions about data modeling with data practitioners. This is also where early drafts of my new data modeling book will be published.
- Fundamentals of Data Engineering by Matt Housley and I, available atAmazon,O’Reilly, and wherever you get your books.
- The Data Therapy Session calendar is postedhere. It’s an incredible group where you can share your experiences with data - good and bad - in a judgment-free place with other data professionals. If you’re interested in regularly attending, add it to your calendar.
- My other show is The Joe Reis Show (Spotifyand wherever you get your podcasts). I interview guests on it, and it’s unscripted and free of shilling.


Be sure to leave a lovely review if you like the content.


Thanks!


Joe Reis


Thanks for reading Joe’s Nerdy Rants! Subscribe for free to receive new posts and support my work.
