---
title: "You Inherited a Failed Data Project. What Do You Do?"
subtitle: "Joe's Nerdy Rants #33 - Weekend reads and other stuff"
date: 2024-02-24T14:32:53+00:00
url: https://joereis.substack.com/p/you-inherited-a-failed-data-project
slug: you-inherited-a-failed-data-project
word_count: 2251
---


My friendGordon Wongtexted me the other day with the following message.


![](https://substackcdn.com/image/fetch/$s_!UP4C!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27a64365-e92f-455e-82b8-a30cb5670604_1179x1806.jpeg)

*Gordon and I chatting about an idea for a podcast.*


Great idea, Gordon! What a great idea for my 5-Minute Friday podcast. Instead of 5 minutes, we riffed for around 30 minutes (6x of value for you ;) about how we’d handle the situation where we’re dropped into a dumpster fire of a data project - no existing data team, no idea about the data stack’s infrastructure or architecture, and no understanding of the business within which this data project operates.


Failed data projects are EVERYWHERE. I’m sure you’ve seen the old trope that 85% of data projects fail (or some other made-up number). Chances are you’ve worked on one or are working on one right now. If you’re the latter, you might know the project is doomed very clearly, or it might not yet be obvious.


What do you do if you’re dropped into the middle of a failed data project? Here’s what I would do (and I’m sure Gordon would have similar advice).

- Stakeholders will expect you to turn the failed project around, and that data will help them improve their jobs and the decisions they’re trying to make. Meet with them and understand the problems they’re trying to solve. It’s your job first to understand the goals the business stakeholders want to achieve, the decisions they want to make, and the problems or challenges that stand in their way toward these goals. How does data play into helping all of this?
- Pay particular attention to what I call “dark matter workflows” or “data things” that happen outside the data stack. Like the dark matter that you can’t see, but supposedly comprises most of the universe, dark matter workflows are things you don’t see that power the business. This often manifests itself in Excel-based Franken-stacks that power business units and analytics. People build these not because they want to (well, most people) but because IT and data teams didn’t address their problems.
- Understand why the project failed. Since this project is new to you, there’s little chance of you knowing why the data project began and ultimately failed. All you have are the remnants of the failed project. You will need to meet with people and investigate the root causes of the failure, treating it like a crime scene or an archaeologist searching for a lost civilization. Organizations are dynamic and political. In my experience, data projects fail because data teams don’t properly address stakeholder needs (see above). Then, the stakeholders often undermine the data team (intentionally or not) by building their own dark matter Franken-stacks, getting the data team fired, or letting the data team whither and die on the vine. As you dig around, expect to uncover political causes and be prepared for whatever happens from that.
- Make sure you’re empowered to make change. You might be granted a lot of accountability and responsibility but with very little authority. Also, suss out who might cause you harm. As I mentioned, organizations are political and teams usually don’t just die on their own. People are territorial. Have situational awareness, and don’t be naive that some people might see you as a threat.
- On that note, the Dalai Lama said, “If you can, help others; if you cannot do that, at least do not harm them.” Words to live by.
- Now, you can move on to technology. Notice I didn’tstartwith technology. That’s a rookie mistake. Until you understand the business objectives and reasons why the data project failed, technology doesn’t matter. Of course, I’ll caveat this and say if you’re hired as an engineer to fix an issue in the tech/data stack, then do that job and stay out of the organizational muck. If you’re talking architecture, it gets murkier because architecture is implicitly tied to the organization because of Conway’s Law. In this scenario, you’re dealing with a data stack abandoned by the last data data team. Assess the existing stack’s architecture. Change it if needed, or leave it alone if it works for now. Brownfield architecture is often harder to change than greenfield. If you assess things that need to be revamped, look at architectural change patterns like thestrangler patternand such.
- Set appropriate and realistic expectations for how long your revamp will take and how much it will cost. I highly suggest readingHow Big Things Get Done, which looks at why most projects (of all types, shapes, and sizes) fail. A major cause of failed projects is sandbagging estimates and crappy scoping and forecasting. I think everyone should read this book, especially given how lousy IT projects are among the worst types of projects for cost and time overruns. Shoutout toDave McCombfor showing me this book.
- Communicate early and often about your successes and learnings (aka failures). Shine a light on the business stakeholders and make them look like heroes. Make them part of the project’s success since you serve them. And critically, don’t make it all about yourself and the data team’s success. This is a great way to piss people off, lose their support, and become another failed data project. Then some unlucky fool will have to be parachuted in to start the resuscitation process all over again ;)


