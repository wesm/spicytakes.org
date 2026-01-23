---
title: "My Definition of Data Modeling (for today)"
subtitle: "Joe's Nerdy Rants #30 - Weekend reads and other stuff"
date: 2024-01-20T20:31:51+00:00
url: https://joereis.substack.com/p/my-definition-of-data-modeling-for
slug: my-definition-of-data-modeling-for
word_count: 1988
---


![An illustration in the style of a 1960s-1970s underground comic, with intricate linework, a vintage feel, and exaggerated, caricature-like characters, reminiscent of R. Crumb's work. The scene shows a man in a quirky, slightly exaggerated form, looking puzzled and thoughtful, surrounded by cartoon-style abstract shapes, mathematical symbols, and data streams. The setting and characters should have a pen and ink appearance, embodying the essence of R. Crumb's unique and influential style.](https://substackcdn.com/image/fetch/$s_!zQob!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d5a11df-dd1c-4a43-a212-e241ff963e1c_1024x1024.webp)


What is a data model? I like to ask this question during my conference talks, and answers are all over the place. I’ve never seen a group of people consistently give a single definition. Before I give my working definition, let’s look at a few ways data modeling is defined by some notable experts.


“A data model is a wayfinding tool for both business and IT professionals, which uses a set of symbols and text to precisely explain a subset of real information to improve communication within the organization and thereby lead to a more flexible and stable application environment.” - Steve Hoberman, Data Modeling Made Simple, p. 13


“Data models are techniques for representing information, and are at the same time sufficiently structured and simplistic as to fit well into computer technology” - William Kent, Data and Reality, p 119.


“A data model tells a story, and the story is about how a group of people come together to use data to solve a business problem (or take advantage of a business opportunity). The data model becomes a record of the journey from the conception of the problem to its solution.” - Larry Burns, Data Model Storytelling, p. 16


“...every model represents some aspect of reality or an idea that is of interest. A model is a simplification. It is an interpretation of reality that abstracts the aspects relevant to solving the problem at hand and ignores extraneous detail.” - Eric Evans, Domain Driven Design, p. 2


As you can see, a data model has many definitions and interpretations. If you ask ten people what they think a data model is, you’ll get at least ten answers. There are some common threads in these and other definitions you’ll find in other books and articles on data modeling. First, a data model represents reality abstractly, not as a complete mirror image. As Hoberman points out, these could be concepts, events, and relationships represented as a set of symbols and text. Second, a data model organizes and standardizes data precisely yet simplistically. Third, a data model improves communication, provides utility, promotes action, and solves problems.


I define a data model in the following way. Note this is a working definition that will very likely change as I write my data modeling book (in fact, it differs from the definition I gave in yesterday’s 5 Minute Friday). But the general points should remain the same.


> A data model is a structured representation that organizes and standardizes data to enable and guide human and machine behavior, inform decision-making, and facilitate actions.


The emphasis on machines is a departure from other definitions of data modeling you might encounter.  Historically, data modeling focused on making data understandable and valuable for humans. This definition recognizes that data is modeled for humans and machines. In fact, most data is modeled for machines, not humans. Think of the computer systems you interact with daily - your computer, smartphone, and other smart devices. Since the dawn of computing, humans modeled data for computer systems and applications to perform automated tasks. While humans use data models (often of the analytical variety) to make decisions and take actions, the number of machine-oriented actions is far greater. And with the rise of machine learning and AI, machines will increasingly become autonomous. Data is growing to a scale where humans have increasing trouble fully reasoning about it without the assistance of machines, and these machines will require better hardware, different types of data processing, and AI. Our thinking and approach to data modeling needs to evolve past a human-centric worldview.


Another major departure is the definition is agnostic to particular approaches like modeling for operational or analytical uses. It subtly recognizes the continuously evolving nature of data models. The definition still preserves the conceptual, logical, and physical phases of data modeling (or, as Steve Hoberman calls it, “align, refine, define”). Those phases won’t go away. However, the definition widens the possibilities for data modeling. Historically, data modeling is often viewed through the lens of particular use cases, like analytics, as if that’s the only place where data is modeled. This ignores the data models that exist upstream and downstream from analytics. The discussion of data modeling needs to be expanded away from myopic fixation on any particular approach or use case. Due to the continuously flowing nature of data, all modeling approaches are worthy of consideration, with varying degrees of utility for the situation at hand. I’ll discuss my thoughts on expanding data modeling in an upcoming discussion on Mixed Model Arts, which approaches data modeling across various use cases the same way you’d approach a mixed martial arts fight - you better know various techniques and when to apply them for the best outcomes. There is not one true way to fight, and there’s no one true approach in data modeling. There are many approaches. Pick what works for your situation.


Again, this definition is a work in progress and will likely evolve as I write my book and receive input from readers. Even people like Steve Hoberman, who I view as the OG of data modeling, regularly review and revise his definition of data modeling. I think that’s a recognition that data modeling isn’t a static thing, and as an industry, we need to constantly challenge our assumptions and evolve. That’s how we grow as an industry. But it’s also important to put a stake in the ground for now, and this is how I view data modeling today.


Speaking of data modeling, we have an awesome community of thousands of data modeling enthusiasts and practitioners atPractical Data Modeling. I’ll be writing more data modeling articles over there, along with early draft chapters of my new book, so check it out!


Listen to the audio clip above on this topic, which is also my5-Minute Friday on Spotify.


---


# Cool Weekend Reads


Here are some cool things I read this week. Enjoy!


### Tech, AI, Data


AlphaGeometry: An Olympiad-level AI system for geometry (Deepmind)


“AlphaGeometry is a neuro-symbolic system made up of a neural language model and a symbolic deduction engine, which work together to find proofs for complex geometry theorems. Akin to the idea of “thinking, fast and slow”, one system provides fast, “intuitive” ideas, and the other, more deliberate, rational decision-making.


Because language models excel at identifying general patterns and relationships in data, they can quickly predict potentially useful constructs, but often lack the ability to reason rigorously or explain their decisions. Symbolic deduction engines, on the other hand, are based on formal logic and use clear rules to arrive at conclusions. They are rational and explainable, but they can be “slow” and inflexible - especially when dealing with large, complex problems on their own.”


Geometry is tricky, to say the least. This is a very interesting approach to mixing symbolic deduction with LLMs. Much like the incorporation of knowledge graphs with LLMs, this is an example of old school meeting new school and each improving on the other. If you want to know where AI is heading, I suggest looking to the past. Understand the “old” approaches and how they can be applied to today’s zeitgeist.


At CES, everything was AI, even when it wasn’t (The Verge)


Yep, I saw the same thing at CES and similar expos. At pretty much every major tech expo I attend, AI is EVERYWHERE. If you believe the hype, every company suddenly pivoted to AI in 2023 and beyond. I’ll let you decide how much of that pivot is true. If everything is AI, is it true? I personally think AI is a massive bubble that will come crashing down to Earth in 2024.


Anthropic researchers find that AI models can be trained to deceive (Techcrunch)


So, pretty much like raising children?


### Biz, Culture, Other Randomness


Mourning Google (TBray)


“I had escaped from the accretion disk the former Sun Microsystems was forming around Oracle, that blackest of holes. And Google, in 2010, was the coolest place in the world to work.”


You escape from what troubles you, to someday again escaping the next thing troubling you.


“For my money, that was the center of Google’s problem. Larry and Sergey were smart guys who recognized they didn’t know shit about corporateness and quickly got into a pattern of hiring and empowering psychotic pricks who were presumably “good at business”. Not gonna talk about some of the things I saw because these people are wealthy and litigious.”Pray tell…The Bozo Event Horizonis a real thing. I’ve seen it in countless companies. First, you get one bozo, then another. Then before you know it, your company is worse than dead. It’s a parody and the exact opposite of its success. It’s a clown show.


The Puritans of Venture Capital (Investing 101)


What makes more sense? Capital agglomeration or Cottage Keepers? Read and find out in this very amazing article about the history and future of VC.


# New Content, Events, and Upcoming Stuff


## Monday Morning Data Chat


#### Coming up…


Dave Langer, Benn Stancil, and more!


#### In case you missed it…


Joe Reis & Matt Housley - Ask Us Anything (Spotify,YouTube)


Alex Gallego - Alex Gallego - The Streaming Data Renaissance, Open Formats, More (Spotify,YouTube)


Mike Ferguson - Top Key Trends in Data Management and Analytics (Spotify,YouTube)


Tristan Handy - Data Engineering Ecosystems, Moats, Semantic Layers (Spotify,YouTube)


Sol Rashidi - Getting Business Value From Data, the CXO Playbook (Spotify,YouTube). Very popular episode with nearly everyone. - PINNED HERE.


## The Joe Reis Show


#### Coming up…


Ari Kaplan, Andrew Meister, Steve Hoberman, and more…


#### This week…


Jordan Morrow - The OG of Data Literacy (Spotify)


5 Minute Friday - How I Define Data Modeling (today) (Spotify)


#### In case you missed it…


Steve Nouri - Building a Global Data Community (Spotify)


5 Minute Friday - Data Engineering in 2024. What I’m Seeing (Spotify)


Sol Rashidi - The Rogue Data Executive (Spotify)


5 Minute Friday - Practical Data Modeling (Spotify)


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