I’m sure there’s much more to add, but this is how I typically approach failed data projects. They’re gnarly, but it’s a cool experience when you can make a real transformation for an organization. Good luck.


Listen to the audio clip above on this topic, which is also my5-Minute Friday on Spotify.


Also, if you haven’t done so, please sign up forPractical Data Modeling. Lots of great discussions on data modeling, and this is also where I’ll be releasing early drafts of chapters for my new data modeling book. Thanks!


---


# Cool Weekend Reads


Here are some cool things I read this week. Enjoy!


### Tech, AI, Data


Things I Don't Know About AI (Elad Gil)


![](https://substackcdn.com/image/fetch/$s_!ueiN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6cea466b-d816-412e-8006-0ae5055142cc_1648x1050.png)


“In most markets, the more time passes the clearer things become. In generative AI (“AI”), it has been the opposite. The more time passes, the less I think I actually understand.”


Elad raises some good questions about the business model(s) behind LLMs. Is this an oligopoly with a very small handful of players? How do open-source LLMs fit in? Does the AI world split into many geographical and political fragments?  I like how Elad dissects the discussion of where LLMs go. Where do they go? Hell if I or anyone knows…


The Shift from Models to Compound AI Systems (Berkely Artificial Intelligence Research)


“In this post, we analyze the trend toward compound AI systems and what it means for AI developers. Why are developers building compound systems? Is this paradigm here to stay as models improve? And what are the emerging tools for developing and optimizing such systems—an area that has received far less research than model training? We argue thatcompound AI systems will likely be the best way to maximize AI results in the future, and might be one of the most impactful trends in AI in 2024.”


“…iterating on a system design is often much faster than waiting for training runs.”


“Finally, how can we optimize an AI system with discrete components end-to-end to maximize a metric, the same way we can train a neural network?”


Small might be big…Also,encapsulationstrikes again. I feel like we will see a new wave of X-Ops (MLOps ain’t young today) hitting whatever we want to call this wave of AI.


LLMs shouldn’t write SQL (Benn Stancil)


With seemingly every MDS company now clamoring to be an LLM text-to-SQL BI company,Benn Stancilbrings up a good point - just because we can use LLMs to replace SQL, should we? I agree with Benn’s position and extend this to math. If you could use natural language to solve math problems, would you? Formulas and code allow you to be very literal and explicit, and language is mushy and fuzzy. Both have their strengths, but sometimes its best not to conflate them.


Aligning Velox and Apache Arrow: Towards composable data management -Engineering at Meta (Meta)


Good article about how Meta is pushing ahead with Apache Arrow and its open-source execution engine, Velox. If you’re reading this and using Velox, message me. I’d love to understand your experience with it. Thanks!


### Biz, Culture, Other Randomness


Should you Stay Technical as an Engineering Manager? (The Hybrid Hacker)


![](https://substackcdn.com/image/fetch/$s_!_CKf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb252d0d-8272-44b4-8d81-075e8012ddef_3000x1688.png)


The paradox of becoming an engineering manager (and titles above that) is you’re doing less and less engineering, and more managing. How do you balance staying technical, hands-on, and leading a team? This is a great article describing some approaches.


The Layoff (Xe Laso)


“That's better. Listen, I don't like that we have to do this either, but there are formal procedures that have to be done in the state of California. I hate having to be the bearer of bad news so much more than you do receiving it, but it comes with the job. Techaro is going to make this as seamless as possible from here. I gave you some of the outlines of your severance package before, but you'll get all of the perks and benefits in your personal email inbox. The severance payment does come with terms, and we'd like to have that signed within a week of today so this is all wrapped up. Please be sure to speak with legal counsel before you sign it, Steven."


James was taken aback. "I'm sorry, but my name is James, not Steven. I'm on the frontend team, not the devops team. I think you might have the wrong person."


"No Steven, you are on the DevOps team. I'm sorry, but I can't disclose the plans we have to ensure that everything is fine, but I can assure you that we have a plan in place to ensure that the company continues to operate as it should. Should you choose to not accept our generous severance package that goes above and beyond the requirements of the state of California, we will comply with all of the relevant laws and regulations that the state of California has in place for involuntary terminations."


"I live in Oregon."


"Right, Oregon. I'm sorry Steven, I misspoke. Do you have any questions about the severance package or the terms of your departure?"


James' watch vibrated again.”


You wanna know why I don’t work in corporate America? This type of not-so-parody is all too real these days.


# New Content, Events, and Upcoming Stuff


## Monday Morning Data Chat


#### Coming up…


Jean-Georges Perrin, Ethan Aaron, and more!


#### In case you missed it…


Joe Reis & Matt Housley - The Demise of the Modern Data Stack & Listener Q&A (Spotify,YouTube)


Scott Taylor - Explaining Value to the Business (Spotify,YouTube)


Michel Tricot - AI's Impact on Traditional Data Practices and More! (Spotify,YouTube)


Benn Stancil -2024 Predictions, GenAI and Product Development, etc.(Spotify,YouTube)


Sol Rashidi - Getting Business Value From Data, the CXO Playbook (Spotify,YouTube). Very popular episode with nearly everyone. - PINNED HERE.


## The Joe Reis Show


#### Coming up…


Christophe Blefari, Annie Nelson, Zach Zeus, Christian Bourdeau, and many more!


#### This week…


5-Minute Friday - Gordon Wong and I are Dropped into a Failed Data Project  (Spotify)


Wendy Turner Williams - The Association.ai, Unleashing Generative AI, and more (Spotify)


Alex Freberg, aka Alex The Analyst - Playing the Long Games with Content - (Spotify)


#### In case you missed it…


Steve Hoberman - Data Modeling’s Past, Present, and Future (Spotify)


Randy Bean - Why GenerativeAI is Making Companies More Data-Driven (Spotify)


5 Minute Friday - Everything Ends (Spotify)


Andrew Meister - Removing Clunk (Spotify)


Roy Hasson - Career Progressions in Data & Tech, Open Table Formats, and more (Spotify)


Ari Kaplan  - Data Intelligence, Evangelism, and More (Spotify)


Bill Inmon - History Lessons of the Data Industry. This is a real treat and a very rare conversation with the godfather himself (Spotify) - PINNED HERE.


## Events


Low Key Meetup (Paris) - February 28.Register here


Skiers in Data (Switzerland), March 1-3 -Register here


Deepfest (Saudi Arabia) - March 4-7.Register here


Onepoint (Paris) - March 21.Register here


Data Universe (NYC) - April 10-12. TBA


J On the Beach (Malaga, Spain) - May 6-10.Register here


GenAI Conference (London) - May, TBA


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


Practical Data Modeling. Great discussions about data modeling with data practitioners. This is also where early drafts of my new data modeling book will be published.


Fundamentals of Data Engineering by Matt Housley and I, available atAmazon,O’Reilly, and wherever you get your books.


Be sure to leave a lovely review if you like the content.


Thanks! - Joe Reis


Thanks for reading Joe’s Nerdy Rants! Subscribe for free to receive new posts and support my work.
